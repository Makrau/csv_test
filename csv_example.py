#!/usr/bin/python3
import csv
import sys

def generate_header_dict(header):
	header_dict = {}
	values_of_interest = ['tn', 'date', 'history_type_id', 'name', 'service', 'create_time']
	
	x = 0

	while(x < len(header)):
		if header[x] in values_of_interest:
			print(header[x] + ' in the position ' + str(x))
			header_dict[header[x]] = x
		x += 1

	return header_dict

def write_filtred_csv(reader):
	status_change_flags = ['27', '28']
	output_file = open('filtred_tickets.csv', 'wt')
	writer = csv.writer(output_file, delimiter=';')
	row_counter = 0

	for row in reader:
		if row_counter == 0:
			header = row
			header_dict = generate_header_dict(header)
			row_counter += 1
			header =  ['tn', 'date', 'history_type_id', 'name', 'service', 'create_time']
			writer.writerow(header)

		elif row[header_dict['history_type_id']] in status_change_flags:
			col_number = 0
			filtred_row = []
			for col in row:
				if col_number in header_dict.values():
					print('value to be printed: ' + row[col_number])
					filtred_row.append(row[col_number])

				col_number += 1

			print('filtred_row after for: ' + str(filtred_row))
			writer.writerow(filtred_row)

	output_file.close()

def main(file_path):
	csv_file = open(file_path, 'rt')
	reader = csv.reader(csv_file, delimiter=';')
	write_filtred_csv(reader)

	csv_file.close()

if __name__ == "__main__":
	if len(sys.argv) > 1:
		main(sys.argv[1])
	else:
		print("Insufficient arguments. Please, set the csv file path.")