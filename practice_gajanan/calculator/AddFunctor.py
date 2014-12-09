from AbstractFunctor import AbstractFunctor


class AddFunctor(AbstractFunctor):
	def __init__(self):
		super(AddFunctor, self).__init__("+")

	def __call__(self, a, b, c):
		"""this function adds two numbers"""
		return a + b + c
