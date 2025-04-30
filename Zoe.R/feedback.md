# Feedback

### **Strengths**
1. **Basic Functionality**:
   - The code implements login, registration, and password change features.
   - It uses a menu-driven approach to guide the user through different actions.

2. **File-Based User Storage**:
   - Usernames and passwords are stored in a file (`plaintext.csv`), allowing data persistence.

3. **Effort to Handle Edge Cases**:
   - The code attempts to handle incorrect usernames, passwords, and short passwords during login and password change.

---

### **Issues and Suggestions for Improvement**

#### 1. **Plain Text Password Storage**
   - Storing passwords in plain text (`plaintext.csv`) is a major security flaw.

   **Fix**: Use password hashing (e.g., `bcrypt`) to securely store passwords.

   Example:
   ```python
   import bcrypt

   salt = b"$2b$12$ieYNkQp8QumgedUo30nuPO"

   # Hashing a password
   hashed_password = bcrypt.hashpw(password.encode(), salt=salt)

   # Verifying a password
   if bcrypt.checkpw(input_password.encode(), hashed_password):
       print("Login successful!")
   ```

---

#### 2. **Inefficient User Lookup**
   - The code reads the entire file line by line for every login and registration operation, which is inefficient.
   - The `userlogin` function uses nested loops to match usernames and passwords, which is unnecessarily complex.

   **Fix**: Load the file into memory once and use a dictionary for faster lookups.

   Example:
   ```python
   def load_users():
       users = {}
       with open("plaintext.csv", "r") as file:
           for line in file:
               user, password = line.strip().split(",")
               users[user] = password
       return users
   ```

---

#### 3. **Global Variables**
   - The use of global variables (`useraction`, `userinput`, `pwdinput`) makes the code harder to debug and maintain.

   **Fix**: Pass these variables as arguments to functions or encapsulate them in a class.

---

#### 4. **No Input Validation**
   - The code does not validate user input, which could lead to unexpected behavior or errors.

   **Fix**: Add input validation to ensure usernames and passwords meet certain criteria (e.g., no special characters, minimum length).

---

#### 5. **No Error Handling**
   - The code does not handle errors, such as file not found or invalid file format.

   **Fix**: Add error handling using `try` and `except` blocks.

   Example:
   ```python
   try:
       with open("plaintext.csv", "r") as file:
           # File operations
   except FileNotFoundError:
       print("Error: User file not found.")
   ```

---

#### 6. **Password Change Logic**
   - The `passwordchanger` function does not actually update the password in the file.
   - It also uses recursion unnecessarily, which could lead to a stack overflow for repeated invalid inputs.

   **Fix**: Rewrite the file with the updated password and avoid recursion.

   Example:
   ```python
   def passwordchanger(users, current_user):
       currentpwd = input("Enter your current password: ")
       if verify_password(currentpwd, users[current_user]):
           newpwd = input("Enter your new password (must be more than 4 characters): ")
           if len(newpwd) < 4:
               print("This password is too short. Please try again.")
               return
           users[current_user] = hash_password(newpwd)
           save_users(users)
           print("Your password has been changed.")
       else:
           print("Incorrect password. Please try again.")
   ```

---

#### 7. **Registration Logic**
   - The `registeruser` function does not check if the username already exists, as the relevant code is commented out.

   **Fix**: Implement a proper check for duplicate usernames.

   Example:
   ```python
   def registeruser(users):
       newuser = input("Username: ").strip()
       if newuser in users:
           print("Error: Username already exists.")
           return
       newpwd = input("Password: ").strip()
       if len(newpwd) < 4:
           print("Error: Password must be at least 4 characters.")
           return
       users[newuser] = hash_password(newpwd)
       save_users(users)
       print("Registered successfully!")
   ```

---

#### 8. **Code Duplication**
   - There is significant duplication of logic, such as reading and writing to the file, and checking password lengths.

   **Fix**: Refactor common functionality into reusable helper functions.

---

#### 9. **No Exit Condition for `main`**
   - The `main` function recursively calls itself, which could lead to a stack overflow for repeated invalid inputs.

   **Fix**: Use a `while` loop to handle the menu logic instead of recursion.