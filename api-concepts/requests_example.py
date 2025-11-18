import json

# Simulation of a user sending a request
request = {
    "method": "POST",
    "endpoint": "/create-user",
    "body": {
        "username": "antonis",
        "email": "antonis@example.com"
    }
}

# Backend receives the request
print("Incoming request:")
print(json.dumps(request, indent=4))

# Backend processing
if (request["method"] == "POST" and request["endpoint"] == "/create-user"):
    username = request["body"]["username"]
    email = request["body"]["email"]
    response = {
        "status": "success",
        "message": f"User '{username}' created successfully!"
    }

# Send response back
print("\nResponse to client:")
print(json.dumps(response, indent=4))
