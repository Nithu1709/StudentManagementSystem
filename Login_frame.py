import tkinter as tk
from tkinter import ttk, messagebox
import db


class LoginFrame(ttk.Frame):
    def __init__(self, master, on_success):
        super().__init__(master, padding=30)
        self.on_success = on_success

        ttk.Label(self, text="Student Management System", font=("Segoe UI", 18, "bold")).grid(
            row=0, column=0, columnspan=2, pady=(0, 20)
        )

        ttk.Label(self, text="Username:").grid(row=1, column=0, sticky="e", pady=5)
        self.username_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.username_var, width=25).grid(row=1, column=1, pady=5)

        ttk.Label(self, text="Password:").grid(row=2, column=0, sticky="e", pady=5)
        self.password_var = tk.StringVar()
        ttk.Entry(self, textvariable=self.password_var, show="*", width=25).grid(
            row=2, column=1, pady=5
        )

        ttk.Button(self, text="Login", command=self.attempt_login).grid(
            row=3, column=0, columnspan=2, pady=(15, 0)
        )

        ttk.Label(
            self, text="Default login -> admin / admin123", foreground="gray"
        ).grid(row=4, column=0, columnspan=2, pady=(10, 0))

        self.bind_all("<Return>", lambda e: self.attempt_login())

    def attempt_login(self):
        username = self.username_var.get().strip()
        password = self.password_var.get().strip()

        if not username or not password:
            messagebox.showwarning("Missing info", "Please enter both username and password.")
            return

        if db.verify_login(username, password):
            self.on_success()
        else:
            messagebox.showerror("Login failed", "Invalid username or password.")
