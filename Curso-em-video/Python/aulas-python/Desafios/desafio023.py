#num = int(input('Digite um número: '))
#n = str(num)
#print('O número tem: ')
#print('{} unidades'.format(n[3]))
#print('{} centenas'.format(n[2]))
#print('{} dezenas'.format(n[1]))
#print('{} milhares'.format(n[0]))

num = int(input('Digite um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('O número {} tem: '.format(num))
print('{} unidades'.format(u))
print('{} dezenas'.format(d))
print('{} centenas'.format(c))
print('{} milhares'.format(m))
