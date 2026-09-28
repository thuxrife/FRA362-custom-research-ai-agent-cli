import os, sys, glob, openpyxl
if sys.stdout and hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

# Find latest excel file
files = glob.glob('feasibility-outcome/*.xlsx')
latest_file = max(files, key=os.path.getctime)
print(f"Loading latest Excel: {latest_file}")

wb = openpyxl.load_workbook(latest_file, data_only=False)
print('Sheet names:', wb.sheetnames)

# Check comparison sheet
ws_comp = wb['เปรียบเทียบทุก Solution']
print('\n=== EXECUTIVE COMPARISON SHEET (เปรียบเทียบทุก Solution) ===')
for r in range(4, 5 + len(wb.sheetnames) - 1):
    if r == 4:
        print('Headers:')
        for idx in range(1, 17):
            h = ws_comp.cell(row=r, column=idx).value
            print(f'  Col {idx} ({openpyxl.utils.get_column_letter(idx)}): {h}')
    else:
        sol_id = ws_comp.cell(row=r, column=2).value
        tot_score = ws_comp.cell(row=r, column=4).value
        verdict = ws_comp.cell(row=r, column=5).value
        rob_score = ws_comp.cell(row=r, column=15).value
        print(f'Row {r}: {sol_id} | Total Score: {tot_score} | Verdict: {verdict} | Robotics Score: {rob_score}')

for sname in wb.sheetnames[1:]:
    ws = wb[sname]
    print(f'\n=== SHEET: {sname} ===')
    q_count = 0
    for col in range(2, ws.max_column + 1):
        q_id = ws.cell(row=4, column=col).value
        if q_id:
            q_count += 1
    print(f'Total evaluated questions: {q_count}')
    total_score_cell = ws.cell(row=9, column=ws.max_column).value
    verdict_cell = ws.cell(row=12, column=ws.max_column).value
    print(f'Summary Col {openpyxl.utils.get_column_letter(ws.max_column)}: Row 9 Total={total_score_cell} | Row 12 Verdict={verdict_cell}')
