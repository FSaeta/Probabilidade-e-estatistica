from menu import R,G,C,Y,W

import basic_funcs as BF
import computes_funcs as CF

import mmm
import desvio_padrao as DP
import box_plot as BP

import graficos

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
	print(f"Soma xi²ni = {values['soma_xi2ni']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xi2ni']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

def run_dp_grupo_classe():

	numeros = BF.pede_numeros()		
	values = DP.computar_dados_grup_classe(numeros)

	print(f"\n{C} ------  GRÁFICO  ------{W}")
	print(DP.montar_graf_grup_classe(values))

	print(f"{Y}_____Resultado da execução: ")
	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xi²ni = {values['soma_xi2ni']}")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xi2ni']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")

	print(f"Classes : {values['classes']}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")


# Box Plot
def run_bp_simples():
	numeros = BF.pede_numeros()
	
	print(f"{C}---- Calculando Media Moda e Mediana ----{W}")
	media = mmm.calc_media_simples(numeros)
	mediana = mmm.calc_mediana(numeros)
	moda = mmm.calc_moda(numeros)
	
	print(f"{C}---- Calculando os Quartis ----{W}")
	quartil1 = BP.calc_quartil(numeros, 1)
	quartil2 = BP.calc_quartil(numeros, 2)
	quartil3 = BP.calc_quartil(numeros, 3)


	values = DP.computar_dados(numeros)
	values.update({'q1': quartil1, 'q3': quartil3})
	values.update({'mediana': mediana, 'moda': moda})
	assimetria = BP.calc_assimetria(values)
	curtose = BP.calc_curtose(values)

	print(f"{Y}_____Resultado da execução: ")
	print(f"Média: {media}")
	print(f"Mediana: {mediana}")
	print(f"Moda: {moda}")
	print("-------")
	print(f"1º Quartil : {quartil1}")
	print(f"2º Quartil : {quartil2}")
	print(f"3º Quartil : {quartil3}")
	print(f"Assimetria: {assimetria}")
	print(f"Curtose: {curtose}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

# Geral

def run_geral_simples(graf=True):
	#numeros = BF.pede_numeros()
	numeros = [66.24, 65.06, 65.52, 65.57, 65.63, 65.67, 65.71, 65.73, 65.92, 65.93, 65.93, 65.93, 66.02, 66.28, 66.32, 66.33, 66.34, 66.45, 66.45, 66.7]
	# Média Moda Mediana
	values = mmm.calc_mmm_simples(numeros)
	# Desvio Padrão Variância
	values.update(DP.computar_dados(numeros))
	# Calculando quartis
	values.update(BP.calc_quartis_simples(numeros))
	# Calculando Assimetria
	values.update({'assimetria': BP.calc_assimetria(values)})
	# Calculando a curtose
	values.update({'curtose': round(BP.calc_curtose(values), 2)})
	# Calculando Coeficiente de Variação
	values.update({'coefv': round(CF.calc_coef_variacao(values),2)})

	print(values)

	print(f"{Y}_____Resultado da execução: ")
	print(f"Média: {values['media']}")
	print(f"Mediana: {values['mediana']}")
	print(f"Moda: {values['moda']}")
	print(f"{W}-------{Y}")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"N = {values['N']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_ni']} / {values['N']})²  = {values['x_2']}")
	print(f"{W}-------{Y}")
	print(f"s² = {values['s2']}")
	print(f"s = {values['s']}")
	print(f"{W}-------{Y}")
	print(f"1º Quartil = {values['q1']}")
	print(f"2º Quartil = {values['q2']}")
	print(f"3º Quartil = {values['q3']}")
	print(f"{W}-------{Y}")
	print(f"Assimetria = {values['assimetria']}")
	print(f"Curtose = {values['curtose']}")
	print(f"{W}-------{Y}")
	print(f"Coeficiente de variação = {values['coefv']}")
	print(f">>>>>>>>>>>>><<<<<<<<<<<<<<{W}")

	if graf:
		colunas = graficos.pede_chaves(values)
		grafico = graficos.montar_graf_generico_simples(values, colunas)
		print(f"\n{C} ------  GRÁFICO  ------{W}")
		print(grafico)
	
	print(f"{Y}>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<{W}")



def run_geral_grupo(graf=True):
	numeros = BF.pede_numeros()
	
	# Desvio Padrão
	values = DP.computar_dados_grup(numeros)
	print(values)
	# Calculando MMM

	values.update(mmm.calc_mmm_grup_classe(values))
	# values.update(BP.calc_quartis_simples(numeros))
	
	# Calculando Assimetria
	values.update({'assimetria': BP.calc_assimetria(values)})
	# Calculando a curtose
	values.update({'curtose': round(BP.calc_curtose(values), 2)})
	# Calculando Coeficiente de Variação
	values.update({'coefv': round(CF.calc_coef_variacao(values),2)})

	print(f"{Y}_____Resultado da execução: ")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xi²ni = {values['soma_xi2ni']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"s² =  ({values['soma_xi2ni']} - {values['soma_ni']} * {values['x_2']}) / {values['soma_ni']-1}  = {values['s2']}")
	print(f"s = {values['s']}")
	print(">>>>>>>>>>>>><<<<<<<<<<<<<<")

	if graf:
		colunas = graficos.pede_chaves(values)
		grafico = graficos.montar_graf_generico_grupo(values, colunas)
		print(f"\n{C} ------  GRÁFICO  ------{W}")
		print(grafico)


def run_geral_classe(graf=True):
	numeros = BF.pede_numeros()
	#numeros = [2.0, 27.0, 19.0, 16.0, 7.0, 4.0]
	
	# Média Moda Mediana
	values = DP.computar_dados_grup_classe(numeros)
	# Desvio Padrão Variância
	values.update(mmm.calc_mmm_grup_classe(values))
	# Calculando quartis
	values.update(BP.calc_quartil_grupos(values))
	# Calculando Assimetria
	values.update({'assimetria': BP.calc_assimetria_classe(values)})
	# Calculando a curtose
	values.update({'curtose': round(BP.calc_curtose_classe(values), 2)})
	# Calculando Coeficiente de Variação
	values.update({'coefv': CF.calc_coef_variacao(values)})

	print(f"{Y}_____Resultado da execução: ")
	print(f"Média: {values['media']}")
	print(f"Mediana: {values['mediana']}")
	print(f"Moda: {values['moda']}")
	print(f"{W}-------{Y}")
	print(f"Soma xini = {values['soma_xini']}")
	print(f"Soma xi²ni = {values['soma_xi2ni']}")
	print(f"Soma ni = {values['soma_ni']}")
	print(f"Média = {values['media']}")
	print(f"Média² = ({values['soma_xini']} / {values['soma_ni']})²  = {values['x_2']}")
	print(f"{W}-------{Y}")
	print(f"s² = {values['s2']}")
	print(f"s = {values['s']}")
	print(f"{W}-------{Y}")
	print(f"1º Quartil = {values['q1']}")
	print(f"2º Quartil = {values['q2']}")
	print(f"3º Quartil = {values['q3']}")
	print(f"{W}-------{Y}")
	print(f"Assimetria = {values['assimetria']}")
	print(f"Curtose = {values['curtose']}")
	print(f"{W}-------{Y}")
	print(f"Coeficiente de variação = {values['coefv']}")
	print(f">>>>>>>>>>>>><<<<<<<<<<<<<<{W}")

	if graf:
		colunas = graficos.pede_chaves(values)
		grafico = graficos.montar_graf_generico_classe(values, colunas)
		print(f"\n{C} ------  GRÁFICO  ------{W}")
		print(grafico)
	
	print(f"{Y}>>>>>>>>>>>>>>>>>>>>>>>><<<<<<<<<<<<<<<<<<<<<<<<<<<<{W}")