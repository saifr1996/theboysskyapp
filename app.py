from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)

@app.route("/", methods = ['POST', 'GET'])
def main_page():
    form_data = request.form
    if request.args.get('bad_input') == "0":
        if request.method == 'POST':
            if request.form['customer_name'] != "":
                # correct inputs
                name = request.form['customer_name']
                return redirect(url_for('thankyou', name=name))
            else:
                #if bad input eg bad name
                return redirect(url_for('main_page', bad_input=0))
        # this will never be reached 
        return render_template("first_page_alt.html")

    else:
        if request.method == 'POST':
            name = request.form['customer_name']
            #this will return false if the full name isnt a valid one
            if bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)):
                return redirect(url_for('thankyou', name=name))
            else:
                return redirect(url_for('main_page', bad_input=0))
        return render_template("first_page.html", form_data = form_data)


@app.route("/thankyou")
def thankyou():
    return render_template("thankyou_page.html", name = request.args['name'] )
