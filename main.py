from flask import Flask
from flask import render_template
 
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
    return render_template('bonsaiBook.html')

@app.route('/simulation')
def simulationView():
    return render_template('simulation.html')
 
if __name__ == '__main__':
    app.run()