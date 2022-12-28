
#parte 1
with open('input', 'r') as file:
	transmission = file.read()

	for i in range(len(transmission)-4):
		if len(set(transmission[i:i+4])) == 4:
			print(f"Resposta: {i+4}")
			break

#parte 2
with open('input', 'r') as file:
	transmission = file.read()

	for i in range(len(transmission)-14):
		if len(set(transmission[i:i+14])) == 14:
			print(f"Resposta: {i+14}")
			break