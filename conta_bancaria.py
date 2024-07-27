saldo = 0.0
contador_saque = 0

extrato = []

def saque (valor):
    global saldo, contador_saque
    saldo_temporario = saldo - valor
    if valor < 0:
        print('valor invalido para saque!')
    elif contador_saque < 2 and valor <= 500.0 and saldo_temporario >= 0:
        contador_saque += 1
        saldo = saldo - valor
        extrato.append(valor * -1)
    elif saldo_temporario <= 0:
        print('Não será possível sacar o dinheiro por falta de saldo!')


def deposito (valor):
    global saldo
    if valor <= 0:
        print('valor invalido para deposito!')
    else:
        saldo = valor
        extrato.append(valor)


def ver_extrato():
    if len(extrato) == 0:
       print('Não foram realizadas movimentações') 
    else:
        for x in extrato:
            print(f'R$ {x}')
        print(f'O saldo da conta é R$ {saldo}')
            
saque(100)
deposito(100)
saque(50)
ver_extrato()
