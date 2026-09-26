import plotly.graph_objects as go

# Options Data
K=55
premium=3

# Stock prices at maturity
stock_prices=list(range(20, 101))

#Calculating profit at each stock price
long_call = []
short_call = []
long_put = []
short_put = []

for stock_price in stock_prices:
    call_payoff=max(stock_price-K, 0)
    put_payoff=max(K-stock_price, 0)

    long_call.append(call_payoff-premium)
    short_call.append(premium-call_payoff)
    long_put.append(put_payoff-premium)
    short_put.append(premium-put_payoff)

#Graphing everything out
fig=go.Figure()
fig.add_trace(
    go.Scatter(
        x=stock_prices,
        y=long_call,
        mode="lines",
        name="Long Call Profit"
    )
)
fig.add_trace(
    go.Scatter(
        x=stock_prices,
        y=short_call,
        mode="lines",
        name="Short Call"
    )
)

fig.add_trace(
    go.Scatter(
        x=stock_prices,
        y=long_put,
        mode="lines",
        name="Long Put"
    )
)

fig.add_trace(
    go.Scatter(
        x=stock_prices,
        y=short_put,
        mode="lines",
        name="Short Put"
    )
)

#Add horizontal zero profit line
fig.add_hline(y=0)

#Add vertical strike price line
fig.add_vline(x=K)

#Graph labels
fig.update_layout(
    title="Options Payoff Analyser",
    xaxis_title="Stock Price at Expiration ($)",
    yaxis_title="Profit/Loss ($)",
    hovermode="x unified"
)

fig.show()