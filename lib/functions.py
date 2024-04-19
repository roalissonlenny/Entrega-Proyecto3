import openpyxl

def cargar_datos_desde_excel(nombre_archivo):
    try:
        wb = openpyxl.load_workbook(nombre_archivo)
        sheet = wb.active
        matriz_adyacencia = []

        for row in sheet.iter_rows(values_only=True):
            matriz_adyacencia.append(list(row))

        return matriz_adyacencia

    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo {nombre_archivo}")
        return None

def mostrar_lista_relaciones(matriz_adyacencia):
    nodos = len(matriz_adyacencia)
    aristas = []

    for i in range(nodos):
        for j in range(nodos):
            if matriz_adyacencia[i][j] != 0:
                aristas.append((chr(65 + i), chr(65 + j), matriz_adyacencia[i][j]))  # Convertir índices a letras

    print("Lista de relaciones:")
    for arista in aristas:
        print(f"{arista[0]} -> {arista[1]} (Peso: {arista[2]})")

    return aristas