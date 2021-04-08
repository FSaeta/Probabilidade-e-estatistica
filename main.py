import mensagens as MSG
import menu
import main_funcs as MF

from menu import R,G,C,Y,W, limpar_tela

import sys

def limpar_tela():
    print(f"{Y}-->{W}")

# ---- Main functions
def mudar_id(novo_id):
    global id_menu, menus
    # menu.define_contexto(menus, id_menu, novo_id)
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

# Moda Media Mediana
menus.update({
    11: menu.Menu(
        nome="MMM - EXECUTAR NÃO AGRUPADOS",
        id=11,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[1])],
                1: [(MF.run_mmm_simples,[]), (mudar_id,[0])],
                2: []
    }),
    12: menu.Menu(
        nome="MMM - EXECUTAR AGRUPADOS SEM CLASSES",
        id=12,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[1])],
                1: [(print,[f"{R}Funcionalidade em desenvolvimento!{W}"]), (mudar_id,[1])],
                2: []
    }),
    13: menu.Menu(
        nome="MMM - EXECUTAR AGRUPADOS POR CLASSES",
        id=13,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[1])],
                1: [(MF.run_mmm_classes,[]), (mudar_id,[0])]
    })
})

# Desvio padrão
menus.update({
    21: menu.Menu(
        nome="DP - EXECUTAR NÃO AGRUPADOS",
        id=21,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[2])],
                1: [(MF.run_dp_simples,[]), (mudar_id,[0])]
    }),
    22: menu.Menu(
        nome="DP - EXECUTAR AGRUPADOS SEM CLASSES",
        id=22,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[2])],
                1: [(MF.run_dp_grupo,[]), (mudar_id,[0])]
    }),
    23: menu.Menu(
        nome="DP - EXECUTAR AGRUPADOS POR CLASSES",
        id=23,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[1])],
                1: [(MF.run_dp_grupo_classe,[]), (mudar_id,[0])]
    })
})

# Box Splot
menus.update({
    31: menu.Menu(
        nome="Box Splot - EXECUTAR NÃO AGRUPADOS",
        id=21,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[2])],
                1: [(MF.run_dp_simples,[]), (mudar_id,[0])]
    }),
    32: menu.Menu(
        nome="Box Splot - EXECUTAR AGRUPADOS SEM CLASSES",
        id=22,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[2])],
                1: [(MF.run_dp_grupo,[]), (mudar_id,[0])]
    }),
    33: menu.Menu(
        nome="Box Splot - EXECUTAR AGRUPADOS POR CLASSES",
        id=23,
        msg= MSG.executar,
        op_dict= {0: [(mudar_id,[1])],
                1: [(MF.run_dp_grupo_classe,[]), (mudar_id,[0])]
    })
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


