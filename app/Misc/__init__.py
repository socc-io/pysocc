
def random_generate_alphabet(length) :
	result = ''
	for idx in range(length) :
		result += chr(random.randint(ord('a'), ord('z')))
	return result