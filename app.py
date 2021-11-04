from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def main_page():
    rating = list(range(0,9))

    form_data = request.form

    if request.method == 'POST':
        name = request.form['customer_name']
        engineer = request.form['subject']
        return redirect(url_for('thankyou', name=name))

  
    return render_template("first_page.html", rating = rating, form_data = form_data)


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou_page.html", name = request.args['name'] )

