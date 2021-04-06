R = '\033[31m' # vermelho
G = '\033[01;32m' # verde
Y = '\033[01;33m' # amarelo
C = '\033[36m' # ciano
W = '\033[0m'  # branco

from os import system, name

def limpar_tela():
	system('cls' if name == 'nt' else 'clear')

def define_contexto(menus, id, id_pai):
	menu = menus[id]
	menu_id = str(id_pai)
	if str(id_pai) != '0':
		new_contexto = menus[id_pai].contexto['msg'] + " > " + menu.nome
		menu.contexto.update({
			'msg': f"{G}{new_contexto}{W}",
			'id_pai': id_pai
		})


class Menu:
	def __init__(self, nome, id, msg, op_dict):
		self.nome = nome
		self.msg = msg
		self.opcoes = op_dict
		self.funcoes_params = self.get_funcoes_params()
		self.contexto = {'msg': f"{G}-> {self.nome}{W}", 'id_pai': 0}

	def get_funcoes_params(self):
		funcoes_parametros = {}
		for opcao in self.opcoes.keys():
			funcs_params = []
			for funcao_params in self.opcoes[opcao]:
				funcs_params.append(funcao_params)

			funcoes_parametros.update({opcao:funcs_params})
		return funcoes_parametros

	def exec_funcs(self, opcao):
		"""Executa todas as funções que o menu possui para a opção escolhida"""
		ret = {}
		for funcao, params in self.funcoes_params[opcao]:
			if len(params) != 0:
				ret_f = funcao(*params)
			else:
				ret_f = funcao()
			ret.update({funcao.__name__: ret_f})
		return ret
	
	def add_funcs(self, opcao, funcao, param):
		"""Adicionar funções em tempo de execução ou em partes do 
		código após a declaração do menu

		- Formato de exemplo: menu.add_funcs(1, limpar_tela, [])"""

		funcao_parametro = (funcao,param)
		self.opcoes.update({opcao, funcao_parametro})
		
	def valida_opcao(self, opcao):
		"""Valida a opção escolhida com as opções disponíveis no op_dict"""
		op_permitidas = list(self.opcoes.keys())
		if opcao not in op_permitidas:
			raise ValueError
	
	def mostrar_msg(self):
		if self.contexto['msg']:
			print(self.contexto['msg'])
		print(self.msg)
