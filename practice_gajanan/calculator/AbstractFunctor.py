from abc import ABCMeta
from inspect import getargspec


class AbstractFunctor(object):
	__metaclass__ = ABCMeta

	# Is there a more Pythonesque way of writing this?
	def __init__(self, function_symbol):
		format_string = ''
		after_first = False
		for parameter in self.list_parameters():
			if after_first:
				format_string = format_string + ' ' + function_symbol + ' '
			else:
				after_first = True
			format_string = format_string + '{' + parameter + '}'
		format_string = format_string + ' = {result}'
		self.described_as = format_string

	def __str__(self):
		return type(self).__name__[0:-7]

	def list_parameters(self):
		parameters = getargspec(self.__call__).args
		return parameters[1:]
