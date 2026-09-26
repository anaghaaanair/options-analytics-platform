async function calculateOption() {

    const stockPrice = parseFloat(
        document.getElementById("stockPrice").value
    );

    const strikePrice = parseFloat(
        document.getElementById("strikePrice").value
    );

    const timeToExpiration = parseFloat(
        document.getElementById("timeToExpiration").value
    );

    const volatility = parseFloat(
        document.getElementById("volatility").value
    );

    const riskFreeRate = parseFloat(
        document.getElementById("riskFreeRate").value
    );


    const response = await fetch("/calculate-option", {

        method: "POST",

        headers: {
            "Content-Type": "application/json"
        },

        body: JSON.stringify({

            stock_price: stockPrice,
            strike_price: strikePrice,
            time_to_expiration: timeToExpiration,
            volatility: volatility,
            risk_free_rate: riskFreeRate

        })
    });


    const data = await response.json();


    document.getElementById("callPrice").textContent =
        "$" + data.call_price.toFixed(4);

    document.getElementById("putPrice").textContent =
        "$" + data.put_price.toFixed(4);

    document.getElementById("callDelta").textContent =
        data.call_delta.toFixed(4);

    document.getElementById("putDelta").textContent =
        data.put_delta.toFixed(4);

    document.getElementById("gamma").textContent =
        data.gamma.toFixed(4);

    document.getElementById("vega").textContent =
        data.vega.toFixed(4);

    document.getElementById("callTheta").textContent =
        data.call_theta.toFixed(4);

    document.getElementById("callRho").textContent =
        data.call_rho.toFixed(4);
}
async function loadStrategyGraphs() {

    const response = await fetch("/strategy-data");

    const data = await response.json();

    const stockPrices = data.stock_prices;


    // --------------------------------
    // BULL CALL SPREAD
    // --------------------------------

    Plotly.newPlot(
        "bullCallGraph",
        [
            {
                x: stockPrices,
                y: data.bull_call.profits,
                mode: "lines",
                name: "Bull Call Spread",
                line: {
                    width: 3
                }
            }
        ],
        {
            title: "Bull Call Spread — Profit / Loss at Expiration",

            xaxis: {
                title: "Stock Price at Expiration ($)"
            },

            yaxis: {
                title: "Profit / Loss ($)"
            },

            template: "plotly_dark",

            hovermode: "x unified",

            shapes: [
                {
                    type: "line",
                    x0: 0,
                    x1: 1,
                    y0: 0,
                    y1: 0,
                    xref: "paper",
                    line: {
                        dash: "dash"
                    }
                }
            ]
        }
    );


    // --------------------------------
    // BEAR PUT SPREAD
    // --------------------------------

    Plotly.newPlot(
        "bearPutGraph",
        [
            {
                x: stockPrices,
                y: data.bear_put.profits,
                mode: "lines",
                name: "Bear Put Spread",
                line: {
                    width: 3
                }
            }
        ],
        {
            title: "Bear Put Spread — Profit / Loss at Expiration",

            xaxis: {
                title: "Stock Price at Expiration ($)"
            },

            yaxis: {
                title: "Profit / Loss ($)"
            },

            template: "plotly_dark",

            hovermode: "x unified"
        }
    );


    // --------------------------------
    // LONG STRADDLE
    // --------------------------------

    Plotly.newPlot(
        "straddleGraph",
        [
            {
                x: stockPrices,
                y: data.straddle.profits,
                mode: "lines",
                name: "Long Straddle",
                line: {
                    width: 3
                }
            }
        ],
        {
            title: "Long Straddle — Profit / Loss at Expiration",

            xaxis: {
                title: "Stock Price at Expiration ($)"
            },

            yaxis: {
                title: "Profit / Loss ($)"
            },

            template: "plotly_dark",

            hovermode: "x unified"
        }
    );


    // --------------------------------
    // LONG STRANGLE
    // --------------------------------

    Plotly.newPlot(
        "strangleGraph",
        [
            {
                x: stockPrices,
                y: data.strangle.profits,
                mode: "lines",
                name: "Long Strangle",
                line: {
                    width: 3
                }
            }
        ],
        {
            title: "Long Strangle — Profit / Loss at Expiration",

            xaxis: {
                title: "Stock Price at Expiration ($)"
            },

            yaxis: {
                title: "Profit / Loss ($)"
            },

            template: "plotly_dark",

            hovermode: "x unified"
        }
    );
}


// Load graphs when the website opens
loadStrategyGraphs().catch(error => {
    console.error("Error loading strategy graphs:", error);
});