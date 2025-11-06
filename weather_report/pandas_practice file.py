import pandas



data_dictionary={
    'name':'Ashis',
    'address':'Khokana',
    'phone':9861909242
}
data=pandas.Series(data_dictionary)
print(data.to_list)