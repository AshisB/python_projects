#extracting mail format
with open('./Input/Letters/starting_letter.txt',mode='r') as file:
    letters=file.read()
    print(letters)



#extracting invited names
with open('./Input/Names/invited_names.txt',mode='r') as file:
    names=file.readlines()
    for name in names:
        new_name=name.strip('\n')
        new_letter = letters.replace('[name]', new_name)
        print(new_letter)
        with open(f'./Output/ReadyToSend/mail_to_{new_name}.txt', 'w') as file:
            file.write(letters)

    



