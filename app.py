from flask import Flask,render_template,request

app = Flask(__name__)
@app.route('/', methods=['GET'])
def home():
    return render_template("index.html")


@app.route("/callme",methods=['GET',"POST"])
def callme_details():
    name=request.form("name")
    email=request.form("email")
    ph_no=request.form("phone_number")
    course=request.form("course")
    return f""" mr {name} your details was updated check once again
            name = {name}
            email = {email}
            phone.no ={ph_no}
            course = {course} """

app.run(debug=True)