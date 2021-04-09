import menu
import basic_funcs as BF
import computes_funcs as CF
from menu import R,G,Y,C,W

menu = f"""-----------------------------------------
TIPOS DE EXERCÍCIO:
{Y}[1]{W} Dados não agrupados
{Y}[2]{W} Dados agrupados por classe

{Y}[0]{W} Sair
-----------------------------------------
"""
def calc_mmm_simples(nums):
	"""Função para calculo de dados não agrupados"""

	print(f"{C}---- Calculando média ----{W}")
	media = calc_media_simples(nums)
	print(f"{C}---- Calculando mediana ----{W}")
	mediana = calc_mediana(nums)
	print(f"{C}---- Calculando moda ----{W}")
	moda = calc_moda(nums)

	return {'media': media, 'mediana': mediana ,'moda': moda}

def calc_mmm_grupo(values):
	"""Função para calculo de dados agrupados sem classe"""

	print(f"{C}---- Calculando média ----{W}")
	media = values['media']
	print(f"{C}-------- Calculando Valores Adicionais --------{W}")
	values = calc_valores_mmm_grupo(values)
	print(f"{C}-------- Calculando Moda --------{W}")
	moda = values['classe_modal']['moda']
	print(f"{C}-------- Calculando Mediana --------{W}")
	mediana = calc_mediana_grupo(values)

	return {'media': media, 'mediana': mediana ,'moda': moda}

def calc_mmm_grup_classe(values):
	"""Função para calculo de dados agrupados por classe"""

	print(f"{C}---- Calculando média ----{W}")
	media = values['media']
	print(f"{C}-------- Calculando Valores Adicionais --------{W}")
	values = calc_valores_mmm_classes(values)
	print(f"{C}-------- Calculando Moda --------{W}")
	moda = calc_moda_classe(values)
	print(f"{C}-------- Calculando Mediana --------{W}")
	mediana = calc_mediana_classe(values)

	return {'media': media, 'mediana': mediana ,'moda': moda}

def calc_media_simples(nums):
	cont = 0
	soma = 0
	for num in nums:
		cont +=1
		soma += num
	media = round(soma/cont, 2)
	string = f"Media = {soma}/{cont} = {media}"
	print(string)
	return media

def calc_mediana(nums):
	len_nums = len(nums)
	nums.sort()
	print(nums)
	if len_nums%2 == 0:
		indice1 = int((len_nums+1)/2)
		indice2 = indice1+1
		mediana = round((nums[indice1-1]+nums[indice2-1])/2, 2)
		string = f"Mediana = ({nums[indice1-1]} + {nums[indice2-1]}) / 2  =  {mediana}"
		print(string)
	else:
		indice = int((len_nums+1)/2)
		mediana = nums[indice-1]
		string = f"Mediana = {nums[indice-1]}"
		print(string) 
	return mediana

def calc_moda(nums):
	dicionario = {}
	for num in nums:
		cont = nums.count(num)
		dicionario.update({num: cont})
	valores_dict = list(dicionario.values())
	print(f"Moda dict = {dicionario}")
	maior = max(valores_dict)
	maiores = []
	for k, v in dicionario.items():
		if dicionario[k] == maior:
			maiores.append(k)
	return maiores

def calc_moda_classe(values=False):
	"""moda = li + (D1 / (D1 + D2)) * h"""
	if not values:
		print("__________________\nSolicitação da moda para classe:")
		li = float(input("Digite o li: "))
		h = float(input("Digite o h: "))
		d1 = float(input("Digite o d1: "))
		d2 = float(input("Digite o d2: "))
		moda = li + (d1/(d1+d2))*h
	else:
		classes = values['classes']

		classe_modal = values['classe_modal']

		print(f"{C}---- Obtendo D1 e D2 ----{W}")
		d1 = values['fmod'] - values['fant']
		d2 = values['fmod'] - values['fpos']
		print(f"D1 = {values['fmod']} - {values['fant']}")
		print(f"D2 = {values['fmod']} - {values['fpos']}")

		print(f"{C}---- Calculando moda ----{W}")
		moda = values['li'] + (d1/(d1+d2))*values['h']
		print(f"Moda = {values['li']} + ({d1} / ({d1} + {d2}))*{values['h']}  = {moda}")
		
		print(f"{G}--> Done !\n{W}")

	return round(moda, 2)

def calc_mediana_grupo(values=False):
	"""mediana = li + ((N/2 - fant) / f) * h"""
	if values:
		classe_modal = values['classe_modal']

		fac = values['fac'][classe_modal['indice']]

		print(f"{C}---- Calculando mediana ----{W}")
		mediana = calc_mediana(values['indexes'])
		print(f"Mediana = {mediana}")
		
	return round(mediana, 2)

def calc_mediana_classe(values=False):
	"""mediana = li + ((N/2 - fant) / f) * h"""
	if not values:
		print("__________________\nSolicitação da mediana para classe:")
		li = float(input("Digite o li: "))
		h = float(input("Digite o h: "))
		f = float(input("Digite o f: "))
		fant = float(input("Digite o fant: "))
		n = float(input("Digite o n: "))
		mediana = li + ((n/2 - fant)/f)*h
	else:
		classe_modal = values['classe_modal']

		fac = values['fac'][classe_modal['indice']]

		print(f"{C}---- Calculando mediana ----{W}")
		mediana = values['li'] + ((values['soma_ni']/2 - fac)/values['fpos'])*values['h']
		print(f"Mediana = {values['li']} + (({values['soma_ni']}/ 2 - {fac})/ {values['fpos']})* {values['h']}  = {mediana}")
		
	return round(mediana, 2)

def calc_valores_mmm_grupo(values):
	indexes = values['indexes']
	
	print(f"{G}----------------------------------------------------------{W}")
	print(f"{C}---- Obtendo Valores: classe_modal, fant, fpos, fi, fac ----\n{W}")
	
	print(f"{C}---- Obtendo Frequencia modal ----{W}")
	classe_modal = CF.calc_frequencia_modal(values)

	print(f"{C}---- Obtendo Frequencias ----{W}")
	fmod = classe_modal['valor']
	try:
		fant = values['numeros'][classe_modal['indice']-1]
	except IndexError:
		fant = classe_modal['valor']
	
	try:
		fpos = values['numeros'][classe_modal['indice']+1]
	except IndexError:
		fpos = classe_modal['valor']

	fi = CF.calc_frequencia_relativa(values)
	fac = CF.calc_frequencia_acumulada(values)
	facant = fac[classe_modal['indice']-1]
	print(f"fmod = {fmod}")
	print(f"fant: {fant}")
	print(f"fpos: {fpos}")
	print(f"fi: {classe_modal['valor']}")
	print(f"fac: {fac[classe_modal['indice']]}")
	print(f"facant: {fac[classe_modal['indice']-1]}")

	values.update({'classe_modal': classe_modal,
		'fmod':fmod, 'fant':fant, 'fpos':fpos, 'fi':fi, 'fac':fac, 'facant':facant
	})

	return values


def calc_valores_mmm_classes(values):
	classes = values['classes']
	
	print(f"{G}----------------------------------------------------------{W}")
	print(f"{C}---- Obtendo Valores: classe_modal, li, h, fant, fpos, fi, fac ----\n{W}")
	
	print(f"{C}---- Obtendo classe modal ----{W}")
	classe_modal = CF.calc_classe_modal(values)
	h = CF.calc_altura_classe(classes)
	li = float(classes[classe_modal['indice']-1][1])
	print(f"Altura da classe: {h}")
	print(f"Limite inferior: {li}")

	print(f"{C}---- Obtendo Frequencias ----{W}")
	fmod = classe_modal['valor']
	try:
		fant = values['numeros'][classe_modal['indice']-1]
	except IndexError:
		fant = classe_modal['valor']
	
	try:
		fpos = values['numeros'][classe_modal['indice']+1]
	except IndexError:
		fpos = classe_modal['valor']

	fi = CF.calc_frequencia_relativa(values)
	fac = CF.calc_frequencia_acumulada(values)
	facant = fac[classe_modal['indice']-1]
	print(f"fmod = {fmod}")
	print(f"fant: {fant}")
	print(f"fpos: {fpos}")
	print(f"fi: {classe_modal['valor']}")
	print(f"fac: {fac[classe_modal['indice']]}")
	print(f"facant: {fac[classe_modal['indice']-1]}")

	values.update({'classe_modal': classe_modal,
		'li':li, 'fmod':fmod, 'fant':fant, 'fpos':fpos, 'fi':fi, 'fac':fac, 'facant':facant, 'h':h
	})

	return values

if __name__ == '__main__':
	pede = True
	while pede:
		try:
			op = int(input("Digite o tipo de exercício: "))
		except KeyboardInterrupt as e:
			pede = False
		except Exception as e:
			print(f"{R}!!! Opção Inválida !!!\nDigite novamente{W}")

	pede = True
	nums = BF.pede_numeros()
	
	# nums = [0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4]

	media = calc_media_simples(nums)
	mediana = calc_mediana(nums)
	moda = calc_moda(nums)

	print("Média:   " + str(media))
	print("Mediana: " + str(mediana))
	print("Moda:    " + str(moda))

	moda_classe = calc_moda_classe()
	print("Moda Classe = " + str(moda_classe))

	mediana_classe = calc_mediana_classe()
	print("Mediana Classe = " + str(mediana_classe))
