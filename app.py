from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="da">
    <head>
        <meta charset="utf-8">
        <title>Test Din IQ på 10 spørgsmål</title>
    </head>
    <body style="font-family: Arial; margin: 40px;">
        <h1>Test Din IQ på 10 spørgsmål</h1>
        <p>Lavet af Gyldendal.dk og samarbejde med det danske bibliotek.</p>
        <form action="/share" method="post">
            <button type="submit">
                Start
            </button>
        </form>
    </body>
    </html>
    """


@app.route("/share", methods=["POST"])
def share():
    forwarded = request.headers.get("X-Forwarded-For", "")

    print("DEBUG XFF:", repr(forwarded), flush=True)
    app.logger.info(
        "TEST - X-Forwarded-For: %s",
        forwarded or "(tom)"
    )

    print("TEST: share-funktionen blev kørt", flush=True)

    return """
    <!doctype html>
    <html lang="da">
    <head>
        <meta charset="utf-8">
        <title>Tak</title>
    </head>
    <body style="font-family: Arial; margin: 40px;">
        <h1>Tak! for din IP-adresse</h1>
        <p>Din IP-adresse er blevet behandlet af serveren.</p>
        <a href="/">Tilbage</a>
    </body>
    </html>
    """

