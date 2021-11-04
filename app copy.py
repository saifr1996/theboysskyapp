from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main_page():
    
    return "goodbye from Flask"


@app.route("/test/")
def static_page():
    return """
            <html>
                <head>
                    <title>Sample - Flask routes </title>
                </head>
                <body>
                    <h1>
                        Test Page
                    </h1>
                    <p>This is a static page</p>
                </body>
            </html>
            """

