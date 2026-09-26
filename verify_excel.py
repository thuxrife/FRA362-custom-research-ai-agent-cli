import sys, openpyxl
sys.stdout.reconfigure(encoding='utf-8')
wb = openpyxl.load_workbook('feasibility-outcome/9-26-2026-1648_0.xlsx', data_only=False)
print('Sheet names:', wb.sheetnames)

# Check comparison sheet
ws_comp = wb['เปรียบเทียบทุก Solution']
print('\n=== EXECUTIVE COMPARISON SHEET (เปรียบเทียบทุก Solution) ===')
for r in range(4, 8):
    if r == 4:
        print('Headers:')
        for idx in range(1, 17):
            h = ws_comp.cell(row=r, column=idx).value
            print(f'  Col {idx} ({openpyxl.utils.get_column_letter(idx)}): {h}')
    else:
        sol_id = ws_comp.cell(row=r, column=2).value
        rob_score = ws_comp.cell(row=r, column=15).value
        rob_rat = ws_comp.cell(row=r, column=16).value
        print(f'Row {r}: {sol_id} | Col 15 (Robotics Score): {rob_score} | Col 16: {str(rob_rat)[:60]}...')

# Check individual sheets
for sname in wb.sheetnames[1:]:
    ws = wb[sname]
    print(f'\n=== SHEET: {sname} ===')
    for r in range(20, ws.max_row + 1):
        c1 = str(ws.cell(row=r, column=1).value)
        c2 = str(ws.cell(row=r, column=2).value)
        if any(w in c1 for w in ['หุ่นยนต์', 'Robotics', 'ศักยภาพ']):
            print(f'Row {r}: Col A="{c1}" | Col B="{c2}"')
            for c in range(1, 7):
                print(f'   Cell {openpyxl.utils.get_column_letter(c)}{r} = {ws.cell(row=r, column=c).value}')
