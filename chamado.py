import datetime

class Chamado:
	def __init__(self, titulo_do_chamado, descricao_do_chamado, id_do_equipamento, data_de_abertura):
		self.titulo_do_chamado = titulo_do_chamado
		self.descricao_do_chamado = descricao_do_chamado
		self.id_do_equipamento = id_do_equipamento
		self.data_de_abertura = data_de_abertura


def validar_titulo_do_chamado():
	titulo_do_chamado = ''
	while True:
		titulo_do_chamado = input('Digite o titulo do chamado: ')
		if len(titulo_do_chamado) < 1:
			print('Input e muito curto.')
			continue
		else:
			break
	return titulo_do_chamado

def validar_descricao_do_chamado():
	descricao_do_chamado = ''
	while True:
		descricao_do_chamado = input('Digite a descricao do chamado: ')
		if len(descricao_do_chamado) < 1:
			print('Input e muito curto.')
			continue
		else:
			break
	return descricao_do_chamado

def validar_id_do_equipamento(empresa):
	if len(empresa) == 0:
		print('Empresa nao possui maquinas registradas.')
	else:
		print('Lista de maquinas registradas:')
		for x in range(len(empresa)):
			print(str(x + 1) + ': Nome da maquina: ' + empresa[x].nome_maquina + '; numero de serie: ' + empresa[x].numero_de_serie + '; fabricante: ' + empresa[x].fabricante)
		maquina_para_criar_chamado = ''
		while True:
			maquina_para_criar_chamado = int(input('Digite o numero da maquina que deseja criar um chamado: ')) - 1
			if 0 <= maquina_para_criar_chamado < len(empresa):
				break
			else:
				print('Input nao esta dentro do tamanho da lista.')
				continue
	return empresa[maquina_para_criar_chamado].id_da_maquina

def validar_data_de_abertura():
	data_de_abertura = ''
	hoje = datetime.date.today()
	while True:
		data_de_abertura = input('Digite a data de abertura no formato dd/mm/yyyy: ')
		dia, mes, ano = data_de_abertura.split('/')
		isValidDate = True
		try:
			datetime.datetime(int(ano), int(mes), int(dia))
			data_de_abertura_date = datetime.date(int(ano), int(mes), int(dia))
		except ValueError:
			isValidDate = False
		# Input tem que ser tando valido como ser uma data antes da data retornada pelo metodo datetime.date.today()
		if(isValidDate and hoje > data_de_abertura_date):
			break
		else:
			print("Input date is not valid..")
	return data_de_abertura

def dias_chamado_aberto(data_de_abertura):
	hoje = datetime.date.today()
	dia, mes, ano = data_de_abertura.split('/')
	data_de_abertura_date = datetime.date(int(ano), int(mes), int(dia))
	dias_chamado_aberto = hoje - data_de_abertura_date
	return str(dias_chamado_aberto.days)

# 1.1 Registrar chamado na empresa
def register_chamado(empresa, chamados):
	# 1. Validar titulo do chamado
	titulo_do_chamado = validar_titulo_do_chamado()

	# 2. Validar descricao do chamado
	descricao_do_chamado = validar_descricao_do_chamado()
	
	# 3. Validar id do equipamento
	id_do_equipamento = validar_id_do_equipamento(empresa)

	# 4. Validar data de abertura
	data_de_abertura = validar_data_de_abertura()

	chamados.append(Chamado(titulo_do_chamado, descricao_do_chamado, id_do_equipamento, data_de_abertura))

# 1.2 Imprime uma lista de todas os chamados registradas
def check_chamados(empresa, chamados):
	machine_info = ''
	if len(chamados) == 0:
		print('Empresa nao possui chamados registradas.')
	else:
		print('Lista de chamados registradas:')
		for x in range(len(chamados)):
			for y in range(len(empresa)):
				if empresa[y].id_da_maquina == chamados[x].id_do_equipamento:
					machine_info = '; nome da maquina: ' + empresa[y].nome_maquina + '; numero de serie: ' + empresa[y].numero_de_serie + '; fabricante: ' + empresa[y].fabricante
					break
			print(str(x + 1) + ': Titulo do chamado: ' + chamados[x].titulo_do_chamado + machine_info +
					'; descricao do chamado: ' + chamados[x].descricao_do_chamado + '; dias que o chamado esta aberto: ' + dias_chamado_aberto(chamados[x].data_de_abertura))

# 1.3 Editar chamados registrados
def edit_chamados(chamados):
	if len(chamados) == 0:
		print('Empresa nao possui chamados registrados.')
	else:
		check_chamados(chamados)
		chamado_para_editar = ''
		while True:
			chamado_para_editar = int(input('Digite o numero do chamado que deseja editar: ')) - 1
			if 0 <= chamado_para_editar < len(chamados):
				break
			else:
				print('Input nao esta dentro do tamanho da lista.')
				continue
	while True:
		operacao_de_edicao  = input('Digite o numero da operacao desejada:\n' +
									'1. Editar o titulo do chamado.\n' +
									'2. Editar a descricao do chamado.\n' +
									'3. Editar a maquina do chamado.\n' +
									'4. Editar data de abertura.\n' +
									'5. Parar a edicao.\n')
		match operacao_de_edicao:
			case '1':
				titulo_do_chamado = validar_titulo_do_chamado()
				chamados[chamado_para_editar].titulo_do_chamado = titulo_do_chamado
				continue
			case '2':
				descricao_do_chamado = validar_descricao_do_chamado()
				chamados[chamado_para_editar].descricao_do_chamado = descricao_do_chamado
				continue
			case '3':
				id_do_equipamento = validar_id_do_equipamento()
				chamados[chamado_para_editar].id_do_equipamento = id_do_equipamento
				continue
			case '4':
				data_de_abertura = validar_data_de_abertura()
				chamados[chamado_para_editar].data_de_abertura = data_de_abertura
				continue
			case _:
				break

# 1.4 Excluir chamado registrado
def delete_chamado(empresa, chamados):
	if len(chamados) == 0:
		print('Empresa nao possui chamados registrados.')
	else:
		check_chamados(empresa, chamados)
		chamado_para_excluir = ''
		while True:
			chamado_para_excluir = int(input('Digite o numero do chamado que deseja excluir: ')) - 1
			if 0 <= chamado_para_excluir < len(chamados):
				break
			else:
				print('Input nao esta dentro do tamanho da lista.')
				continue
		chamados.pop(chamado_para_excluir)