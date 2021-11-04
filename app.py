from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def main_page():
    rating = list(range(0,9))
    
    form_data = request.form
    #return render_template('data.html',form_data = form_data)
  
    return render_template("first_page.html", rating = rating, form_data = form_data)


@app.route("/thankyou")
def static_page():
    return render_template("thankyou_page.html", name="Miguel")

