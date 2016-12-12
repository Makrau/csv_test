import csv
from files_handler import close_files

def get_reader_csv(csv_file):
	reader = csv.reader(csv_file, delimiter=';')

	return reader

def write_row(writers_dict, header_dict, row):
	col_number = 0
	filtred_row = []
	for col in row:
		if col_number in header_dict.values():
			filtred_row.append(row[col_number])

		col_number += 1
		service_name = row[header_dict['service']]
		key = get_key_by_service_name(service_name)

	writers_dict[key].writerow(filtred_row)

def get_key_by_service_name(service_name):
	if len(service_name) > 51:
		key = service_name[19:-32]

	return key

def update_output_files_dict(output_files_dict, service_name):
	key = get_key_by_service_name(service_name)

	if key in list(output_files_dict.keys()):
		return output_files_dict

	else:
		file_name = key + '.csv'
		new_output_file = open(file_name, 'wt')
		output_files_dict.update({key:new_output_file})
		return output_files_dict

def update_writers_dict(writers_dict, service_name, output_files_dict):
	key = get_key_by_service_name(service_name)

	if key in list(writers_dict.keys()):
		return writers_dict

	else:
		new_csv_writer = csv.writer(output_files_dict[key], delimiter=';')
		writers_dict.update({key:new_csv_writer})
		return writers_dict

def write_filtred_csv(reader):
	status_change_flags = ['27', '28']
	#default_ouput_file = open('default_output.csv', 'wt')
	output_files_dict = {}
	#default_writer = csv.writer(output_files_dict['default'], delimiter=';')
	writers_dict = {}
	row_counter = 0

	for row in reader:
		if row_counter == 0:
			header = row
			header_dict = generate_header_dict(header)
			row_counter += 1
			header =  ['tn', 'date', 'history_type_id', 'name', 'service', 'create_time']
			#writers_dict['default'].writerow(header)

		elif row[header_dict['history_type_id']] in status_change_flags:
			service_name = row[header_dict['service']]
			output_files_dict = update_output_files_dict(output_files_dict, service_name)
			writers_dict = update_writers_dict(writers_dict, service_name, output_files_dict)
			write_row(writers_dict, header_dict, row)

	close_files(output_files_dict)

def generate_header_dict(header):
	header_dict = {}
	values_of_interest = ['tn', 'date', 'history_type_id', 'name', 'service', 'create_time']
	
	x = 0

	while(x < len(header)):
		if header[x] in values_of_interest:
			header_dict[header[x]] = x
		x += 1

	return header_dict