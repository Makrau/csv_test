#!/usr/bin/python3
from files_handler import *
from csv_handler import *
import sys

def main(file_path):
	csv_file = get_csv_file(file_path)
	reader = get_reader_csv(csv_file)
	write_filtred_csv(reader)

	close_csv_file(csv_file)

if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		print("Insufficient arguments. Please, set the csv file path.")