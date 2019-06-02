import psycopg2
conn=psycopg2.connect(dbname= 'prod', 
                     host='preverity-prod.c1klgawkvuni.us-east-1.redshift.amazonaws.com', 
                     port= '5439', 
                     user= 'username', 
                     password= 'password'
                     )

cur = conn.cursor()  # create a cursor for executing queries
cur.execute("select * from sburklund.nucc_compare;")
cur.fetchall()
print(cur.fetchall())


cur.close() 
conn.close()