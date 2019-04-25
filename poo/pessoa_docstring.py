# -*- coding: utf-8 -*-

""" Módulo contém classe para representar uma pessoa. """

class Pessoa:
	"""
	Classe pessoa: armazena o nome e idade de uma pessoa.
	"""

	def __init__(self, nome='', idade=0):
		"""Inicializa pessoa com nome informado (padrão: string vazia
		   ) e idade (padrão: 0)"""
		self._nome = nome
		self._idade = idade

	def get_nome(self):
		"""Obtem nome da pessoa"""
		return self._nome

	def set_nome(self, n):
		"""Atribui nome da pessoa"""
		self._nome = n

	def get_idade(self):
		"""Obtem idade da pessoa"""
		return self._idade

	def set_idade(self, i):
		"""Atribui idade da pessoa"""
		self._idade = i

	def __repr__(self):
		"""Retorna uma Pessoa como string, no formato '>>> self._nome (self._idade)'"""
		s = '>>> {} ({})'.format(self._nome, self._idade)
		return s

	def __lt__(self, outro):
		"""Retorna verdadeiro se self._idade < outro._idade"""
		if self._idade < outro._idade:
			return True
		else:
			return False

	def __le__(self, outro):
		"""Retorna verdadeiro se self._idade <= outro._idade"""
		if self._idade <= outro._idade:
			return True
		else:
			return False

	def __gt__(self, outro):
		"""Retorna verdadeiro se self._idade > outro._idade"""
		if self._idade > outro._idade:
			return True
		else:
			return False

	def __ge__(self, outro):
		"""Retorna verdadeiro se self._idade >= outro._idade"""
		if self._idade >= outro._idade:
			return True
		else:
			return False

	nome = property(get_nome, set_nome)
	idade = property(get_idade, set_idade)

if __name__ == "__main__":
	p1 = Pessoa('Joao', 25)
	p2 = Pessoa('Jose', 20)
	p3 = Pessoa('Amanda', 33)
	p4 = Pessoa()
	p4.nome = 'Renata'
	p4.idade = 29
	print(p1)
	print(p2)
	print(p3)
	print(p4)
	print(p1 > p2)
	print(p3 <= p1)
	print(p4 >= p2)
	print(p2 < p3)
	l = [p1, p2, p3, p4]
	print(l)