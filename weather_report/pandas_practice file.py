import pandas as pd

df=pd.read_csv('./squirrel_data.csv')
# pd.set_option('display.max.columns',31)
# pd.set_option('display.max.rows',100)
# df.head(50)
squirrel_color_df=df['Primary Fur Color']
squirrel_colors=squirrel_color_df.to_list()
squirrel_dict={}

for color in squirrel_colors:
    if not pd.isna(color):
        if color not in squirrel_dict :
            squirrel_dict[color]=1
        else:
            squirrel_dict[color]+=1
# print(squirrel_dict)
# squirrel_color=squirrel_dict.keys()
# count=squirrel_dict.values()
#
# dataframe_dict={
#     'Fur Color':list(squirrel_color),
#     'Count':list(count)
#
# }
# print(dataframe_dict)

df_color=pd.DataFrame(list(squirrel_dict.items()),columns=['Fur Color','Count'])
df_color.to_csv('squirrel_color.csv')

# df['Primary Fur Color'].value_counts().reset_index().to_csv('squirrel_color.csv', index=False, header=['Fur Color', 'Count'])

