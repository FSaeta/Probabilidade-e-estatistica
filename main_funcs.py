from menu import R,G,C,Y,W
import basic_funcs as BF

import mmm
import desvio_padrao as DP
import box_plot as BP

# Moda Media Mediana
def run_mmm_simples():
    numeros = BF.pede_numeros()
    values = mmm.calc_mmm_simples(numeros)
    print(f"{Y}_____Resultado da execução: ")
    print(f"Média: {values['media']}")
    print(f"Mediana: {values['mediana']}")
    print(f"Moda: {values['moda']}")
    print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

def run_mmm_classes():
    numeros = BF.pede_numeros()
    values = DP.computar_dados_grup_classe(numeros)

    mmm_values = mmm.calc_mmm_grup_classe(values)
    print(f"{Y}_____Resultado da execução: ")
    print(f"Média: {mmm_values['media']}")
    print(f"Mediana: {mmm_values['mediana']}")
    print(f"Moda: {mmm_values['moda']}")
    print(">>>>>>>>>>>>><<<<<<<<<<<<<<")


# Desvio Padrão
def run_dp_simples():

	numeros = BF.pede_numeros()
	values = DP.computar_dados(numeros)
	
	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(DP.montar_graf_simples(values))

	print(f"{Y}_____Resultado da execução: ")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"N = {values['N']}")
	print(f"Média = {values['media']}")
	print(f"x_2 = ({values['soma_ni']} / {values['N']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_ni2']} - {values['N']} * {values['x_2']}) / {values['N']-1}  = {values['s2']}")
	print(f"s = {values['s']}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

def run_dp_grupo():

	numeros = BF.pede_numeros()
	values = DP.computar_dados_grup(numeros)

	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(DP.montar_graf_grup(values))

	print(f"{Y}_____Resultado da execução: ")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xi²ni = {values['soma_xini2']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xini2']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

def run_dp_grupo_classe():

	numeros = BF.pede_numeros()		
	values = DP.computar_dados_grup_classe(numeros)

	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(DP.montar_graf_grup_classe(values))

	print(f"{Y}_____Resultado da execução: ")
	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xini2 = {values['soma_xini2']}")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xini2']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")

	print(f"Classes : {values['classes']}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

# Box Splot

