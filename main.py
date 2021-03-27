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
msg_opcoes = f""" 

{Y}[1]{W} MEDIA - MODA - MEDIANA
{Y}[2]{W} DESVIO PADRÃO
{Y}[3]{W} BOXPLOT

{Y}[0]{W} VOLTAR
""" 

def mudar_id(novo_id):
	global id_menu
	id_menu = novo_id
	return id_menu

# ---- Declarando menus
menus = []
id_menu = 0
menu_principal = menu.Menu(
    nome="Menu Principal",
    id=0,
    msg= msg_principal,
    op_dict= {0: [(sys.exit,[])], 1: [(mudar_id,[1])], 2: [(mudar_id,[2])], 3: [(mudar_id,[3])]}
)
menu_nao_agrupados = menu.Menu(
    nome="MENU NÃO AGRUPADOS",
    id=1,
    msg= msg_principal,
    op_dict= {0: [(sys.exit,[])], 1: [(mudar_id,[1])]}
)
menu_agrupados_simples = menu.Menu(
    nome="MENU AGRUPADOS SEM CLASSE",
    id=2,
    msg= msg_principal,
    op_dict= {0: [(sys.exit,[])], 1: [(mudar_id,[1])]}
)
menu_agrupados_classes = menu.Menu(
    nome="MENU AGRUPADOS POR CLASSE",
    id=3,
    msg= msg_principal,
    op_dict= {0: [(sys.exit,[])], 1: [(mudar_id,[1])]}
)

if __name__ == '__main__':
    pass

