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

@app.route("/shopping", methods=["GET"])
def shopping_page():
    return render_template('shopping.html')

@app.route("/learning/page=<int:id>", defaults={'id': 1}, methods=["GET"])
def learning_page(id):
    print(id)

    db_connection = connect_to_database()
    # query = "select word as keyword, chinese_char as rightAns from Words where word_id=%s"
    # data = execute_query(db_connection, query, (id,)).fetchone()
    # print(data)
    if 1 <= id <=3:
        choice_query = "select chinese_char as choices from Words where word_id>=1 and word_id <=3;"
        choices = execute_query(db_connection, choice_query).fetchall()
        print(choices)
    
    if 4 <= id <= 6:
        choice_query = "select chinese_char as choices from Words where word_id>=4 and word_id <=6;"
        choices = execute_query(db_connection, choice_query).fetchall()
        print(choices)

    return render_template('learning.html', word_id=id, choices=choices)


@app.route("/api/learning/<int:id>", methods=["POST", "GET"])
def find_word(id):
    if request.method == "GET":
        db_connection = connect_to_database()
        query = "select word from Words where word_id=%s"
        param = (id,)
        word = execute_query(db_connection, query, param).fetchone()
        print(word)
        return word[0] 
    
    if request.method == "POST":
        print('submit button click')
        chosen_ans = request.form['chosen_ans']
        print(chosen_ans)
        check_answer(chosen_ans, id)


def check_answer(answer, id):
    db_connection = connect_to_database()
    query = 'Select chinese_char from Words where word_id=%s'
    data = execute_query(db_connection, query, (id,)).fetchone()
    print(data)
    if data[0] == answer:
        flash('Congrats, you are right.')
        return
    else:
        flash('Wrong! Try it again.')
        return


    


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, host='localhost', port=5000)
