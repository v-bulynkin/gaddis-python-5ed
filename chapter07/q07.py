# Экзамен на получение водительских прав

# Проходной балл
CHECKPOINT = 15

def main():
  #reference = ['a','c','a','a','d','b','c','a','c','b','a','d','c','a','d','c','b','b','d','a']
	reference = get_answers(r'C:\temp\reference.txt')
	student_solution = get_answers(r'C:\temp\student_solution.txt')
	score = get_score(reference,student_solution)
	if score >= CHECKPOINT:
		print(f'Поздравляю, вы правильно ответили на {score} вопросов и успешно сдали экзамен!')
	else:
		print(f'К сожалению, вы ответили правильно только на {score} вопросов. Необходима пересдача.')

def get_answers(file_path):
	answers_file = open(file_path, 'r')
	answers_raw = answers_file.readlines()
	answers_file.close()
	answers_list = [i.rstrip('\n') for i in answers_raw]
	return answers_list
	
def get_score(reference,student_solution):
	score = 0
	for i in range(len(reference)):
		if student_solution[i].lower() == reference[i]:
			score += 1
	return score

if __name__ == '__main__':
	main()

