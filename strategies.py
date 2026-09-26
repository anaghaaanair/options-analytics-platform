import plotly.graph_objects as go
from option_functions import (
    bull_call_spread,
    bear_put_spread,
    long_straddle,
    long_strangle,
    bull_call_metrics,
    bear_put_metrics,
    straddle_metrics,
    strangle_metrics
)

#Bull Call Spread

lower_strike = 50
higher_strike = 60

long_call_premium = 5
short_call_premium = 2

net_premium = long_call_premium - short_call_premium

max_loss, max_profit, breakeven = bull_call_metrics(
    lower_strike,
    higher_strike,
    net_premium
)

print("Bull Call Spread")
print("Maximum Loss =", max_loss)
print("Maximum Profit =", max_profit)
print("Breakeven =", breakeven)


# Stock prices at expiration
stock_prices = list(range(20, 101))

# Calculate profits
bull_call_profits = []

for stock_price in stock_prices:

    profit = bull_call_spread(
        stock_price,
        lower_strike,
        higher_strike,
        long_call_premium,
        short_call_premium
    )

    bull_call_profits.append(profit)


# --------------------------------
# BULL CALL SPREAD GRAPH
# --------------------------------

fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=stock_prices,
        y=bull_call_profits,
        mode="lines",
        name="Bull Call Spread",
        line=dict(width=3),
        hovertemplate="Stock Price: $%{x}<br>Profit / Loss: $%{y:.2f}<extra></extra>"
    )
)

# Breakeven line
fig.add_hline(
    y=0,
    line_width=1,
    line_dash="dash"
)

# Strike price lines
fig.add_vline(
    x=lower_strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Lower Strike: ${lower_strike}"
)

fig.add_vline(
    x=higher_strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Higher Strike: ${higher_strike}"
)

fig.update_layout(
    title="Bull Call Spread — Profit / Loss at Expiration",
    xaxis_title="Stock Price at Expiration ($)",
    yaxis_title="Profit / Loss ($)",
    hovermode="x unified",
    template="plotly_dark",
    height=550,
    margin=dict(l=70, r=40, t=80, b=70)
)

fig.show()

#Long Straddle
strike = 55

call_premium = 3
put_premium = 4

total_premium = call_premium + put_premium

max_loss_straddle, lower_breakeven_straddle, upper_breakeven_straddle = straddle_metrics(
    strike,
    total_premium
)

print("Long Straddle")
print("Maximum Loss =", max_loss_straddle)
print("Lower Breakeven =", lower_breakeven_straddle)
print("Upper Breakeven =", upper_breakeven_straddle)

straddle_profits = []

for stock_price in stock_prices:

    profit = long_straddle(
        stock_price,
        strike,
        call_premium,
        put_premium
    )

    straddle_profits.append(profit)


fig2 = go.Figure()

fig2.add_trace(
    go.Scatter(
        x=stock_prices,
        y=straddle_profits,
        mode="lines",
        name="Long Straddle",
        line=dict(width=3),
        hovertemplate="Stock Price: $%{x}<br>Profit / Loss: $%{y:.2f}<extra></extra>"
    )
)

fig2.add_hline(
    y=0,
    line_width=1,
    line_dash="dash"
)

fig2.add_vline(
    x=strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Strike: ${strike}"
)

fig2.add_vline(
    x=lower_breakeven_straddle,
    line_width=1,
    line_dash="dash",
    annotation_text=f"Lower BE: ${lower_breakeven_straddle}"
)

fig2.add_vline(
    x=upper_breakeven_straddle,
    line_width=1,
    line_dash="dash",
    annotation_text=f"Upper BE: ${upper_breakeven_straddle}"
)

fig2.update_layout(
    title="Long Straddle — Profit / Loss at Expiration",
    xaxis_title="Stock Price at Expiration ($)",
    yaxis_title="Profit / Loss ($)",
    hovermode="x unified",
    template="plotly_dark",
    height=550,
    margin=dict(l=70, r=40, t=80, b=70)
)

fig2.show()

#Bear Put Spread
higher_strike = 60
lower_strike = 50

long_put_premium = 6
short_put_premium = 2

net_premium_bear = long_put_premium - short_put_premium

max_loss_bear, max_profit_bear, breakeven_bear = bear_put_metrics(
    higher_strike,
    lower_strike,
    net_premium_bear
)

print("Bear Put Spread")
print("Maximum Loss =", max_loss_bear)
print("Maximum Profit =", max_profit_bear)
print("Breakeven =", breakeven_bear)

bear_put_profits = []

for stock_price in stock_prices:

    profit = bear_put_spread(
        stock_price,
        higher_strike,
        lower_strike,
        long_put_premium,
        short_put_premium
    )

    bear_put_profits.append(profit)


#Graphing everything out

fig3 = go.Figure()

fig3.add_trace(
    go.Scatter(
        x=stock_prices,
        y=bear_put_profits,
        mode="lines",
        name="Bear Put Spread",
        line=dict(width=3),
        hovertemplate="Stock Price: $%{x}<br>Profit / Loss: $%{y:.2f}<extra></extra>"
    )
)

fig3.add_hline(
    y=0,
    line_width=1,
    line_dash="dash"
)

fig3.add_vline(
    x=lower_strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Lower Strike: ${lower_strike}"
)

fig3.add_vline(
    x=higher_strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Higher Strike: ${higher_strike}"
)

fig3.add_vline(
    x=breakeven_bear,
    line_width=1,
    line_dash="dash",
    annotation_text=f"Breakeven: ${breakeven_bear}"
)

fig3.update_layout(
    title="Bear Put Spread — Profit / Loss at Expiration",
    xaxis_title="Stock Price at Expiration ($)",
    yaxis_title="Profit / Loss ($)",
    hovermode="x unified",
    template="plotly_dark",
    height=550,
    margin=dict(l=70, r=40, t=80, b=70)
)

fig3.show()

#Long Strangle
put_strike = 50
call_strike = 60

strangle_put_premium = 2
strangle_call_premium = 3

total_strangle_premium = (
    strangle_put_premium
    + strangle_call_premium
)

max_loss_strangle, lower_breakeven_strangle, upper_breakeven_strangle = strangle_metrics(
    put_strike,
    call_strike,
    total_strangle_premium
)

print("Long Strangle")
print("Maximum Loss =", max_loss_strangle)
print("Lower Breakeven =", lower_breakeven_strangle)
print("Upper Breakeven =", upper_breakeven_strangle)
strangle_profits = []

for stock_price in stock_prices:

    profit = long_strangle(
        stock_price,
        put_strike,
        call_strike,
        strangle_put_premium,
        strangle_call_premium
    )

    strangle_profits.append(profit)


#Graphing everything out

fig4 = go.Figure()

fig4.add_trace(
    go.Scatter(
        x=stock_prices,
        y=strangle_profits,
        mode="lines",
        name="Long Strangle",
        line=dict(width=3),
        hovertemplate="Stock Price: $%{x}<br>Profit / Loss: $%{y:.2f}<extra></extra>"
    )
)

fig4.add_hline(
    y=0,
    line_width=1,
    line_dash="dash"
)

fig4.add_vline(
    x=put_strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Put Strike: ${put_strike}"
)

fig4.add_vline(
    x=call_strike,
    line_width=1,
    line_dash="dot",
    annotation_text=f"Call Strike: ${call_strike}"
)

fig4.add_vline(
    x=lower_breakeven_strangle,
    line_width=1,
    line_dash="dash",
    annotation_text=f"Lower BE: ${lower_breakeven_strangle}"
)

fig4.add_vline(
    x=upper_breakeven_strangle,
    line_width=1,
    line_dash="dash",
    annotation_text=f"Upper BE: ${upper_breakeven_strangle}"
)

fig4.update_layout(
    title="Long Strangle — Profit / Loss at Expiration",
    xaxis_title="Stock Price at Expiration ($)",
    yaxis_title="Profit / Loss ($)",
    hovermode="x unified",
    template="plotly_dark",
    height=550,
    margin=dict(l=70, r=40, t=80, b=70)
)

fig4.show()