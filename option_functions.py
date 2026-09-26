def long_call_payoff(stock_price, strike_price, premium):
    payoff = max(stock_price - strike_price, 0)
    profit = payoff - premium

    return profit
def short_call_payoff(stock_price, strike_price, premium):
    payoff = max(stock_price - strike_price, 0)
    profit = premium - payoff

    return profit
def long_put_payoff(stock_price, strike_price, premium):
    payoff = max(strike_price - stock_price, 0)
    profit = payoff - premium

    return profit
def short_put_payoff(stock_price, strike_price, premium):
    payoff = max(strike_price - stock_price, 0)
    profit = premium - payoff

    return profit
def bull_call_spread(
    stock_price,
    lower_strike,
    higher_strike,
    long_call_premium,
    short_call_premium
):
    long_call = max(stock_price - lower_strike, 0)
    short_call = -max(stock_price - higher_strike, 0)

    net_premium = long_call_premium - short_call_premium

    profit = long_call + short_call - net_premium

    return profit


def bear_put_spread(
    stock_price,
    higher_strike,
    lower_strike,
    long_put_premium,
    short_put_premium
):
    long_put = max(higher_strike - stock_price, 0)
    short_put = -max(lower_strike - stock_price, 0)

    net_premium = long_put_premium - short_put_premium

    profit = long_put + short_put - net_premium

    return profit
def long_straddle(
    stock_price,
    strike,
    call_premium,
    put_premium
):
    call_payoff = max(stock_price - strike, 0)
    put_payoff = max(strike - stock_price, 0)

    total_premium = call_premium + put_premium

    profit = call_payoff + put_payoff - total_premium

    return profit


def long_strangle(
    stock_price,
    put_strike,
    call_strike,
    put_premium,
    call_premium
):
    put_payoff = max(put_strike - stock_price, 0)
    call_payoff = max(stock_price - call_strike, 0)

    total_premium = put_premium + call_premium

    profit = put_payoff + call_payoff - total_premium

    return profit
print("Long Call =", long_call_payoff(60, 55, 3))

print(
    "Bull Call Spread =",
    bull_call_spread(55, 50, 60, 5, 2)
)

print(
    "Long Straddle =",
    long_straddle(55, 55, 3, 4)
)

print(
    "Long Strangle =",
    long_strangle(55, 50, 60, 2, 3)
)
def bull_call_metrics(lower_strike, higher_strike, net_premium):
    max_loss = net_premium
    max_profit = (higher_strike - lower_strike) - net_premium
    breakeven = lower_strike + net_premium

    return max_loss, max_profit, breakeven


def bear_put_metrics(higher_strike, lower_strike, net_premium):
    max_loss = net_premium
    max_profit = (higher_strike - lower_strike) - net_premium
    breakeven = higher_strike - net_premium

    return max_loss, max_profit, breakeven


def straddle_metrics(strike, total_premium):
    max_loss = total_premium
    lower_breakeven = strike - total_premium
    upper_breakeven = strike + total_premium

    return max_loss, lower_breakeven, upper_breakeven


def strangle_metrics(put_strike, call_strike, total_premium):
    max_loss = total_premium
    lower_breakeven = put_strike - total_premium
    upper_breakeven = call_strike + total_premium

    return max_loss, lower_breakeven, upper_breakeven