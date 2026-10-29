from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <!doctype html>
    <html lang="da">
    <head>
        <meta charset="utf-8">
        <title>Frivillig IP-test</title>
    </head>
    <body style="font-family: Arial; margin: 40px;">
        <h1>Frivillig IP-test</h1>
        <p>Tryk kun, hvis du accepterer at dele din IP med hjemmesidens ejer.</p>
        <form action="/share" method="post">
            <button type="submit">
                Jeg accepterer og deler min IP
            </button>
        </form>
    </body>
    </html>
    """


@app.route("/share", methods=["POST"])
def share():
    forwarded = request.headers.get("X-Forwarded-For", "")
    ip = forwarded.split(",")[0].strip() if forwarded else request.remote_addr

    app.logger.info("Frivilligt delt IP: %s", ip)

    return """
    <!doctype html>
    <html lang="da">
    <head><meta charset="utf-8"><title>Tak</title></head>
    <body style="font-family: Arial; margin: 40px;">
        <h1>Tak!</h1>
        <p>Din IP er sendt til serveren.</p>
        <a href="/">Tilbage</a>
    </body>
    </html>
    """
