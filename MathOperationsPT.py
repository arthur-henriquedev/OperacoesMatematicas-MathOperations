#Coleta de dados
while True: 
    valor_a = int(input("Digite o valor a: "))
    valor_b = int(input("Digite o valor b: "))

#Operações lógicas
    soma = valor_a + valor_b
    subtracao = valor_a - valor_b   
    multiplicacao = valor_a * valor_b
    divisao = valor_a / valor_b

#Confirmação dos valores
    print("Os valores dados são: ", valor_a, " e ", valor_b)
    
    continuar = input("Deseja prosseguir com esses valores? (S/N): ").strip().upper()

#Processo matemático  
    if continuar == "S": 
        while True:  
            print("Qual operação deseja realizar? (+, -, *, /):")
            operacao = input().strip()

            if operacao == "+":
                print("A soma dos valores é: ", soma)
                break  
            elif operacao == "-":
                print("A subtração dos valores é: ", subtracao)
                break
            elif operacao == "*":
                print("A multiplicação dos valores é: ", multiplicacao)
                break
            elif operacao == "/":
                print("A divisão dos valores é: ", divisao)
                break
            else:
                print("Operação inválida, insira um operador matemático válido (+, -, *, /):")

         
    elif continuar == "N": 
        print("Reinsira os novos valores abaixo.")
        continue 
