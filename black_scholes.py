
import numpy as np
from scipy.stats import norm
import pandas as pd

def black_scholes_call(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    call = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    return call

def black_scholes_put(S, K, T, r, sigma):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)
    put = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return put

stock_prices = [90, 100, 110]
strike_prices = [100]
time_to_expiry = [0.25, 0.5, 1.0]
risk_free_rate = 0.05
volatilities = [0.1, 0.2, 0.3]

results = []
for S in stock_prices:
    for K in strike_prices:
        for T in time_to_expiry:
            for sigma in volatilities:
                call_price = black_scholes_call(S, K, T, risk_free_rate, sigma)
                put_price = black_scholes_put(S, K, T, risk_free_rate, sigma)
                results.append({
                    'Stock_Price': S,
                    'Strike_Price': K,
                    'Time_to_Expiry': T,
                    'Volatility': sigma,
                    'Call_Price': round(call_price, 4),
                    'Put_Price': round(put_price, 4)
                })

df = pd.DataFrame(results)
df.to_csv('option_price_table.csv', index=False)
