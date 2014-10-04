from flask import Flask, request, redirect
import twilio.twiml
 
app = Flask(__name__)
 
# Try adding your own number to this list!
callers = {
    "+447763501564": "Jordi",
    "+14158675310": "Bootsso",
    "+14158675311": "Virgil",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    """Respond and greet the caller by name."""
 
    from_number = request.values.get('From', None)

    #NewPart
    body_message = request.values.get('Body', None)
    rocket_name = body_message.split(' ') [0]
    motor = body_message.split(' ') [1]
'''
    if from_number in callers:
        message = "Hi " + callers[from_number] + "! Rocket name: " + rocket_name + " Motor: " + motor
'''
    if from_number in callers:
        message = callers[from_number] + ", thanks for the message!"
    else:
        message = "Phone not found"
 
    resp = twilio.twiml.Response()
    resp.message(message)
 
    return str(resp)
 
if __name__ == "__main__":
    app.run(debug=True)
