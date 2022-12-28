
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
	first_calories = 0
	second_calories = 0
	third_calories = 0
	elf_total_calories = 0

	for line in input_file:
		line = line.strip()
		if line != "":
			elf_total_calories += int(line)
		else:
			if elf_total_calories > first_calories:
				first_calories = elf_total_calories
			elif elf_total_calories >= second_calories:
				second_calories = elf_total_calories
			elif elf_total_calories >= third_calories:
				third_calories = elf_total_calories

			elf_total_calories = 0

	print(f"Top 3: {first_calories} {second_calories} {third_calories}")

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