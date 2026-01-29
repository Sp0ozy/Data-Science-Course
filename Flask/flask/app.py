from flask import Flask, render_template, request, redirect


app=Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to this Flask course"

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        name=request.form["name"]
        return f"Hello, {name}!"
    return render_template("form.html")
@app.route("/success/<int:score>")
def score(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res="FAIL"
    exp={'score': score, "res": res}
    return render_template("result1.html", results=exp)
if __name__=="__main__":
    app.run()
    