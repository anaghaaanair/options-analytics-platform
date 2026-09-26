import math
from scipy.stats import norm


def calculate_option(
    stock_price,
    strike_price,
    time_to_expiration,
    volatility,
    risk_free_rate
):
    S = stock_price
    K = strike_price
    T = time_to_expiration
    sigma = volatility
    r = risk_free_rate

    # d1
    d1 = (
        math.log(S / K)
        + (r + sigma**2 / 2) * T
    ) / (
        sigma * math.sqrt(T)
    )

    # d2
    d2 = d1 - sigma * math.sqrt(T)

    # Normal distribution values
    Nd1 = norm.cdf(d1)
    Nd2 = norm.cdf(d2)

    # Option prices
    call_price = (
        S * Nd1
        - K * math.exp(-r * T) * Nd2
    )

    put_price = (
        K * math.exp(-r * T) * norm.cdf(-d2)
        - S * norm.cdf(-d1)
    )

    # Greeks
    call_delta = Nd1
    put_delta = Nd1 - 1

    gamma = norm.pdf(d1) / (
        S * sigma * math.sqrt(T)
    )

    vega = (
        S * norm.pdf(d1) * math.sqrt(T)
    )

    call_theta = (
        -(S * norm.pdf(d1) * sigma)
        / (2 * math.sqrt(T))
        - r * K * math.exp(-r * T) * Nd2
    )

    call_rho = (
        K * T * math.exp(-r * T) * Nd2
    )

    return {
        "call_price": call_price,
        "put_price": put_price,
        "call_delta": call_delta,
        "put_delta": put_delta,
        "gamma": gamma,
        "vega": vega,
        "call_theta": call_theta,
        "call_rho": call_rho
    }