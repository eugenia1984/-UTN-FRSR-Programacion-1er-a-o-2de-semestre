# Colas
# FIFO First In First Out
# Como la cola del banco, el primero que llega es el que primero atienden
cola = ['Ariel', 'Osvaldo', 'Liliana', 'Pilar']
cola.append('Natalia') # agrego un elemento la final
print(cola) # 'Ariel', 'Osvaldo', 'Liliana', 'Pilar', 'Natalia'
seRetira = cola.pop(0) # se elemina el primer elemento y se guarda en variable
print(f"Se retira {seRetira} de la cola y quedan: {cola}")