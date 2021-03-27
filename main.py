import menu
import box_plot as BP
import desvio_padrao as DP
import mmm
import sys

from menu import R,G,C,Y,W

msg_bem_vindo = f"""
{C}--*--*--*--*{R}--*--*--*--*{G}--*--*--*--*{Y}--*--*--*--*--*--{W}
{C}XXXXXXXXXXXX{R}XXXXXXXXXXXXX{G}XXXXXXXXXXXXX{Y}XXXXXXXXXXXXXXX{W}

 BEM VINDO AO PROGRAMA DE PROBABLIDADE E ESTATÍSTICA

{C}XXXXXXXXXXXX{R}XXXXXXXXXXXXX{G}XXXXXXXXXXXXX{Y}XXXXXXXXXXXXXXX{W}
"""
msg_principal = f"""

{Y}[1]{W} Media - Moda - Mediana
{Y}[2]{W} Desvio Padrão
{Y}[3]{W} BoxPlot

{Y}[0]{W} Sair
""" 
menus = []
# ---- Declarando menus
menu_principal = menu.Menu(
    nome="Menu Principal",
    id=0,
    msg= msg_principal,
    op_dict= {0: (sys.exit,[]), 1: ()}
)

if __name__ == '__main__':

