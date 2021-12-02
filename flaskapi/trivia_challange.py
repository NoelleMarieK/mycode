#!/usr/bin/python3

from flask import Flask
from flask import redirect
from flask import request
from flask import render_template, jsonify

app = Flask(__name__)

html= """<style>
body {
  background-color: black;
  text-align: center;
  color: white;
  font-family: Arial, Helvetica, sans-serif;
}
</style>
</head>
<body>

<h1>TRIVIA TIME</h1>
<p>What is the meaning of life, the universe, and everything?</p>
<img src="https://stevetobak.com/wp-content/uploads/2021/02/dont-panic.png" alt="Avatar" style="width:200px">

    <form action = "/login" method = "POST">
        <p><input type = "text" name = "nm"></p>
        <p><input type = "submit" value = "submit"></p>
    </form>

</body>
</html>"""

jsondata=[]

@app.route("/post", methods=['POST'])
def post():
    data= request.json
    if data:
        answer= data['answ']
        jsondata.append({'answer':answer})
        if answer == "42":
                return redirect("/ans")
        else:
                return redirect("/correct")

@app.route("/ans")
def good():
    return jsonify(jsondata)


@app.route("/correct")
def success():
    return f"That is correct!"

@app.route("/")
def start():
    return html

@app.route("/login", methods = ["POST"])
def login():
        if request.form.get("nm"):
            answer = request.form.get("nm")
            if answer == "42":
                return redirect("/correct")
            else:
                return redirect("/")
        else:
            return redirect("/")

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application

