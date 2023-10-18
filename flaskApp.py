from flask import Flask

# app is nothing but an object of the Flask class
# name variable refers to how a particular script was invoked

app = Flask(__name__)

# We need to tell Flask what to return when a certain URL is requested. 
# For that we need to register a route which is simply a part of the URL after the 
# domain name.


@app.route("/")
def hello_world():
  return "Hii my Pikachu!! My phone is updating so I probably can't use WhatsApp rn! Refresh the page to see if the text has been updated"


if __name__ == '__main__':
  # To run the script we have to specify the port number. 
  # We give 0.0.0.0 to make it run locally
  app.run(host='0.0.0.0', debug=True)