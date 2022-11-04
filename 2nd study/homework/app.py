from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://pablaw:9dlrhd!357@cluster0.spvewgv.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta


@app.route('/')
def home():
    return render_template('index.html')

@app.route("/homework", methods=["POST"])
def homework_post():
    name = request.form['name_give']
    comment = request.form['comment_give']

    doc = {
        'name': name,
        'comment': comment
    }
    db.homeworkpage.insert_one(doc)
    return jsonify({'msg':'작성 완료!'})

@app.route("/homework", methods=["GET"])
def homework_get():
    all_msg = list(db.homeworkpage.find({}, {'_id': False}))
    return jsonify({'result':all_msg})

if __name__ == '__main__':app.run('0.0.0.0', port=2000, debug=True)