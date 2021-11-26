from random import choice
questions = ['Why is the sky blue? ', 'Why do birds sing? ', 'Why do the stars shine? ']
question = choice(questions)
answer = input(question).lower().strip()
while answer != 'just because':
    answer = input("Why ").strip().lower()
print('Oh, okay')
