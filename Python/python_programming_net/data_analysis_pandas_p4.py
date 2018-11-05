import pandas as pd 
import quandl 

api_key = open('C:\\Users\\Scott Burklund\OneDrive - Preverity, Inc\\Personal\\data_science\\apikeys\\quandlapikey.txt', 'r').read()

df = quandl.get("FMAC/HPI_TX", authtoken = api_key)

print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states') 
print(fiddy_states[0][1][1:])

for abbv in fiddy_states[0][0][1:]:
#    print(abbv)
    print("FMAC/HPI_"+str(abbv))
    
