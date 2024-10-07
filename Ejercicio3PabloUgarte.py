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

    mayor_venta = max(ventas, key=sum)
    menor_venta = min(ventas, key=sum)

    with open('totales.txt', 'a') as archivo_totales:
        archivo_totales.write(f"Mayor venta: Tienda {ventas.index(mayor_venta) + 1} con {sum(mayor_venta)} ventas\n")
        archivo_totales.write(f"Menor venta: Tienda {ventas.index(menor_venta) + 1} con {sum(menor_venta)} ventas\n")
