import tkinter as tk
from tkinter import messagebox

# Function to switch to the main trading interface after successful login
def switch_to_trading_interface():
    # Hide the login screen
    for widget in root.winfo_children():
        widget.destroy()

    # Set a background color for the main interface
    root.configure(bg="#282c34")
    root.geometry("350x420")
    root.resizable(False, False)

    # Main trading interface UI
    tk.Label(root, text="Expiry Date:", bg="#282c34", fg="#ffffff", font=("Arial", 14, "bold")).grid(row=0, column=0, padx=10, pady=10)
    strike_expiry_entry = tk.Entry(root, bg="#000000", fg="#ffffff",font=("Arial", 12), width=10)
    strike_expiry_entry.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Lot Size:", bg="#282c34", fg="#ffffff", font=("Arial", 12, "bold")).grid(row=5, column=0, padx=10, pady=10)    
    lot_size_spinbox = tk.Spinbox(root, from_=1, to=1000, bg="#000000", fg="#ffffff", font=("Arial", 12),width=4)
    lot_size_spinbox.grid(row=5, column=1, padx=10, pady=10)

    tk.Label(root, text="Stoploss Points:", bg="#282c34", fg="#ffffff", font=("Arial", 12, "bold")).grid(row=6, column=0, padx=10, pady=10)
    trailing_points_entry = tk.Spinbox(root, from_=1, to=1000, bg="#000000", fg="#ffffff", font=("Arial", 12),width=4)
    trailing_points_entry.grid(row=6, column=1, padx=10, pady=10)
    
    tk.Label(root, text="Product Type:", bg="#282c34", fg="#ffffff", font=("Arial", 14, "bold")).grid(row=1, column=0, padx=10, pady=10)
    product_type_entry = tk.Spinbox(root, bg="#000000", fg="#ffffff",font=("Arial", 12),width=6)
    product_type_entry.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Symbol:", bg="#282c34", fg="#ffffff", font=("Arial", 12, "bold")).grid(row=4, column=0, padx=10, pady=10)
    symbol_entry = tk.Entry(root, bg="#000000", fg="#ffffff",font=("Arial", 12),width=10)
    symbol_entry.grid(row=4, column=1, padx=10, pady=10)

    tk.Label(root, text="Margin:", bg="#282c34", fg="#ffffff", font=("Arial", 12, "bold")).grid(row=2, column=0, padx=10, pady=10)
    margin_label = tk.Label(root, text="------------", bg="#282c34", fg="#000000", font=("Arial", 12))
    margin_label.grid(row=2, column=1, padx=10, pady=10)

    tk.Label(root, text="P&L:", bg="#282c34", fg="#ffffff", font=("Arial", 12, "bold")).grid(row=7, column=0, padx=10, pady=10)
    pnl_label = tk.Label(root, text="----------", bg="#282c34", fg="#000000", font=("Arial", 12))
    pnl_label.grid(row=7, column=1, padx=10, pady=10)

    tk.Label(root, text="Strike Price:", bg="#282c34", fg="#ffffff", font=("Arial", 12, "bold")).grid(row=3, column=0, padx=10, pady=10)
    strike_price_entry = tk.Entry(root, bg="#000000", fg="#ffffff",font=("Arial", 12),width=10)
    strike_price_entry.grid(row=3, column=1, padx=10, pady=10)

    # Buy and Sell buttons with vibrant colors
    buy_button = tk.Button(root, text="Buy", bg="#4caf50", fg="#ffffff",width=8, height=1,font=("Arial", 12, "bold"), command=lambda: messagebox.showinfo("Buy", "Buy order placed"))
    buy_button.grid(row=8, column=0, padx=10, pady=10)

    sell_button = tk.Button(root, text="Sell", bg="#f44336", fg="#ffffff", width=8, height=1,font=("Arial", 12, "bold"), command=lambda: messagebox.showinfo("Sell", "Sell order placed"))
    sell_button.grid(row=8, column=1, padx=10, pady=10)

  # Function to validate login and switch screen
def validate_login():
    mobile_number = mobile_entry.get()
    tpin = tpin_entry.get()
    api_key = api_key_entry.get()

    if mobile_number and tpin and api_key:
        switch_to_trading_interface()
    else:
        messagebox.showerror("Error", "Please fill in all fields")

# Tkinter GUI setup for login screen
root = tk.Tk()
root.title("Trading App - Login")
root.configure(bg="#2e2e2e") 
root.geometry("350x410")
root.resizable(False, False) # Background color

# Mobile number input with vibrant colors
tk.Label(root, text="Mobile Number:", bg="#2e2e2e", fg="#ffffff", font=("Arial", 15)).grid(row=0, column=0, padx=10, pady=10)
mobile_entry = tk.Entry(root, bg="#2f2f2f", fg="#ffffff",font=("Arial", 12),width=10)
mobile_entry.grid(row=0, column=1, padx=10, pady=10)

# T-PIN input
tk.Label(root, text="T-PIN:", bg="#2e2e2e", fg="#ffffff", font=("Arial", 15)).grid(row=1, column=0, padx=10, pady=10)
tpin_entry = tk.Entry(root, bg="#2f2f2f", fg="#ffffff",font=("Arial", 12),width=10)
tpin_entry.grid(row=1, column=1, padx=10, pady=10)

# API Key input
tk.Label(root, text="API Key:", bg="#2e2e2e", fg="#ffffff", font=("Arial", 15)).grid(row=2, column=0, padx=10, pady=10)
api_key_entry = tk.Entry(root, bg="#2f2f2f", fg="#ffffff")
api_key_entry.grid(row=2, column=1, padx=10, pady=10)

# Submit button with color
login_button = tk.Button(root, text="Login", bg="#ffffff", fg="#000000", font=("Arial", 12, "bold"), command=validate_login)
login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

root.geometry("360x400")  # Set window size
root.mainloop()
