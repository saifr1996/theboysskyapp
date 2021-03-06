from flask import Flask, render_template, request, redirect, url_for
import re

app = Flask(__name__)
names = {'John':5, 'Juan': 4}

saved_response = {}

@app.route("/", methods = ['POST', 'GET'])
def main_page():
    form_data = request.form
    arg = request.args.get('bad_input')

    if  arg == "1" or arg == "2":
        if request.method == 'POST':
            name = request.form['customer_name']
            engineer = request.form['subject']
            rating = request.form['rating']
            #comment = request.form['comment']


            if bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)):
                if not name in saved_response:
                    #correct input
                    print("hello")
                    saved_response[name] = engineer,rating
                    print(saved_response[name])
                    return redirect(url_for('thankyou', name=name))
                else:
                    #Wrong input with repeated name
                    return redirect(url_for('main_page', bad_input=1))
            else:
                #wrong input bad name format
                return redirect(url_for('main_page', bad_input=2))
        if arg == "1":
            return render_template("first_page_used_name.html")
        elif arg == '2':
            return render_template("first_page_invalid_input.html")

    else:
        if request.method == 'POST':

            name = request.form['customer_name']
            engineer = request.form['subject']
            rating = request.form['rating']
            #comment = request.form['comment']
            #this will return false if the full name isnt a valid one
            if bool(re.fullmatch('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name)):
                if not name in saved_response:
                    saved_response[name] = engineer,rating
                    print(saved_response[name])
                    return redirect(url_for('thankyou', name=name))
                else:
                    return redirect(url_for('main_page', bad_input=1))
            else:
                return redirect(url_for('main_page', bad_input=2))
        return render_template("first_page.html", form_data = form_data)


@app.route("/thankyouu")
def thankyou():
    return render_template("thankyou_page.html", name = request.args['name'] )

if __name__ == "__main__":
    app.run(port=5000,host="0.0.0.0", debug=True)