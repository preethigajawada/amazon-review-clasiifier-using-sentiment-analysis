from flask import Flask,render_template,request
#from flask_sqlalchemy import SQLAlchemy
import pymysql as sql
from textblob import TextBlob

app= Flask(__name__)

session={}

@app.route("/")

def hello():
	return render_template("index.html")

@app.route("/login")
def login():
	
	return render_template("login.html")


@app.route("/signup")
def signup():
	return render_template("signup.html")

@app.route("/abc",methods =["GET","POST"])

def contact():
	if(request.method=='POST'): 
		db_connection= sql.connect(host="localhost",user="root",password="",database="amazonreview") 
		cur=db_connection.cursor()
		name = request.form.get('name')
		email = request.form.get('email')
		phone = request.form.get('phone')
		password = request.form.get('password')
		cur.execute("INSERT INTO userdetails(Name,Email,Phone,Password) VALUES(%s,%s,%s,%s)",[name,email,phone,password])
		db_connection.commit()
		db_connection.close()
		return render_template('login.html')


@app.route("/def",methods=["GET","POST"])

def fg():
	if(request.method=='POST'):
			db_connection= sql.connect(host="localhost",user="root",password="",database="amazonreview") 	
			name= request.form.get('name')
			email=request.form.get('email')
			password=request.form.get('password')
			cur=db_connection.cursor()
			cur.execute("SELECT * from userdetails where Name='%s' and Password='%s' and Email='%s'"%(name,password,email))
			x=cur.fetchall()

			cur.close()
			db_connection.commit()
			db_connection.close()
			if len(x)>0:
				session['name']="Welcome "+str(x[0][1])
				return render_template('index.html',his_name=session['name'],session=session)
			else:
				return render_template('signup.html')


@app.route("/write_feedback",methods=["GET","POST"])

def feedback():
	return render_template('feedback.html',session=session)
@app.route("/thor",methods=["GET","POST"])

def thor():
	if request.method=="POST":
		db_connection= sql.connect(host="localhost",user="root",password="",database="amazonreview") 
		cur=db_connection.cursor()
		uname= request.form.get('short_desc')
		category=request.form.get('cat')
		review=request.form.get('review')
		cur=db_connection.cursor()
		cur.execute("INSERT INTO customer_reviews1(name,category,feedback) VALUES(%s,%s,%s)",[uname,category,review])
		cur.close()
		db_connection.commit()
		db_connection.close()
	return render_template('feedback.html')


@app.route('/feedback_senti',methods=["POST","GET"])
def get_polarity_fashion():
		db_connection= sql.connect(host="localhost",user="root",password="",database="amazonreview") 
		cur=db_connection.cursor()
		cur.execute("SELECT feedback FROM customer_reviews1")
		cb=cur.fetchall()
		li_pos,li_neg,li_neu=0,0,0	
		for t in cb:
			for i in t:
				obj=TextBlob(i).sentiment.polarity
				if obj<=0.4:
					li_neg+=1
				elif obj>0.4 and obj<0.6:
					li_neu+=1
				else:
					li_pos+=1
		db_connection.commit()
		db_connection.close()
		return render_template('feedback_senti.html',li_pos=li_pos,li_neg=li_neg,li_neu=li_neu)






#cur.close()
#db_connection.close()
app.run(debug=True)





