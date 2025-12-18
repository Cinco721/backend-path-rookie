import json

users = [
    {"id": 1, "name": "Ana", "active": True},
    {"id": 2, "name": "Luis", "active": False},
    {"id": 3, "name": "Eric", "active": True}
]

active_users = []

for user in users:
    if user["active"]:
        active_users.append(user["name"])

result = {
    "total_users": len(users),
    "active_users": active_users
}

print(json.dumps(result, indent=2))
