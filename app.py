from flask import Flask, render_template, json
import os
import database.db_connector as db

# Configuration

app = Flask(__name__)

db_connection = db.connect_to_database()

# Routes 

@app.route('/')
def root():
    people_from_app_py =[
{
    "name": "Thomas",
    "age": 33,
    "location": "New Mexico",
    "favorite_color": "Blue"
},
{
    "name": "Gregory",
    "age": 41,
    "location": "Texas",
    "favorite_color": "Red"
},
{
    "name": "Vincent",
    "age": 27,
    "location": "Ohio",
    "favorite_color": "Green"
},
{
    "name": "Alexander",
    "age": 29,
    "location": "Florida",
    "favorite_color": "Orange"
}
]
    return render_template("main.j2", people=people_from_app_py)

@app.route('/bsg-people')
def bsg_people():
    query = "Select * from bsg_people;"
    cursor = db.execute_query(db_connection=db_connection, query=query)
    results = cursor.fetchall()
    return render_template("bsg.j2", bsg_people=results)

# Listener

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000)) 
    #                                 ^^^^
    #              You can replace this number with any valid port
    
    app.run(port=port, debug=True) 