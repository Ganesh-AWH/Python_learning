from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# The Base URL for the Open Brewery DB API
API_URL = "https://api.openbrewerydb.org/v1/breweries"

@app.route("/", methods=["GET", "POST"])
def index():
    breweries = []
    city_query = ""
    
    if request.method == "POST":
        city_query = request.form.get("city")
        if city_query:
            # Making the HTTP GET request to the API with a filter
            response = requests.get(API_URL, params={"by_city": city_query, "per_page": 10})
            response.raise_for_status() # Check for errors
            breweries = response.json()
            
    return render_template("index.html", breweries=breweries, city=city_query)

if __name__ == "__main__":
    app.run(debug=True)