from openpyxl import load_workbook

def getDataXlsx(nombre_archivo):
    wb = load_workbook(nombre_archivo)
    hoja = wb.active
    filas = hoja.max_row
    columnas = hoja.max_column
