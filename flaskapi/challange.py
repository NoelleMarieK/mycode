 #!/usr/bin/python3
from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("postmaker.html")

@app.route("/answer", methods = ["POST", "GET"])
def answer():
    if request.method == "POST":
        if request.form.get("nm"): # if nm was assigned via the POST
            answer = request.form.get("nm") # grab the value of nm from the POST
        else: # if a user sent a post without nm then assign value defaultuser
            return redirect(url_for("/")
    # GET would likely come from a user interacting with a browser
    if request.method == "GET":
        if request.args.get("nm"): # if nm was assigned as a parameter=value
            user = request.args.get("nm") # pull nm from localhost:5060/login?nm=larry
        else: # if nm was not passed...
            user = "defaultuser" # ...then user is just defaultuser
    return redirect(url_for("success", name = user)) # pass back to /success with val for name

@app.route("/correct")
def hello_user(name):
    ## if you go to hello_user with a value of admin
    if name =="admin":
        # return a 302 response to redirect to /admin
        return redirect(url_for("hello_admin"))
    else:
        # return a 302 response to redirect to /guest/<guesty>
        return redirect(url_for("hello_guest",guesty = name))

if __name__ == "__main__":
   app.run(host="0.0.0.0", port=2224) # runs the application
