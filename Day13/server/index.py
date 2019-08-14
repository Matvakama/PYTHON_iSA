from flask import render_template # aby móc renderować szablony
from Day13.server.app import app_connexion
from Day13.server.models import Album, AlbumSchema
# Get the application instance
connex_app = app_connexion
# Read the swagger.yml file to configure the endpoints
connex_app.add_api("swagger.yml") # API dodany
# create a URL route in our application for "/"
@connex_app.route("/")
def home():
 """
 This function just responds to the browser URL
 localhost:5000/
 :return:        the rendered template "index.html"
 """
 albums = Album.query.order_by(Album.artist).all()

 # Serialize the data for the response
 # album_schema = AlbumSchema(many=True)
 # dump = album_schema.dump(albums)
 # data = dump.data

 return render_template("index.html", albums=albums)


if __name__ == "__main__":
 connex_app.run(port=8080, debug=True)

# def home():
#  """
#      This function just responds to the browser URL
#      localhost:8080/
#      :return: the rendered template
#      """
#  return "<h1>That is a REST API example.</h1>"
#
# if __name__ == "__main__":
#  connex_app.run(port=8080, debug=True)
