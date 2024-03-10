import pandas as pd
import pymongo
import urllib.parse

from lp_pymango.var.variables import *# username, password, dbname, colname

# Escape the username and password
escaped_username = urllib.parse.quote_plus(username)
escaped_password = urllib.parse.quote_plus(password)

# Construct the connection URI with the escaped username and password
uri = f"mongodb+srv://{escaped_username}:{escaped_password}@cluster0.nyhdbb1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Establish a connection to the MongoDB server
client = pymongo.MongoClient(uri)

db = client[dbname]
collection = db[colname]

# Retrieve all documents from the collection
documents = collection.find()
# Convert the MongoDB documents into a DataFrame
df = pd.DataFrame(documents)

# Specify the full file path including the filename where you want to save the CSV file
csv_file_path = downlode_file_path


# Save the DataFrame to a CSV file
df.to_csv(csv_file_path, index=False)

print(f"CSV file created: {csv_file_path}")
