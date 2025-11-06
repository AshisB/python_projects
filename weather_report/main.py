# import csv
# with open('weather_data.csv') as data_file:
#     data=csv.reader(data_file)
#     print(data)
#     temperatures=[]
#     count=1
#     for row in data:
#         print(row)
#         if count!=1:
#             temperature_of_a_day=int(row[1])
#             temperatures.append(temperature_of_a_day)
#         count+=1
#     print(temperatures)


import pandas

data=pandas.read_csv('weather_data.csv')
list_data=data['temp'].to_list()
average=data['temp'].mean()
maximum=data['temp'].max()
print(average)
print(maximum)

print(data[data.temp==maximum])
monday=data[data.day=='Monday']
print(monday.temp)
celcius=monday.temp
fahrenheit=(celcius*(9/5))+32
print(fahrenheit)
