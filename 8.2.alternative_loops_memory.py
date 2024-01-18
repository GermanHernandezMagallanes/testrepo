#Códigos alternativos

#Cálculo del promedio con 1 sola entrada en la memoria secundaria.
total=0
count=0
while True:
    inp=input ('Enter a number: ')

    if inp=='done':break
    value=float(inp)
    total=total+value
    count=count+1

average=total/count
print('Average: ', average)

#alternativa con listas

numlist=list()
while True:
    inp=input('Enter a number: ')
    if inp=='done':break
    value=float(inp)
    #Append introduce los números que ingreso dentro de la lista 'list'
    numlist.append(value)

average=sum(numlist)/len(numlist)
print('Average: ', average)
