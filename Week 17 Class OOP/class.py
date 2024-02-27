# PascalCase, camelCase, snake_case
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        self.following += 1
        user.followers += 1


user1 = User(1, "Fahad")
user2 = User(2, "Sima")

user1.follow(user2)
print(user1.followers, user1.following)
print(user2.followers, user2.following)
