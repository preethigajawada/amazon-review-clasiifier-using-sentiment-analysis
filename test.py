
from flask import Flask,render_template,request
import pymysql as sql


app= Flask(__name__)

@app.route("/abc",methods=["GET","POST"])
def tu():
	if(request.method=='POST'): 
			db_connection= sql.connect(host="localhost",user="root",password="",database="amazonreview") 
			cur=db_connection.cursor()
			print("Done")
			name = request.form.get('name')
			email = request.form.get('email')
			phone = request.form.get('phone')
			password = request.form.get('password')
			cur.execute("INSERT INTO userdetails(Name,Email,Phone,Password) VALUES(%s,%s,%s,%s)"%(name,email,phone,password))
			db_connection.commit()
			db_connection.close()
	return render_template('login.html',n=name)

app.run(debug=True)

@app.route("/signup")
def f():
	return render_template("signup.html")