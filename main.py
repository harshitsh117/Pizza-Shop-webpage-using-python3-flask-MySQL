# Importing flask and mysql modules
from flask import Flask,render_template,request
import mysql.connector

# Creating connection with database
con = mysql.connector.connect(host="localhost",user="harshit",password="123",database='Responsivewebsite')
cur=con.cursor()

app=Flask(__name__)

# Making home page route
@app.route("/")
def home():
    return render_template('Responsive website.html')

# For storing data to database
@app.route("/",methods=["Post"])
def Sending_data():
    # Getting data from inout fields and storing them in these variables
    name=request.form.get('name')
    email=request.form.get('email')
    phone=request.form.get('phone')
    message=request.form.get('message')

    query = "insert into CustomerDetails values('%s','%s','%s','%s')"%(name,email,phone,message)
    try:
        cur.execute(query)
    except Exception as e:
        print(e)
    con.commit()

    return render_template('Responsive website.html')

app.run(debug=True)

cur.close()
con.close
