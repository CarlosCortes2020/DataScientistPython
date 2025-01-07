numbers = []
for element in range(1, 11):
    numbers.append(element)
print('Primer ciclo for ')
print(numbers)

numbers_2 = [element for element in range(1, 11)]
print('Primer sintaxis reducida ')
print(numbers_2)


numbers = []
for element in range(1, 11):
    numbers.append(element*2)
print('Segundo ciclo for numeros duplicados') 
print(numbers)

numbers_2 = [element*2 for element in range(1, 11)]
print('Segunda sintaxis reducida numeros duplicados')
print(numbers_2)


numbers = []
for i in range(1, 11):
    if i % 2 == 0:
        numbers.append(i * 2)
print('Tercer ciclo for  numeros pares ')
print(numbers)

numbers_2 = [i * 2 for i in range(1, 11) if i % 2 == 0]
print('Segunda sintaxis reducida numeros pares')
print(numbers_2)
