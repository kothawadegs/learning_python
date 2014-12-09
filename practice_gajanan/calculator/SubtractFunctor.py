from AbstractFunctor import AbstractFunctor


class SubtractFunctor(AbstractFunctor):
	def __init__(self):
		super(SubtractFunctor, self).__init__("-")

	def __call__(self, a, b):
		"""this function subtracts two numbers"""
		return a - b
