import configparser
config = configparser.ConfigParser()
config.read('config.ini')

# Access values using section and key names
db_url = config['common']['DATABASE_URL']
debug = config['common']['DEBUG']

print(f"Database Host: {db_url}")
print(f"Server Port: {debug}")