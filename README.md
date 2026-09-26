# Options Analytics Platform

An interactive quantitative finance platform for Black-Scholes option pricing, Greeks analysis, and options strategy payoff visualization.

## Overview

This project combines financial mathematics with an interactive web application to analyze options using the Black-Scholes model.

Users can enter key market assumptions and calculate option prices and risk sensitivities, while also exploring the profit and loss profiles of common options strategies.

## Features

### Black-Scholes Option Pricing

- European Call Option Pricing
- European Put Option Pricing
- Black-Scholes model implementation

### Option Greeks

- Delta
- Gamma
- Vega
- Theta
- Rho

### Options Strategy Analysis

Interactive payoff visualizations for:

- Bull Call Spread
- Bear Put Spread
- Long Straddle
- Long Strangle

### Interactive Web Application

The platform includes:

- FastAPI backend
- JavaScript frontend
- Plotly interactive visualizations
- REST API endpoints
- Interactive option calculator

## Technology Stack

- Python
- FastAPI
- NumPy
- SciPy
- Plotly
- JavaScript
- HTML
- CSS

## Project Structure

```text
Options-analytics-platform/
│
├── black_scholes.py
├── option_api.py
├── option_functions.py
├── payoffs.py
├── strategies.py
├── main.py
│
├── static/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── README.md