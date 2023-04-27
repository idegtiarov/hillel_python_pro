from flask import Flask, request
from random import randint


app = Flask(__name__)


class User():
    name = ''  # validation ascii
    language = ''
    course = ''
    grade = ''

    def __init__(self, name='', language=''):
        ...

    def chose_course(self, course):
        ...

    def get_grade(self, grade):
        ...


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
    app.run(host='0.0.0.0', port=8000, debug=True)


"""
HTTP Status Codes

Informational responses (100 – 199)
Successful responses (200 – 299)

200 OK
201 Created
202 Accepted

Redirection messages (300 – 399)

301 Moved Permanently

Client error responses (400 – 499)

400 Bad Request
401 Unauthorized
403 Forbidden
404 Not Found
405 Method Not Allowed
408 Request Timeout
429 Too Many Requests

Server error responses (500 – 599)

500 Internal Server Error
501 Not Implemented
"""
