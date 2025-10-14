from turtle import Turtle,Screen
from prettytable import PrettyTable

table=PrettyTable()
# table.field_names=['SN','Name','Roll','Marks']
table.add_column('Pokemon Name',['Pikachu','Squirtle','Charmander'])
table.add_column('Type',['Electric','Water','Fire'])
table.align='l'
print(table)
# timmy=Turtle()
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)
#
# my_screen=Screen()
# my_screen.exitonclick()
