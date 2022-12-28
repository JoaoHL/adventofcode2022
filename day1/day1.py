
#parte 1
with open('day1.input', 'r') as input_file:
	max_calories = 0
	elf_total_calories = 0

	for line in input_file:
		line = line.strip()
		if line != "":
			elf_total_calories += int(line)
		else:
			max_calories = max(elf_total_calories, max_calories)
			elf_total_calories = 0

	print(f"Calorias máximas: {max_calories}")

#parte 2
with open('day1.input', 'r') as input_file:
	calories = list()
	elf_total_calories = 0

	for line in input_file:
		line = line.strip()
		if line != "":
			elf_total_calories += int(line)
		else:
			calories.append(elf_total_calories)
			elf_total_calories = 0

	calories.sort()

	print(f"Top 3: {calories[-1]} {calories[-2]} {calories[-3]}")