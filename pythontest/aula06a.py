n1 = int(input('Digite o valor.'))
n2 = int(input('Digite outro:'))
s = n1 + n2
print('A soma vale ',s )
print(type(n1))
print(type(n2))
print(type(s))

#print('A soma entre', n1, 'e', n2, 'vale',s)
print('A soma de {} com {} vale {}' .format(n1,n2,s))
