import menu
from menu import R,G,Y,C,W
import sys
from math import sqrt

import basic_funcs as BF


msg_menu_inicial = f"""{G}BEM VINDO AO PROGRAMA DE DESVIO PADRÃO{W}

{Y}[1]{W} Dados não agrupados
{Y}[2]{W} Dados agrupados {Y}sem{W} classe
{Y}[3]{W} Dados agrupados {Y}com{W} classe

{Y}[0]{W} Sair
"""
msg_simples = f"""{G}DADOS NÃO AGRUPADOS{W}

{Y}[1]{W} Amostra
{Y}[2]{W} População (A desenvolver)

{Y}[0]{W} Voltar
"""
msg_grup = f"""{G}DADOS AGRUPADOS SEM CLASSE{W}

{Y}[1]{W} Amostra
{Y}[2]{W} População (A desenvolver)

{Y}[0]{W} Voltar
"""
msg_grup_classe = f"""{G}DADOS AGRUPADOS POR CLASSES{W}

{Y}[1]{W} Amostra
{Y}[2]{W} População (A desenvolver)

{Y}[0]{W} Voltar
"""

#--------------------------------
def soma(*args):
	soma = 0
	for arg in args[0]:
		soma += arg
	return soma

def soma2(*args):
	new_x = [x**2 for x in args[0]]
	return soma(new_x)

def calc_xini(indx, nums):
	xini = []
	cont = 0
	for n in nums:
		xini.append(round(indx[cont]*n, 2))
		cont += 1
	print(f"XINI = {xini}")
	return xini

# Funções de computar dados
# -------------------------
def computar_dados(numeros):
	N = len(numeros)

	print(f"{C}---- Calculando as somas ----{W}")
	soma_ni = round(soma(numeros),2)
	soma_ni2 = round(soma2(numeros),2)
	print(f"Soma Ni =  {soma_ni}")
	print(f"Soma Ni² =  {soma_ni2}")

	print(f"{C}---- Calculando média ----{W}")
	media = round(soma_ni / N, 2)
	x_2 = round(media**2, 2)
	print(f"Média =  {soma_ni} / {N}  = {media}")
	print(f"Média² =  {x_2}")

	print(f"{C}---- Calculando Frequencias ----{W}")
	fi = [round(x/soma_ni,2) for x in numeros]
	soma_fi = soma(fi)

	print(f"{C}---- Calculando Desvio Padrão ----{W}")
	s2 = round((soma_ni2 - N * x_2) / (N-1), 2)
	s = round(sqrt(s2), 2)
	print(f"s² =  ({soma_ni2} - {N} * {x_2}) / ({N}- 1)  = {s2}")
	print(f"s =  {s}")

	print(f"{G}--> Done !\n{W}")
	values = {'numeros': numeros, 'ni2': [n**2 for n in numeros], 'N': N, 'soma_ni': soma_ni, 'soma_ni2': soma_ni2, 
			'media': media, 'x_2': x_2, 's2': s2, 's': s, 'fi': fi, 'soma_fi':soma_fi}
	return values



def computar_dados_grup(numeros):	
	N = len(numeros)
	indexes = BF.pede_frequencias(numeros)

	xini = calc_xini(indexes, numeros)
	xi2ni = calc_xini(indexes, xini)
	
	print(f"{C}---- Calculando as somas ----{W}")
	soma_ni = round(soma(numeros),2)
	soma_xini = round(soma(xini),2)
	soma_xi2ni = round(soma(xi2ni),2)
	
	print(f"{C}---- Calculando média ----{W}")
	media = round(soma_xini / soma_ni, 2)
	x_2 = round(media**2, 2)
	print(f"Média =  {soma_xini} / {soma_ni}")
	print(f"Média² =  {x_2}")

	print(f"{C}---- Calculando Desvio Padrão ----{W}")
	s2 = round((soma_xi2ni - soma_ni * x_2) / (soma_ni-1), 2)
	s = round(sqrt(s2),2)
	print(f"s² =  ({soma_xi2ni} - {soma_ni} * {x_2}) / ({soma_ni}- 1)")
	print(f"s =  {s}")

	print(f"{G}--> Done !\n{W}")
	values = {'indexes': indexes,'numeros': numeros, 'soma_ni': soma_ni, 'xini': xini, 'xi2ni': xi2ni,
			  'soma_xini': soma_xini, 'soma_xi2ni': soma_xi2ni, 'media': media, 'x_2': x_2, 's2': s2, 's': s}
	return values

def computar_dados_grup_classe(numeros):
	N = len(numeros)
	classes = BF.pedir_classes(numeros)
	#classes = ['2.35,2.55', '2.55,2.75', '2.75,2.95', '2.95,3.15', '3.15,3.35', '3.35,3.55']
	#classes = [classe.split(',') for classe in classes]
	print(f"{C}---- Calculando dados da tabela ----{W}")
	xi = BF.calc_pontos_medios_classes(classes)
	xi2 = [x**2 for x in xi]
	xini = calc_xini(xi, numeros)
	xi2ni = calc_xini(xi2, numeros)

	print(f"{C}---- Calculando as somas ----{W}")
	soma_ni = round(soma(numeros),2)
	soma_xini = round(soma(xini),2)
	soma_xi2ni = round(soma(xi2ni),2)
	
	print(f"{C}---- Calculando média ----{W}")
	media = round(soma_xini / soma_ni, 2)
	x_2 = round(media**2, 2)
	print(f"Média =  {soma_xini} / {soma_ni}")
	print(f"Média² =  {x_2}")

	print(f"{C}---- Calculando Desvio Padrão ----{W}")
	s2 = round((soma_xi2ni - soma_ni * x_2) / (soma_ni-1),2)
	s = round(sqrt(s2),2)
	print(f"s² =  ({soma_xi2ni} - {soma_ni} * {x_2}) / ({soma_ni}- 1)")
	print(f"s =  {s}")

	print(f"{G}--> Done <--\n{W}")
	values = {'classes': classes,'numeros': numeros,'xi':xi,'xi2':xi2,'xini':xini,'xi2ni': xi2ni, 
			  'soma_ni': soma_ni, 'soma_xini': soma_xini, 'soma_xi2ni': soma_xi2ni, 
			  'media': media, 'x_2': x_2, 's2': s2, 's':s}
	return values


#### GRÁFICOS

# Funções de montagem dos gráficos
# --------------------------------
def montar_graf_simples(values):
	header = "      ni    |    ni²   \n"
	escopo = header
	for n in values['numeros']:
		linha = f"      {n}".ljust(12) + f"|    {n**2}".ljust(10) + "\n"
		escopo += linha
	linha_soma = f"\nsoma= {values['soma_ni']}".ljust(13)+ f"|    {values['soma_ni2']}"
	escopo += linha_soma
	escopo += f"\n{C}___________________________{W}\n\n"
	return escopo

def montar_graf_grup(values):
	header = "      xi   |   ni   |   xi.ni  |   xi².ni   \n"
	escopo = header
	indx = 0
	for xi in values['indexes']:
		linha = f"      {xi}".ljust(11) + \
				f"|   {values['numeros'][indx]}".ljust(9) + \
				f"|    {values['xini'][indx]}".ljust(11) + \
				f"|    {values['xi2ni'][indx]}".ljust(10) + \
				"\n"
		escopo += linha
		indx += 1
	linha_soma = f"\nsoma= ".ljust(12)+ \
				 f"|  {values['soma_ni']}".ljust(9) + \
				 f"|  {values['soma_xini']}".ljust(11) + \
				 f"|  {values['soma_xi2ni']}".ljust(10)
	escopo += linha_soma
	escopo += "\n________________________________\n\n"
	return escopo

def montar_graf_grup_classe(values):
	header = "    Classes   |   ni   |   xi   |   xi²   |   xi.ni  |   xi².ni   \n"
	cels_len = [len(cel) for cel in header.split('|')]
	escopo = header
	indx = 0
	for classe in values['classes']:
		linha = f"   {classe[0]}|-{classe[1]}".ljust(cels_len[0]) + \
				f"|   {values['numeros'][indx]} ".ljust(cels_len[1]) + \
				f"|   {values['xi'][indx]}" .ljust(cels_len[2]) + \
				f"|    {values['xi2'][indx]} ".ljust(cels_len[3]) + \
				f"|    {values['xini'][indx]} ".ljust(cels_len[4]) + \
				f"|    {values['xi2ni'][indx]} ".ljust(cels_len[5]) + \
				"\n"
		escopo += linha
		indx += 1
	linha_soma = f"\nsoma= ".ljust(15)+ \
				 f"|   {values['soma_ni']}".ljust(9) + \
				 f"|".ljust(9) + \
				 f"|".ljust(9) + \
				 f"|    {values['soma_xini']}".ljust(11) + \
				 f"|    {values['soma_xi2ni']}".ljust(10)
	escopo += linha_soma
	escopo += "\n________________________________\n\n"
	return escopo


# --------- Main Functions ----------

def mudar_id(novo_id):
	global id_menu
	id_menu = novo_id
	return id_menu

def muda_pede():
	global pede
	pede = not pede

# -----------------------------------

def run_simples_amostra():

	numeros = BF.pede_numeros()
	values = computar_dados(numeros)
	
	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(montar_graf_simples(values))

	print(f"Soma xi = {values['soma_ni']}")
	print(f"N = {values['N']}")
	print(f"Média = {values['media']}")
	print(f"x_2 = ({values['soma_ni']} / {values['N']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_ni2']} - {values['N']} * {values['x_2']}) / {values['N']-1}  = {values['s2']}")
	print(f"s = {values['s']}")

def run_grupo_amostra():

	numeros = BF.pede_numeros()
	values = computar_dados_grup(numeros)

	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(montar_graf_grup(values))

	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xi²ni = {values['soma_xi2ni']}")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Média = {values['media']}")
	print(f"x_2 = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xi2ni']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")

def run_grupo_class_amostra():

	numeros = BF.pede_numeros()		
	values = computar_dados_grup_classe(numeros)

	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(montar_graf_grup_classe(values))

	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xi2ni = {values['soma_xi2ni']}")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Média = {values['media']}")
	print(f"x_2 = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xi2ni']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")

menu_inicial = menu.Menu(nome="Inicial", id=0, msg=msg_menu_inicial, 
						 op_dict={0:[(sys.exit,[])], 
						 		  1:[(mudar_id,[1])],
						 		  2:[(mudar_id,[2])],
						 		  3:[(mudar_id,[3])]
						 		  })
menu_simples = menu.Menu(nome="Simples", id=1, msg=msg_simples, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_simples_amostra,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })
menu_grup = menu.Menu(nome="Grupo sem Classe", id=2, msg=msg_grup, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_grupo_amostra,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })
menu_grup_classe = menu.Menu(nome="Grupo por Classe", id=3, msg=msg_grup_classe, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_grupo_class_amostra,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })
if __name__ == '__main__':
	running = True
	menus = {0:menu_inicial, 1:menu_simples, 2:menu_grup, 3:menu_grup_classe}
	id_menu = 0

	while running:
		try:
			menu_ativo = menus[id_menu]
			print(menu_ativo.msg)
			op = int(input("op :"))
			menu_ativo.valida_opcao(op)
			menu_ativo.exec_funcs(op)
		except SystemExit:
			running = False
		except:
			print(f"{R}ops... algo deu ruim{W}")
