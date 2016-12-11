import sys

def get_csv_file(file_path):
	csv_file = open(file_path, 'rt')

	return csv_file

def close_csv_file(csv_file):
	csv_file.close()

def close_files(output_files_dict):
	dict_values = list(output_files_dict.values())

	x = 0

	while(x < len(dict_values)):
		dict_values[x].close()
		x += 1