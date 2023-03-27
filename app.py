# Import necessary libraries
import requests
from flask import Flask, render_template, request, flash, redirect
from urllib.parse import urlparse

# Create the Flask app
app = Flask(__name__, template_folder='template', static_folder='static')

# Define a function to bypass paywalls
def paywall(url):
    """
    This function takes a URL as input and tries to bypass the paywall by sending a GET request to the URL with
    a Google Crawler user agent. If the URL does not have a scheme (http:// or https://), it adds https:// to the beginning.
    If the request is successful (status code 200), it returns the content of the response as a string.
    """
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
        }
        parsed_url = urlparse(url)
        if not parsed_url.scheme:
            url = "https://" + url
        response = requests.get(url, headers=headers)
        return response.text
    except requests.exceptions.MissingSchema as e:
        # Handle missing schema error
        flash(str(e))
        return None

# Define a route for the main page
@app.route("/", methods=["GET", "POST"])
def bypass():
    """
    This function handles requests to the main page. If the request method is GET, it returns the "index.html" template.
    If the request method is POST, it tries to bypass the paywall for the URL submitted in the form. If the URL is invalid
    (i.e. not provided), it flashes a message asking the user to enter a valid URL. If the paywall bypass is successful,
    it returns the "index.html" template with the content of the response.
    """
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        url = request.form.get('url')
        if not url:
            flash("Please enter a valid URL.")
            return redirect(request.url)

        response = requests.post(url)
        if response.status_code == 200:
            content = response.content
            return render_template("index.html", content=content)
        else:
            flash("Failed to bypass the paywall. Please try again later.")
            return redirect(request.url)

# Define a route for the bypassed link
@app.route("/link", methods=["POST"])
def show_article():
    link = request.form["link"]
    return paywall(link)


# Start the app
if __name__ == '__main__':
    host = 'localhost'  # Change this to your preferred host
    port = 5000  # Change this to your preferred port
    app.run(host=host, port=port)
   
