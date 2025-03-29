import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Connect to MySQL Database
conn = mysql.connector.connect(
    host="localhost",
    user="root",  
    password="IPTFINALSPROJ",  
    database="my_database",
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
    management_window.geometry("500x400")
    
    frame = tk.Frame(management_window, padx=20, pady=20)
    frame.pack(expand=True)
    
    tk.Label(frame, text="Player Management", font=("Helvetica", 16, "bold")).pack(pady=10)
    tk.Button(frame, text="Add Player", command=add_player, width=20).pack(pady=5)
    tk.Button(frame, text="Search Player", command=search_player, width=20).pack(pady=5)
    tk.Button(frame, text="Delete Player", command=delete_player, width=20).pack(pady=5)
    tk.Button(frame, text="Update Player", command=update_player, width=20).pack(pady=5)

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
    add_window.geometry("400x300")
    
    frame = tk.Frame(add_window, padx=20, pady=20)
    frame.pack(expand=True)
    
    tk.Label(frame, text="Jersey Number:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
    entry_jersey = tk.Entry(frame)
    entry_jersey.grid(row=0, column=1, padx=5, pady=5)

    tk.Label(frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_name = tk.Entry(frame)
    entry_name.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="College:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_college = tk.Entry(frame)
    entry_college.grid(row=2, column=1, padx=5, pady=5)

    tk.Label(frame, text="Salary:").grid(row=3, column=0, padx=5, pady=5, sticky="w")
    entry_salary = tk.Entry(frame)
    entry_salary.grid(row=3, column=1, padx=5, pady=5)

    tk.Button(frame, text="Save", command=save).grid(row=4, columnspan=2, pady=10)

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
    search_window.geometry("400x200")
    
    frame = tk.Frame(search_window, padx=20, pady=20)
    frame.pack(expand=True)
    
    tk.Label(frame, text="Search Player", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(frame, text="Enter Jersey Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_jersey = tk.Entry(frame)
    entry_jersey.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(frame, text="Search", command=find, width=15).grid(row=2, columnspan=2, pady=10)

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
    delete_window.geometry("400x200")
    
    frame = tk.Frame(delete_window, padx=20, pady=20)
    frame.pack(expand=True)
    
    tk.Label(frame, text="Delete Player", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(frame, text="Enter Jersey Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_jersey = tk.Entry(frame)
    entry_jersey.grid(row=1, column=1, padx=5, pady=5)

    tk.Button(frame, text="Delete", command=remove, width=15).grid(row=2, columnspan=2, pady=10)

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
    update_window.geometry("400x250")
    
    frame = tk.Frame(update_window, padx=20, pady=20)
    frame.pack(expand=True)
    
    tk.Label(frame, text="Update Player", font=("Helvetica", 14, "bold")).grid(row=0, column=0, columnspan=2, pady=10)
    tk.Label(frame, text="Enter Jersey Number:").grid(row=1, column=0, padx=5, pady=5, sticky="w")
    entry_jersey = tk.Entry(frame)
    entry_jersey.grid(row=1, column=1, padx=5, pady=5)

    tk.Label(frame, text="New Salary:").grid(row=2, column=0, padx=5, pady=5, sticky="w")
    entry_salary = tk.Entry(frame)
    entry_salary.grid(row=2, column=1, padx=5, pady=5)

    tk.Button(frame, text="Save", command=save, width=15).grid(row=3, columnspan=2, pady=10)


# Tkinter GUI Setup
root = tk.Tk()
root.title("Login System")
root.geometry("350x250")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(expand=True)

tk.Label(frame, text="Login", font=("Helvetica", 16, "bold")).pack(pady=10)
tk.Label(frame, text="Username:").pack(anchor="w")
entry_username = tk.Entry(frame, width=30)
entry_username.pack()

tk.Label(frame, text="Password:").pack(anchor="w")
entry_password = tk.Entry(frame, show="*", width=30)
entry_password.pack()

tk.Button(frame, text="Login", command=login, width=20).pack(pady=20)

root.mainloop()

# Close connection when done
cursor.close()
conn.close()
