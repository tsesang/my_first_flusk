from flask import Flask,render_template,request;

app = Flask(__name__);

@app.route('/')
def home_func():
    return "HOME PAGE"

@app.route('/signup',methods=['POST','GET'])
def signup_func():
    if request.method=='POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        password = request.form['password']
        repassword = request.form['repassword']

        if(password!=repassword):
            return "password not matching ... "
        else:
            return render_template('signup_details.html',success="SIGNUP SUCESS !!!",fname=fname,lname=lname,email=email,password=password,repassword=repassword);
    else:
        return render_template('signup.html')

if __name__=='__main__':
    app.run();