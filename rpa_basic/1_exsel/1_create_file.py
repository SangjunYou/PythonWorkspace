from openpyxl import Workbook

wb = Workbook() # 새로운 워크북 생성
ws =wb.active  # 현제 활성화된 sheet 가져옴
ws.title = "NadoSheet"
wb.save("sample.xlsx")
wb.close()
