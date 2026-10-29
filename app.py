       Jeg accepterer og deler min IP
            </button>
        </form>

        <p>Du vælger selv, om du vil dele din IP.</p>
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
    <head>
        <meta charset="utf-8">
        <title>Tak</title>
    </head>
    <body style="font-family: Arial; margin: 40px;">
        <h1>Tak!</h1>
        <p>Din IP er sendt til serveren.</p>
        <a href="/">Tilbage</a>
    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=False)
