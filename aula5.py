
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

# atividade 43
from datetime import date

an = int(input('Ano de Nascimento: '))
ana = date.today().year
n = (ana - an)

print('O atleta tem {} anos.'.format(n))

if n > 25:
    print('Clasificação: MASTER')
elif n > 19 and n <= 25:
    print('Clasificação: SÊNIOR')
elif n > 14 and n <= 19:
    print('Clasificação: JÚNIOR')
elif n > 9 and n <= 14:
    print('Clasificação: INFANTIL')
elif n > 0 and n <= 9:
    print('Clasificação: MIRIM')

# atividade 44
s1 = int(input('Primeiro segmento: '))
s2 = int(input('Segundo segmento: '))
s3 = int(input('Terceiro segmento: '))

if s1 < s2 + s3 and s2 < s1 + s3 and s3 < s1 + s2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')

    if s1 == s2 == s3:
        print('EQUILÁTERO!')
    elif s1 != s2 and s2 != s3 and s3 != s1:
        print('ESCALENO!')
    else:
        print('ISÓCELES')

else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')

# atividade 45
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = (peso / (altura ** 2))
print('O IMC dessa pessoa é de {:.1f}'.format(imc))


if imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')

elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')

elif imc >= 18.5 and imc < 25:
    print('Você está na faixa de PESO IDEAL!')

elif imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL, cuidado!')

# atividade 45
peso = float(input('Qual é o seu peso? (kg) '))
altura = float(input('Qual é a sua altura? (m) '))

imc = (peso / (altura ** 2))
print('O IMC dessa pessoa é de {:.1f}'.format(imc))


if imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')

elif imc >= 30 and imc < 40:
    print('Você está em OBESIDADE!')

elif imc >= 25 and imc < 30:
    print('Você está em SOBREPESO!')

elif imc >= 18.5 and imc < 25:
    print('Você está na faixa de PESO IDEAL!')

elif imc < 18.5:
    print('Você está ABAIXO DO PESO IDEAL, cuidado!')

# atividade 46
print('=' * 25, 'LOJAS DO SEU ZÉ', '=' * 25)
pre = float(input('Preço das compras: R$'))

print('_' * 40)
print('FORMAS DE PAGAMENTO')

print('[ 1 ] à vista dinheiro/cheque')
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
print('[ 5 ] fish ball cat')


print('_' * 40)
opc = input('Qual é a opção? ')

print('_' * 40)
if opc == '1':
    pre2 = (pre - (pre * 10  / 100))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(pre,pre2))

elif opc == '2':
    pre2 = (pre - (pre * 5  / 100))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(pre,pre2))

elif opc == '3':
    pre2 = pre 
    parcela = pre2 / 2

    print('Sua compra será parcelada em 2X de R${:.2f} SEM JUROS'.format(parcela))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(pre,pre2))

elif opc == '4':
    pre2 = pre + (pre * 20 / 100)
    tparcela = int(input('Quantas parcelas? '))
    parcela = pre2 / tparcela

    print('Sua compra será parcelada em {}X de R${:.2f} COM JUROS'.format(tparcela,parcela))
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(pre,pre2))

elif opc == '5':
    print('ain~')

else:
    pre2 = 0
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente!')
    print('Sua compra de R${:.2f} vai custar {:.2f} no final'.format(pre,pre2))

# atividade 47



