from flask import Flask

app = Flask(__name__)

constant = [1, 2, 3]


@app.route("/")
def show_items():
    return f"<h3>Our Items are: {constant}!!!<h3>"


@app.route("/delete_item")
def delete_item():
    ...


@app.route("/add_item")
def add_item():
    ...


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)


"""
http:// 137.56.0.1 :5000 / ?length=20&name=Dima&age=30
1       2             3  4  5

1. protocol
   http:// https:// ftp:// (filezilla) smtp:// amqp://

2. Destination. Domain, IPv4, IPv6
IPv4
0-255.0-255.0-255.0-255
0.0.0.0 - yes
254.0.0.1 - yes
254.0.0.0.1 - no
254.0.1 - no
localhost - 127.0.0.1

3. Port - 0 - 65_535
0 - root
80 - http
443 - https

4 Path

5 Query string

Stateless
Stateful

CRUD
C - Create
R - Read
U - Update
D - Delete
"""
