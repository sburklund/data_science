import psycopg2

# Try to connect
try:   
    conn=psycopg2.connect(dbname= 'prod', 
                          host='preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com', 
                          port= '5439', 
                          user= 'username', 
                          password= 'password'
                          )
except:
    print("I am unable to connect to the database.")

cur = conn.cursor()  # create a cursor for executing queries
cur.execute("select * from sburklund.nucc_compare;")
data = cur.fetchall()

for row in data:
    print(row)

cur.execute("select * from edw.claims_monthly where proc_month >= '20190301' order by proc_month, claim_type;")
data = cur.fetchall()

for row in data:
    print(row)

cur.close() 
conn.close()