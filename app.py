import requests
from flask import Flask, render_template, request, flash, redirect
from urllib.parse import urlparse

app = Flask(__name__, template_folder='template', static_folder='static')

def paywall(url):
    try:
        headers = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "https://" + url
        response = requests.get(url, headers=headers)
        return response.text if response.status_code == 200 else None
    except requests.exceptions.MissingSchema as e:
        flash(str(e))

@app.route("/", methods=["GET", "POST"])
def bypass():
    if request.method == "POST":
        url = request.form.get('url')
        if not url:
            flash("Please enter a valid URL.")
        else:
            content = paywall(url)
            if content:
                return render_template("index.html", content=content)
            else:
                flash("Failed to bypass the paywall. Please try again later.")
    return render_template("index.html")

@app.route("/link", methods=["POST"])
def show_article():
    return paywall(request.form["link"])

if __name__ == '__main__':
    app.run(host='localhost', port=5000)

