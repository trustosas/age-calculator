from datetime import date, time, datetime
from dateutil.relativedelta import relativedelta
import datetime

#Enter your birthday
birthday = '4-8-2001'
#birthday = str(input('Enter your birthday in DD-MM-YYYY format:\n'))

#A datetime object is created with the provided birthday
datetime_object = datetime.datetime.strptime(birthday, '%d-%m-%Y')

birthtime = ''

"""(OPTIONAL) Enter your birthtime or press ENTER to skip [comment out the line after this docstring (line 16) if you don't want the functionality in the code]
Please note that the code will naively assume you were born at 00:00 or 12am of your birthday if this piece of information is not provided"""
#birthtime = str(input('Enter your birthtime in HH:MM (24-hour format), if you are aware of it or simply press ENTER to skip:\n'))

#Updating the datetime object with hour & minute information, if provided
if birthtime != '':
	datetime_object = datetime_object.replace(hour=int(birthtime[0:2].replace(':', '')), minute=int(birthtime[3:5]))

#Creating a relative delta (This is where the magic happens!)
age_rdelta = relativedelta(datetime.datetime.now(), datetime_object)

#A dictionary containing the attributes of the relative delta is created (for reference purposes)
rdelta_dict = {'year': age_rdelta.years, 'month': age_rdelta.months, 'week': age_rdelta.weeks, 'day': age_rdelta.days, 'hour': age_rdelta.hours, 'minute': age_rdelta.minutes}
#print(rdelta_dict)

#Conditional formatting of the output string
rdelta_value_list = []
for key, value in rdelta_dict.items():
	if value == 0 or key == list(rdelta_dict)[-1]:
		pass
	else:
		rdelta_value_list.append(f'{value} {key}{"s" if value != 1 else ""}')
output_string ="You've lived for " + ' and '.join([', '.join(rdelta_value_list), f'{rdelta_dict[list(rdelta_dict)[-1]]} {list(rdelta_dict)[-1]}{"s" if rdelta_dict[list(rdelta_dict)[-1]] != 1 else ""}.'])

#A near exact time at which the output was printed out
print(f'The current date & time is {datetime.datetime.now()}')

#Final result
print(output_string)