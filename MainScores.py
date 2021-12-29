from flask import Flask, render_template

import Utils

app = Flask(__name__)


@app.route("/")
def score_server():
    try:
        with open(Utils.SCORES_FILE_NAME,'r') as f:
            return f"""<html>
<head>
<title>Scores Game</title>
</head>
<body>
<h1>The score is <div id="score">{f.read()}</div></h1>
</body>
</html>"""
    except:
        return """<html>
<head>
<title>Scores Game</title>
</head>
<body>
<body>
<h1><div id="score" style="color:red">{ERROR}</div></h1>
</body>
</html>"""

if __name__ == "__main__":
    app.run(debug=True)