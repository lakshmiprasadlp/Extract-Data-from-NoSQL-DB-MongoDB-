import pandas as pd
import pymongo
import urllib.parse
from lp_pymango.var import username,password
# Escape the username and password
escaped_username = urllib.parse.quote_plus(username)
escaped_password = urllib.parse.quote_plus(password)

# Construct the connection URI with the escaped username and password
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.nyhdbb1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

print(uri)