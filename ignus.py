# [START imports]
from flask import Flask, render_template, request , redirect ,flash ,url_for
# [END imports]
from functools import wraps
from flask_mail import Mail , Message
import os
import sqlite3
mail = Mail()

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ignus2k19toce@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ignus19toce'

app.secret_key = "!@#$%^&*()a-=afs;'';312$%^&*k-[;.sda,./][p;/'=-0989#$%^&0976678v$%^&*(fdsd21234266OJ^&UOKN4odsbd#$%^&*(sadg7(*&^%32b342gd']"

mail.init_app(app)

def sqlconnection():
    conn = sqlite3.connect("ignus.db")
    return conn

html = ['gaming','staroi','lipread','pubg','photography','terror','kannada',
 'pictionary','shortfilm','reta','arcania', 'clickndrun',
 'bestoutof','poster','bbs','oxsherlock','madlibs','hotwheels','sustaineri','maya','devil', 'buzzwire']

name= ['GAMING','STAR OF IGNUS','LIP READ YOUR PARTNER','PUBG', 'PHOTOGRAPHY','TERROR HUNT',
 'KANNADA QUIZ','PICTIONARY','SHORTFILM','RETALITION - THE SURGICAL STRIKE','ARCANIA',
 'CLICK AND RUN','BEST OUT OF E-WASTE','POSTER PRESENTATION','BEG BORROW STEAL', 'OXFORD SHERLOCK',
 'MAD LIB THEATER', 'HOT WHEELS', 'SUSTAINERI', 'MAYA', 'DEVIL SEAGUE', 'BUZZ WIRE'
	]

photo = ['gaming.jpg',
		'sti.jpg',
		'lryp.jpg',
		'pubg.jpg',
		'pho.jpg',
		'teh.jpg',
		'kaq.jpg',
		'pict.jpg',
		'shfl.jpg',
		'retaweb.jpg',
		'arcaniaweb.jpg',
		'clickandrunweb.jpg',
		'boew.jpg',
		'popr.jpg',
		'bbs.jpg',
		'oxsh.jpg',
		'mlt.jpg',
		'hotw.jpg',
		'sus.jpg',
		'maya.jpg',
		'devs.jpg',
		'bzw.jpg',
	]

zippedName = dict(zip(html ,name))
zippedPicture = dict(zip(html , photo))
@app.route("/test")
def test():
    return "hello"

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/main" , methods=["GET","POST"])
def main():
    if request.method == "GET":
        return render_template("main.html", zipped=zip([x for x in range(len(html))] , html , photo , name))
    elif request.method== "POST":
        contact_name = request.form["name"]
        contact_email = request.form["email"]
        contact_message = request.form["message"]
        msg = Message("Message From the Website",
                  sender='ignus2k19toce@gmail.com',
                  recipients=['ignus2k19toce@gmail.com'])
        msg.body ="""
        From {0} : {1} 
             {2}""".format(contact_name,contact_email,contact_message)
        mail.send(msg)
        flash("Thanks for contacting us")
        return redirect(request.url)

@app.route("/events/<string:event>")
def events(event):
    return render_template(event+".html" , register=event)

@app.route("/register/<string:event>"  , methods=["GET","POST"])
def register(event):
    if request.method =="GET":
        return render_template("register.html" , tagline=zippedName[event] ,backgroundPicture = zippedPicture[event])
    elif request.method =="POST":
        user_name = request.form["name"]
        user_email = request.form["email"]
        user_college = request.form["college"]
        user_phone = request.form["phone"]
        conn = sqlconnection()
        conn.execute('''INSERT INTO REGISTER(USER_NAME,EMAIL,COLLEGE,MOBILE,EVENT) VALUES (?,?,?,?,?)''',(user_name , user_email,user_college,user_phone, zippedName[event] ))
        conn.commit()
        conn.close()
        msg = Message("IGNUS 2K19",
                  sender='ignus2k19toce@gmail.com',
                  recipients=[user_email])
        msg.body ="""
        From IGNUS 2k19 Team :
            Thank you for registering with Ignus 2k19.
            You have registered for {0}.
            You will be Notified with future updates.""".format(zippedName[event] )
        mail.send(msg)
        return redirect(url_for('events',event=event))
if __name__ =="__main__":
    app.run(debug=True)
