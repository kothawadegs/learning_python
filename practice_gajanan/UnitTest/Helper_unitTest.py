import unittest


class AtmosphericUnitTest(unittest.TestCase):
	if not Atmospheric.t_mean == 27.5:
		message = "The t_mean is correct"

	raise ValueError(message)
