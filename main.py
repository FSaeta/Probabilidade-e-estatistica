import box_plot as BP
import desvio_padrao as DP
import mmm

import mensagens as MSG
import menu
import main_funcs as MF

from menu import R,G,C,Y,W, limpar_tela

import sys

# ---- Main functions
def mudar_id(novo_id):
    global id_menu, menus
    menu.define_contexto(menus, id_menu, novo_id)
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

# Menus primários
menus.update({
    0: menu.Menu(
        nome="Menu Principal",
        id=0,
        msg= MSG.principal,
        op_dict= {0: [(sys.exit,[])],
                1: [(mudar_id,[1]), (limpar_tela,[]) ],
                2: [(mudar_id,[2]), (limpar_tela,[]) ],
                3: [(mudar_id,[3]), (limpar_tela,[]) ]
    }),
    1: menu.Menu(
        nome="MODA MÉDIA MEDIANA",
        id=1,
        msg= MSG.opcoes,
        op_dict= {0: [(mudar_id,[0])],
                1: [(mudar_id,[11]), (limpar_tela,[]) ],
                2: [(mudar_id,[12]), (limpar_tela,[]) ],
                3: [(mudar_id,[13]), (limpar_tela,[]) ]
    }),
    2: menu.Menu(
        nome="DESVIO PADRÃO",
        id=2,
        msg= MSG.opcoes,
        op_dict= {0: [(mudar_id,[0])],
                1: [(mudar_id,[21]), (limpar_tela,[]) ],
                2: [(mudar_id,[22]), (limpar_tela,[]) ],
                3: [(mudar_id,[23]), (limpar_tela,[]) ]
    }),
    3: menu.Menu(
        nome="BOXPLOT",
        id=3,
        msg= MSG.opcoes,
        op_dict= {0: [(mudar_id,[0])],
                1: [(mudar_id,[31]), (limpar_tela,[]) ],
                2: [(mudar_id,[32]), (limpar_tela,[]) ],
                3: [(mudar_id,[33]), (limpar_tela,[]) ]
    }),
    9: menu.Menu(
        nome="MENU GERAL",
        id=9,
        msg= MSG.montagem_geral,
        op_dict= {0: [(mudar_id,[0])],
                1: [],
                2: []
    })
})
# Menus Secundários
menus.update({
    11: menu.Menu(
        nome="Menu MMM",
        id=11,
        msg= f"{G}Menu MMM{W}\n" + MSG.opcoes,
        op_dict= {0: [(mudar_id,[1]) ],
                1: [(mudar_id,[111]) ],
                2: [(mudar_id,[112]) ],
                3: [(mudar_id,[113]) ]
    })
})
# Menus Ternários
menus.update({
    111: menu.Menu(
        nome="EXECUTAR NÃO AGRUPADO",
        id=111,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[0])],
                1: [(MF.run_mmm_simples,[]), (mudar_id,[0])],
                2: []
    }),
    112: menu.Menu(
        nome="EXECUTAR AGRUPADO SEM CLASSE",
        id=112,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[0])],
                1: [],
                2: []
    }),
    113: menu.Menu(
        nome="EXECUTAR AGRUPADO POR CLASSE",
        id=113,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[0])],
                1: [],
                2: []
    }),
})


# Main
if __name__ == '__main__':
    running = True
    while running:
        if True:
            menu_ativo = menus[id_menu]
            menu_ativo.mostrar_msg()
            op = pede_opcao(menu_ativo)
            menu_ativo.exec_funcs(op)


