from geminipy import Geminipy

# The connection defaults to the Gemini sandbox.
# Add 'live=True' to use the live exchange
con = Geminipy(api_key='hhcHpZ0swQj4eN1zRhca', secret_key='2m5h3ijRob7HParopxCCNEESypmg', live=True)
    
# public request
symbols = con.symbols()
    
# a Requests response is returned.
# So we can access the HTTP reponse code,
# the raw response content, or a json object
#print (symbols.status_code)
#print (symbols.content)
#print (symbols.json())
    
# authenticated request
#order = con.new_order(amount='.0016', price='5531',side='buy')

#trade_history = con.past_trades(symbol='btcusd', limit_trades=50, timestamp=0)
trades = con.trades(symbol="btcusd", since=0, limit_trades=10, include_breaks=0)
#print (order.json())
print(trades.json())
#send a heartbeat
con.heartbeat()
