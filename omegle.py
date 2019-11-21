def calcGrades(namenscores):
	name = ""
	sc = []
	index = 0
	average = 0
	while index < len(namenscores):
		if(namenscores[index] == "_"): 
			break 
		name += namenscores[index]
		index += 1

	while index < len(namenscores):
		if(namenscores[index] != "_"):
			break
		index += 1

	while index < len(namenscores):
		if(namenscores[index] == " "):
			index += 1
		sc.append(namenscores[index])
		index += 1
	for number in sc:
		average += float(number)

	average /= len(sc)

	grade = round(average) 

	print("{} has an average of {}".format(name,int(grade)))

def preparegraph(similaritynnames):
	string = similaritynnames.split(";")
	scores = string[0].split("=")
	names = string[1].split(",")

	graph = ""

	index = 0

	while index < len(scores):
		score = int(scores[index])
		
		if(score == 0):
			graph += "_"
		if(score > 0 and score < 20):
			graph += "-"
		if(score >= 20):
			graph += "^"
		index += 1

	print(graph)
	if(len(names) > 1):
		for n in names:
			print(n)
	else:
		print("No matches found")








def main():
	filename = input("Input the file name: ")

	f = open(filename, "r")
	line = f.readline()

	while line:
		namenscores = line.strip()
		similaritynnames = f.readline()

		calcGrades(namenscores)
		preparegraph(similaritynnames)

		line = f.readline()

	f.close()

main()
