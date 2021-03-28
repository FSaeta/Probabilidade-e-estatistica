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

# ---- Main functions
def mudar_id(novo_id):
	global id_menu
	id_menu = novo_id
	return id_menu

def pede_opcao(menu):
    while True:
        try:
            op = int(input(f"Opção: {G}"))
            print(f"{W}")
            menu.valida_opcao(op)
            return op
        except ValueError:
            print(f"{R}Opção Inválida !{W}")

# ---- Declarando menus
# Primários
menus = {}
id_menu = 0
menu_principal = menu.Menu(
    nome="Menu Principal",
    id=0,
    msg= msg_principal,
    op_dict= {0: [(sys.exit,[])], 1: [(mudar_id,[1])], 2: [(mudar_id,[2])], 3: [(mudar_id,[3])]}
)
menu_mmm = menu.Menu(
    nome="MENU MODA MÉDIA MEDIANA",
    id=1,
    msg= msg_opcoes,
    op_dict= {0: [(mudar_id,[0])], 1: [(mudar_id,[11])]}
)
menu_desvio_padrao = menu.Menu(
    nome="MENU DESVIO PADRÃO",
    id=2,
    msg= msg_opcoes,
    op_dict= {0: [(mudar_id,[0])], 1: [(mudar_id,[21])]}
)
menu_boxplot = menu.Menu(
    nome="MENU BOXPLOT",
    id=3,
    msg= msg_opcoes,
    op_dict= {0: [(mudar_id,[0])], 1: [(mudar_id,[31])]}
)
menu_montagem_geral = menu.Menu(
    nome="MENU GERAL",
    id=9,
    msg= msg_montagem_geral,
    op_dict= {0: [(mudar_id,[0])], 1: []}
)
menus.update({
    0: menu_principal, 
    1: menu_mmm, 
    2: menu_desvio_padrao, 
    3: menu_boxplot
})

# Secundários
menu_mmm = menu.Menu(
    nome="Menu MMM",
    id=1

)

# Main
if __name__ == '__main__':
    try:
        menu_ativo = menus[id_menu]
        print(menu_ativo.msg)
        op = pede_opcao(menu_ativo)


