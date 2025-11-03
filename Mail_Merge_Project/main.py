#extracting mail format
with open('./Input/Letters/starting_letter.txt',mode='r') as file:
    letters=file.read()
    words=letters.split()


#extracting invited names
with open('./Input/Names/invited_names.txt',mode='r') as file:
    names=file.read()
    name_list=names.split()



positions=[1,9,14]



for name in name_list:
    mail = ''
    words[1]=name+','
    for word in words:
        mail += word
        if words.index(word) in positions:
           mail+='\n'
        else:
            mail+=" "

    with open(f'./Output/ReadyToSend/mail_to_{name}.txt', 'w') as file:
        file.write(mail)


