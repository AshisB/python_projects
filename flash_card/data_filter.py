import pandas as pd
import json
class DataFilter:
    def __init__(self):
        self.GetData()

    def GetData():    
        try:
            with open('./data/word_list.json','r') as f:
                datalist=json.load(f) 
        except FileNotFoundError:        
            df=pd.read_csv('./data/english_words.csv')
            datalist=[({'english':row.English,'nepali':row.Nepali,'correct':0}) for row in df.itertuples()]
        
        return datalist  

    # def GetData():    
    #     df=pd.read_csv('./data/english_words.csv')
    #     datalist=[({'english':row.English,'nepali':row.Nepali,'correct':0}) for row in df.itertuples()]
    #     return datalist 