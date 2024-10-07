with open('ventas.txt', 'r') as archivo:
    ventas = []
    for linea in archivo:
        ventas.append([int(x) for x in linea.strip().split(',')])

for i, tienda in enumerate(ventas, 1):
    total_ventas = sum(tienda)
    print(f"Tienda {i}: {total_ventas} ventas")
  
  with open('totales.txt', 'w') as archivo_totales:
    for i, tienda in enumerate(ventas, 1):
        total_ventas = sum(tienda)
        archivo_totales.write(f"Tienda {i}: {total_ventas}\n")
