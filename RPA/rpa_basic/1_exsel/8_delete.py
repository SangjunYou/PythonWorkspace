from openpyxl import load_workbook
wb = load_workbook("semple.xlsx")
ws = wb.active

# ws.delete_rows(8) # 8번째 줄에 있는  7번 데이터 삭제
# ws.delete_rows(8, 3) # 8번째 줄부터 3줄 삭제
# wb.save("semple_delete_rows.xlsx")

ws.delete_cols(2) # 2번째 열(B) 삭제
wb.save("semple_delete_cols.xlsx")