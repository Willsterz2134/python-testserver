from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="da">
    <head>
        <meta charset="utf-8">
        <title>Min testside</title>
    </head>
    <body>
        <h1>Min testside virker!</h1>
        <p>Dette er en frivillig testside.</p>
        <p>Besøgsoplysninger kan blive behandlet af serveren.
        Fortsæt kun, hvis du accepterer det.</p>
    </body>
    </html>
    """
