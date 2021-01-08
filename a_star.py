
def busca(mapa, heuristica, ponto_inicial, ponto_final, custo, setas_aux, setas):

	lista_fechada = [[0 for row in range(len(mapa[0]))] for col in range(len(mapa))]
	lista_fechada[ponto_inicial[0]][ponto_inicial[1]] = 1

	expand = [[-1 for row in range(len(mapa[0]))] for col in range(len(mapa))]
	acoes_agente = [[-1 for row in range(len(mapa[0]))] for col in range(len(mapa))]

	path = [[' ' for row in range(len(mapa[0]))] for col in range(len(mapa))]

	x = ponto_inicial[0]
	y = ponto_inicial[1]

	g = 0
	f = g + heuristica[x][y]

	lista_aberta = [[f, g, x, y]]

	finalizado = False
	acabou_exp = False
	cont = 0

	while (not finalizado and not acabou_exp):

		if (len(lista_aberta) == 0):

			acabou_exp = True
			return 'fail'

		else:

			lista_aberta.sort()
			lista_aberta.reverse()
			proximo_no = lista_aberta.pop()
			f = proximo_no[0]
			g = proximo_no[1]
			x = proximo_no[2]
			y = proximo_no[3]

			expand[x][y] = cont
			cont = cont + 1

			if (x == ponto_final[0] and y == ponto_final[1]):

				finalizado = True

			else:

				for i in range(len(setas_aux)):

					x_aux = x + setas_aux[i][0]
					y_aux = y + setas_aux[i][1]

					if (x_aux >= 0 and x_aux < len(mapa) and y_aux >= 0 and y_aux < len(mapa[0])):

						if (lista_fechada[x_aux][y_aux] == 0 and mapa[x_aux][y_aux] == 0):

							g_aux = g + custo
							f_aux = g_aux + heuristica[x_aux][y_aux]

							lista_aberta.append([f_aux, g_aux, x_aux, y_aux])

							lista_fechada[x_aux][y_aux] = 1
							acoes_agente[x][y] = i

	x = 0
	y = 0

	while (x != ponto_final[0] or y != ponto_final[1]):

		x_aux = x + setas_aux[acoes_agente[x][y]][0]
		y_aux = y + setas_aux[acoes_agente[x][y]][1]
		path[x][y] = setas[acoes_agente[x][y]]
		x = x_aux
		y = y_aux

	path[ponto_final[0]][ponto_final[1]] = '*'

	return path

mapa = [[0, 0, 1, 0, 0, 0, 0, 0, 1],
		[0, 0, 1, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 0, 0, 1],
		[1, 1, 1, 0, 0, 1, 0, 0, 1],
		[0, 0, 0, 0, 0, 1, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 1],
		[0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 1, 1, 1, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0]]

heuristica = [[17, 16, 15, 14, 13, 12, 11, 10, 9],
			  [16, 15, 14, 13, 12, 11, 10,  9, 8],
			  [15, 14, 13, 12, 11, 10,  9,  8, 7],
			  [14, 13, 12, 11, 10,  9,  8,  7, 6],
			  [13, 12, 11, 10,  9,  8,  7,  6, 5],
			  [12, 11, 10,  9,  8,  7,  6,  5, 4],
			  [11, 10,  9,  8,  7,  6,  5,  4, 3],
			  [10,  9,  8,  7,  6,  5,  4,  3, 2],
			  [ 9,  8,  7,  6,  5,  4,  3,  2, 1],
			  [ 8,  7,  6,  5,  4,  3,  2,  1, 0]]

ponto_inicial = [0, 0]
ponto_final = [9, 8]
custo = 1

setas_aux = [[-1, 0],
		 [0, -1],
		 [1, 0],
		 [0, 1]]

setas = ['^', '<', 'v', '>']

resultado = busca(mapa, heuristica, ponto_inicial, ponto_final, custo, setas_aux, setas)

print('################# TRAJETORIA ##################')
print()
for x in range(len(resultado)):
	print(resultado[x])
print()
print('###############################################')
print('############ LISTA DAS COORDENADAS ############')
print()
lista_coordenadas = []
for i in range(len(resultado)):
	for j in range(len(resultado[i])):
		valor = resultado[i][j]
		if setas.count(valor) == 1:
			lista_coordenadas.append([i, j])

print(lista_coordenadas)
print()
print('###############################################')
