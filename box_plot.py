import mmm
import desvio_padrao
import menu
from menu import R,G,Y,C,W
import sys
from math import sqrt

import basic_funcs as BF

msg_menu_inicial = f"""{G}BEM VINDO AO PROGRAMA DE BOX-PLOT{W}

{Y}[1]{W} Dados não agrupados

{R}[2]{W} Dados agrupados {Y}sem{W} classe
{R}[3]{W} Dados agrupados {Y}com{W} classe

{Y}[0]{W} Sair
"""

msg_simples = f"""{G}SIMPLES{W}

{Y}[1]{W} INICIAR

{R}[2]{W} Dados agrupados {Y}sem{W} classe
{R}[3]{W} Dados agrupados {Y}com{W} classe

{Y}[0]{W} Voltar
"""

# -- Funções / atributos geral --
id_menu = 0

def mudar_id(novo_id):
	global id_menu
	id_menu = novo_id
	return id_menu

def calc_quartil(nums, tp_q):
	len_nums = len(nums)
	nums.sort()
	if tp_q != 2:
		if len_nums%2 == 0:
			indice1 = int((len_nums)/2)
		else:
			indice1 = int((len_nums+1)/2)

		if indice1%2 == 0:
			ind1 = int(indice1/2)
			if tp_q == 1:
				indice1 = indice1-ind1
				indice2 = indice1 + 1
			elif tp_q == 3:
				indice1 = indice1+ind1
				indice2 = indice1+1
			quartil = (nums[indice1-1]+nums[indice2-1])/2 
		else:
			ind1 = int((indice1+1)/2)
			if tp_q == 1:
				indice1 = indice1-ind1
				quartil = nums[indice1]
			elif tp_q == 3:
				indice1 = indice1+ind1
				quartil = nums[indice1-2]
		
	else:
		quartil = mmm.calc_mediana(nums)
	return quartil

def calc_quartis_simples(nums):
	print(f"{C}---- Calculando os Quartis ----{W}")
	q1 = calc_quartil(nums, 1)
	q2 = calc_quartil(nums, 2)
	q3 = calc_quartil(nums, 3)
	return {'q1':q1,'q2':q2,'q3':q3}


def calc_quartil_grupos(values):
	print(f"{C}---- Calculando os Quartis ----{W}")

	quartil1 = values['li'] + (((25*values['soma_ni'])/100 - values['facant'])*values['h']) / values['fmod']
	quartil2 = values['mediana']
	quartil3 = values['li'] + (((75*values['soma_ni'])/100 - values['facant'])*values['h']) / values['fmod']


	print(f"quartil1 = {values['li']} + (((25*{values['soma_ni']})/100 - {values['facant']})*{values['h']}) / {values['fmod']}  = {quartil1}")
	print(f"quartil2 = {values['mediana']}")
	print(f"quartil3 = {values['li']} + (((75*{values['soma_ni']})/100 - {values['facant']})*{values['h']}) / {values['fmod']}  = {quartil3}")

	return {'q1':round(quartil1, 2), 'q2':round(quartil2, 2), 'q3':round(quartil3, 2)}

def calc_percentil(values, perc):
	percentil = (values['N']*perc)/100
	print(f"percentil = ({values['N']}*{perc}) / 100")
	return percentil

def calc_percentil_classe(values, perc):
	percentil = values['li'] + (((perc*values['soma_ni'])/100 - values['facant'])*values['h']) / values['fmod']
	print(f"percentil = {values['li']} + ((({perc}*{values['soma_ni']})/100 - {values['facant']})*{values['h']}) / {values['fmod']}")
	return percentil

def calc_assimetria(values):
	print(f"{C}---- Calculando a Assimetria ----{W}")
	assimetria = (values['media']-values['moda'][0])/values['s']

	string = f"Assimetria = ( {values['media']} - {values['moda'][0]} ) / {values['s']}  = {assimetria}"
	print(string)

	return round(assimetria, 2)

def calc_assimetria_classe(values):
	print(f"{C}---- Calculando a Assimetria ----{W}")
	assimetria = (values['media']-values['moda'])/values['s']

	string = f"Assimetria = ({values['media']} - {values['moda']} ) / {values['s']}  = {assimetria}"
	print(string)

	return round(assimetria, 2)

def calc_curtose(values):
	print(f"{C}---- Calculando a Curtose ----{W}")
	amplitude = (values['q3'] - values['q1'])
	curtose = amplitude / 2*(calc_percentil(values, 90) - calc_percentil(values, 10))

	print(f"Amplitude = {values['q3']} - {values['q1']}  = {amplitude}")
	print(f"Curtose = {amplitude} / 2*({calc_percentil(values, 90)} - {calc_percentil(values, 10)})  = {curtose}")
	return curtose

def calc_curtose_classe(values):
	print(f"{C}---- Calculando a Curtose ----{W}")
	amplitude = (values['q3'] - values['q1'])

	soma = 0
	res_str = ""
	print(f"pontos médios = {values['xi']}")
	for pm in values['xi']:
		res = (pm-values['media'])**4
		res_str += f"({pm}-{values['media']})^4 + "
		soma += res
	m4 = soma / values['soma_ni']
	print(f"M4 = {res_str} / {values['soma_ni']}")
	curtose = m4 / (values['s']**4)
	print(f"Curtose = M^4 / s^4  =  {m4} / {values['s']**4}")
	return curtose

def run_simples():
	#numeros = BF.pede_numeros()
	#numeros = [22.0, 29.0, 33.0, 35.0, 35.0, 37.0, 38.0, 43.0, 43.0, 44.0, 48.0, 48.0, 52.0, 53.0, 55.0, 57.0, 61.0, 62.0, 67.0, 69.0]
	numeros = [6.9, 6.9, 7.0, 7.1, 7.2, 7.2, 7.2, 7.3, 7.3, 7.3, 7.3, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.4, 7.5, 7.5, 7.5, 7.5, 7.5, 7.5, 7.6, 7.6, 7.6, 7.6, 7.6, 7.6, 7.7, 7.7, 7.7, 7.8, 7.9, 8.1, 8.1, 8.1, 8.2, 8.2]
	numeros.sort()
	media = mmm.calc_media_simples(numeros)
	mediana = mmm.calc_mediana(numeros)
	moda = mmm.calc_moda(numeros)
	
	quartil1 = calc_quartil(numeros, 1)
	quartil2 = calc_quartil(numeros, 2)
	quartil3 = calc_quartil(numeros, 3)

	values_dp = desvio_padrao.computar_dados(numeros)
	values_dp.update({'q1': quartil1, 'q3': quartil3})
	values_dp.update({'mediana': mediana, 'moda': moda})
	assimetria = calc_assimetria(values_dp)
	curtose = calc_curtose(values_dp)

	print(f"Média: {media}")
	print(f"Mediana: {mediana}")
	print(f"Moda: {moda}")
	print("-------")
	print(f"1º Quartil : {quartil1}")
	print(f"2º Quartil : {quartil2}")
	print(f"3º Quartil : {quartil3}")
	print(f"Assimetria: {assimetria}")
	print(f"Curtose: {curtose}")


def run_classe():
	numeros = BF.pede_numeros()
	values = desvio_padrao.computar_dados_grup_classe(numeros)

	values.update(mmm.calc_valores_mmm_classes(values))
	mediana = mmm.calc_mediana_classe(values)
	moda = mmm.calc_moda_classe(values)

	values.update({'mediana': mediana, 'moda': moda})
	quartil1, quartil2, quartil3 = calc_quartil_grupos(values)
	values.update({'q1': quartil1, 'q3': quartil3})
	assimetria = calc_assimetria_classe(values)
	curtose = calc_curtose_classe(values)

	print(f"Média: {values['media']}")
	print(f"Mediana: {mediana}")
	print(f"Moda: {moda}")
	print("-------")
	print(f"1º Quartil : {quartil1}")
	print(f"2º Quartil : {quartil2}")
	print(f"3º Quartil : {quartil3}")
	print(f"Assimetria : {assimetria}")
	print(f"Curtose : {curtose}")
	
if __name__ == '__main__':
	run_simples()
	run_classe()

menu_inicial = menu.Menu(nome="Inicial", id=0, msg=msg_menu_inicial, 
						 op_dict={0:[(sys.exit,[])], 
						 		  1:[(mudar_id,[1])]
						 		  })

menu_simples = menu.Menu(nome="Simples", id=1, msg=msg_simples, 
						 op_dict={0:[(mudar_id,[0])],
						 		  1:[(run_simples,[])],
						 		  2:[(print,[f"{R}FUNCIONALIDADE EM DESENVOLVIMENTO{W}"])],
						 		  })