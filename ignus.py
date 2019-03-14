# [START imports]
from flask import Flask, render_template, request , redirect ,flash ,url_for
# [END imports]
from functools import wraps
from flask_mail import Mail , Message
import os
import sqlalchemy
import logging

db_user = "root"
db_pass = "ignusdatabase"
db_name = "ignus"
cloud_sql_connection_name = "ignus2k19:asia-east1:ignusdatabase"

mail = Mail()

app = Flask(__name__)


app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'ignus2k19toce@gmail.com'
app.config['MAIL_PASSWORD'] = 'Ignus19toce'

app.secret_key = "!@#$%^&*()a-=afs;'';312$%^&*k-[;.sda,./][p;/'=-0989#$%^&0976678v$%^&*(fdsd21234266OJ^&UOKN4odsbd#$%^&*(sadg7(*&^%32b342gd']"

mail.init_app(app)
# [START cloud_sql_mysql_sqlalchemy_create]
# The SQLAlchemy engine will help manage interactions, including automatically
# managing a pool of connections to your database
db = sqlalchemy.create_engine(
    # Equivalent URL:
    # mysql+pymysql://<db_user>:<db_pass>@/<db_name>?unix_socket=/cloudsql/<cloud_sql_instance_name>
    sqlalchemy.engine.url.URL(
        drivername='mysql+pymysql',
        username=db_user,
        password=db_pass,
        database=db_name,
        query={
            'unix_socket': '/cloudsql/{}'.format(cloud_sql_connection_name)
        }
    ),
    # ... Specify additional properties here.
    # [START_EXCLUDE]

    # [START cloud_sql_mysql_sqlalchemy_limit]
    # Pool size is the maximum number of permanent connections to keep.
    pool_size=5,
    # Temporarily exceeds the set pool_size if no connections are available.
    max_overflow=2,
    # The total number of concurrent connections for your application will be
    # a total of pool_size and max_overflow.
    # [END cloud_sql_mysql_sqlalchemy_limit]

    # [START cloud_sql_mysql_sqlalchemy_backoff]
    # SQLAlchemy automatically uses delays between failed connection attempts,
    # but provides no arguments for configuration.
    # [END cloud_sql_mysql_sqlalchemy_backoff]

    # [START cloud_sql_mysql_sqlalchemy_timeout]
    # 'pool_timeout' is the maximum number of seconds to wait when retrieving a
    # new connection from the pool. After the specified amount of time, an
    # exception will be thrown.
    pool_timeout=30,  # 30 seconds
    # [END cloud_sql_mysql_sqlalchemy_timeout]

    # [START cloud_sql_mysql_sqlalchemy_lifetime]
    # 'pool_recycle' is the maximum number of seconds a connection can persist.
    # Connections that live longer than the specified amount of time will be
    # reestablished
    pool_recycle=1800,  # 30 minutes
    # [END cloud_sql_mysql_sqlalchemy_lifetime]

    # [END_EXCLUDE]
)
# [END cloud_sql_mysql_sqlalchemy_create

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

@app.before_first_request
def create_tables():
    # Create tables (if they don't already exist)
    with db.connect() as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS REGISTER(USER_NAME TEXT(50) NOT NULL ,
                 EMAIL VARCHAR(50)  NOT NULL,
                 COLLEGE VARCHAR(50),
                MOBILE VARCHAR(50),
                 EVENT VARCHAR(50))''' )


@app.route("/test")
def test():
    return "hello"

@app.errorhandler(404)
def handleerror(e):
    return render_template("error.html")

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
        stmt = sqlalchemy.text(
        "INSERT INTO REGISTER (USER_NAME,EMAIL,COLLEGE,MOBILE,EVENT)"
            " VALUES (:USER_NAME,:EMAIL,:COLLEGE,:MOBILE,:EVENT)")
        try:
        # Using a with statement ensures that the connection is always released
        # back into the pool at the end of statement (even if an error occurs)
            with db.connect() as conn:
                conn.execute(stmt, USER_NAME=user_name ,EMAIL=user_email,COLLEGE=user_college,MOBILE=user_phone,EVENT=zippedName[event])
        except Exception as e:
            # If something goes wrong, handle the error in this section. This might
            # involve retrying or adjusting parameters depending on the situation.
            # [START_EXCLUDE]
            logger.exception(e)  
            return Response(status=500, response="Unable To register. Please try after some time" )
        # [END_EXCLUDE]
        # [END cloud_sql_mysql_sqlalchemy_connection]
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

@app.route("/code")
def code():
    return render_template("code1.html")

@app.route('/registrations', methods=['GET'])
def registrations():
    with db.connect() as conn:
        # Execute the query and fetch all results
        recent_votes = conn.execute("SELECT * FROM REGISTER").fetchall()
        # Convert the results into a list of dicts representing votes
        return render_template('output.html',data=recent_votes)

if __name__ =="__main__":
    app.run(debug=True)
