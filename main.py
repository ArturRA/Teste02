import datetime

class Maquina:
	def __init__(self, nome_maquina, preco_de_aquisicao_da_maquina, numero_de_serie, data_de_fabricacao, fabricante):
		self.nome_maquina = nome_maquina
		self.preco_de_aquisicao_da_maquina = preco_de_aquisicao_da_maquina
		self.numero_de_serie = numero_de_serie
		self.data_de_fabricacao = data_de_fabricacao
		self.fabricante = fabricante


# Verifica se a maquina e valido
def register_machine(empresa):

	# 1. Validar nome da maquina
	nome_maquina = ''
	while True:
		nome_maquina = input('Digite o nome da maquina(deve possuir no minimo 6 digitos): ')
		if len(nome_maquina) < 6:
			print('Input e muito curto.')
			continue
		else:
			break

	# 2. Validar preco de aquisicao da maquina
	preco_de_aquisicao_da_maquina = 0
	while True:
		try:
			preco_de_aquisicao_da_maquina = float(input('Digite o preco de aquisicao da maquina(use "." ): '))
		except ValueError:
			print('Input nao e um numero.')
			continue
		if preco_de_aquisicao_da_maquina > 0:
			break
		else:
			print('Input deve ser maior que zero')
	
	# 3. Validar numero de serie
	numero_de_serie = ''
	while True:
		numero_de_serie = input('Digite o numero de serie: ')
		if len(numero_de_serie) < 1:
			print('Input e muito curto.')
			continue
		else:
			break

	# 4. Valida data de fabricacao
	data_de_fabricacao = ''
	while True:
		data_de_fabricacao = input('Digite a data de fabricacao no formato dd/mm/yy: ')
		dia, mes, ano = data_de_fabricacao.split('/')
		isValidDate = True
		try:
			datetime.datetime(int(ano), int(mes), int(dia))
		except ValueError:
			isValidDate = False
		if(isValidDate):
			break
		else:
			print("Input date is not valid..")

	# 5. Validar fabricante
	fabricante = ''
	while True:
		fabricante = input('Digite o nome da fabricante: ')
		if len(numero_de_serie) < 1:
			print('Input e muito curto.')
			continue
		else:
			break
	empresa.append(Maquina(nome_maquina, preco_de_aquisicao_da_maquina, numero_de_serie, data_de_fabricacao, fabricante))

if __name__ == "__main__":

	empresa = list()

	while True:
		lang  = input('Digite o numero da operacao desejada:\n' +
					  '1. Registrar maquina.\n')
		match lang:
			case "1":
				register_machine(empresa)
				#print(empresa[0].__dict__)
				continue
			case _:
				break

		
















# Verifica qual o tipo de triangulo
def type_of_triangle(a,b,c):
	if a==b and b==c:
		print('Triangulo e equilatero.\n')
	elif a==b or b==c or a==c:
		print('Triangulo e isosceles.\n')
	else:
		print('Triangulo e escaleno\n')

if __name__ == "__main__":
	
	executar = True
	while(executar):
		# Lendo as entradas exemplo: 15;17.5;9
		entradas = input('Digite os valores de a, b e c separados por ";" e usando "." para separar a parte decimal.\n' +
						 'Exemplo: 15;17.5;9\n')
		lista_de_entradas = entradas.split(";")
		a = float(lista_de_entradas[0])
		b = float(lista_de_entradas[1])
		c = float(lista_de_entradas[2])

		if is_triangle(a,b,c):
			type_of_triangle(a,b,c)
		else:
			print('Triangulo e invalido.\n')

		continuar = ''
		while continuar != 'sim' and continuar != 'nao':
			continuar = input('Deseja checar mais um triangulo? Responda sim ou nao.\n')
			if continuar == 'sim':
				executar = True
			elif continuar == 'nao':
				executar = False
				print('Terminando o programa...')
			else:
				print('Comando invalido.')

	