import pandas as pd 
import quandl 

#api_key = open('apikeys/quandlapikey.txt', 'r').read()

#df = quandl.get("FMAC/HPI_TX", authtoken = api_key)
df = quandl.get("FMAC/HPI_TX", authtoken = 'ZpBWE7_zn_D9Jz8z2if7')

print(df.head())

fiddy_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states') 
print(fiddy_states[0][1][1:])

for abbv in fiddy_states[0][0][1:]:
#    print(abbv)
    print("FMAC/HPI_"+str(abbv))
    