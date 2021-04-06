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

if __name__ == '__main__':
    pede_numeros()
