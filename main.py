from flask import Flask, render_template, request, json
import dbtool
import jsontool
import sqlite3
 
app = Flask(__name__)
 
@app.route('/')
def homeView():
    name='test'
    return render_template('home.html', name=name)
    
@app.route('/matching')
def matchingView():
	test = jsontool.matchingLoad()
	return render_template('matching.html', debug = test)

@app.route('/bonsaibook', methods=['GET','POST'])
def bonsaibookView():
	con = sqlite3.connect('bonsai.sqlite3')
	sql = createSql()
	cur = con.cursor()
	cur.execute(sql)
	# for row in cur.fetchall():
	# 	print(row)
	# for row in cur:
	# 	print(row[0], row[1])
	bonsai_data_list = cur.fetchall()
	print(bonsai_data_list[0][5])
	con.close()
		# print(request.form['action'])
	return render_template('bonsaiBook.html', title="盆栽図鑑", bonsai_list = bonsai_data_list, bonsai_count = len(bonsai_data_list))
	# if request.method == 'GET':
	# 	print(request.args.get('kind'))
	# 	return render_template('bonsaiBook.html', title="盆栽図鑑", name=["黒松","真柏"])
	# else:
	# 	print("test")
	# 	return render_template('bonsaiBook.html', title="盆栽図鑑", name=["黒松","真柏"])

def createSql():
    sql = "SELECT * FROM bonsai"
    return sql

@app.route('/simulation')
def simulationView():
    return render_template('simulation.html')

@app.route('/postTest', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name"
    return render_template('post.html', name = name)
 
if __name__ == '__main__':
    app.run()