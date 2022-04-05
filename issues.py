from flask import Flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

issues = Flask(__name__)
issues.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:mira@localhost:3306/issues'
db = SQLAlchemy(issues)

class issue(db.Model):
    id = db.Column(db.Integer, primary_key=1)
    name = db.Column(db.String(30))
    email = db.Column(db.String(40))
    reported_issue = db.Column(db.String(4000))
    def __init__(self, n, e, r):
        super(issue).__init__(name=n, email=e, reported_issue=r)

@issues.route('/submit', methods=['POST'])
def submitIssue():
    name = request.json['name']
    email = request.json['email']
    reported_issue = request.json['reported_issue']
    i = issue(name, email, reported_issue)
    return jsonify(message="Issue successfully reported")