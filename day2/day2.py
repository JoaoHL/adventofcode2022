label = dict()
label["A"] = label["X"] = 0
label["B"] = label["Y"] = 1
label["C"] = label["Z"] = 2

points = list()
x_score = [4,1,7]
y_score = [8,5,2]
z_score = [3,9,6]
points.append(x_score)
points.append(y_score)
points.append(z_score)

#parte 1
with open('day2.input', 'r') as file:
	total_points = 0
	for line in file:
		line = line.strip()
		opponent, me = [label[x] for x in line.split()]
		total_points += points[me][opponent]

	print(total_points)

#parte 2
outcomes = dict()
outcomes["A"] = {"X": "C", "Y": "A", "Z": "B"}
outcomes["B"] = {"X": "A", "Y": "B", "Z": "C"}
outcomes["C"] = {"X": "B", "Y": "C", "Z": "A"}
with open('day2.input', 'r') as file:
	total_points = 0
	for line in file:
		line = line.strip()
		inputs = line.split()
		opponent = label[inputs[0]]
		must_choose = outcomes[inputs[0]][inputs[1]]
		me = label[must_choose]
		total_points += points[me][opponent]

	print(total_points)