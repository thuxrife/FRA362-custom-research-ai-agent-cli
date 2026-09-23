#!/usr/bin/env python3
"""
feasibility-analysis.py
-----------------------
เครื่องมือแปลงข้อมูลการประเมินของ AI Agents เป็น Excel Matrix (TELOS+S Horizontal Compiler)
หน้าที่ของสคริปต์นี้:
  - รับข้อมูลการประเมินจาก AI Agents (Group 2: The Jury และผู้เชี่ยวชาญ 6 ด้าน) ในรูปแบบ JSON
  - ไม่มี (Zero) การล็อกหรือเขียนคำถามไว้ในโค้ด Python แม้แต่ข้อเดียว
  - ตรวจสอบและบังคับคะแนนเป็นจำนวนเต็มเด็ดขาด {1, 2, 3, 4, 5} เท่านั้น
  - จัดรูปแบบเป็น Transposed Horizontal Matrix ภาษาไทย (1 Solution ต่อ 1 Sheet)
  - สร้างหน้าสรุปเปรียบเทียบทุก Solution (Executive Comparison Tab)
  - บันทึกไฟล์ลงใน 'feasibility-outcome/{month}-{date}-{year}-{time}_{seq}.xlsx'

การใช้งาน:
    python feasibility-analysis.py --input-json feasibility-outcome/jury_eval_data.json
    python feasibility-analysis.py (จะโหลด feasibility-outcome/jury_eval_data.json โดยอัตโนมัติ)
"""

import os
import sys
import json
import argparse
from datetime import datetime
import openpyxl
from openpyxl.styles import Font, Alignment, PatternFill, Border, Side
from openpyxl.utils import get_column_letter

# Ensure UTF-8 printing in Windows terminals
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
if sys.stderr and hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8', errors='replace')


# ==============================================================================
# Helper: Canonical Pillar Normalization & Weighting
# ==============================================================================

def get_canonical_pillar(pillar_str):
    """
    จัดกลุ่มข้อความมิติการประเมินให้เป็น Canonical Key และค่าน้ำหนักมาตรฐาน (Two-Tier Model)
    รองรับทั้งภาษาไทย ภาษาอังกฤษ และรูปแบบข้อความที่ไม่สม่ำเสมอ
    """
    p = str(pillar_str).lower()
    if any(k in p for k in ["tech", "เทคนิค"]):
        return ("T", 0.20)
    elif any(k in p for k in ["econ", "เศรษฐ"]):
        return ("E", 0.20)
    elif any(k in p for k in ["legal", "กฎหมาย"]):
        return ("L", 0.15)
    elif any(k in p for k in ["operat", "ปฏิบัติการ"]):
        return ("O", 0.20)
    elif any(k in p for k in ["sched", "เวลา", "กำหนด"]):
        return ("S", 0.15)
    elif any(k in p for k in ["sdg", "ยั่งยืน"]):
        return ("SDG", 0.10)
    return ("OTHER", 1.0 / 6.0)


# ==============================================================================
# 1. ฟังก์ชันจัดรูปแบบและเขียนแผ่นงานสำหรับแต่ละ Solution (Transposed Horizontal Matrix)
# ==============================================================================

def write_solution_sheet(wb, sheet_title, assessment_data, solution_name="Solution"):
    ws = wb.create_sheet(title=sheet_title)
    ws.views.sheetView[0].showGridLines = True

    # ฟอนต์และสี
    title_font = Font(name="Segoe UI", size=13, bold=True, color="1F497D")
    sub_font = Font(name="Segoe UI", size=9.5, italic=True, color="595959")
    attr_header_font = Font(name="Segoe UI", size=10, bold=True, color="FFFFFF")
    q_id_font = Font(name="Segoe UI", size=11, bold=True, color="1F497D")
    score_font = Font(name="Segoe UI", size=15, bold=True, color="002060")
    bold_font = Font(name="Segoe UI", size=9.5, bold=True)
    regular_font = Font(name="Segoe UI", size=9)
    verdict_font = Font(name="Segoe UI", size=12, bold=True, color="006100")

    attr_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    score_hdr_fill = PatternFill(start_color="002060", end_color="002060", fill_type="solid")
    score_cell_fill = PatternFill(start_color="DCE6F1", end_color="DCE6F1", fill_type="solid")
    highlight_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")
    q_id_fill = PatternFill(start_color="F2F4F7", end_color="F2F4F7", fill_type="solid")

    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    # หัวเรื่องตาราง
    ws.cell(row=1, column=1, value=f"เมทริกซ์ประเมินความเป็นไปได้เชิงระบบ TELOS+S: {solution_name}").font = title_font
    ws.cell(row=2, column=1, value="ระบบคะแนนจำนวนเต็มเด็ดขาด: 1, 2, 3, 4, 5 เท่านั้น (ไม่มีจุดทศนิยม / ไม่มี 0.5) | โครงสร้างแบบ Transposed แนวนอน").font = sub_font

    # นิยามแถวคุณลักษณะใน Column A
    attributes = [
        (4, "รหัสคำถาม (Question Code)", q_id_font, q_id_fill),
        (5, "มิติการประเมิน (TELOS+S Pillar)", attr_header_font, attr_fill),
        (6, "คำถามทดสอบความเสี่ยงจริง (Stress-Test Question)", attr_header_font, attr_fill),
        (7, "เหตุผลในการถาม & โหมดความล้มเหลวที่เฝ้าระวัง (Rationale)", attr_header_font, attr_fill),
        (8, "เกณฑ์การให้คะแนน (Scoring Rubric Definition: ระดับ 1, 2, 3, 4, 5 ครบทุกระดับ)", attr_header_font, attr_fill),
        (9, "คะแนนที่ได้รับ (ASSIGNED SCORE: 1, 2, 3, 4, 5 STRICT INTEGER)", Font(name="Segoe UI", size=10, bold=True, color="FFFFFF"), score_hdr_fill),
        (10, "ค่าน้ำหนัก (Weight %)", attr_header_font, attr_fill),
        (11, "คะแนนถ่วงน้ำหนัก (=Score * Weight)", attr_header_font, attr_fill),
        (12, "คำอธิบาย & หลักฐานอ้างอิงจากไฟล์ Intake (Evidence Citation)", attr_header_font, attr_fill),
        (13, "แผนลดขอบเขตงาน & มาตรการลดความเสี่ยง (De-scoping Action)", attr_header_font, attr_fill)
    ]

    for r_idx, label, fnt, fll in attributes:
        cell = ws.cell(row=r_idx, column=1, value=label)
        cell.font = fnt
        cell.fill = fll
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        cell.border = thin_border

    ws.column_dimensions['A'].width = 38

    # นับจำนวนคำถามต่อมิติแบบ Canonical เพื่อใช้ใน Two-Tier Normalized Weighting Fallback
    pillar_counts = {}
    for it in assessment_data:
        c_key, _ = get_canonical_pillar(it.get("pillar", ""))
        pillar_counts[c_key] = pillar_counts.get(c_key, 0) + 1

    # เติมข้อมูลคำถามจาก AI Agents ลงในแนวคอลัมน์ (Columns B, C, D, ...)
    start_col = 2
    for idx, item in enumerate(assessment_data):
        col = start_col + idx
        col_letter = get_column_letter(col)
        ws.column_dimensions[col_letter].width = 30

        # Row 4: รหัส
        c4 = ws.cell(row=4, column=col, value=item.get("id", f"Q-{idx+1:02d}"))
        c4.font = q_id_font
        c4.fill = q_id_fill
        c4.alignment = Alignment(horizontal="center", vertical="center")
        c4.border = thin_border

        # Row 5: มิติ
        c5 = ws.cell(row=5, column=col, value=item.get("pillar", "มิติการประเมิน"))
        c5.font = bold_font
        c5.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c5.border = thin_border

        # Row 6: คำถาม Stress-Test
        c6 = ws.cell(row=6, column=col, value=item.get("question", ""))
        c6.font = regular_font
        c6.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c6.border = thin_border

        # Row 7: เหตุผล
        c7 = ws.cell(row=7, column=col, value=item.get("rationale", ""))
        c7.font = regular_font
        c7.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c7.border = thin_border

        # Row 8: เกณฑ์ Rubric
        c8 = ws.cell(row=8, column=col, value=item.get("rubric", ""))
        c8.font = regular_font
        c8.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c8.border = thin_border

        # Row 9: คะแนน (Strict Integer: 1, 2, 3, 4, 5 เด็ดขาด)
        raw_val = item.get("score", 3)
        try:
            score_int = int(round(float(raw_val)))
        except (ValueError, TypeError):
            score_int = 3
        score_int = max(1, min(5, score_int))

        c9 = ws.cell(row=9, column=col, value=score_int)
        c9.font = score_font
        c9.fill = score_cell_fill
        c9.alignment = Alignment(horizontal="center", vertical="center")
        c9.number_format = '0'
        c9.border = thin_border

        # Row 10: น้ำหนัก (Two-Tier Normalized Weighting Architecture)
        weight_val = None
        if "weight" in item and item["weight"] is not None:
            try:
                raw_w = str(item["weight"]).replace('%', '').strip()
                parsed_w = float(raw_w)
                if parsed_w > 1.0:
                    parsed_w = parsed_w / 100.0  # แปลง 20 หรือ 6.67 ให้เป็น 0.20 หรือ 0.0667
                weight_val = parsed_w
            except (ValueError, TypeError):
                weight_val = None

        if weight_val is None:
            c_key, p_wt = get_canonical_pillar(item.get("pillar", ""))
            p_count = max(1, pillar_counts.get(c_key, 1))
            weight_val = p_wt / p_count

        c10 = ws.cell(row=10, column=col, value=weight_val)
        c10.font = bold_font
        c10.alignment = Alignment(horizontal="center", vertical="center")
        c10.number_format = '0.0%'
        c10.border = thin_border

        # Row 11: คะแนนถ่วงน้ำหนัก (สูตร Excel)
        c11 = ws.cell(row=11, column=col, value=f"={col_letter}9*{col_letter}10")
        c11.font = bold_font
        c11.alignment = Alignment(horizontal="center", vertical="center")
        c11.number_format = '0.00'
        c11.border = thin_border

        # Row 12: หลักฐานอ้างอิง
        c12 = ws.cell(row=12, column=col, value=item.get("evidence", ""))
        c12.font = regular_font
        c12.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c12.border = thin_border

        # Row 13: มาตรการลดความเสี่ยง
        c13 = ws.cell(row=13, column=col, value=item.get("descope", ""))
        c13.font = regular_font
        c13.alignment = Alignment(horizontal="left", vertical="top", wrap_text=True)
        c13.border = thin_border

    # คอลัมน์สรุปภาพรวม (Summary Column)
    summary_col_idx = start_col + len(assessment_data)
    sum_letter = get_column_letter(summary_col_idx)
    ws.column_dimensions[sum_letter].width = 30

    first_col = get_column_letter(start_col)
    last_col = get_column_letter(summary_col_idx - 1)

    c_s4 = ws.cell(row=4, column=summary_col_idx, value="สรุปภาพรวม (SUMMARY)")
    c_s4.font = q_id_font
    c_s4.fill = q_id_fill
    c_s4.alignment = Alignment(horizontal="center", vertical="center")
    c_s4.border = thin_border

    c_s5 = ws.cell(row=5, column=summary_col_idx, value="ผลรวมทุกมิติ (All Pillars)")
    c_s5.font = bold_font
    c_s5.alignment = Alignment(horizontal="center", vertical="center")
    c_s5.border = thin_border

    ws.cell(row=6, column=summary_col_idx, value=f"ประเมินคำถามทั้งสิ้น {len(assessment_data)} ข้อ").font = regular_font
    ws.cell(row=6, column=summary_col_idx).alignment = Alignment(wrap_text=True)
    ws.cell(row=6, column=summary_col_idx).border = thin_border

    ws.cell(row=7, column=summary_col_idx, value="สังเคราะห์จาก AI Agents Group 2").font = regular_font
    ws.cell(row=7, column=summary_col_idx).alignment = Alignment(wrap_text=True)
    ws.cell(row=7, column=summary_col_idx).border = thin_border

    ws.cell(row=8, column=summary_col_idx, value="เกณฑ์รวม: >=80 ผ่านสูง, >=60 มีเงื่อนไข, <60 เสี่ยงสูง | หากมีข้อใดได้ 1 = VETOED ตกเกณฑ์ทันที").font = regular_font
    ws.cell(row=8, column=summary_col_idx).alignment = Alignment(wrap_text=True)
    ws.cell(row=8, column=summary_col_idx).border = thin_border

    # ตรวจสอบว่ามีคำถามใดได้คะแนน 1 หรือไม่ (Knockout / Fatal-Flaw Detection)
    has_fatal_flaw = any(
        (isinstance(it.get("score"), (int, float)) and int(round(it["score"])) == 1)
        or str(it.get("score", "")).strip() == "1"
        for it in assessment_data
    )

    # คะแนนรวมเต็ม 100 คำนวณแบบ Normalized กับผลรวมค่าน้ำหนักจริง (Dynamic Normalization)
    c_tot_score = ws.cell(row=9, column=summary_col_idx, value=f'=IF({sum_letter}10>0, ({sum_letter}11/{sum_letter}10)*20, 0)')
    if has_fatal_flaw:
        c_tot_score.font = Font(name="Segoe UI", size=16, bold=True, color="9C0006")
        c_tot_score.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    else:
        c_tot_score.font = Font(name="Segoe UI", size=16, bold=True, color="006100")
        c_tot_score.fill = highlight_fill
    c_tot_score.number_format = '0.0'
    c_tot_score.alignment = Alignment(horizontal="center", vertical="center")
    c_tot_score.border = thin_border

    # ค่าน้ำหนักรวม
    c_tot_wt = ws.cell(row=10, column=summary_col_idx, value=f"=SUM({first_col}10:{last_col}10)")
    c_tot_wt.font = bold_font
    c_tot_wt.number_format = '0.0%'
    c_tot_wt.alignment = Alignment(horizontal="center", vertical="center")
    c_tot_wt.border = thin_border

    # ผลรวมคะแนนถ่วงน้ำหนัก
    c_tot_weighted = ws.cell(row=11, column=summary_col_idx, value=f"=SUM({first_col}11:{last_col}11)")
    c_tot_weighted.font = bold_font
    c_tot_weighted.number_format = '0.00'
    c_tot_weighted.alignment = Alignment(horizontal="center", vertical="center")
    c_tot_weighted.border = thin_border

    # คำตัดสิน Verdict ตามกฎ Knockout / Fatal-Flaw Gating Rule
    # หาก MIN ของคะแนน = 1 ให้ขึ้น VETOED ตกเกณฑ์ข้อบังคับวิกฤตทันที
    verdict_c = ws.cell(row=12, column=summary_col_idx, value=f'=IF(MIN({first_col}9:{last_col}9)=1, "VETOED / ตกเกณฑ์ข้อบังคับวิกฤต (คะแนนระดับ 1)", IF({sum_letter}9>=80, "ผ่านเกณฑ์ระดับสูง (HIGHLY VIABLE)", IF({sum_letter}9>=60, "ผ่านแบบมีเงื่อนไข (CONDITIONALLY VIABLE)", "ความเสี่ยงสูง (HIGH RISK)")))')
    if has_fatal_flaw:
        verdict_c.font = Font(name="Segoe UI", size=11, bold=True, color="9C0006")
        verdict_c.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
    else:
        verdict_c.font = verdict_font
        verdict_c.fill = highlight_fill
    verdict_c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
    verdict_c.border = thin_border

    ws.cell(row=13, column=summary_col_idx, value="ปฏิบัติตามแผนลดขอบเขตงาน (De-scoping Advisory)").font = bold_font
    ws.cell(row=13, column=summary_col_idx).alignment = Alignment(horizontal="center", vertical="center")
    ws.cell(row=13, column=summary_col_idx).border = thin_border

    ws.row_dimensions[4].height = 24
    ws.row_dimensions[5].height = 24
    ws.row_dimensions[6].height = 75
    ws.row_dimensions[7].height = 95
    ws.row_dimensions[8].height = 110
    ws.row_dimensions[9].height = 36
    ws.row_dimensions[10].height = 22
    ws.row_dimensions[11].height = 24
    ws.row_dimensions[12].height = 95
    ws.row_dimensions[13].height = 70

    return sum_letter


# ==============================================================================
# 2. ฟังก์ชันสร้างหน้าสรุปเปรียบเทียบทุก Solution (Executive Comparison Tab)
# ==============================================================================

def write_comparison_sheet(wb, solutions_info):
    ws = wb.create_sheet(title="เปรียบเทียบทุก Solution", index=0)
    ws.views.sheetView[0].showGridLines = True

    title_font = Font(name="Segoe UI", size=14, bold=True, color="1F497D")
    sub_font = Font(name="Segoe UI", size=10, italic=True, color="595959")
    hdr_font = Font(name="Segoe UI", size=11, bold=True, color="FFFFFF")
    data_font = Font(name="Segoe UI", size=10)
    bold_data_font = Font(name="Segoe UI", size=10, bold=True)
    score_sum_font = Font(name="Segoe UI", size=13, bold=True, color="006100")

    hdr_fill = PatternFill(start_color="1F497D", end_color="1F497D", fill_type="solid")
    zebra_fill = PatternFill(start_color="F9FAFC", end_color="F9FAFC", fill_type="solid")
    highlight_fill = PatternFill(start_color="C6EFCE", end_color="C6EFCE", fill_type="solid")

    thin_border = Border(
        left=Side(style='thin', color='D9D9D9'),
        right=Side(style='thin', color='D9D9D9'),
        top=Side(style='thin', color='D9D9D9'),
        bottom=Side(style='thin', color='D9D9D9')
    )

    ws.cell(row=1, column=1, value="ตารางเปรียบเทียบความเป็นไปได้ของทุกข้อเสนอ (Multi-Solution Feasibility Summary)").font = title_font
    ws.cell(row=2, column=1, value="วิเคราะห์เปรียบเทียบเชิงระบบ (Systems-Thinking) ตามเกณฑ์ TELOS+S จาก AI Agents | รวมทุก Solution ในไฟล์เดียว").font = sub_font

    headers = [
        ("ลำดับ", 8),
        ("รหัสข้อเสนอ (Solution ID)", 22),
        ("ชื่อแนวทางแก้ปัญหา (Title / Concept)", 34),
        ("คะแนนรวม (เต็ม 100)", 18),
        ("ผลการประเมิน (Verdict)", 28),
        ("จุดแข็งสำคัญ (Key Strengths)", 35),
        ("จุดติดขัดวิกฤต (Critical Bottlenecks)", 35),
        ("คำแนะนำเชิงระบบ (Strategic Advice)", 35)
    ]

    ws.row_dimensions[4].height = 28
    for col_idx, (hdr_text, col_width) in enumerate(headers, start=1):
        cell = ws.cell(row=4, column=col_idx, value=hdr_text)
        cell.font = hdr_font
        cell.fill = hdr_fill
        cell.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        cell.border = thin_border
        col_letter = get_column_letter(col_idx)
        ws.column_dimensions[col_letter].width = col_width

    for r_idx, sol in enumerate(solutions_info, start=5):
        ws.row_dimensions[r_idx].height = 55
        fill_to_use = zebra_fill if r_idx % 2 == 1 else PatternFill(fill_type=None)

        c1 = ws.cell(row=r_idx, column=1, value=r_idx - 4)
        c1.alignment = Alignment(horizontal="center", vertical="center")

        c2 = ws.cell(row=r_idx, column=2, value=sol["sheet_title"])
        c2.font = bold_data_font
        c2.alignment = Alignment(horizontal="center", vertical="center")

        c3 = ws.cell(row=r_idx, column=3, value=sol["concept"])
        c3.font = data_font
        c3.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

        safe_sheet_name = sol['sheet_title'].replace("'", "''")
        sheet_ref = f"'{safe_sheet_name}'"
        c4 = ws.cell(row=r_idx, column=4, value=f"={sheet_ref}!{sol['sum_col']}9")
        c4.alignment = Alignment(horizontal="center", vertical="center")
        c4.number_format = '0.0'

        c5 = ws.cell(row=r_idx, column=5, value=f"={sheet_ref}!{sol['sum_col']}12")
        c5.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)

        if sol.get("has_fatal_flaw", False):
            c4.font = Font(name="Segoe UI", size=13, bold=True, color="9C0006")
            c4.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
            c5.font = Font(name="Segoe UI", size=10, bold=True, color="9C0006")
            c5.fill = PatternFill(start_color="FFC7CE", end_color="FFC7CE", fill_type="solid")
        else:
            c4.font = score_sum_font
            c4.fill = highlight_fill
            c5.font = bold_data_font

        c6 = ws.cell(row=r_idx, column=6, value=sol.get("strength", "จุดแข็งด้านซอฟต์แวร์และการใช้ฮาร์ดแวร์ COTS"))
        c6.font = data_font
        c6.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

        c7 = ws.cell(row=r_idx, column=7, value=sol.get("bottleneck", "ระเบียบปฏิบัติหน้างานและสัปดาห์สอบของมหาวิทยาลัย"))
        c7.font = data_font
        c7.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

        c8 = ws.cell(row=r_idx, column=8, value=sol.get("advice", "ล็อกสเปกฮาร์ดแวร์ก่อนสัปดาห์ที่ 9 และทำระบบสร้างใบปิดงานดิจิทัล"))
        c8.font = data_font
        c8.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)

        for col_idx in range(1, 9):
            cell = ws.cell(row=r_idx, column=col_idx)
            cell.border = thin_border
            if col_idx not in (4, 5) and fill_to_use.fill_type:
                cell.fill = fill_to_use
            elif col_idx == 5 and not sol.get("has_fatal_flaw", False) and fill_to_use.fill_type:
                cell.fill = fill_to_use


# ==============================================================================
# 3. ฟังก์ชันบันทึกไฟล์ Excel ตามลำดับ _0, _1, _2
# ==============================================================================

def compile_excel_from_eval_data(solutions_eval_data, output_dir="feasibility-outcome", custom_filename=None):
    import re
    os.makedirs(output_dir, exist_ok=True)

    # ป้องกันข้อผิดพลาด Gap 1: กรณี LLM ห่อ List ด้วย Dictionary เช่น {"solutions": [...]}
    if isinstance(solutions_eval_data, dict):
        for candidate_key in ["solutions", "data", "evaluations", "results", "proposals"]:
            if candidate_key in solutions_eval_data and isinstance(solutions_eval_data[candidate_key], list):
                solutions_eval_data = solutions_eval_data[candidate_key]
                break
        else:
            for val in solutions_eval_data.values():
                if isinstance(val, list):
                    solutions_eval_data = val
                    break

    if not isinstance(solutions_eval_data, list):
        print("[ข้อผิดพลาด] รูปแบบข้อมูลการประเมินต้องเป็น List ของ Solutions!")
        return

    if not custom_filename:
        now = datetime.now()
        base_name = f"{now.month}-{now.day}-{now.year}-{now.strftime('%H%M')}"
        counter = 0
        filename = f"{base_name}_{counter}.xlsx"
        while os.path.exists(os.path.join(output_dir, filename)):
            counter += 1
            filename = f"{base_name}_{counter}.xlsx"
    elif not custom_filename.endswith(".xlsx"):
        filename = f"{custom_filename}.xlsx"
    else:
        filename = custom_filename

    excel_path = os.path.join(output_dir, filename)

    wb = openpyxl.Workbook()
    default_sheet = wb.active

    solutions_summary_info = []
    used_titles = set()

    for idx, sol in enumerate(solutions_eval_data, start=1):
        # ป้องกันข้อผิดพลาด Gap 3: ตัดอักขระต้องห้ามของ Excel \ / ? * : [ ] และป้องกันชื่อซ้ำ
        raw_title = str(sol.get("sheet_title", f"Solution-{idx}"))
        safe_title = re.sub(r'[\\/*?:\[\]]', '_', raw_title).strip()
        safe_title = safe_title[:28] if safe_title else f"Solution-{idx}"

        unique_title = safe_title
        dup_counter = 1
        while unique_title in used_titles or unique_title in wb.sheetnames:
            unique_title = f"{safe_title[:25]}_{dup_counter}"
            dup_counter += 1
        used_titles.add(unique_title)
        sheet_title = unique_title

        assessment_data = sol.get("assessment_data", [])
        concept = sol.get("concept", sheet_title)
        sum_col = write_solution_sheet(wb, sheet_title, assessment_data, solution_name=concept)

        has_fatal = any(
            (isinstance(it.get("score"), (int, float)) and int(round(it["score"])) == 1)
            or str(it.get("score", "")).strip() == "1"
            for it in assessment_data
        )

        solutions_summary_info.append({
            "sheet_title": sheet_title,
            "concept": concept,
            "sum_col": sum_col,
            "has_fatal_flaw": has_fatal,
            "strength": sol.get("strength", "-"),
            "bottleneck": sol.get("bottleneck", "-"),
            "advice": sol.get("advice", "-")
        })

    write_comparison_sheet(wb, solutions_summary_info)

    if default_sheet in wb.worksheets and len(wb.worksheets) > 1:
        wb.remove(default_sheet)

    try:
        wb.save(excel_path)
        print(f"[สำเร็จ] คอมไพล์เมทริกซ์ Excel จาก AI Agents เรียบร้อยแล้วที่:\n  --> {excel_path}")
        print(f"  --> จำนวนแท็บ Solution: {len(solutions_summary_info)} แท็บ + แท็บสรุปเปรียบเทียบ")
    except PermissionError:
        base, ext = os.path.splitext(excel_path)
        alt_path = f"{base}_alt{ext}"
        wb.save(alt_path)
        print(f"[แจ้งเตือน] ไฟล์ '{excel_path}' ถูกเปิดค้างอยู่ในโปรแกรมอื่น จึงบันทึกไปยัง:\n  --> {alt_path}")


def main():
    parser = argparse.ArgumentParser(description="คอมไพล์ผลการประเมิน TELOS+S จาก AI Agents เป็น Excel Matrix แนวนอน")
    parser.add_argument("--name", "-n", type=str, default=None, help="ชื่อไฟล์ Excel เช่น {month}-{date}-{year}-{time}")
    parser.add_argument("--input-json", "-i", type=str, default=None, help="ไฟล์ JSON ผลการประเมินจาก AI Agents")
    parser.add_argument("--outdir", "-o", type=str, default="feasibility-outcome", help="โฟลเดอร์สำหรับบันทึกไฟล์ผลลัพธ์")
    args = parser.parse_args()

    # ลำดับการหาไฟล์ input JSON จาก AI Agents
    json_path = args.input_json
    if not json_path:
        default_candidates = [
            os.path.join(args.outdir, "jury_eval_data.json"),
            "jury_eval_data.json",
            "eval_data.json"
        ]
        for candidate in default_candidates:
            if os.path.exists(candidate):
                json_path = candidate
                break

    if not json_path or not os.path.exists(json_path):
        print("[ข้อผิดพลาด] ไม่พบไฟล์ข้อมูลการประเมิน JSON จาก AI Agents!")
        print("กรุณาส่งพาธไฟล์ JSON ผ่าน: python feasibility-analysis.py --input-json <path_to_json>")
        sys.exit(1)

    with open(json_path, "r", encoding="utf-8") as f:
        solutions_eval_data = json.load(f)

    compile_excel_from_eval_data(solutions_eval_data, output_dir=args.outdir, custom_filename=args.name)


if __name__ == "__main__":
    main()
