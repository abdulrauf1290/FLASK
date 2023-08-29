## Flask app Routing


from flask import Flask,render_template,request,redirect,url_for



## create a simple flak application
app=Flask(__name__)

@app.route("/")
def home():
    return "<h2> Hello, World!</h2>"


@app.route("/welcome")
def welcome():
    return "Welcome to Flask app"

@app.route("/index")
def index():
    return "<h2>welcome to index page</h2>"

# Variable Rule
@app.route("/success/<int:score>")
def success(score):
    return "The person has passed and the score is : "+ str(score)

@app.route("/fail/<int:score>")
def fail(score):
    return "The person has failed and the score is : "+ str(score)

@app.route('/form',methods=["GET","POST"])
def calculate():
    if request.method=="GET":
      return render_template('calculate.html')

    else:
        maths=float(request.form['maths'])
        science=float(request.form['science'])
        history=float(request.form['history'])

        average_marks=(maths+science+history)/3

        result=""
        if average_marks>=50:
            result="success"

        else:
            result="fail"

        return render_template('result.html',score=average_marks)



        


if __name__=='__main__':
    app.run(debug=True)




