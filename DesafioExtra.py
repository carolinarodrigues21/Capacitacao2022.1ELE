prateleira = ['arduino','servoMotor','potenciometro','LEDverm','LEDverd','resistor1','resistor100k']
precoPrat = [74,5,1.9,1,1,0.1,0.5]

comprados = ['resistor100k','resistor100k','servoMotor','arduino', 'arduino', 'arduino', 'potenciometro']
precoPago = [0.7,1,5,100,74,2.5,0.1]

def confirma(produtos, precos, compras, preco_pago): 
    erros = 0
    tabela = dict(zip(produtos,precos))
    for i in range(len(compras)):
        if tabela[compras[i]] != preco_pago[i]:
            erros+=1
            #erros = erros + 1 
    return erros 

Erro = confirma(prateleira,precoPrat,comprados,precoPago)

print("o número de erros foi:" + str(Erro))
