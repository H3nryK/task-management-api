import requests

url = 'http://localhost:5000/tasks'
data = {
    'title': 'Buy groceries',
    'description': 'Pick up milk, eggs, and bread from the store.'
}

response = requests.post(url, json=data)

if response.status_code == 201:
    print('Task created successfully!')
    print(response.json())
else:
    print('Failed to create task.')
    print(response.text)