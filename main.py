import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="IPTFINALSPROJ",  
    database="my_database"
)
cursor = conn.cursor()

# Login Function
def login():
    username = entry_username.get()
    password = entry_password.get()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    if user:
        messagebox.showinfo("Login Success", f"Welcome, {username}!")
        open_management_system()
    else:
        messagebox.showerror("Login Failed", "Invalid username or password")

# Open Player Management System
def open_management_system():
    root.withdraw()  # Hide login window
    management_window = tk.Toplevel()
    management_window.title("Lakers Management System")
    management_window.geometry("400x400")

    tk.Button(management_window, text="Add Player", command=add_player).pack()
    tk.Button(management_window, text="Search Player", command=search_player).pack()
    tk.Button(management_window, text="Delete Player", command=delete_player).pack()
    tk.Button(management_window, text="Update Player", command=update_player).pack()

# Add Player
def add_player():
    def save():
        jersey = entry_jersey.get()
        name = entry_name.get()
        college = entry_college.get()
        salary = entry_salary.get()

        cursor.execute("INSERT INTO players (jersey_number, name, college, salary) VALUES (%s, %s, %s, %s)",
                       (jersey, name, college, salary))
        conn.commit()
        messagebox.showinfo("Success", "Player added successfully")
        add_window.destroy()

    add_window = tk.Toplevel()
    add_window.title("Add Player")
    tk.Label(add_window, text="Jersey Number:").pack()
    entry_jersey = tk.Entry(add_window)
    entry_jersey.pack()

    tk.Label(add_window, text="Name:").pack()
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    tk.Label(add_window, text="College:").pack()
    entry_college = tk.Entry(add_window)
    entry_college.pack()

    tk.Label(add_window, text="Salary:").pack()
    entry_salary = tk.Entry(add_window)
    entry_salary.pack()

    tk.Button(add_window, text="Save", command=save).pack()

# Search Player
def search_player():
    def find():
        jersey = entry_jersey.get()
        cursor.execute("SELECT * FROM players WHERE jersey_number = %s", (jersey,))
        player = cursor.fetchone()
        if player:
            messagebox.showinfo("Player Found", f"Name: {player[1]}\nCollege: {player[2]}\nSalary: {player[3]}")
        else:
            messagebox.showerror("Not Found", "Player not found")

    search_window = tk.Toplevel()
    search_window.title("Search Player")
    tk.Label(search_window, text="Enter Jersey Number:").pack()
    entry_jersey = tk.Entry(search_window)
    entry_jersey.pack()

    tk.Button(search_window, text="Search", command=find).pack()

# Delete Player
def delete_player():
    def remove():
        jersey = entry_jersey.get()
        cursor.execute("DELETE FROM players WHERE jersey_number = %s", (jersey,))
        conn.commit()
        messagebox.showinfo("Success", "Player deleted successfully")
        delete_window.destroy()

    delete_window = tk.Toplevel()
    delete_window.title("Delete Player")
    tk.Label(delete_window, text="Enter Jersey Number:").pack()
    entry_jersey = tk.Entry(delete_window)
    entry_jersey.pack()

    tk.Button(delete_window, text="Delete", command=remove).pack()

# Update Player
def update_player():
    def save():
        jersey = entry_jersey.get()
        salary = entry_salary.get()

        cursor.execute("UPDATE players SET salary = %s WHERE jersey_number = %s", (salary, jersey))
        conn.commit()
        messagebox.showinfo("Success", "Player salary updated")
        update_window.destroy()

    update_window = tk.Toplevel()
    update_window.title("Update Player")
    tk.Label(update_window, text="Enter Jersey Number:").pack()
    entry_jersey = tk.Entry(update_window)
    entry_jersey.pack()

    tk.Label(update_window, text="New Salary:").pack()
    entry_salary = tk.Entry(update_window)
    entry_salary.pack()

    tk.Button(update_window, text="Save", command=save).pack()

# Tkinter GUI Setup
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")

tk.Label(root, text="Username:").pack()
entry_username = tk.Entry(root)
entry_username.pack()

tk.Label(root, text="Password:").pack()
entry_password = tk.Entry(root, show="*")
entry_password.pack()

tk.Button(root, text="Login", command=login).pack()

root.mainloop()

# Close connection when done
cursor.close()
conn.close()
