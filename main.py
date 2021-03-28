import box_plot as BP
import desvio_padrao as DP
import mmm

import mensagens as MSG
import menu

from menu import R,G,C,Y,W, limpar_tela

import sys

# ---- Main functions
def mudar_id(novo_id):
    global id_menu, menus
    menu.muda_msg_contexto(menus, id_menu, novo_id)
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
menu_ativo = id_menu
menu_principal = menu.Menu(
    nome="Menu Principal",
    id=0,
    msg= MSG.principal,
    op_dict= {0: [(sys.exit,[])],
              1: [(mudar_id,[1])],
              2: [(mudar_id,[2])],
              3: [(mudar_id,[3])]
    }
)
menu_mmm = menu.Menu(
    nome="MODA MÉDIA MEDIANA",
    id=1,
    msg= MSG.opcoes,
    op_dict= {0: [(mudar_id,[0])],
              1: [(mudar_id,[11])],
              2: [(mudar_id,[12])],
              3: [(mudar_id,[13])]
    }
)
menu_desvio_padrao = menu.Menu(
    nome="DESVIO PADRÃO",
    id=2,
    msg= MSG.opcoes,
    op_dict= {0: [(mudar_id,[0])],
              1: [(mudar_id,[21])],
              2: [(mudar_id,[22])],
              3: [(mudar_id,[23])]
    }
)
menu_boxplot = menu.Menu(
    nome="BOXPLOT",
    id=3,
    msg= MSG.opcoes,
    op_dict= {0: [(mudar_id,[0])],
              1: [(mudar_id,[31])],
              2: [(mudar_id,[32])],
              3: [(mudar_id,[33])]

    }
)
menu_montagem_geral = menu.Menu(
    nome="MENU GERAL",
    id=9,
    msg= MSG.montagem_geral,
    op_dict= {0: [(mudar_id,[0])],
              1: [],
              2: []

    }
)
menus.update({
    0: menu_principal, 
    1: menu_mmm, 
    2: menu_desvio_padrao, 
    3: menu_boxplot
})

# Secundários
"""menu_mmm = menu.Menu(
    nome="Menu MMM",
    id=11,
    msg = 
)"""

# Main
if __name__ == '__main__':
    running = True
    while running:
        if True:
            menu_ativo = menus[id_menu]
            menu_ativo.mostrar_msg()
            op = pede_opcao(menu_ativo)
            menu_ativo.exec_funcs(op)


