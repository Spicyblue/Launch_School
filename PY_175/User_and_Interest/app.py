# import flask web development framework and yaml
from flask import Flask, redirect, url_for, render_template # type: ignore
import yaml # type: ignore

app = Flask(__name__)

# Load users data once at the start of the application
with open("users.yaml", "r") as file:
    users = yaml.safe_load(file)

def total_interests(users):
    return sum(len(user['interests']) for user in users.values())

@app.route("/")
def home():
    return redirect(url_for('users'))

@app.route("/users")
def users_list():
    return render_template('users.html', users=users, total_users=len(users), total_interests=total_interests(users))

@app.route("/user/<user_name>")
def user_profile(user_name):
    user = users.get(user_name)
    if not user:
        return redirect(url_for('users_list'))
    return render_template('user.html', user_name=user_name, user=user, users=users)

if __name__ == "__main__":
    app.run(debug=True, port=5003)