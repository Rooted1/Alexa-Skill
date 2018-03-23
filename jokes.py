from flask import Flask
from flask_ask import Ask, statement, question

app = Flask (__name__)
ask = Ask(app, '/')

@ask.intent('OneLiner')
def one_liner():
    return statement('Warning, keyboard not found. Press Enter to continue.')

if __name__ == '__main__':
    app.run(debug=True)