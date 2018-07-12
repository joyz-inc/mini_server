from flask import Flask,request
from flask import Flask
from flask import render_template ,flash, redirect,session
from forms import MyForm
app = Flask(__name__)


app.config['SECRET_KEY']='bendawang'

@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html',title = 'Sign in',form=form)

@app.route('/success',methods = ['GET', 'POST'])
def success():
    name=request.form.get("name")#session.get('name')
    file = open("./word.txt")
    words = file.read()
    if name in words:
        validation = "Valid Word"
    else:
        validation = "invalid word"
    return render_template('success.html',title = validation)

@app.route('/')
def hello():
    file = open("./word.txt")
    words = file.read()
    if request.args.get('word') in words:
        return "True word"
    else:
        return "False word"


if __name__ == '__main__':
    app.run(host = "0.0.0.0",port=5000)
