from flask import flask
app = flask(__name__)
@app.route("/")
def hello_world():
  message "Hello WORLD hiiii!"
  return render_template(index.html, message=message)
  
  
