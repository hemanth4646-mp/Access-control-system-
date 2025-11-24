from datetime import datetime

# ---- USER DATABASE ----
USERS = {
    "admin": {"password": "admin123", "role": "Admin"},
    "manager": {"password": "manager123", "role": "Manager"},
    "john": {"password": "john123", "role": "Member"}
}

# ---- ROLE PERMISSIONS ----
ROLE_ACCESS = {
    "Admin": ["Add User", "Delete User", "View Logs", "Access Dashboard"],
    "Manager": ["Access Dashboard", "View Logs"],
    "Member": ["Access Dashboard"]
}

# ---- SYSTEM LOGS ----
LOGS = []

def log_event(user, action):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    LOGS.append(f"{time} - {user} - {action}")

def login():
    print("\n------ LOGIN --------")
    username = input("Enter Username: ")
    password = input("Enter Password: ")

    if username in USERS and USERS[username]["password"] == password:
        role = USERS[username]["role"]
        log_event(username, "Logged In")
        print(f"\nLogin Successful! Welcome {username} ({role})")
        return username, role
    else:
        print("\nInvalid credentials! Try again.")
        return None, None

def show_menu(role):
    print("\n--- AVAILABLE ACTIONS ---")
    actions = ROLE_ACCESS[role]

    for i, action in enumerate(actions):
        print(f"{i+1}. {action}")

    choice = int(input("\nEnter your choice: "))
    return actions[choice-1]

def admin_add_user():
    print("\n--- ADD NEW USER ---")
    username = input("Enter new username: ")
    password = input("Enter password: ")
    role = input("Enter role (Admin/Manager/Member): ")

    if role not in ROLE_ACCESS:
        print("Invalid role!")
        return

    USERS[username] = {"password": password, "role": role}
    print(f"User '{username}' added successfully!")

def admin_delete_user():
    print("\n--- DELETE USER ---")
    username = input("Enter username to delete: ")

    if username in USERS:
        del USERS[username]
        print(f"User '{username}' deleted!")
    else:
        print("User not found!")

def view_logs():
    print("\n--- SYSTEM LOGS ---")
    for entry in LOGS:
        print(entry)

def dashboard(user, role):
    print(f"\n📌 Dashboard: Hello {user}, Your Role = {role}")
    print("You can view sensitive information here.")

def main():
    while True:
        user, role = login()
        if not user:
            continue

        while True:
            action = show_menu(role)

            if action == "Add User":
                admin_add_user()
            elif action == "Delete User":
                admin_delete_user()
            elif action == "View Logs":
                view_logs()
            elif action == "Access Dashboard":
                dashboard(user, role)
            
            log_event(user, f"Performed action: {action}")

            next_step = input("\nDo you want to continue? (y/n): ")
            if next_step.lower() != "y":
                print("Logging out...\n")
                break

# ---- START PROGRAM ----
main()
