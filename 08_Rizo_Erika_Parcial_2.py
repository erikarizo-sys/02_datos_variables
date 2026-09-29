productos =[
    {"nombre":"Teclado","precio":80000,"cantidad":3},
    {"nombre":"Mouse","precio":50000,"cantidad":5},
    {"nombre":"Monitor","precio":700000,"cantidad":2},
    {"nombre":"Camara","precio":120000,"cantidad":1},
]
def calcular_total(precio,cantidad):
    total = precio * cantidad
    return total
total = 0
for producto in productos:
    total += calcular_total(producto["precio"],producto["cantidad"])
    print(f"Producto: {producto['nombre']}, Precio: {producto['precio']}, {producto['cantidad']},  Total: {calcular_total(producto['precio'],producto['cantidad'])}")
print(f"Valor total del inventario: {total}")
bajo_stock = []
for producto in productos:
    if producto["cantidad"] < 3:
        bajo_stock.append(producto)
        print(f"Productos con bajo stock: {producto['nombre']}, Cantidad: {producto['cantidad']}")
        



    



 