from flask import Flask,render_template,request,redirect,url_for,session,flash
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes = 10)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        flash("Login successful!")
        session['user'] = user
        return redirect(url_for('user', user=user))
    else:
        if "user" in session:
            flash("Already logged in!")
            return redirect(url_for("user"))
        return render_template("login.html")



@app.route('/user')
def user():
   if 'user' in session :
    user = session['user'] 
    return render_template("view.html")
   else:
      return redirect(url_for('login'))
   
@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("You have been loggedout!", "info")
    return redirect(url_for('login'))


if __name__== '__main__':
 app.run(debug=True, port=9000)