### Clase 8

#### Contexto estatico y Contexto Dinamico

1. Contexto Estatico -> carga de clases

2. Contexto Dinamico -> carga de objetos

Todo lo definido con **static** se asocian a la **class** y no al **object**.


PALABRA STATIC
```
---------------------
 NombreObjeto1                         ------------------------------
---------------------                   NombreClase
+atributoNoEstatico1    -------------> -------------------------------
+atributoNoEstatico2     comparten      +atributoEstatico:
...                      los
---------------------    atributos     -------------------------------
                         y              + metodoEstatico(arg): return
--------------------     metodos
 NombreObjeto2           estaticos      ------------------------------
--------------------    ------------->
+atributoNoEstatico1
+atributoNoEstatico2
...
--------------------- 

```