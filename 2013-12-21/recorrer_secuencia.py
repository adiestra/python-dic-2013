lista = ["Hugo", "Paco", "Luis", "Donald", "Daisy"]



print lista

print "Recorriendo con while..."

i = 0
elementos = len(lista)
while i < elementos:
    print lista[i]
    i += 1
    
    
print "Recorriendo con for..."

for elemento in lista:
    print elemento
