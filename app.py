from flask import Flask,render_template,request,redirect,url_for,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(minutes = 10)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=["POST","GET"])
def index():
    if request.method == 'POST':
        session.permanent = True
        user = request.form['nm']
        session['user'] = user
        return redirect(url_for('user', usr=user))
    else:
        return render_template("login.html")



@app.route('/<usr>')
def user(usr):
   if 'user' in session :
    user = session['user'] 
    return f'<h1>{usr}<h1>'
   else:
      return redirect(url_for('login'))
   
@app.route('/logout')
def logout():
    session.pop('user', None)
    return render_template('login')


if __name__== '__main__':
 app.run(debug=True)