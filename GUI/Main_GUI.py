import tkinter as tk
from tkinter import messagebox
import threading
import ccxt

# MAIN-WINDOW
root = tk.Tk()
root.title("LearnReflect AI-TradingBot")
root.geometry("1000x900")

root.config(bg="#2E2E2E")
# Variable to store exchange information and connection status
exchange_selected = tk.StringVar(value="Select Exchange")
api_key = tk.StringVar()
api_secret = tk.StringVar()
connection_status = tk.StringVar(value="Not connected")

# Functions for GUI-Elements
def check_connection():
    exchange_name = exchange_selected.get()  # Gets the exchange selected by the user
    key = api_key.get()  # Public key
    secret = api_secret.get()  # Secret key
    
    if exchange_name == "Select Exchange":
        log_message("Please select an exchange.")
        return
    
    if not key or not secret:
        log_message("Please enter both API and Secret keys.")
        return   
    
    try:  # Proper indentation for try block
        exchange_class = getattr(ccxt, exchange_name.lower())  # Get the exchange class (e.g., ccxt.binance)
        exchange = exchange_class({
            'apiKey': key,
            "secret": secret,
        })
        
        # Checks the balance to see if the connection is successful
        balance = exchange.fetch_balance()  # Correct method call (added `fetch_balance()`)
        
        # If the connection is successful, show the connected message
        connection_status.set(f"Connected to {exchange_name}")
        log_message(f"Successfully connected to {exchange_name}!")
    
    except Exception as e:  # Proper indentation for except block
        # Handle errors (e.g., invalid API keys, connection issues)
        connection_status.set("Connection failed")
        log_message(f"Failed to connect to {exchange_name}: {str(e)}")


def log_message(message):
    log_text.insert(tk.END,message + "\n")
    log_text.see(tk.END)


#SECTION for exchange-Login

frame_exchange = tk.Frame(root)
frame_exchange.pack(padx=10,pady=10)

tk.Label(frame_exchange,text="Select Exchange:",bg="#2E2E2E",fg="white").grid(row=0,column=0, sticky="w",pady=5)
exchange_options = ["Select Exchange","binance","bybit","okx"]
exchange_menu = tk.OptionMenu(frame_exchange,exchange_selected, *exchange_options)   
exchange_menu = tk.OptionMenu(frame_exchange,exchange_selected, *exchange_options)
exchange_menu.grid(row=0,column=1,pady=5)



tk.Label(frame_exchange,text="API key:",bg="#2E2E2E",fg="white").grid(row=1,column=0,sticky="w",pady=5)
entry_api_key = tk.Entry(frame_exchange,textvariable=api_key,bg="#444444",fg="white",width=40)
entry_api_key.grid(row=1,column=1,pady=5)



tk.Label(frame_exchange,text="Secret Key:",bg="#2E2E2E",fg="white").grid(row=2,column=0,sticky="w",pady=5)
entry_api_secret = tk.Entry(frame_exchange,textvariable=api_secret, show="*",bg="#333333",fg="white",width=40) 
entry_api_secret.grid(row=2,column=1,pady=5)



btn_connect = tk.Button(frame_exchange,text="Connect",command=check_connection,bg="#444444",fg="white")
btn_connect.grid(row=3,column=1,pady=10)

tk.Label(frame_exchange,textvariable=connection_status,bg="#2E2E2E",fg="white").grid(row=4,column=0,columnspan=2,pady=5)


#SECTION FOR START/STOP BOT (seperate buttons)
frame_control = tk.Frame(root,bg="#2E2E2E")
frame_control.pack(pady=10)

btn_start = tk.Button(frame_control,text="Start Tradingbot", state="disabled", command=lambda: log_message("Bot Started."),bg="#333333",fg="white")
btn_start.grid(row=0,column=0,padx=5)
btn_stop = tk.Button(frame_control,text="Stop Tradingbot",state="disabled",command=lambda: log_message("Bot stopped"),bg="#333333",fg="white")
btn_stop.grid(row=0,column=1,padx=5)



#Section for LOG
frame_log = tk.Frame(root,bg="#2E2E2E")
frame_log.pack(pady=10)

log_text = tk.Text(frame_log,width=70,height=10,state="normal",bg="#444444",fg="white")
log_text.pack()

root.mainloop()