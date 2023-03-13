from maquina import Maquina
from chamado import Chamado




if __name__ == "__main__":

	empresa = list()
	id_da_maquina = 0
	empresa.append(Maquina(999,'testtest',5,'basic1','01/01/2023','artur'))
	empresa.append(Maquina(1000,'testtest2',5,'basic1','01/01/2023','artur'))
	chamados = list()
	chamados.append(Chamado('chamado 1','descicao 1',999,'01/03/2023'))
	chamados.append(Chamado('chamado 2','descicao 2',1000,'10/03/2023'))

	while True:
		operacao  = input('Digite o numero da operacao desejada:\n' +
					  '1. Registrar maquina.\n' +
					  '2. Verificar maquinas registradas.\n' +
					  '3. Editar maquina registrada.\n' +
					  '4. Excluir maquina registrada.\n' +
					  '5. Registrar chamado.\n' +
					  '6. Verificar chamados registrados.\n' +
					  '7. Editar chamado registrado.\n' +
					  '8. Excluir chamado registrados.\n' +
					  '9. Terminar a execucao.\n')
		match operacao:
			case '1':
				Maquina.register_machine(empresa, id_da_maquina)
				continue
			case '2':
				Maquina.check_machines(empresa)
				continue
			case '3':
				Maquina.edit_machines(empresa)
				continue
			case '4':
				Maquina.delete_machine(empresa)
				continue
			case '5':
				Chamado.register_chamado(empresa,chamados)
				continue
			case '6':
				Chamado.check_chamados(empresa, chamados)
				continue
			case '7':
				Chamado.edit_chamados(chamados)
				continue
			case '8':
				Chamado.delete_chamado(empresa, chamados)
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

	