def encode(message):
	encoded_message = ""

	for char in message:
		if (ord(char) - ord('a')) < 10:
			new_letter = ("0" + (str(ord(char) - ord('a'))))
		else:
			new_letter = (str(ord(char) - ord('a')))
		encoded_message += new_letter

	return int(encoded_message)

def decode(coded):
	coded_cypher = str(coded)
	decoded_message = ""

	if len(coded_cypher) % 2 == 1:
		coded_cypher = '0' + coded_cypher
	else:
		coded_cypher = coded_cypher
	
	for i in range(len(coded_cypher)/2):
		decoded_message = decoded_message + str(chr(int(coded_cypher[2*i:(2*i + 2)]) + ord('a')))
		
	return decoded_message