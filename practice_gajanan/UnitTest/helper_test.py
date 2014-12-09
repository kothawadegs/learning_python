import unittest

from apps.dss.weather.agromet.helpers import Atmospheric


class AtmosphericUnitTest(unittest.TestCase):
	Atmospheric = Atmospheric

	def unit_test_check_t_mean_returns_correct_output(self):
		self.assertEqual(Atmospheric.t_mean(25, 30), 27.5)


if __name__ == '__main__':
	unittest.main()
