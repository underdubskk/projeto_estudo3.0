
# atividade 39
num = int(input('Digite um número inteiro: '))
print('Escolha uma das bases para conversão:')

print('[ 1 ] converter para BINÁRIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

op = int(input('Sua opção: '))

if op == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif op == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num,oct(num)[2:]))
elif op == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num,hex(num)[2:]))
else:
    print('Opção inválida. Tente novamente!')

# atividade 40
p1 = int(input('Prmeiro número: '))
p2 = int(input('Segundo número: '))

if p1 > p2:
    print('O PRIMEIRO valor é maior')
elif p1 < p2:
    print('O SEGUNDO valor é o maior')
elif p1 == p2:
    print('Os dois valores são IGUAIS')

# atividade 41
from datetime import date

anoa = date.today().year
anon = int(input('Ano de nascimento: '))

idade = (anoa - anon)
print('Quem nasceu em {} tem {} anos em {}'.format(anon,idade,anoa))

if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE!')
elif idade < 18:
    saldo1 = (18 - idade)
    print('Você ainda não tem 18 anos. Ainda faltam {} anos para o alistamento'.format(saldo1))

elif idade > 18:
    saldo2 = (idade - 18)
    print('Você já deveria ter se alistado a há {} anos'.format(saldo2))

# atividade 42
p1 = float(input('Primeira nota: '))
p2 = float(input('Segunda nota: '))

m = (p1 + p2) / 2
print('Tirando {} e {}, a média do aluno é {}'.format(p1,p2,m))

if 7 > m >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif m < 5:
    print('O aluno está REPROVADO')
elif m >= 7:
    print('O aluno está APROVADO.')