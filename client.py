import ccxt
import credentials


exchange = ccxt.deribit({
    'apiKey': credentials.client_id,
    'secret': credentials.client_secret
})
