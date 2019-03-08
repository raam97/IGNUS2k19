# [START imports]
from flask import Flask, render_template, request , redirect 
# [END imports]
from functools import wraps


app = Flask(__name__)

app.secret_key = "!@#$%^&*()a-=afs;'';312$%^&*k-[;.sda,./][p;/'=-0989#$%^&0976678v$%^&*(fdsd21234266OJ^&UOKN4odsbd#$%^&*(sadg7(*&^%32b342gd']"
html = ['pubg','shortfilm','poster','kannada','maya',
 'lipread','pictionary','photography','reta','gaming',
 'oxsherlock','staroi','clickndrun','sustaineri', 'buzzwire',
 'hotwheels',
 'madlibs',
 'bestoutof',
 'bbs',
 'arcania',
 'terror',
 'devil']

name= [
 'GAMING',
 'STAR OF IGNUS',
 'LIP READ YOUR PARTNER',
 'PUBG',
 'PHOTOGRAPHY',
 'TERROR HUNT',
 'KANNADA QUIZ',
 'PICTIONARY',
 'SHORTFILM',
 'RETALITION - THE SURGICAL STRIKE',
 'ARCANIA',
 'CLICK AND RUN',
 'BEST OUT OF E-WASTE',
 'POSTER PRESENTATION'
 'BEG BORROW STEAL',
 'OXFORD SHERLOCK',
 'MAD LIB THEATER',
 'HOT WHEELS',
 'SUSTAINERI',
 'MAYA',
 'DEVIL SEAGUE',
 'BUZZ FIRE',
]

photo = [
'gam.jpg',
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
'sust.jpg',
'maya.jpg',
'devs.jpg',
'bzw.jpg',
]

@app.route("/test")
def test():
    return "hello"

@app.route("/")
def index():
    return  render_template("index.html")

@app.route("/main")
def main():
    return render_template("main.html", zipped=zip([x for x in range(len(html))] , html , photo , name))

@app.route("/events/<string:event>")
def events(event):
    return render_template(event+".html")

if __name__ =="__main__":
    app.run(debug=True)
