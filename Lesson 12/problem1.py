import time
import random

print('-'*65)
print('Welcome! I am the Magic 8 Ball')
print()
question = input('What is your question, my child? ')
time.sleep(1)
print('processing!')
time.sleep(1)
print('...thinking...')
time.sleep(1)
print('...thinking...')
time.sleep(1)

choice = random.randint(1,6)

if choice == 1:
	print('Uhhh no?')
elif choice == 2:
	print('maybe? ')
elif choice == 3:
	print('How would I know? ')
elif choice == 4:
	print('I have no idea')
elif choice == 5:
	print('Idk bro')
elif choice == 6:
	print('Bye')

print('-'*65)