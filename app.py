from flask import Flask, request, render_template, redirect, url_for
from form import MyloveForm
from database import db
import pymongo

app = Flask(__name__)
app.config['SECRET_KEY'] = 'FOR MY DEAREST GIRL'


@app.route('/love', methods=['POST', 'GET'])
def love():
    form = MyloveForm()
    if form.is_submitted():
        myname = form.myname.data
        lovername = form.lovername.data
        comment = form.comment.data
        print("myname:{}, lovename:{},comment:{}".format(myname, lovername, comment))
        id1 = db.lovers.insert_one({'name': myname}).inserted_id
        id2 = db.beloved.insert_one({'name': lovername}).inserted_id
        db.loverelation.insert_one({'host': myname, 'beloved': lovername, 'comment': comment, 'id1': str(id1), 'id2': str(id2)})
        if db.loverelation.find({'beloved': myname}):
            for data in db.loverelation.find({'beloved': myname}):
                print("有情人终成眷属:{}".format(data['comment']))
                return render_template('inlove.html')
    return redirect(url_for('home'))


@app.route('/home', methods=['POST', 'GET'])
def home():
    return render_template('index.html')


def judge(name):
    cur = db.beloved.find({'name': name})
    if cur:
        return True
    else:
        return False


if __name__ == '__main__':
    app.run('0.0.0.0')
