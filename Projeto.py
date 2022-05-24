print("================== SEU PESO IDEAL ==================")
print("SEJA BEM VINDO AO SEU PESO IDEAL \nME DIGA SEU NOME, SUA IDADE, E SUA ALTURA A SEGUIR...")
nome = str(input("NOME: "))
idade = int(input("IDADE: "))
altura = float(input("ALTURA: "))
peso = float(input("PESO ATUAL: "))
pesoIdeal = (72.7 * altura) - 58
print("DADOS FORNECIDOS:\n- NOME: {} \n- IDADE: {} \n- ALTURA: {} \n- PESO: {:.2f}".format(nome, idade, altura, peso))
if peso > pesoIdeal:
    print("{} DE ACORDO COM OS DADOS FORNECIDOS, VOCÊ ESTA ACIMA DO SEU PESO IDEAL\nE ISSO É PREJUDICIAL A SUA SAÚDE, VOCÊ PRECISA CHEGAR AO PESO {:.2f} PARA SE MANTER EM FORMA !!".format(nome, pesoIdeal))
elif peso <= pesoIdeal:
    print("PARABÉNS {} SEU PESO ESTÁ DE ACORDO COM O SEU PESO IDEAL\n- PESO ATUAL: {:.2f}\n- PESO IDEAL: {:.2f}".format(nome, peso, pesoIdeal))