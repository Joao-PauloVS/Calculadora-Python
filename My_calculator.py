#Título
print("********************************** Python calculator **********************************")

#Apresentação das opcões e recebimetno da operação desejada
print("Selecione a opção desejada: \n \n 1 - Adição \n 2 - Subtração \n 3 - Divisão \n 4 - Multiplicação \n")
opcao = int(input("Sua escolha(1/2/3/4): "))

#Laço da operação de adição
if opcao == 1:
	num1 = eval(input("Digite o primeiro número: "))
	num2 = eval(input("Digite o segundo número: "))
	def somar(num1, num2):
		print("O resultado é:", (num1 + num2))
	somar(num1, num2)

#Laço da operação de subtração
elif opcao == 2:
	num1 = eval(input("Digite o primeiro número: "))
	num2 = eval(input("Digite o segundo número: "))
	def subtrair(num1, num2):
		print("O resultado é:", (num1 - num2))
	subtrair(num1, num2)

#Laço da operação de divisão
elif opcao == 3:
	num1 = eval(input("Digite o primeiro número: "))
	num2 = eval(input("Digite o segundo número: "))
	def dividir(num1, num2):
		print("O resultado é:", (num1 / num2))
	dividir(num1, num2)

#Laço da operação de multiplicação
elif opcao == 4:
	num1 = eval(input("Digite o primeiro número: "))
	num2 = eval(input("Digite o segundo número: "))
	def multiplicar(num1, num2):
		print("O resultado é:", (num1 * num2))
	multiplicar(num1, num2)

else:
	print("A operação escolhida não é válida!")