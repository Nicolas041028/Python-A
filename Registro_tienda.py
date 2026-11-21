Product = input("Ingrese el nombre del producto, (escriba FIN para terminar): ")
Regiproducts = 0
descproducts = 0
Totalbuy = 0
Totalpay = 0
Totaldesc = 0

while Product != "FIN":
    price = float(input("Ingrese el precio unitario del producto: "))
    Cant = int(input("Ingrese la cantidad del producto: "))
    Regiproducts += 1

    totprice = price * Cant
    desc = 0

    if totprice >= 100000:
        desc = totprice * 0.10
        descproducts = descproducts + 1
    else:
        if totprice > 50000 and totprice < 100000:
                desc = totprice * 0.05
        descproducts = descproducts + 1

    Finalprice = totprice - desc
    print(f"Producto: {Product}")
    print(f"Precio unitario: {price}")
    print(f"Cantidad: {Cant}")
    print(f"Precio total: {totprice}")
    print(f"Descuento aplicado: {desc}")
    print(f"Precio final a pagar: {Finalprice}")

    Totalbuy = Totalbuy + totprice
    Totalpay = Totalpay + Finalprice
    Totaldesc = Totaldesc + desc 

    Product = input("Ingrese el nombre del producto, (escriba FIN para terminar): ")

print("---RESUMEN DE COMPRA---")
print(f"Cantidad de productos registrados: {Regiproducts}")
print(f"Cantidad de productos con descuento: {descproducts}")
print(f"Precio total de la compra: {Totalbuy}")
print(f"Precio total de descuentos aplicados: {Totaldesc}")
print(f"Precio total a pagar: {Totalpay}")





    



