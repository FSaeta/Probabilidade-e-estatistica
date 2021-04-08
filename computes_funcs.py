from menu import R, C, Y, W, G

def calc_classe_modal(values):
	maior_freq = {'classe': [], 'valor': 0, 'indice': 0}
	indx = 0
	for classe in values['classes']:
		valor = values['numeros'][indx]
		if valor >= maior_freq['valor']:
			maior_freq.update({'classe': classe, 'valor': valor, 'indice': indx})
		indx += 1

	print(f"Classe Modal = {maior_freq['classe']}\nFrequencia Modal = {maior_freq['valor']}\nIndice = {maior_freq['indice']}")
	return maior_freq

def calc_altura_classe(classes):
	"""h = altura das classes"""
	classe = classes[0]
	h = float(classe[1])-float(classe[0])
	return h

def calc_frequencia_relativa(values):
	"""fi = frequencia relativa"""
	freqs = [round(x/values['soma_ni'],2) for x in values['numeros']]
	return freqs


def calc_frequencia_acumulada(values):
	"""fac = frequencia acumulada"""
	fac = 0
	freqs = []
	for num in values['numeros']:
		fac += num
		freqs.append(fac)
	return freqs

def calc_coef_variacao(values):
	print(f"{C}---- Calculando Coeficiente de Variação ----{W}")
	coef = values['s'] / values['media']
	print(f"Coeficiente de variação: {values['s']} / {values['media']}  = {coef}")
	return round(coef, 2)