from menu import R,G,C,Y,W

def mudar_id(novo_id):
	return novo_id

def pede_numeros():
    """ Solicita os números que serão adicionados
    - Retorna uma lista com esses números após apertar Ctrl+C"""
    numeros = []
    while True:
        try:
            numero = float(input("numero: "))
            numeros.append(numero)
        except ValueError:
            print(f"{R}Número digitado incorretamente{W}")
        except KeyboardInterrupt:
            print(f"{G}-- Done !{W}")
            return numeros

def pede_frequencias(nums):
	while True:
		indexes = []
		print("\nComeço das Frequências (x): ")
		for num in nums:
			freq = int(input('Frequência:'))
			indexes.append(freq)
		return indexes

def pedir_classes(nums):
	pede_cl = True
	classes = []
	while pede_cl:
		try:
			for n in nums:
				classe = input("Classe: ")
				valida_classe(classe)
				classe = classe.split(',')
				classes.append(classe)
			pede_cl = False
		except ValueError:
			print(f"{R}Valor incorreto pra classe ! {Y}Valores válidos: (X,Y){W}")
			classes.clear()

	return classes

def valida_classe(classe):
	split_classes = classe.split(',')
	if len(split_classes) != 2:
		raise ValueError
	float(split_classes[0])
	float(split_classes[1])

def calc_pontos_medios_classes(classes):
	pontos_medios = []
	for classe in classes:
		pm = (float(classe[0])+float(classe[1]))/2
		pontos_medios.append(pm)
	return pontos_medios

if __name__ == '__main__':
    pede_numeros()
