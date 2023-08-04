from flask import Flask, render_template, request;

app = Flask(__name__)

@app.route('/home')
def home_fun():
    return 'this is home page'

@app.route('/<custom_route>')
def custom_fun(custom_route):
    return f'this is     {custom_route}';

@app.route('/login',methods=['POST','GET'])
def login_fun():
    if request.method=='POST':
        fname=request.form['fullname']
        passwrd=request.form['password']
        return f'successfully login with fullname : {fname}  password : {passwrd}';
    else:
        return render_template('index.html')

if __name__=='__main__':
    app.run()
#__name__ : predefined variable __main__
#__main__ : 