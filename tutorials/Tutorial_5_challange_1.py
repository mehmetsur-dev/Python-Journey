# dictionaries_challenge

player = {"username": "ShadowWalker", "level": 14, "languages": ["English", "Turkish"], "status": "Active"}

print(player)

player. update({"level": 15, "rank": "Veteran"})
print(player)

print(player. get("discord_id", "Not Linked"))

del player["status"]
print(player)


for key, value in player. items():
    print(f"{key}: {value}")
