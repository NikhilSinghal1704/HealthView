from flask import Flask, render_template, request, redirect, url_for, session, flash
import healthview
import secrets

app=Flask(__name__)
secret_key = secrets.token_hex(16)
app.secret_key = secret_key
mail = ""

@app.route("/")
def home():
    
    #if mail != "":
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@app.route('/medcalable')
def history():
    return render_template('medcalable.html')

@app.route("/About")
def about():
    return render_template("About.html")

@app.route("/Firstaid")
def first():
    return render_template("Firstaid.html")

@app.route("/aid_details/<word>")
def aid_details(word):
    print(word)
    flag3 = healthview.data(word)
    data = {
        'title': word,
        'header': flag3[0],
        'body': flag3[1],
        'src': flag3[2]
        }
    return render_template('aid_details.html', data=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route('/loginform', methods=['POST'])
def login_form():
    email = request.form['email']
    password = request.form['password']
    
    flag = healthview.get_login_row(email)
    #print(flag)
    #print(password)
    if flag is not None and password == flag[2]:
        # Successful login
        mail = email
        session['email'] = email
        return redirect(url_for("dashboard"))
    else:
        flash('Invalid email or password', 'error')
        return redirect(url_for("login"))
    
        
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        # Retrieve the user's input from the form fields
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']
        login_list = [name, password, email]
        flag2 = healthview.get_login_row(email)
        if password == confirm_password:
            if flag2 is None:
                healthview.add_to_login_database(login_list)
                return render_template('login.html')
            else:
                flash('Account already exists', 'error')
                return redirect(url_for("login"))
        else:
            # Render the template with an error message
            return render_template('signup.html', error_message="Passwords do not match")

    # Render the template with an empty form
    return render_template('signup.html', error_message="")

@app.route('/protected')
def protected():
    if not session.get('logged_in'):
        return 'You need to log in first'
    else:
        return 'This is a protected page'

@app.route('/logout')
def logout():
    session['logged_in'] = False
    return 'Logged out successfully!'

app.run()