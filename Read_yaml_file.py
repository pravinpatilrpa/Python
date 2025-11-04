import yaml
try:
    with open('config.yaml', 'r') as file:
        data = yaml.safe_load(file)
        print(data)
        
    output = {'UserName': data.get('user'),'Password': data.get('port')}
    print(output)

except FileNotFoundError:
    print("Error: config.yaml not found.")
except yaml.YAMLError as e:
    print(f"Error parsing YAML file: {e}")