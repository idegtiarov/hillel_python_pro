import sqlite3

from flask import Flask, request
from random import randint


app = Flask(__name__)

user = None


class User():
    name = ''  # validation ascii
    language = ''
    course = ''
    grade = ''

    def __init__(self, name='', language=''):
        self.name = self.check_ascii(name)
        self.language = self.check_ascii(language)

    def check_ascii(self, param):
        # check param is str
        if param.isascii():
            return param
        return Exception('String is not ascii')

    def chose_course(self, course):
        ...

    def get_grade(self, grade):
        ...


def validate_alphabetical(form_input, error_key, error_dict=None):
    if form_input.isalpha():
        return form_input
    error_dict[error_key] = "Verbose error description"


@app.route('/login', methods=["GET", "POST"])
def login_user():
    error_dict = {}

    name = validate_alphabetical(request.form.get('name'), 'name', error_dict)

    language = request.form.get('language')

    if error_dict:
        return f"""
               {error_dict['name']}
        """

    try:
        global user
        user = User(name, language)
        return  # redirect to home
    except:
        return f"""
            Name or Language is not in ascii
        """


@app.route("/")
def show_items():

    return f"""
        <h3>Values in list are: {state_list}</h3>
        
        <form action="/add_item" method="POST">
          <div>
             <label for="new_item">Please enter item to add to the list, random int is default option?</label>
             <input name="item" id="new_item" value="random int" />
          </div>
            <button>Send my choice</button>
        </form>
        
    """


@app.route("/add_item", methods=["POST"])
def add_item():
    user_input = False
    try:
        item = int(request.form.get('item'))
        user_input = True
    except ValueError:
        item = randint(0, 100)
    state_list.append(item)
    return f"""
        <h3>Updated list: {state_list}</h3>
        </br>
        <h4>New item {'added by user: ' if user_input else 'random integer: '}{item}</h4>
        </br>
        <a href="/">Return to the HOME page</a>
        
    """


if __name__ == "__main__":
    try:
        conn = sqlite3.connect('user.db')
    finally:
        conn.close()
    app.run(host='0.0.0.0', port=8000, debug=True)
