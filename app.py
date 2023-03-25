from flask import Flask,render_template,jsonify


app = Flask(__name__)
JOBS =[
  {
    "ID":1,
    "TITLE":"DATA ANALYST",
    "LOCATION":"BENGALURU,INDIA",
    "SALARY":"10 LPA"
    
  },
  {
    "ID":2,
    "TITLE":"DATA SCIENTIST",
    "LOCATION":"DELHI,INDIA",
    "SALARY":"15 LPA"
  },

  {
    
    "ID":3,
    "TITLE":"FRONT END ENGINEER",
    "LOCATION":"REMOTE",
    "SALARY":"12 LPA"
  },
  {
    
    "ID":4,
    "TITLE":"BACK END ENGINEER",
    "LOCATION":"SAN FRANSICO ,USA",
    "SALARY":"$120,000"
  }
  
]

@app.route("/")
def helloworld():
  return render_template("home.html",jobs =JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host = "0.0.0.0",debug = True)
