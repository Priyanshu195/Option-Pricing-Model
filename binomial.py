import numpy as np
import pandas as pd

def binomial_option_price(S, K, T, r, sigma, steps, option_type='call'):
    dt = T / steps  # time step size
    u = np.exp(sigma * np.sqrt(dt))  # up factor
    d = 1 / u                       # down factor
    p = (np.exp(r * dt) - d) / (u - d)  # risk-neutral probability
    
    # Asset prices at maturity
    asset_prices = np.array([S * (u ** j) * (d ** (steps - j)) for j in range(steps + 1)])
    
    # Option values at maturity
    if option_type == 'call':
        option_values = np.maximum(asset_prices - K, 0)
    else:
        option_values = np.maximum(K - asset_prices, 0)
    
    # Step backwards through the tree to present value
    for i in range(steps - 1, -1, -1):
        option_values = np.exp(-r * dt) * (p * option_values[1:i+2] + (1 - p) * option_values[0:i+1])
    
    return round(option_values[0], 4)

# Input Parameters
stock_prices = [90, 100, 110]
strike_prices = 
time_to_expiry = [0.25, 0.5, 1.0]  # in years
risk_free_rate = 0.05
volatilities = [0.1, 0.2, 0.3]
steps = 50  # number of binomial steps

# Compute option prices for all combinations
results = []
for S in stock_prices:
    for K in strike_prices:
        for T in time_to_expiry:
            for sigma in volatilities:
                call_price = binomial_option_price(S, K, T, risk_free_rate, sigma, steps, 'call')
                put_price = binomial_option_price(S, K, T, risk_free_rate, sigma, steps, 'put')
                results.append({
                    'Stock_Price': S,
                    'Strike_Price': K,
                    'Time_to_Expiry': T,
                    'Volatility': sigma,
                    'Call_Price': call_price,
                    'Put_Price': put_price
                })

# Save pricing results to CSV
df = pd.DataFrame(results)
df.to_csv('binomial_option_price_table.csv', index=False)
