from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from options_api import calculate_option
from option_functions import (
    bull_call_spread,
    bear_put_spread,
    long_straddle,
    long_strangle
)

app = FastAPI(
    title="Options Analytics Platform",
    description="An interactive quantitative finance platform for options pricing, risk analysis, payoff visualization, and strategy evaluation.",
    version="1.0"
)

app.mount("/static", StaticFiles(directory="static"), name="static")

class OptionInput(BaseModel):
    stock_price: float
    strike_price: float
    time_to_expiration: float
    volatility: float
    risk_free_rate: float


@app.get("/")
def home():
    return FileResponse("static/index.html")


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.post("/calculate-option")
def calculate_option_endpoint(option: OptionInput):

    results = calculate_option(
        option.stock_price,
        option.strike_price,
        option.time_to_expiration,
        option.volatility,
        option.risk_free_rate
    )

    return results

@app.get("/strategy-data")
def strategy_data():

    stock_prices = list(range(20, 101))

    # -----------------------------
    # BULL CALL SPREAD
    # -----------------------------

    lower_strike = 50
    higher_strike = 60

    long_call_premium = 5
    short_call_premium = 2

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


    # -----------------------------
    # BEAR PUT SPREAD
    # -----------------------------

    higher_strike_bear = 60
    lower_strike_bear = 50

    long_put_premium = 6
    short_put_premium = 2

    bear_put_profits = []

    for stock_price in stock_prices:
        profit = bear_put_spread(
            stock_price,
            higher_strike_bear,
            lower_strike_bear,
            long_put_premium,
            short_put_premium
        )

        bear_put_profits.append(profit)


    # -----------------------------
    # LONG STRADDLE
    # -----------------------------

    straddle_strike = 55

    call_premium = 3
    put_premium = 4

    straddle_profits = []

    for stock_price in stock_prices:
        profit = long_straddle(
            stock_price,
            straddle_strike,
            call_premium,
            put_premium
        )

        straddle_profits.append(profit)


    # -----------------------------
    # LONG STRANGLE
    # -----------------------------

    put_strike = 50
    call_strike = 60

    strangle_put_premium = 2
    strangle_call_premium = 3

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


    return {
        "stock_prices": stock_prices,

        "bull_call": {
            "profits": bull_call_profits,
            "lower_strike": lower_strike,
            "higher_strike": higher_strike
        },

        "bear_put": {
            "profits": bear_put_profits,
            "lower_strike": lower_strike_bear,
            "higher_strike": higher_strike_bear,
            "breakeven": 56
        },

        "straddle": {
            "profits": straddle_profits,
            "strike": straddle_strike,
            "lower_breakeven": 48,
            "upper_breakeven": 62
        },

        "strangle": {
            "profits": strangle_profits,
            "put_strike": put_strike,
            "call_strike": call_strike,
            "lower_breakeven": 45,
            "upper_breakeven": 65
        }
    }