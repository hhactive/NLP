import pandas as pd
import datetime

def insertNew(DataPath,words,outputPath,source='default'):
    df1=pd.read_csv(DataPath)
    #get date as formatted
    today = datetime.date.today()
    formatted_today = today.strftime("%Y-%m-%d")
    currnum = df1['Index'].max()
    currnum1=currnum
    columns=df1.columns
    for newword in words:
        if newword not in df1['TEXT']:
            currnum += 1
            df1.loc[currnum+3]=[currnum,newword,today,source]
            #df1.append({'Index':currnum,'TEXT':newword,'Date':today,'Source':source},ignore_index=True)

    print('We added {0} words to list!'.format(currnum-currnum1))
    df1.to_csv(outputPath,index=False)


