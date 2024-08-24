import numpy as np
from scipy.stats import norm
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import io
import base64


def compute_c(curr_price, time_to_expiry, K, r, volatility, option_type="call"):
    """
    The Black-Scholes model is a mathematical model used to price European call and put options. It was developed by Fischer Black, Myron Scholes, and Robert Merton in 1973.

    The Black-Scholes model assumes that the underlying asset follows a geometric Brownian motion, which means that its price at any given time t is determined by its current price P_t, the risk-free interest rate r, the volatility σ, and the time to maturity T - t.

    The model can be used to price European call and put options with continuously compounded interest rates and dividends. The Black-Scholes formula provides the Black-Scholes option price as a function of the underlying asset's price, strike price, risk-free interest rate, volatility, and time to maturity.

    Args:
        S (float): The current price of the underlying asset.
        K (float): The strike price of the option.
        r (float): The risk-free interest rate (in decimal form).
        volatility (float): The volatility of the underlying asset (in decimal form).
        time_to_expiry (float): The time to maturity of the option (in years).
        option_type (str): The type of option ('call' or 'put').

    Returns:
        float: The Black-Scholes option price.
    """

    if time_to_expiry == 0:
        return max(0, curr_price - K) if option_type == 'call' else max(0, K - curr_price)

    d1 = (np.log(curr_price / K) + (r + volatility**2 / 2) *
          time_to_expiry) / (volatility * np.sqrt(time_to_expiry))
    d2 = d1 - volatility * np.sqrt(time_to_expiry)

    if option_type == "call":
        price = curr_price * norm.cdf(d1) - K * \
            np.exp(-r * time_to_expiry) * norm.cdf(d2)
    elif option_type == "put":
        price = K * np.exp(-r * time_to_expiry) * \
            norm.cdf(-d2) - curr_price * norm.cdf(-d1)
    else:
        raise ValueError("Invalid option type. Please use 'call' or 'put'.")

    return price


def bs_dataframe(K, r, volatility, option_type="call"):
    """
    Generate a dataframe with option prices computed using the Black-Scholes model for different combinations of time_to_maturity and stock_prices.

    Args:
        K (float): The strike price of the option.
        r (float): The risk-free interest rate (in decimal form).
        volatility (float): The volatility of the underlying asset (in decimal form).
        option_type (str): The type of option ('call' or 'put').

    Returns:
        option_prices: A dataframe with option prices for different combinations of time_to_maturity and stock_prices.
    """
    # creating a placeholder dataframe
    time_to_maturity = np.linspace(0, 1, 10)
    time_to_maturity = np.round(time_to_maturity, decimals=2)

    stock_prices = np.linspace(0.5 * K, 1.5 * K, 10)
    stock_prices = np.round(stock_prices, decimals=2)

    option_prices = pd.DataFrame(
        np.nan, index=time_to_maturity, columns=stock_prices)

    # computing option prices for each combination of time_to_maturity and stock_prices

    for S in option_prices.columns:
        for T in option_prices.index:
            option_prices.at[T, S] = compute_c(
                S, T, K, r, volatility, option_type)

    # for col in option_prices.columns:
    #     option_prices.apply(lambda x: compute_c(col, x, K, r, volatility, option_type))

    # option_prices = option_prices.applymap(lambda _: compute_c(
    #     option_prices.columns[_], option_prices.index[_], K, r, volatility, option_type))
    return option_prices


def heatmap_gen(K, r, sigma, type):
    """
    Plots a heatmap of option prices

    Args:
    df (pd.DataFrame): The dataframe containing option prices.
    type (str): The type of option ('CALL' or 'PUT').
    """
    if type != 'call' and type != 'put':
        raise ValueError("Invalid option type. Please use 'call' or 'put'.")

    df = bs_dataframe(K, r, sigma, type)
    fig, ax = plt.subplots(figsize=(12, 8))
    fig.patch.set_facecolor('#201d1d')

    # Create the heatmap
    sns.heatmap(df,
                cmap='viridis',
                annot=True,  # true for values in each cell
                cbar=False,  # get tid of color bar
                ax=ax)

    # Set title and labels
    ax.set_facecolor('#201d1d')
    ax.set_xlabel('Stock Price', fontsize=12, color='white')
    ax.set_ylabel('Time to Maturity', fontsize=12, color='white')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=0,
                       ha='right', color='white')
    ax.set_yticklabels(ax.get_yticklabels(), rotation=0, color='white')

    # Instead of displaying, save to BytesIO
    img = io.BytesIO()
    fig.savefig(img, format='png', bbox_inches='tight')
    plt.close(fig)  # Close the figure to free up memory
    img.seek(0)
    return base64.b64encode(img.getvalue()).decode('utf8')
