import os


def main():
	INPUT_PATH='/home/fury/github/dbc_model/IRL_dogs'
	input_names = os.listdir(INPUT_PATH)

	for name in input_names:
		if name.endswith('.jpg'):
			target_file=INPUT_PATH+"/"+name
			# print("TESTING: " + name)
			os.system("python -m src.inference.classify file " + target_file)
			# print("\n\n\n")

if __name__ == '__main__':
	main()