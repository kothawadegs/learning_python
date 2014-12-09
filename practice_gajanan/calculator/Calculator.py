class InvalidUserInputError(Exception):
	def __init__(self, explanation, incorrect_value):
		self.explanation = explanation
		self.incorrect_value = incorrect_value

	def __str__(self):
		return "User input was invalid: {explanation}; the value input was '{incorrect_value}'".format(
			explanation=self.explanation, incorrect_value=self.incorrect_value)


class Calculator(object):
	def __init__(self, *functors):
		self.functors = functors

	def display_calculator(self):
		for index, functor in enumerate(self.functors):
			print '{index}: {functor}'.format(index=index, functor=functor)
		index = self.__read_number_from_input_and_convert_to_index()
		functor = self.functors[index]
		arguments = []
		for parameter in functor.list_parameters():
			argument = self.__read_number_from_input_and_convert_to_integer(
				"Enter '{0}': ", parameter)
			arguments.append(argument)
		result = functor(*arguments)

		format_arguments = dict(zip(functor.list_parameters(), arguments))
		format_arguments['result'] = result

		print functor.described_as.format(**format_arguments)

	def __read_number_from_input_and_convert_to_index(self):
		potentially_valid_index = self.__read_number_from_input(
			"Enter the index of the operation you want: ")
		potential_index = self.__convert_to_integer(potentially_valid_index,
													"index")
		if potential_index < 0:
			raise InvalidUserInputError("the index was negative",
										potentially_valid_index)
		if str(potential_index) != potentially_valid_index:
			raise InvalidUserInputError("the index was not a valid index",
										potentially_valid_index)
		if potential_index >= len(self.functors):
			raise InvalidUserInputError("the index was not in range",
										potential_index)
		return potential_index

	def __read_number_from_input_and_convert_to_integer(self,
														input_message_format,
														number_name):
		return self.__convert_to_integer(self.__read_number_from_input(
			input_message_format.format(number_name)), number_name)

	def __read_number_from_input(self, input_message):
		potentially_invalid_number = 0
		try:
			potentially_invalid_number = raw_input(input_message)
		except EOFError:
			raise InvalidUserInputError("no input was given", "")
		return potentially_invalid_number

	def __convert_to_integer(self, potentially_valid_integer, number_name):
		if len(potentially_valid_integer) == 0:
			raise InvalidUserInputError(
				"the {0} was not a single digit".format(number_name),
				potentially_valid_integer)
		converted_integer = 0
		try:
			converted_integer = int(potentially_valid_integer)
		except ValueError:
			raise InvalidUserInputError(
				"the {0} was not a valid integer".format(number_name),
				potentially_valid_integer)
		return converted_integer
