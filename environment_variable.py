import os

# print(os.environ)

# Set a new environment variable
os.environ['MY_VARIABLE'] = 'my_value'
database_url = os.getenv("MY_VARIABLE")
print(database_url)


# Working with ‘.env’ Files (Best Practice)
import os
from dotenv import load_dotenv, find_dotenv
dotnet_envfilepath = find_dotenv()
load_dotenv()  # this reads your .env file
secret = os.getenv("DATABASE_URL")
print("Your secret key is safe:", secret)