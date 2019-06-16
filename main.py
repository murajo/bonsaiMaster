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
	question = ''
	choice = ''
	result = ''
	rootLog = str(request.json['rootLog']) + str(request.json['choice_id'])
	question_id = matching.matchingRoot(rootLog)
	if question_id != 0:
		question = dbtool.questionGet(question_id)
		choice = dbtool.choiceGet(question_id)
		return_data = {"rootLog": rootLog, "question_text": question[0][1], "choice_list": choice, "choice_count": len(choice), "result": result}
	else:
		result = matching.resultGet(rootLog)
		return_data = {"rootLog": rootLog, "result": result}
	return jsonify(ResultSet=json.dumps(return_data))

@app.route('/bonsaibook', methods=['GET','POST'])
def bonsaibookView():
	if request.args.get('id'):
		where = "bonsai_id = " + request.args.get('id')
		bonsai_data_list = dbtool.bonsaiBookGet(where)
	elif request.args.get('keyword'):
		where = "bonsai_name like '%" + request.args.get('keyword') + "%' OR" 
		where = where + " training_difficulty like '%" + request.args.get("keyword") + "%' OR"
		where = where + " description like '%" + request.args.get("keyword") + "%' OR"
		where = where + " cultivate like '%" + request.args.get("keyword") + "%' OR"
		where = where + " price_range like '%" + request.args.get("keyword") + "%' OR"
		where = where + " kind like '%" + request.args.get("keyword") + "%' OR"
		where = where + " season like '%" + request.args.get("keyword") + "%'"
		print(where)
		bonsai_data_list = dbtool.bonsaiBookGet(where)
	else:
		bonsai_data_list = dbtool.bonsaiBookGet()
	return render_template('bonsaiBook.html', title="盆栽図鑑", bonsai_list = bonsai_data_list, bonsai_count = len(bonsai_data_list))


@app.route('/simulation')
def simulationView():
    return render_template('simulation.html', title='盆栽シュミレーション')

@app.route('/request')
def requestView():
    return render_template('request.html', title='お問い合わせ')
 
if __name__ == '__main__':
    app.run()