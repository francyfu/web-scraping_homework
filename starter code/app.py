from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import mission_to_mars

app = Flask(__name__)

# Use flask_pymongo to set up mongo connection
app.config["MONGO_URI"] = "mongodb://localhost:27017/mission_to_mars_app"
mongo = PyMongo(app)

# Or set inline
# mongo = PyMongo(app, uri="mongodb://localhost:27017/craigslist_app")


@app.route("/")
def index():
    mars = mongo.db.mars
    return render_template("index.html", mars=mars)
 

@app.route("/scrape")
def scrape():
    mars = mongo.db.mars
    data = mission_to_mars.scrape_all()
    mars.update({},data,upsert=True)
    return "done!"
    # listings = mongo.db.listings.find_one()
    # return render_template("index.html", listings = listings)


if __name__ == "__main__":
    app.run(debug=True)

