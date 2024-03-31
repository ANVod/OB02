# Пользовательская система управления

Этот проект реализует простую систему управления пользователями с возможностью добавления и удаления пользователей администратором. У пользователей есть уникальные идентификаторы, имена и уровни доступа. Система предусматривает два типа пользователей: обычные пользователи и администраторы. Администраторы обладают дополнительной функциональностью для управления списком пользователей.

## Основные функции

- **Добавление пользователей:** Администраторы могут добавлять объекты пользователей в систему.
- **Удаление пользователей:** Администраторы могут удалять объекты пользователей из системы.
- **Просмотр списка пользователей:** Администраторы могут просматривать список текущих пользователей в системе.

## Классы

### User

Базовый класс, представляющий пользователя. Содержит следующие атрибуты:
- `user_id` (int): Уникальный идентификатор пользователя.
- `name` (str): Имя пользователя.
- `access_level` (str): Уровень доступа пользователя (по умолчанию "user").

### Admin

Класс, производный от `User`, представляющий администратора системы. Расширяет базовый класс следующими функциями:
- `add_user(user)`: Добавление пользователя в систему.
- `remove_user(user)`: Удаление пользователя из системы.
- `list_users()`: Вывод списка всех пользователей.

## Пример использования

```python
admin = Admin(1, "Admin User")
user1 = User(2, "Regular User 1")
user2 = User(3, "Regular User 2")

admin.add_user(user1)  # Добавление пользователя user1
admin.add_user(user2)  # Добавление пользователя user2

print("\nСписок пользователей после добавления:")
admin.list_users()  # Вывод списка пользователей

admin.remove_user(user1)  # Удаление пользователя user1

print("\nСписок пользователей после удаления:")
admin.list_users()  # Вывод обновлённого списка пользователей
```

## Замечания

- Этот пример представляет основную идею системы управления пользователями и может быть расширен или модифицирован в соответствии с конкретными требованиями проекта.
- Объекты класса `User` могут быть расширены дополнительными атрибутами и методами в зависимости от требований к системе управления пользователями.
- В примере кода использованы печатные сообщения для иллюстрации процесса добавления и удаления пользователей, что может быть изменено или дополнено в реальных приложениях.
