import tkinter as tk
from tkinter import messagebox
import requests

# Global variable to store the API key
api_key = ""

# Function to handle login
def login():
    global api_key
    mobile_number = mobile_entry.get()
    otp = otp_entry.get()
    api_key = api_key_entry.get()

    # Here you would typically verify the mobile number and OTP
    # For this example, we will assume they're always correct

    messagebox.showinfo("Login Successful", "You are now logged in for trading!")
    login_frame.pack_forget()  # Hide login frame
    trading_frame.pack(pady=20)  # Show trading frame

# Function to place an order
def place_order(order_type):
    try:
        price = float(call_price.get()) if order_type == "Call" else float(put_price.get())
        qty = int(call_qty.get()) if order_type == "Call" else int(put_qty.get())
        
        # Dummy API call (replace with actual API endpoint)
        url = "https://api.kotakneo.com/v1/orders"  # Replace with actual API URL
        headers = {
            "Authorization": f"Bearer {api_key}"  # Use the global API key
        }
        data = {
            "order_type": order_type,
            "price": price,
            "quantity": qty
        }

        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()  # Raise an error for bad responses
        
        messagebox.showinfo("Order Placed", f"{order_type} order placed successfully!")
    
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Create the main application window
root = tk.Tk()
root.title("Trading Application")
root.geometry("400x400")
root.configure(bg="#f0f8ff")
root.resizable(False, False)

# Login Section
login_frame = tk.Frame(root, bg="#f0f8ff")
login_frame.pack(pady=20)

tk.Label(login_frame, text="Mobile Number:", bg="#f0f8ff").grid(row=0, column=0)
mobile_entry = tk.Entry(login_frame)
mobile_entry.grid(row=0, column=1)

tk.Label(login_frame, text="OTP:", bg="#f0f8ff").grid(row=1, column=0)
otp_entry = tk.Entry(login_frame)
otp_entry.grid(row=1, column=1)

tk.Label(login_frame, text="API Key:", bg="#f0f8ff").grid(row=2, column=0)
api_key_entry = tk.Entry(login_frame)
api_key_entry.grid(row=2, column=1)

tk.Button(login_frame, text="Login", command=login).grid(row=3, columnspan=2, pady=10)

# Trading Section (hidden initially)
trading_frame = tk.Frame(root, bg="#f0f8ff")

# Call options
tk.Label(trading_frame, text="CALL Price:", bg="#f0f8ff").grid(row=0, column=0)
call_price = tk.Entry(trading_frame, bg="#e6f7ff")
call_price.grid(row=0, column=1)

tk.Label(trading_frame, text="CALL Quantity:", bg="#f0f8ff").grid(row=1, column=0)
call_qty = tk.Entry(trading_frame, bg="#e6f7ff")
call_qty.grid(row=1, column=1)

tk.Button(trading_frame, text="BUY CALL", command=lambda: place_order("Call"), bg="#66cdaa").grid(row=2, columnspan=2, pady=10)

# Put options
tk.Label(trading_frame, text="PUT Price:", bg="#f0f8ff").grid(row=3, column=0)
put_price = tk.Entry(trading_frame, bg="#e6f7ff")
put_price.grid(row=3, column=1)

tk.Label(trading_frame, text="PUT Quantity:", bg="#f0f8ff").grid(row=4, column=0)
put_qty = tk.Entry(trading_frame, bg="#e6f7ff")
put_qty.grid(row=4, column=1)

tk.Button(trading_frame, text="BUY PUT", command=lambda: place_order("Put"), bg="#ff69b4").grid(row=5, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
