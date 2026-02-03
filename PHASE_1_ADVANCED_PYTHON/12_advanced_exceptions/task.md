# Task: Build a User Management System with Custom Exceptions

Open `answer.py` in this folder and complete the following objectives:

## Goal 1: Create Exception Hierarchy
Create these custom exceptions:
- `UserServiceError` (base exception)
- `UserNotFoundError(UserServiceError)`
- `DuplicateUserError(UserServiceError)`
- `InvalidUserDataError(UserServiceError)`

## Goal 2: Create User class
Create a simple `User` class with:
- Attributes: `id`, `username`, `email`
- Validation in `__init__`: raise `InvalidUserDataError` if email doesn't contain "@"

## Goal 3: Create UserService class
Create a `UserService` class with:
- Attribute: `users` (dictionary mapping id to User)
- Method `create_user(id, username, email)`: 
  - Check if user already exists (raise `DuplicateUserError`)
  - Create and store user
- Method `get_user(id)`:
  - Return user or raise `UserNotFoundError`
- Method `delete_user(id)`:
  - Delete user or raise `UserNotFoundError`

## Goal 4: Test Exception Handling
Write code that:
- Creates valid users successfully
- Tries to create duplicate user (catch `DuplicateUserError`)
- Tries to get non-existent user (catch `UserNotFoundError`)
- Tries to create user with invalid email (catch `InvalidUserDataError`)

---

**Expected Output:**
```text
Created user: alice (alice@example.com)
Created user: bob (bob@example.com)

Error creating duplicate: User with ID 1 already exists

Retrieved user: alice

Error: User with ID 999 not found

Error: Invalid email format
```
