# PaywallBypasser
Bypass paywalls by pretending to be a google bot.

This is a simple Flask web application that allows you to bypass paywalls for news articles by simply entering the URL of the article. The app will retrieve the article content for you, allowing you to read the article without any restrictions.

**Dependencies:**

    Python 3.x
    Flask
    Requests

**How to run:**

 1. Clone or download the repository.
 2. Install pip and the dependencies.
 3. Run the app using: ```python3 app.py```
 4. Open your webbrowser and go to http://127.0.0.1:5000 to access the URL shortener.
 The host and port can be changed under in the python script.

**How to use:**

 1. Enter the URL of the article you want to read in the input box and click "Submit".
 2. If the URL is valid and the paywall is bypassed successfully, the article content will be displayed on the page.
 3. If the URL is invalid or the paywall cannot be bypassed, an error message will be displayed.
 
Included in the static and template folder is a basic index.html with an okayish form.
You're free to use it or change it if you like.

That's it.
