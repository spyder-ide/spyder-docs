#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Financial Data Analysis with Spyder

Created on Thu May 20 10:17:27 2021

@author: Spyder Team
"""


# %% Import libraries
import numpy as np
import pandas as pd
import matplotlib as mpl
from scipy.optimize import minimize
import matplotlib.pyplot as plt
import pprint

from Historic_Crypto import Cryptocurrencies
from Historic_Crypto import HistoricalData
import yfinance as yf



# %% Detailed stock information
netflix = yf.Ticker("NFLX")
netflix_info = netflix.info
pprint.pprint(netflix_info)


# %%% Show major holders
print(netflix.major_holders)


# %%% Show institutional holders
print(netflix.institutional_holders)


# %%% Get historical market data
hist = netflix.history(period="max")
print(hist)


# %% Set general style of plotting
plt.style.use("fivethirtyeight")
mpl.rcParams["savefig.dpi"] = 300
mpl.rcParams["font.family"] = "serif"
np.set_printoptions(precision=5, suppress=True,
                    formatter={"float": lambda x: f"{x:6.3f}"})



# ---- PORTFOLIO 1
# %% Portfolio 1 (Google, Apple, Microsoft, Netflix, Amazon)

# %%% Download finance data
SYMBOLS_1 = ["GOOG", "AAPL", "MSFT", "NFLX", "AMZN"]

data_1 = yf.download(" ".join(SYMBOLS_1), start="2012-01-01",
                     end="2021-01-01", group_by="Ticker")


# %% Format downloaded data
data_1 = data_1.stack(level=1).rename_axis(
    ["Date", "Ticker"]).reset_index(level=1)

close_data_1 = data_1[data_1.Ticker == "Close"].drop(
    "Ticker", inplace=False, axis=1)


# %% Monthly data
monthly_data_1 = close_data_1.resample("M").ffill().pct_change()


# %%% Mean and stadard deviation
print(monthly_data_1.mean())
print(monthly_data_1.std())


# %% Plot daily timeline
(close_data_1/ close_data_1.iloc[0]).plot(figsize=(16, 10), title="Portfolio 1 daily stock growth")


# %% Plot monthly timeline
(monthly_data_1 + 1).cumprod().plot(figsize=(16, 10), title="Portfolio 1 monthly stock growth")


# %% Returns per day
rets_1 = np.log(close_data_1/close_data_1.shift(1)).dropna()
weights_1 = [0.2, 0.2, 0.2, 0.2, 0.2]


# %% Portfolio returns
def portfolio_return(returns, weights):
    return np.dot(returns.mean(), weights) * 252

print(portfolio_return(rets_1, weights_1))


# %% Portfolio volatility
def portfolio_volatility(returns, weights):
    return np.dot(weights, np.dot(returns.cov() * 252, weights)) ** 0.5

print(portfolio_volatility(rets_1, weights_1))


# %% Portfolio Sharpe ratio
def portfolio_sharpe(returns, weights):
    return portfolio_return(returns, weights) / portfolio_volatility(returns, weights)

print(portfolio_sharpe(rets_1, weights_1))


# %% Sharpe ratio with Monte Carlo simulation
def monte_carlo_sharpe(returns, symbols, weights):

    sim_weights = np.random.random((1000, len(symbols)))
    sim_weights = (sim_weights.T / sim_weights.sum(axis=1)).T

    volat_ret = [(portfolio_volatility(returns[symbols], weights),
                  portfolio_return(returns[symbols], weights))
                 for weights in sim_weights]
    volat_ret = np.array(volat_ret)

    sharpe_ratio = volat_ret[:, 1] / volat_ret[:, 0]

    return volat_ret, sharpe_ratio

port_1_vr, port_1_sr = monte_carlo_sharpe(rets_1, SYMBOLS_1, weights_1)


# %%% Plot Sharpe scatter plot with color mapping
plt.figure(figsize=(16, 10))
fig = plt.scatter(port_1_vr[:, 0], port_1_vr[:, 1],
                  c=port_1_sr, cmap="cool")
CB = plt.colorbar(fig)
CB.set_label("Sharpe ratio")
plt.xlabel("expected volatility")
plt.ylabel("expected return")
plt.title(" | ".join(SYMBOLS_1))


# %% Optimal weights
start_year, end_year = (2012, 2020)

def optimal_weights(returns, symbols, actual_weights, start_y, end_y):

    bounds = len(symbols) * [(0, 1), ]
    constraints = {"type": "eq", "fun": lambda weights: weights.sum() - 1}
    opt_weights = {}

    for year in range(start_y, end_y):
        _rets = returns[symbols].loc[f"{year}-01-01":f"{year}-12-31"]
        _opt_w = minimize(lambda weights: -portfolio_sharpe(_rets, weights),
                      actual_weights,
                      bounds=bounds,
                      constraints=constraints)["x"]
        opt_weights[year] = _opt_w
    return opt_weights

opt_weights_1 = optimal_weights(rets_1, SYMBOLS_1, weights_1, start_year, end_year)
port_1_ow = pd.DataFrame.from_dict(opt_weights_1, orient='index')
port_1_ow.columns = SYMBOLS_1


# %% Expected and realized returns
def exp_real_rets(returns, opt_weights, symbols, start_year, end_year):

    _rets = {}
    for year in range(start_year, end_year):
        prev_year = returns[symbols].loc[f"{year}-01-01":f"{year}-12-31"]
        current_year = returns[symbols].loc[f"{year + 1}-01-01":f"{year + 1}-12-31"]
        expected_pr = portfolio_return(prev_year, opt_weights[year])
        realized_pr = portfolio_return(current_year, opt_weights[year])
        _rets[year + 1] = [expected_pr, realized_pr]

    return _rets


port_1_exp_real = pd.DataFrame.from_dict(
    exp_real_rets(rets_1, opt_weights_1, SYMBOLS_1, start_year, end_year),
    orient='index')
port_1_exp_real.columns = ["expected", "realized"]


# %%% Plot expected and realized returns
port_1_exp_real.plot(kind="bar", figsize=(16, 10),title="Expected vs. realized portfolio returns")


# %%% Mean and standard deviation
print(port_1_exp_real.mean())
print(port_1_exp_real[["expected", "realized"]].corr())


# ---- PORTFOLIO 2
# %% Portfolio 2 (Pfizer, Astra Zeneca, Johnson N Johnson)


# %%% Download finance data
SYMBOLS_2 = ["PFE", "AZN", "JNJ"]  # Pfizer, Astra Zeneca, Johnson N Johnson

data_2 = yf.download(" ".join(SYMBOLS_2), start="2012-01-01",
                     end="2021-01-01", group_by="Ticker")


# %% Format downloaded data
data_2 = data_2.stack(level=1).rename_axis(
    ["Date", "Ticker"]).reset_index(level=1)

close_data_2 = data_2[data_2.Ticker == "Close"].drop(
    "Ticker", inplace=False, axis=1)


# %% Monthly data
monthly_data_2 = close_data_2.resample("M").ffill().pct_change()


# %%% Mean and standard deviation
print("Mean:")
print(monthly_data_2.mean())
print("STD:")
print(monthly_data_2.std())


# %% Plot daily timeline
rets_2 = np.log(close_data_2[SYMBOLS_2] /
                close_data_2[SYMBOLS_2].shift(1)).dropna()

(close_data_2[SYMBOLS_2] /
 close_data_2[SYMBOLS_2].iloc[0]).plot(figsize=(16, 10),
                                       title="Portfolio 2 daily stock growth")


# %% Plot monthly timeline
(monthly_data_2 + 1).cumprod().plot(figsize=(16, 10),
                                    title="Portfolio 2 monthly stock grouth")


# %% Returns per day
weights_2 = len(close_data_2.columns) * [1 / len(close_data_2.columns)]

# %% Portfolio returns
print(f"Portfolio 2 returns: {portfolio_return(rets_2, weights_2):.4f}")


# %% Portfolio volatility
print(f"Portfolio 2 volatility: {portfolio_volatility(rets_2, weights_2):.4f}")


# %% Portfolio Sharpe ratio
print(f"Portfolio 2 Sharpe: {portfolio_sharpe(rets_2, weights_2):.4f}")


# %% Sharpe ratio with Monte Carlo simulation
port_2_vr, port_2_sr = monte_carlo_sharpe(rets_2, SYMBOLS_2, weights_2)


# %%% Plot scatter plot with color mapping
plt.figure(figsize=(16, 10))
fig = plt.scatter(port_2_vr[:, 0], port_2_vr[:, 1],
                  c=port_2_sr, cmap="cool")
CB = plt.colorbar(fig)
CB.set_label("Sharpe ratio")
plt.xlabel("expected volatility")
plt.ylabel("expected return")
plt.title(" | ".join(SYMBOLS_2))


# %% Optimal weights
start_year, end_year = (2012, 2020)

opt_weights_2 = optimal_weights(
    rets_2, SYMBOLS_2, weights_2, start_year, end_year)

port_2_ow = pd.DataFrame.from_dict(opt_weights_2, orient='index')
port_2_ow.columns = SYMBOLS_2


# %% Expected and realized returns
port_2_exp_real = pd.DataFrame.from_dict(
    exp_real_rets(rets_2, opt_weights_2, SYMBOLS_2, start_year, end_year),
    orient='index')
port_2_exp_real.columns = ["expected", "realized"]


# %%% Plot expected and realized returns
port_2_exp_real.plot(kind="bar", figsize=(16, 10),title="Expected vs. realized portfolio returns")


# %%% Mean and standard deviation
print("Expected and realized means:")
print(port_2_exp_real.mean())
print("Expected and realized correlations:")
print(port_2_exp_real[["expected", "realized"]].corr())


# ---- PORTFOLIO 3
# %% Portfolio 3 (ETH, BTC, LTC))

crypto_list = Cryptocurrencies(
    coin_search="", extended_output=True).find_crypto_pairs()
print(crypto_list.loc[crypto_list.base_currency == "ETH"])


# %%% Download and format ETC data
ETC_HIST = HistoricalData(
    "ETH-USD", 3600 * 24, "2016-01-01-00-00",
    "2021-01-01-00-00").retrieve_data()
ETC_HIST.rename(columns={"close": "ETC"}, inplace=True)
ETC_HIST.drop(["low", "high", "open", "volume"], axis=1, inplace=True)


# %%% Download and format BTC data
BTC_HIST = HistoricalData(
    "BTC-USD", 3600 * 24, "2016-01-01-00-00",
    "2021-01-01-00-00").retrieve_data()
BTC_HIST.rename(columns={"close": "BTC"}, inplace=True)
BTC_HIST.drop(["low", "high", "open", "volume"], axis=1, inplace=True)


# %%% Download and format LTC data
LTC_HIST = HistoricalData(
    "LTC-USD", 3600 * 24, "2016-01-01-00-00",
    "2021-01-01-00-00").retrieve_data()
LTC_HIST.rename(columns={"close": "LTC"}, inplace=True)
LTC_HIST.drop(["low", "high", "open", "volume"], axis=1, inplace=True)


# %% Merge data form BTC, LTC and ETC
crypto_hist = pd.merge(BTC_HIST, ETC_HIST, on=["time"])
crypto_hist = pd.merge(crypto_hist, LTC_HIST, on=["time"])
crypto_hist.set_index("time")

# %%% Crypto Ticker Symbols
SYMBOLS_3 = ["BTC", "ETC", "LTC"]


#%%% Plot monthly timeline
monthly_data_3 = crypto_hist.resample("M").ffill().pct_change()
(monthly_data_3 + 1).cumprod().plot(figsize=(16, 10), title="Portfolio 3 monthly stock growth")


# %% Returns per day
rets_3 = np.log(crypto_hist[SYMBOLS_3] /
                crypto_hist[SYMBOLS_3].shift(1)).dropna()


# %% Weights
weights_3 = len(crypto_hist.columns) * [1 / len(crypto_hist.columns)]


# %% Portfolio retunrs
print(portfolio_return(rets_3, weights_3))


# %% Portfolio volatility
print((portfolio_volatility(rets_3, weights_3)))


# %% Portfolio Sharpe ratio
print(portfolio_sharpe(rets_3, weights_3))


# %% Sharpe ratio with Monte Carlo simulation
port_3_vr, port_3_sr = monte_carlo_sharpe(rets_3, SYMBOLS_3, weights_3)


# %%% Plot scatter plot with color mapping
plt.figure(figsize=(16, 10))
fig = plt.scatter(port_3_vr[:, 0], port_3_vr[:, 1],
                  c=port_3_sr, cmap="cool")
CB = plt.colorbar(fig)
CB.set_label("Sharpe ratio")
plt.xlabel("expected volatility")
plt.ylabel("expected return")
plt.title(" | ".join(SYMBOLS_3))


# %% Optimal weights
start_year, end_year = (2016, 2021)

opt_weights_3 = optimal_weights(
    rets_3, SYMBOLS_3, weights_3, start_year, end_year)

port_3_ow = pd.DataFrame.from_dict(opt_weights_3, orient='index')
port_3_ow.columns = SYMBOLS_3


# %% Expected and realized returns
start_year, end_year = (2016, 2020)

port_3_exp_real = pd.DataFrame.from_dict(
    exp_real_rets(rets_3, opt_weights_3, SYMBOLS_3, start_year, end_year),
    orient='index')
port_3_exp_real.columns = ["expected", "realized"]


# %%% Plot expected and realized returns
port_3_exp_real.plot(kind="bar", figsize=(16, 10),title="Expected vs. realized portfolio returns")


# %%% Mean and standard deviation
print(port_3_exp_real.mean())
print(port_3_exp_real[["expected", "realized"]].corr())
