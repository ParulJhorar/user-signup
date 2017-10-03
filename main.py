from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)
app.config['DEBUG']= True


@app.route("/", methods = ['POST'])
def user_signup():
    name = request.form ['username']
    password = request.form['password']
    vpassword=request.form['vpassword']
    email=request.form['email']
    name_error=''
    password_error=''
    vpassword_error=''
    email_error=''

    if name=="" or len(name) < 3 or len(name) >20 or ' ' in name:
        name_error="Please enter a valid username"
    if password ==''or vpassword!=password:
        password_error="Please enter a valid password"
    if vpassword =='' or vpassword!=password:
        vpassword_error="Passwords doesn't match" 
    if email!='' : 
        if len(email) <3 or len(email)>20 or ' ' in email or email.count('@')>1 or email.count('.')>1:
             email_error="Please enter a valid email."



    if not name_error and not password_error and not vpassword_error and not email_error:
        return render_template('welcome.html', name=name)
    else:
        return render_template ('edit.html',name =name,email=email,name_error=name_error,password_error=password_error, vpassword_error=vpassword_error,email_error=email_error)   





    

@app.route("/")
def index():
    return render_template ('edit.html')

app.run()