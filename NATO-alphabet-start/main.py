# student_dict = {
#     "student": ["Angela", "James", "Lily"], 
#     "score": [56, 76, 98]
# }

# #Looping through dictionaries:
# for (key, value) in student_dict.items():
#     #Access key and value
#     pass

# import pandas
# student_data_frame = pandas.DataFrame(student_dict)

# #Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
#     #Access index and row
#     #Access row.student or row.score
#     pass

# # Keyword Method with iterrows()
# # {new_key:new_value for (index, row) in df.iterrows()}

# #TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

# #TODO 2. Create a list of the phonetic code words from a word that the user inputs.

import pandas as pd

data_nato=pd.read_csv('nato_phonetic_alphabet.csv')
# print(data_nato)
df=pd.DataFrame(data_nato)
# new_dict={value['letter']:value['code'] for index,value in df.iterrows()}
new_dict={value.letter:value.code for value in df.itertuples()}

is_on=True
while is_on:
    user_input=input('Enter a word: ').upper()
    if user_input=='EXIT':
        is_on=False
    else:    
        nato_aplha=[(letter,new_dict[letter]) for letter in user_input if letter in new_dict]
        [print(f'{item[0]}=>{item[1]}\n') for item in nato_aplha]
    

    





