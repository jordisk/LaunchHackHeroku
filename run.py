from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
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

    from_number = request.values.get('From', None)
  
    if from_number in callers:
        message = "Rocket name: " + rocket_name + " Motor: " + motor
    else:
        message = "Monkey, thanks for the message!"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)