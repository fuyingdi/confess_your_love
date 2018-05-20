from flask import Flask, request, render_template, redirect
from form import MyloveForm
from database import db
import pymongo

app = Flask(__name__)


@app.route('/love')
def love():
    form = MyloveForm()
    if form.validate_on_submit():
        myname = form.myname.data
        lovername = form.lovername.data
        db.lovers.insert_one({'name': myname})
        db.beloved.insert_one({'name': lovername})
    return render_template('submit.html',form=form)


def judge(name):
    cur=db.beloved.find({'name':name})
    if cur:
        return True
    else:
        return False


@app.route('/home')
def index():
    pass




if __name__ == '__main__':
    app.run()
