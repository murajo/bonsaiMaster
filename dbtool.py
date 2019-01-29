import sqlite3
 
con = sqlite3.connect('bonsai.sqlite3')

def query_run(sql):
    cur = con.cursor()
    cur.execute(sql)
    # for row in cur:
    #     print(row[0], row[1])
    con.close()
    return cur