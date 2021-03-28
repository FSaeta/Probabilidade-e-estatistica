from menu import R,G,C,Y,W

def mudar_id(novo_id):
	return novo_id

def pede_numeros():
    """ Solicita os números que serão adicionados
    - Retorna uma lista com esses números após apertar Ctrl+C"""
    numeros = []
    pede = True
    while pede:
        try:
            numero = float(input("numero: "))
            numeros.append(numero)
        except ValueError:
            print(f"{R}Número digitado incorretamente{W}")
        except KeyboardInterrupt:
            pede = False
            return numeros

if __name__ == '__main__':
    pede_numeros()
