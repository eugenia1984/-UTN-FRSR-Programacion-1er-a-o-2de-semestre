# Ejercicio 9 : Mostrar una frase sin espacios y contrar su longitus
# Hacer un programa donde el usuario ingrese una frase, 
# se le devolverá la misma frase pero sin los espacios en blanco, 
# y ademas un contador de cuántos caracteres tiene la frase (sin contar los espacios en blanco)
# Ejempo:
# frase = vivir por siempre en paz
# frase final = vivirporsiemprenepaz
# Nº de caracters = 20
frase1 = input("ingrese un numero: ")
frase2 = " "

for i in frase1:
  if i != " ":
    frase2 += i

frase1 = frase2
print(f"\nFrase final: {frase1}")
print(f"Nº de caracteres: {len(frase1)}")