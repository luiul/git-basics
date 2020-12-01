import sys

<<<<<<< HEAD
def cat():
	print("Meow!")
=======
def dog():
	print('Woof!')
>>>>>>> dog

def default():
	print('Hello!')

def main():
<<<<<<< HEAD
	if sys.argv[1] == 'cat':
		cat()
=======
	if sys.argv[1] == 'dog':
		dog()
>>>>>>> dog
	else: 
		default()

if __name__ == '__main__':
	main()