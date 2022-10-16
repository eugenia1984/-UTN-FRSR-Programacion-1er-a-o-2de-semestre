# Crear una funcion para calcular el total de un pago incluyendo un impuesto aplicado. (IVA)
# Formula: pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
# Proporcionar el pago_sin_impuesto de 1000
# Proporcionar el monto del impuesto del 21%
# Pago con impuesto: XXX
def calcular_total_pago(pago_sin_impuesto, impuesto):
  if impuesto <= 0:
    return("El impuesto debe ser mayor a 0")
  else:
    pago_total = pago_sin_impuesto + pago_sin_impuesto * (impuesto/100)
    return pago_total

# Ejecuto la funcion pidiendole los datos al usuario
pago_sin_impuesto = float(input("Ingrese el pago sin impuestos: "))
impuesto = float(input("Ingrese el monto dle impuesto a aplicar: "))
pago_con_impuesto = calcular_total_pago(pago_sin_impuesto, impuesto)
print(f"El pago total es: {pago_con_impuesto}")