#!/usr/bin/python3
import csv
import sys

def filter_dict_header(header):
	#Setting default values. But it still should find what is the correct position
	header_dict = {}
	values_of_interest = ['tn', 'date', 'history_type_id', 'name', 'service', 'create_time']
	
	x = 0

	while(x < len(header)):
		if header[x] in values_of_interest:
			print(header[x] + ' in the position ' + str(x))
			header_dict[header[x]] = x
		x += 1

	return header_dict

def main(file_path):
	csv_file = open(file_path, 'rt')

	reader = csv.reader(csv_file, delimiter=';')
	row_counter = 0

	status_change_flags = ['27', '28']

	for row in reader:
		if row_counter == 0:
			header = row
			header_dict = filter_dict_header(header)

		elif row[header_dict['history_type_id']] in status_change_flags:
			print('row# ' + str(row_counter + 1) + ' ' + row[header_dict['name']])

		row_counter += 1

		if row_counter > 100:
			break

	csv_file.close()

if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		print("Insufficient arguments. Please, set the csv file path.")