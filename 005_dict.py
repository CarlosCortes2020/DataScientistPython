#Sintaxis larga
dict = {}
for i in range (1, 11):
    dict[i] = i * 2

print(dict)

#Sintaxis corta
dict_v2 = {i: i * 2 for i in range(1, 11)}
print(dict_v2)
