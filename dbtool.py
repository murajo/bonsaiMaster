import sqlite3
 
def bonsaiBookGet():
	table_name = 'bonsai'
	con = sqlite3.connect('bonsai.sqlite3')
	sql = createSql(table_name)
	cur = con.cursor()
	cur.execute(sql)
	bonsai_data_list = cur.fetchall()
	con.close()
	return bonsai_data_list

# whereはlist型で渡す
def createSql(table, where=""):
	sql = "SELECT * FROM " + table
	if where != "":
		sql = sql + " where " + where
	# where = ["question_id=question_id"]
	# if where != "":
	# 	if type(where) == list:
	# 		print("aiueo")
	# 		for whe in where:

	# 	else:
	# 		sql = sql + " " + where
	return sql

def questionGet(question_id):
	con = sqlite3.connect('bonsai.sqlite3')
	table_name = 'question'
	where = 'question_id=' + str(question_id)
	sql = createSql(table_name, where)
	cur = con.cursor()
	cur.execute(sql)
	question = cur.fetchall()
	con.close()
	return question

def choiceGet(question_id):
	con = sqlite3.connect('bonsai.sqlite3')
	table_name = 'choice'
	where = 'question_id=' + str(question_id)
	sql = createSql(table_name, where)
	cur = con.cursor()
	cur.execute(sql)
	choice_list = cur.fetchall()
	con.close()
	return choice_list