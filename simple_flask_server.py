import json
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    html = """
    <html>
        <body>
            <h1>Python User Group Meetup December 2018</h1>
            <ul>
                <li>
                    <a href="/rest">Sample JSON Data</a>
                </li>
                <li>
                    <a href="/error">Sample 500 Error</a>
                </li>
                <li>
                    <a href="/beautiful_soup">Sample HTML</a>
                </li>
            </ul>
        </body>
    </html>
    """
    return html

@app.route('/rest')
def test_enpoint():
    some_data = {
                  'first_name': 'Ryan'
                 ,'last_name' : 'Thielke'
                 ,'location'  : 'Python User Group Meetup'
                 ,'employer'  : 'Two Sigma'
                }
    return json.dumps(some_data)

@app.route('/error')
def raise_error():
    raise RuntimeError("Should give me a 500")

@app.route("/beautiful_soup")
def beautiful_soup():
    with open("beautiful_soup_demo.txt") as htmlfile:
        html = htmlfile.read()
    return "<pre>{html}</pre>".format(html=html)

if __name__ == "__main__":
    app.run(port=3000)

