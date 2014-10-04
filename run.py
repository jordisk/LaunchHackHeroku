from flask import Flask, request, redirect
import twilio.twiml
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect("rockets.db") 

# Try adding your own number to this list!
callers = {
    "+447763501564": "Jordi",
    "+447804654075": "Thomas",
    "+447795958759": "Charles",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    #NewPart
    body_message = str(request.values.get('Body', None))
    rocket_name = body_message.split(' ') [0]
    motor = body_message.split(' ') [1]

    cursor1 = conn.execute("SELECT VAR1, VAR2 FROM TBL_ROCKETS WHERE ID = " + rocket_name)
    temp1 = []
    for row in cursor1:
        temp1.append(row)

    cursor2 = conn.execute("SELECT VAR1, VAR2 FROM TBL_MOTORS WHERE ID = " + motor)
    temp2 = []
    for row in cursor2:
        temp2.append(row)

    from_number = request.values.get('From', None)
  
    if from_number in callers:
        message = "Hi! Rocket name: " + rocket_name + " Motor: " + motor + temp1[0]+ temp2[0]
    else:
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)