class User:
    def __init__(self, user_id, name, access_level='user'):
        self._user_id = user_id
        self._name = name
        self._access_level = access_level

    def __str__(self):
        return f"ID: {self._user_id}, Name: {self._name}, Access Level: {self._access_level}"
    @property
    def user_id(self):
        return self._user_id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def access_level(self):
        return self._access_level

    @access_level.setter
    def access_level(self, value):
        self._access_level = value

class Admin(User):
    def __init__(self, user_id, name):
        super().__init__(user_id, name, access_level='admin')
        self._users = []

    def add_user(self, user):
        if not isinstance(user, User):
            print("Можно добавлять только пользовательские экземпляры")
            return
        self._users.append(user)
        print(f"User {user._name} добавлен.")

    def remove_user(self, user):
        if user in self._users:
            self._users.remove(user)
            print(f"User {user._name} удаленный.")
        else:
            print("Пользователь не найден")

    def list_users(self):
        for user in self._users:
            print(user)


admin = Admin(1, "Admin User")
user1 = User(2, "Regular User 1")
user2 = User(3, "Regular User 2")

admin.add_user(user1)
admin.add_user(user2)

print("\nСписок пользователей после добавления:")
admin.list_users()

admin.remove_user(user1)

print("\nСписок пользователей после удаления:")
admin.list_users()