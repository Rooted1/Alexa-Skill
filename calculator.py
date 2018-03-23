from flask import Flask
from flask_ask import Ask, statement, question, session, delegate

app = Flask (__name__)
ask = Ask(app, '/')


def get_dialog_state():
    return session['dialogState']

@ask.launch
def launched ():
    return question('Welcome to calculation! What calculation would you like to perform?')\
    .reprompt('Sorry I missed that! What kind of calculation would you like to do?')

@ask.intent('Addition', convert={'first': int, 'second': int})
def addition(first, second):
    dialog_state = get_dialog_state()
    if dialog_state != "COMPLETED":
        return delegate()

    sum = first + second
    return statement('The sum of {} and {} is {}'.format(first, second, sum))

@ask.intent('Subtraction', convert={'first': int, 'second': int})
def subtraction(first, second):
    dialog_state = get_dialog_state()
    if dialog_state != "COMPLETED":
        return delegate()

    difference = first + second
    return statement('The difference of {} and {} is {}'.format(first, second, difference))
    
if __name__ == '__main__':
    app.run(debug=True)