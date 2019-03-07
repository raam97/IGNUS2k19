from flask import Flask, render_template, url_for, redirect, request, flash, session, g, abort, jsonify
from functools import wraps


app = Flask(__name__)

app.secret_key = "!@#$%^&*()a-=afs;'';312$%^&*k-[;.sda,./][p;/'=-0989#$%^&0976678v$%^&*(fdsd21234266OJ^&UOKN4odsbd#$%^&*(sadg7(*&^%32b342gd']"

@app.route("/test")
def test():
    return "hello"

if __name__ =="__main__":
    app.run(host="0.0.0.0")
