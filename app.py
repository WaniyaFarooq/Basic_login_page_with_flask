from flask import Flask,request,redirect,url_for,session,Response,render_template

app = Flask(__name__)
app.secret_key  = "supersecret"  #we use it with session to lock it taky koi bahir sy modify na kr len 

 
@app.route("/",methods = ["GET","POST"])
def login():
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        valid_users ={
            'admin':'123',
            'waniya':'pass',
            'muazan':'word'
        }
        if username  in valid_users and password ==valid_users[username] :
            session["user"] = username
            return redirect(url_for("welcome"))
        
        else:
            return render_template("login.html", error="Invalid username or password")
            # return Response(f"Invalid credentials. try again {username}",mimetype="text/plain")  #by default text / html 
        
    return render_template("login.html")


@app.route("/welcome")
def welcome():
    if "user" in session: #agar user k data session main agaya h
        return render_template("welcome.html", user=session["user"])
    return redirect(url_for("login"))
    #     return f'''
    # <h2>Welcome,{session["user"]}!</h2>
    # <a href = {url_for("logout")}>Logout</a>
    # '''
    # return redirect(url_for("login"))

#logout route
@app.route("/logout")
def logout():
    session.pop("user",None)#agar in some case user bhi hn to none error sy bachy ga
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)
        
        
    
        