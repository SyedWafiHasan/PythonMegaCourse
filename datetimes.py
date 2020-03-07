import datetime

filename = datetime.datetime.now()

def create_file():
	with open(str(filename), 'w') as file:
		file.write(f"This file was created  at {filename}")

create_file()
