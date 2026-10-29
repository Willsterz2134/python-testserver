from flask import Flask, request

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

    <body style="
        font-family: Arial, sans-serif;
        margin: 40px;
        background-image: url('/static/background.jpg');
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    ">
        <h1>Frivillig IP-test</h1>

        <p>
            Tryk kun på knappen, hvis du accepterer,
            at hjemmesidens ejer kan se din IP-adresse
            i serverens logs.
        </p>

        <form action="/share" method="post">
            <button type="submit" style="
                padding: 12px 20px;
                font-size: 16px;
                cursor: pointer;
            ">
                Jeg accepterer og deler min IP
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
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Tak</title>
    </head>

    <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Tak!</h1>

        <p>
            Din IP-adresse er blevet behandlet af serveren.
        </p>

        <a href="/">Tilbage til forsiden</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run()
