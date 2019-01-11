from flask import Flask, render_template, request
import dbtool
 
app = Flask(__name__)
 
@app.route('/')
def homeView():
    name='test'
    return render_template('home.html', name=name)
    
@app.route('/matching')
def matchingView():
    return render_template('matching.html')

@app.route('/bonsaibook')
def bonsaibookView():
    return render_template('bonsaiBook.html', name=["黒松","真柏"])

def createSql():
    kind = request.args.get('kind')
    size = request.args.get('size')
    sql = "SELECT * FROM bonsai WHERE "
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