from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# from flask import Flask, render_template, request, redirect, url_for
# import os

# app = Flask(__name__, template_folder='templates', static_folder='static')
# Global list to store to-do items
todo_list = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Get the task from the form
        task = request.form.get("task")
        if task:
            todo_list.append(task)
        return redirect(url_for("index"))
    
    return render_template("index.html", todo_list=todo_list)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001,debug=True)
