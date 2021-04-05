#print("Hello Preksha"+__name__)# here it will give output __name__ as main but if you import this filein another file then it will give the name of file
#__name__ is a special variable for main
def main():
	print("Hello from main")


if __name__ == "__main__":# it will print the statement only if this file is main file
	main()
