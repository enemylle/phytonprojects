#
n = input('digite algo.')
print('o Tipo primitivo é: ', type(n))
print('é um número: ',n.isnumeric())
print('é alfabético: ',n.isalpha())
print('é um alfanumérico: ',n.isalnum())
print('está maiusculo: ',n.isupper())
print('está minúsculo: ',n.islower())
print('está captalizada? ',n.istitle())
print('pode ser impresso: ',n.isprintable())
print('é um número decimal: ',n.isdecimal())
print('Possuí espaço: ',n.isspace())
