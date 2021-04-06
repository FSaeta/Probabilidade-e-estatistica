from menu import R,G,C,Y,W

def formatar_bem_vindo():
    inicial_line = f"{C}--*{G}--*-{R}-*--*{Y}--*{W}"*4 + "\n"
    x_line = f"{C}XXX{G}XXX{R}XXXX{Y}XXX{W}"*4 + "\n"
    msg = "BEM VINDO AO PROGRAMA DE PROBABLIDADE E ESTATÍSTICA\n"
    ret = inicial_line + x_line + msg + x_line
    return ret

bem_vindo = formatar_bem_vindo()

principal = f"""
{Y}[1]{W} MEDIA - MODA - MEDIANA
{Y}[2]{W} DESVIO PADRÃO
{Y}[3]{W} BOXPLOT

{Y}[9]{W} Computar Dados (Geral)

{Y}[0]{W} SAIR
""" 

opcoes = f"""
{Y}[1]{W} Dados não Agrupados
{Y}[2]{W} Dados Agrupados {Y}sem{W} Classe
{Y}[3]{W} Dados Agrupados {Y}por{W} Classe

{Y}[0]{W} VOLTAR
""" 

montagem_geral = f"""
{Y}[1]{W} Sem Gráfico
{Y}[2]{W} Com Gráfico
"""

executar = f"""
{Y}[1]{W} EXECUTAR

{Y}[0]{W} VOLTAR
"""


print(bem_vindo)
if __name__ == '__main__':
    print(opcoes)
    print(principal)
    print(montagem_geral)
