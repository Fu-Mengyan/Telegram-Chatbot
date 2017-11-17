'''

this module aims at facilitate the process of using database in the main program.
the module includes multiple functions.
Make use of csv files.
Including the usage of normal file reading and writing 
and dictionary reading and writing. 

'''
import csv
def filter(lst):
	return [item for item in lst if item != []]

class Data:
	def __init__(self,file_name,ID):
		self.file_name=str(file_name)
		self.ID=str(ID)
		self.data_buffer=[]
		self.count = 0

	def test(self):
		print(self.Database)

	def write_file(self,_field_name):
		with open(self.file_name+'.csv','w') as file:		
			write_file = csv.writer(file)
			write_file.writerow(_field_name)

	# read all keys, all value, personal value, and others value (row)
	def read_file(self,read_content,object=''):#output values: all, keys, all_values, specific_name_oriented_values
		with open(self.file_name+'.csv','r') as file:		
			read_file = filter(csv.reader(file))
			if read_content == 'values':
				read_file = read_file[1:]
			for line in read_file:
				if read_content == 'values':
					if line[3].lower() in object.lower():#the fourth value of the line: name(system default)
						self.data_buffer = []
						return line
					self.data_buffer.append(line)
				elif read_content == 'keys':
					return line
				elif read_content == 'personal value':
					if str(line[0]) == self.ID:
						return line
			return_list = self.data_buffer
			self.data_buffer=[]
			return return_list

	# read all value of one or self in dict
	def dict_reader(self,object = 'me'):
		with open(self.file_name+'.csv','r') as file:		
			read_file = filter(csv.DictReader(file))
			for line in read_file:
				if object == 'me':
					if line['ID']==self.ID:
						line = dict(line)
						return(line)
				elif line['Name'] == object:
					line = dict(line)
					return line
	
	# read vaue of a person, read id as default
	# used for sending message to others.
	def read_id(self,object = 'me'):
		with open(self.file_name+'.csv','r') as file:		
			read_id = filter(csv.DictReader(file))
			Me = ''
			id_buffer=[]
			for line in read_id:
				if line['ID']!=self.ID:
					id_buffer.append(line['ID'])
				else:
					Me = line['ID']
			if object == 'me':
				return Me
			else:
				return id_buffer

	def read_position(self):
		with open(self.file_name+'.csv','r') as file:
			read_position = filter(csv.DictReader(file))
			for line in read_position:
				if line['ID']==self.ID:
					return line['Hierarchy']

	# read all name in database except president.
	def read_name(self,restriction = []):
		with open(self.file_name+'.csv','r') as file:
			read_name = filter(csv.reader(file))
			name_buffer = []
			read_name = read_name[1:]
			for line in read_name:
				if line[2] not in restriction:
					name_buffer.append(line[3])
		return name_buffer

	# special function for group leaders
	# get the name of group members.
	def extract_group_member(self,groupname):
		with open(self.file_name+'.csv','r') as file:
			name_list = []
			read_name = filter(csv.DictReader(file))
			for line in read_name:
				if line['Group Name']==groupname:
					name_list.append(line['Name'])
			return name_list

	# for create a new profile in the database
	def append_file(self,list_values):
		with open(self.file_name+'.csv','a') as file:		
			append_file = csv.writer(file)
			append_file.writerow(list_values)

	# edit self or edit others file by president (change club officer position) 
	def edit_file(self,list_values,object = 'me'):# either to use DictReader and DictWriter depends largely on list_values input
		field_name = self.read_file('keys')
		_buffer = self.read_file('values')
		with open(self.file_name+'.csv','w') as file:
			write_file = csv.writer(file)
			write_file.writerow(field_name)
			if object == 'me':
				for line in _buffer:
					if line[0] == self.ID:
						new_line=list_values
						write_file.writerow(new_line)
					else:
						write_file.writerow(line)
			else:
				for line in _buffer:
					if line[3] == object:
						new_line=list_values
						write_file.writerow(new_line)
					else:
						write_file.writerow(line)

if __name__ == '__main__':
	print('Testing')