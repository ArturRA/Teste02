import datetime

class Maquina:
	def __init__(self, id_da_maquina, nome_maquina, preco_de_aquisicao_da_maquina, numero_de_serie, data_de_fabricacao, fabricante):
		self.id_da_maquina= id_da_maquina
		self.nome_maquina = nome_maquina
		self.preco_de_aquisicao_da_maquina = preco_de_aquisicao_da_maquina
		self.numero_de_serie = numero_de_serie
		self.data_de_fabricacao = data_de_fabricacao
		self.fabricante = fabricante


def validar_nome_maquina():
	nome_maquina = ''
	while True:
		nome_maquina = input('Digite o nome da maquina(deve possuir no minimo 6 digitos): ')
		if len(nome_maquina) < 6:
			print('Input e muito curto.')
			continue
		else:
			break
	return nome_maquina

def validar_preco_de_aquisicao_da_maquina():
	preco_de_aquisicao_da_maquina = 0
	while True:
		try:
			preco_de_aquisicao_da_maquina = float(input('Digite o preco de aquisicao da maquina(use "." como divisor da casa decimal): '))
		except ValueError:
			print('Input nao e um numero.')
			continue
		if preco_de_aquisicao_da_maquina > 0:
			break
		else:
			print('Input deve ser maior que zero')
	return preco_de_aquisicao_da_maquina

def validar_numero_de_serie():
	numero_de_serie = ''
	while True:
		numero_de_serie = input('Digite o numero de serie: ')
		if len(numero_de_serie) < 1:
			print('Input e muito curto.')
			continue
		else:
			break
	return numero_de_serie

def validar_data_de_fabricacao():
	data_de_fabricacao = ''
	hoje = datetime.date.today()
	while True:
		data_de_fabricacao = input('Digite a data de fabricacao no formato dd/mm/yyyy: ')
		dia, mes, ano = data_de_fabricacao.split('/')
		isValidDate = True
		try:
			datetime.datetime(int(ano), int(mes), int(dia))
			data_de_fabricacao =datetime.date(int(ano), int(mes), int(dia))
		except ValueError:
			isValidDate = False
		# Input tem que ser tando valido como ser uma data antes da data retornada pelo metodo datetime.date.today()
		if(isValidDate and hoje > data_de_fabricacao):
			break
		else:
			print("Input date is not valid..")
	return data_de_fabricacao

def validar_fabricante():
	fabricante = ''
	while True:
		fabricante = input('Digite o nome da fabricante: ')
		if len(fabricante) < 1:
			print('Input e muito curto.')
			continue
		else:
			break
	return fabricante

# 1.1 Registra maquina na empresa
def register_machine(empresa, id_da_maquina):

	# 1. Validar nome da maquina
	nome_maquina = validar_nome_maquina()

	# 2. Validar preco de aquisicao da maquina
	preco_de_aquisicao_da_maquina = validar_preco_de_aquisicao_da_maquina()
	
	# 3. Validar numero de serie
	numero_de_serie = validar_numero_de_serie()

	# 4. Validar data de fabricacao
	data_de_fabricacao = validar_data_de_fabricacao()

	# 5. Validar fabricante
	fabricante = validar_fabricante()

	empresa.append(Maquina(id_da_maquina, nome_maquina, preco_de_aquisicao_da_maquina, numero_de_serie, data_de_fabricacao, fabricante))
	id_da_maquina += 1

# 1.2 Imprime uma lista de todas as maquinas registradas
def check_machines(empresa):
	if len(empresa) == 0:
		print('Empresa nao possui maquinas registradas.')
	else:
		print('Lista de maquinas registradas:')
		for x in range(len(empresa)):
			print(str(x + 1) + ': Nome da maquina: ' + empresa[x].nome_maquina + '; numero de serie: ' + empresa[x].numero_de_serie + '; fabricante: ' + empresa[x].fabricante)

# 1.3 Editar maquina registrada
def edit_machines(empresa):
	if len(empresa) == 0:
		print('Empresa nao possui maquinas registradas.')
	else:
		check_machines(empresa)
		maquina_para_editar = ''
		while True:
			maquina_para_editar = int(input('Digite o numero da maquina que deseja editar: ')) - 1
			if 0 <= maquina_para_editar < len(empresa):
				break
			else:
				print('Input nao esta dentro do tamanho da lista.')
				continue
	while True:
		operacao_de_edicao  = input('Digite o numero da operacao desejada:\n' +
						'1. Editar nome da maquina.\n' +
						'2. Editar preco de aquisicao da maquina.\n' +
						'3. Editar numero de serie.\n' +
						'4. Editar data de fabricacao.\n' +
						'5. Editar fabricante.\n' +
						'6. Parar a edicao.\n')
		match operacao_de_edicao:
			case '1':
				nome_maquina = validar_nome_maquina()
				empresa[maquina_para_editar].nome_maquina = nome_maquina
				continue
			case '2':
				preco_de_aquisicao_da_maquina = validar_preco_de_aquisicao_da_maquina()
				empresa[maquina_para_editar].preco_de_aquisicao_da_maquina = preco_de_aquisicao_da_maquina
				continue
			case '3':
				numero_de_serie = validar_numero_de_serie()
				empresa[maquina_para_editar].numero_de_serie = numero_de_serie
				continue
			case '4':
				data_de_fabricacao = validar_data_de_fabricacao()
				empresa[maquina_para_editar].data_de_fabricacao = data_de_fabricacao
				continue
			case '5':
				fabricante = validar_fabricante()
				empresa[maquina_para_editar].fabricante = fabricante
				continue
			case _:
				break

# 1.4 Excluir maquina registrada
def delete_machine(empresa, chamados):
	if len(empresa) == 0:
		print('Empresa nao possui maquinas registradas.')
	else:
		check_machines(empresa)
		maquina_para_deletar = ''
		while True:
			maquina_para_deletar = int(input('Digite o numero da maquina que deseja excluir(chamados relacionados a essa maquisa tambem serao deletados): ')) - 1
			if 0 <= maquina_para_deletar < len(empresa):
				break
			else:
				print('Input nao esta dentro do tamanho da lista.')
				continue
		
		while True:
			tamanho_list = len(chamados)
			posicao_atual = ''
			for x in range(len(chamados)):
				posicao_atual = x
				if chamados[x].id_do_equipamento == empresa[maquina_para_deletar].id_da_maquina:
					chamados.pop(x)
					break
			if posicao_atual == tamanho_list - 1:
				break
		empresa.pop(maquina_para_deletar)
		