from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify
import json
import os

app = Flask(__name__)

@app.route('/login')
def start():
	return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        starttime = request.form['username']
        print "the start time is"
        print starttime
        print "the end time is"
        endtime = request.form['password']
        print endtime
	os.system("python statistictest.py %s %s" % (starttime, endtime))
        return render_template('login.html')
    else:
        return jsonify({'status': '-1', 'errmsg': 'err code!'})
    return render_template('login.html')


if __name__=='__main__':
     app.run('0.0.0.0')
