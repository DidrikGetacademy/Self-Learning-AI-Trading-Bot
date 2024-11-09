#: Inneholder kode for å koble til trading API-er, håndtere autentisering og sende forespørsler til børsen.
import os
import ccxt 
from dotenv import load_dotenv

load_dotenv()

#API keys
api_key = os.getenv("BINANCE_API_KEY")
secret_key = os.getenv("BINANCE_SECRET_KEY")


#SETUP Binance-client

exchange = ccxt.binance({
    'apikey': api_key,
    'secret': secret_key,
    'enableRateLimit': True,
})

balance = exchange.fetch_balance()
print(balance)
