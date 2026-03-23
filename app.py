from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []
error_message = ""

@app.route("/")
def index():
    return render_template("index.html", tasks=tasks, error_message=error_message)

@app.route("/add", methods=["POST"])
def add():
    global error_message

    task = request.form.get("task")

    if task and task.strip():
        task = task.strip()

        if any(t["name"] == task for t in tasks):
            error_message = "Task already exists."
        else:
            tasks.append({"name": task, "done": False})
            error_message = ""

    return redirect("/")

@app.route("/done/<int:id>")
def done(id):
    tasks[id]["done"] = True
    return redirect("/")

@app.route("/delete/<int:id>")
def delete(id):
    tasks.pop(id)
    return redirect("/")

app.run(debug=True)
