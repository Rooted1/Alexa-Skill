from flask import Flask
from flask_ask import Ask, statement, question

app = Flask (__name__)
ask = Ask(app, '/')

@ask.launch
def launched():
    return question('Welcome to jokes! What kind of joke do you want to hear, '\
    'a one liner or a knock knock joke?')\
    .reprompt('Sorry I missed that. Would you like to hear a one liner or a knock knock joke?')

@ask.intent('OneLiner')
def one_liner():
    return statement('Warning, keyboard not found. Press Enter to continue.')

@ask.intent('KnockKnock')
def knock_knock():
    return question('Knock Knock')

@ask.intent('WhosThere')
def who():
    return question('Bing')

@ask.intent('Bing')
def bing():
    return statement('No, I usually prefer Google.')

if __name__ == '__main__':
    app.run(debug=True)