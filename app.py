lask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    ip = request.remote_addr or "Ukendt"

    return f"""
    <!doctype html>
    <html lang="da">
    <head>
        <meta charset="utf-8">
        <title>IP-test</title>
    </head>
    <body>
        <h1>Frivillig IP-test</h1>
        <p>Din offentlige IP-adresse, som serveren ser den, er:</p>
        <h2>{ip}</h2>
        <p>Besøg kun siden, hvis du accepterer, at IP-adressen vises.</p>
    </body>
    </html>
    """
