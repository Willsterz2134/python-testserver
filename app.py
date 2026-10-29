from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="da">
    <head>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Frivillig IP-test</title>
    </head>
    <body style="font-family: Arial; max-width: 600px; margin: 40px auto; padding: 15px;">
        <h1>Frivillig IP-test</h1>

        <p>
            Tryk på knappen for selv at se din offentlige IP-adresse
            og det omtrentlige område. Området kan være upræcist.
        </p>

        <a href="https://ipinfo.io/" target="_blank" rel="noopener noreferrer">
            <button style="padding: 12px 18px; cursor: pointer;">
                Se min IP og omtrentlige placering
            </button>
        </a>

        <p>Du vælger selv, om du vil dele resultatet.</p>
    </body>
    </html>
    """
