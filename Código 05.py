nota1 =  int(input('Digite sua primeira nota: '))
nota2 = int(input('Digite sua segunda nota: '))
nota3 = int(input('Digite sua terceira nota: '))


media = int(nota1 + nota2 + nota3) / 3


if media >= 7:
    print('Aprovado')


else:
    print('Reprovado')
