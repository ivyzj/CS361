from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify, Response
from datetime import timedelta

from flask.helpers import make_response
from db_connector import connect_to_database, execute_query

app = Flask(__name__)
app.secret_key = "group19"
app.permanent_session_lifetime = timedelta(days=1)


@app.route("/", methods=["GET"])
def home_page():
    return render_template('home.html')

@app.route("/users", methods=["GET"])
def users_page():
    return render_template('users.html')

@app.route("/faq", methods=["GET"])
def faq_page():
    return render_template('faq.html')

@app.route("/learning/page=<int:id>", defaults={'id': 1}, methods=["GET"])
def learning_page(id):
    print(id)
    db_connection = connect_to_database()
    
    query = "select word as keyword, chinese_char as rightAns from Words where word_id=%s"
    data = execute_query(db_connection, query, (id,)).fetchone()
    print(data)
    if 1 <= id <=3:
        choice_query = "select chinese_char as choices from Words where word_id>=1 and word_id <=3;"
        choices = execute_query(db_connection, query).fetchall()
        print(choices)
    
    if 4 <= id <= 6:
        choice_query = "select chinese_char as choices from Words where word_id>=4 and word_id <=6;"
        choices = execute_query(db_connection, query).fetchall()
        print(choices)

    return render_template('learning.html', data=data, choices=choices)

@app.route("/quiz", methods=["GET"])
def quiz_page():
    return render_template('quiz.html')

@app.route("/shopping", methods=["GET"])
def shopping_page():
    return render_template('shopping.html')

@app.route("/api/learning")
def next_word():
    id = request.args.get()
    word_id = int(id) + 1
    redirect(url_for('learning_page()', id=word_id))



@app.route("/api/learning/<int:id>", methods=["POST", "GET"])
def check_answer(id):
    if request.form['choice_1']:
        chosen_ans = request.form['choice_1']
    elif request.form['choice_2']:
        chosen_ans = request.form['choice_2']
    else:
        chosen_ans = request.form['choice_3']

    db_connection = connect_to_database()
    query = 'Select chinese_char from Words where word_id=%s'
    data = execute_query(db_connection, query, (id,)).fetchone()
    if data[0] == chosen_ans:

        msg = jsonify({
            'msg': 'Congrats, you are right.'
        })
    else:
        msg = jsonify({
            'msg': 'Wrong! Try it again.'
        })
    return redirect(url_for('learning_page', id=id, msg=msg))




if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='localhost', port=5000)
