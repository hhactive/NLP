import extxt
import insnew
def InputModel():
    print('----------Input Model------')
    inputpath1 = 'E:\\Programming\\2021\\Words\\Park Avenue.txt'
    datapath = 'E:\\Programming\\2021\\Words\\words2020_0313_new.csv'
    outputpath = 'E:\\Programming\\2021\\Words\\words2020_0314.csv'
    words=extxt.process(inputpath1)
    print(len(words))
    print(words)
    source='Park Avenue'
    print('Do you want to add these to data file? (Y/N)')
    st=input()
    if st=='Y':
        insnew.insertNew(datapath,words,outputpath,source)
    print('---------Done-------------')

def OutputModel():
    print('---------Output Model-----------')
    datapath = 'E:\\Programming\\2021\\Words\\words2020_0313_new.csv'
    outputpath='E:\\Programming\\2021\\Words\\newwords2020_0313_new.txt'
    cdate='2021-03-14'
    extxt.processout(datapath,outputpath,cdate)



print('Please select Model: (1)Input  (2)Output')
typ=input()
if typ=='1':
    InputModel()
elif typ=='2':
    OutputModel()
else:
    print('Not a valid selection')
