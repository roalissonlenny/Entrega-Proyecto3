from lib import*
import sys

def main():
    nombre_archivo = input("Ingrese el nombre del archivo Excel (incluyendo la extensión .xlsx): ")
    matriz_adyacencia = cargar_datos_desde_excel(nombre_archivo)

    if matriz_adyacencia:
        grafo = Grafo(matriz_adyacencia)
        print("Matriz de Adyacencia Ponderada:")
        print(grafo)

        aristas = mostrar_lista_relaciones(matriz_adyacencia)

    grafo.dijkstra(1, 8)

if __name__ == "__main__":
    main()

