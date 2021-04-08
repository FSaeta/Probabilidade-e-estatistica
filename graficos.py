from menu import R, G, C, Y, W

import desvio_padrao as DP

import basic_funcs as BF

import pdb

def pede_chaves(values):
    print(f"{Y} ------------------")
    chaves_disp = [x for x in values.keys() if type(values[x])==list]
    print(f"{W}Chaves Disponíveis : {G}{chaves_disp}{W}")
    print(f"{Y}-------")
    print(f"{G}Digite as colunas da tabela: {W}")
    colunas = []
    while True:
        try:
            coluna = input(f"{W}Coluna: {G}")
            if coluna not in chaves_disp:
                raise ValueError
            colunas.append(coluna)
            chaves_disp.remove(coluna)
        except KeyboardInterrupt:
            print(f"{W}Colunas selecionadas: {G} {colunas}")
            return colunas
        except Exception:
            print(f"{R}Coluna inválida!{W}")
            print(f"Disponiveis {G}{chaves_disp}{W}")


def montar_graf_generico_simples(values, chaves):
    # Montando Header
    header = "       |"
    for head_topic in chaves:
        header += f"     {head_topic}     |"
    header += '\n'
    cels_len = [len(cel) for cel in header.split('|')]
    escopo = header

    # Montando linhas
    indx = 0
    for num in values['numeros']:
        linha = f" ".ljust(cels_len[0])
        i = 1
        for valor in chaves:
            linha += f"|  {values[valor][indx]}".ljust(cels_len[i]+1)
            i += 1
        linha += "\n"
        escopo += linha
        indx += 1

    # Montando linha de Soma
    # Obtendo chaves das somas
    soma_head_topics = []
    for head_topic in chaves:
        if head_topic == 'numeros':
            head_topic = 'ni'
        soma_key = 'soma_'+head_topic
        if soma_key in values.keys():
            soma_head_topics.append(soma_key)
        else:
            soma_head_topics.append(" ")
    # Adicionando linhas
    linha_soma = f"\nsoma= ".ljust(cels_len[0]+1)
    i = 1
    for soma in soma_head_topics:
        if soma != " ":
            linha_soma += f"|  {values[soma]}".ljust(cels_len[i]+1)
        else:
            linha_soma += f"| {soma}".ljust(cels_len[i]+1)
        i += 1

    # Finalizando o Gráfico
    escopo += linha_soma
    escopo += "\n________________________________\n\n"
    return escopo


def montar_graf_generico_grupo(values, chaves):
    # Montando Header
    header = "       |"
    for head_topic in chaves:
        header += f"     {head_topic}     |"
    header += '\n'
    cels_len = [len(cel) for cel in header.split('|')]
    escopo = header

    # Montando linhas
    indx = 0
    for num in values['numeros']:
        linha = f" ".ljust(cels_len[0])
        i = 1
        for valor in chaves:
            linha += f"|  {values[valor][indx]}".ljust(cels_len[i]+1)
            i += 1
        linha += "\n"
        escopo += linha
        indx += 1

    # Montando linha de Soma
    # Obtendo chaves das somas
    soma_head_topics = []
    for head_topic in chaves:
        if head_topic == 'numeros':
            head_topic = 'ni'
        soma_key = 'soma_'+head_topic
        if soma_key in values.keys():
            soma_head_topics.append(soma_key)
        else:
            soma_head_topics.append(" ")
    # Adicionando linhas
    linha_soma = f"\nsoma= ".ljust(cels_len[0]+1)
    i = 1
    for soma in soma_head_topics:
        if soma != " ":
            linha_soma += f"|  {values[soma]}".ljust(cels_len[i]+1)
        else:
            linha_soma += f"| {soma}".ljust(cels_len[i]+1)
        i += 1

    # Finalizando o Gráfico
    escopo += linha_soma
    escopo += "\n________________________________\n\n"
    return escopo


def montar_graf_generico_classe(values, chaves):
    # Montando Header
    header = "   Classes   |"
    for head_topic in chaves:
        header += f"   {head_topic}   |"
    header += '\n'
    cels_len = [len(cel) for cel in header.split('|')]
    escopo = header

    # Montando linhas
    indx = 0
    for classe in values['classes']:
        linha = f"   {classe[0]}|-{classe[1]}".ljust(cels_len[0])
        i = 1
        for valor in chaves:
            linha += f"|  {values[valor][indx]}".ljust(cels_len[i]+1)
            i += 1
        linha += "\n"
        escopo += linha
        indx += 1

    # Montando linha de Soma
    soma_head_topics = []
    for head_topic in chaves:
        if head_topic == 'numeros':
            head_topic = 'ni'
        soma_key = 'soma_'+head_topic
        if soma_key in values.keys():
            soma_head_topics.append(soma_key)
        else:
            soma_head_topics.append(" ")
    linha_soma = f"\nsoma= ".ljust(cels_len[0]+1)
    i = 1
    for soma in soma_head_topics:
        if soma != " ":
            linha_soma += f"|  {values[soma]}".ljust(cels_len[i]+1)
        else:
            linha_soma += f"| {soma}".ljust(cels_len[i]+1)
        i += 1

    # Finalizando o Gráfico
    escopo += linha_soma
    escopo += "\n________________________________\n\n"
    return escopo

if __name__ == '__main__':
    numeros = BF.pede_numeros()
    values = DP.computar_dados_grup_classe(numeros)

    grafico = montar_graf_generico_classe(values, ['numeros', 'xini', 'xi2ni'])
    print(grafico)