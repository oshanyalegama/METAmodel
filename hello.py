import json

# Specify the path to your JSON file
file_path = r's1.json'
print("hello world")

try:
    # Open the file with UTF-8 encoding
    with open(file_path, 'r') as file:
        contents = file.read().strip()
        
        if contents:
            data = json.loads(contents)
            print(data)
        else:
            print("The file is empty.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
except FileNotFoundError:
    print("The file does not exist.")
except Exception as e:
    print(f"An error occurred: {e}")
