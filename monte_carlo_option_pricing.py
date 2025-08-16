
import numpy as np
import pandas as pd

def monte_carlo_call(S, K, T, r, sigma, simulations=10000):
    np.random.seed(42)
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(ST - K, 0)
    call_price = np.exp(-r * T) * np.mean(payoffs)
    return round(call_price, 4)

def monte_carlo_put(S, K, T, r, sigma, simulations=10000):
    np.random.seed(42)
    Z = np.random.standard_normal(simulations)
    ST = S * np.exp((r - 0.5 * sigma ** 2) * T + sigma * np.sqrt(T) * Z)
    payoffs = np.maximum(K - ST, 0)
    put_price = np.exp(-r * T) * np.mean(payoffs)
    return round(put_price, 4)

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
                call_price = monte_carlo_call(S, K, T, risk_free_rate, sigma)
                put_price = monte_carlo_put(S, K, T, risk_free_rate, sigma)
                results.append({
                    'Stock_Price': S,
                    'Strike_Price': K,
                    'Time_to_Expiry': T,
                    'Volatility': sigma,
                    'Call_Price': call_price,
                    'Put_Price': put_price
                })

df = pd.DataFrame(results)
df.to_csv('monte_carlo_option_price_table.csv', index=False)
