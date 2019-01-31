from flask import Flask, render_template, request, json, jsonify
import dbtool
import matching
import sqlite3
import json
 
app = Flask(__name__)
 
@app.route('/')
def homeView():
    return render_template('home.html', title='盆栽マスター')
    
@app.route('/matching')
def matchingView():
	return render_template('matching.html', title='盆栽マッチング')



@app.route('/matching_post', methods=['POST'])
def matchingProcess():
	print(request.json)
	rootLog = request.json['rootLog']
	question_id = matching.matchingRoot(rootLog)
	question = dbtool.questionGet(question_id)
	choice = dbtool.choiceGet(question_id)
	print(question[0][1])
	return_data = {"rootLog": rootLog, "question_text": question[0][1], "choice_list": choice, "choice_count": len(choice)}
	return jsonify(ResultSet=json.dumps(return_data))

@app.route('/bonsaibook', methods=['GET','POST'])
def bonsaibookView():
	bonsai_data_list = dbtool.bonsaiBookGet()
	return render_template('bonsaiBook.html', title="盆栽図鑑", bonsai_list = bonsai_data_list, bonsai_count = len(bonsai_data_list))


@app.route('/simulation')
def simulationView():
    return render_template('simulation.html', title='盆栽シュミレーション')

@app.route('/postTest', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        name = request.form['name']
    else:
        name = "no name"
    return render_template('post.html', name = name)
 
if __name__ == '__main__':
    app.run()