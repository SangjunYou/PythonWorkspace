from openpyxl import load_workbook
wb = load_workbook("semple.xlsx")
ws = wb.active

# ws.insert_rows(8)  # 8번째 줄이 비워짐
# ws.insert_rows(8, 5) # 8번째 줄에 5줄 추가


# ws.insert_cols(2) # B번째 열이 지워짐 (새로운 빈 열이 추가)
ws.insert_cols(2, 3)
wb.save("semple_insert_cols.xlsx")