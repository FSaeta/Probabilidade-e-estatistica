from menu import R,G,C,Y,W
import basic_funcs as BF
import mmm

def run_mmm_simples():
    numeros = BF.pede_numeros()
    values = mmm.calc_mmm_simples(numeros)
    print(f"{Y}_____Resultado da execução: ")
    print(f"Média: {values['media']}")
    print(f"Mediana: {values['mediana']}")
    print(f"Moda: {values['moda']}")
    print(f"{W}________________________________")