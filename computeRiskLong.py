from datetime import datetime
import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import yfinance as yf
import random
from scipy import stats
import time

accuracy_tolerance = 0.005

# -----------------------------------#
# User sets parameter values here
# scalars, unless otherwise noted

issue = 'spy'
data_source = 'yahoo'
start_time = datetime(1999,1,1)
end_date = datetime(2012,1,1)

hold_days = 5
system_accuracy = .65
DD95_limit = 0.20
initial_equity = 1_00_000.0
fraction = 1.00
forecast_horizon = 504 # trading days in two years
number_forecasts = 10 # number of simulated forecasts

print('\n\n\tNew simulation run ')
print('\tTesting profit potential for long positions\n ')
print(f'Issue:\t\t\t{issue}')
print(f'Dates:\t\t\t{start_time.strftime("%d %b %Y")}')
print(f' to:\t\t\t{end_date.strftime("%d %b %Y")}')
print(f'Hold days:\t\t{hold_days}')
print(f'System Accuracy:\t{system_accuracy:.2f}')
print(f'DD 95 limit:\t\t{DD95_limit:.2f}')
print(f'Forecast Horizon:\t{forecast_horizon}')
print(f'Number forecasts:\t{number_forecasts}')
print(f'Initial Equity:\t\t{initial_equity}')

# -------------------------------------------#
# Variables used for simulation

qt = yf.download(tickers= issue, start= start_time, end= end_date, interval='1d', progress= False)

# print(qt.shape)
# print(qt.head())


nrows = qt.shape[0]
print(f'Number of rows:\t\t{nrows}')

qtC = qt.Close

number_trades = math.floor(forecast_horizon / hold_days) # must be integer 
number_days = math.floor(number_trades * hold_days) # must be integer

print(f'Number of days: \t{number_days}')
print(f'Number of trades:\t{number_trades}')


a1 = int(number_days + 1)
# these arrays are the number of days in the forecast
account_balance = np.zeros(a1) #account balance

pltx = np.zeros(a1)
plty = np.zeros(a1)

max_IT_DD = np.zeros(a1) # maximum intra-trade drawdown
max_IT_eq = np.zeros(a1) # maximum intra-trade equity

# These arrays are the number of simulation runs
# Max intra-trade drawdown

FC_max_IT_DD = np.zeros(number_forecasts)

# Trade equity (TWR)
FC_tr_eq = np.zeros(number_forecasts)

# ----------------------------------------
# Set up gainer and loser list

gainer = np.zeros(nrows)
loser = np.zeros(nrows)
i_gainer = 0
i_loser = 0

for i in range(0, nrows-hold_days):
    if qtC.iloc[i+hold_days]> qtC.iloc[i]:
        gainer[i_gainer] = i
        i_gainer = i_gainer + 1
    else:
        loser[i_loser] = i
        i_loser = i_loser + 1

number_gainers = i_gainer
number_losers = i_loser

print(f'Number Gainers:\t\t{number_gainers}')
print(f'Number Losers:\t\t{number_losers}')

#################################################
# Solve for fraction
fraction = 1.00
done = False

while not done:
    done = True
    print(f'Using fraction:\t\t{fraction:.3f}')
    # ---------------------------------
    # Beginning a new forecast run
    for i_forecast in range(number_forecasts):
    # Initialize for trade sequence
        i_day = 0 # i_day counts to end of forecast
        # Daily arrays, so running history can be plotted
        # starting account balance
        account_balance[0] = initial_equity
        # Maximum intra-trade equity
        max_IT_eq[0] = account_balance[0]
        max_IT_DD[0] = 0

        # for each trade
        for i_trade in range(0, number_trades):
            # select the trade and retrieve its index
            # into the price array
            # gainer of loser?
            # Uniform for win/loss
            gainer_loser_random = np.random.random()
            # pick a trade accordingly
            # for a long positions, test is "<"
            # for a short positions, test is ">"
            if gainer_loser_random < system_accuracy:
                # choose a gaining trade
                gainer_index = np.random.randint(0, number_gainers + 1)
                entry_index = gainer[gainer_index]
            else:
                # choose a losing trade
                loser_index = np.random.randint(0, number_losers + 1)
                entry_index = loser[loser_index]

            # process the trade, day by day
            for i_day_in_trade in range(0, hold_days+1):
                if i_day_in_trade==0:
                    # Things that happen immediately
                    # after the close of the signal day
                    # Initialize for the trade
                    buy_price = qtC.iloc[math.floor(entry_index)]
                    number_shares = account_balance[i_day] * fraction / buy_price
                    share_dollars = number_shares * buy_price
                    cash = account_balance[i_day] - share_dollars
                else:
                    # Things that change during a
                    # day the trade is held
                    i_day = i_day + 1
                    j = entry_index + i_day_in_trade
                    # Drawdown for the trade
                    profit = number_shares * (qtC.iloc[math.floor(j)]- buy_price)
                    MTM_equity = cash + share_dollars + profit
                    IT_DD = (max_IT_eq[i_day-1] - MTM_equity) / max_IT_eq[i_day-1]
                    max_IT_DD[i_day] = max(max_IT_DD[i_day-1], IT_DD)
                    max_IT_eq[i_day] = max(max_IT_eq[i_day-1], MTM_equity)
                    account_balance[i_day] = MTM_equity
                if i_day_in_trade == hold_days:
                    # Exit at the close
                    sell_price = qtC.iloc[math.floor(j)]
                    # Check for end of forecast
                    if i_day >= number_days:
                        FC_max_IT_DD[i_forecast] = max_IT_DD[i_day]
                        FC_tr_eq[i_forecast] = MTM_equity
    # All the forecast have been run
    # Find the drawdown at the 95th percentile
    DD_95 = stats.scoreatpercentile(FC_max_IT_DD, 95)
    print(f'DD95: \t\t\t{DD_95:.3f}')

    if (abs(DD95_limit - DD_95) < accuracy_tolerance):
        # Close enough
        done = True
    else:
        # Adjust fracton and make a new set of forecasts
        fraction = fraction * DD95_limit / DD_95
        done = False

# Report
# IT_DD_25 = stats.scoreatpercentile(FC_max_IT_DD, 25)
# IT_DD_50 = stats.scoreatpercentile(FC_max_IT_DD, 50)
IT_DD_95 = stats.scoreatpercentile(FC_max_IT_DD, 95)

print(f'DD95: \t\t\t{IT_DD_95:.3f}')

years_in_forecast = forecast_horizon / 252

TWR_25 = stats.scoreatpercentile(FC_tr_eq, 25)
CAR_25 = 100 * (((TWR_25/initial_equity) ** (1.0/years_in_forecast)) - 1.0)

TWR_50 = stats.scoreatpercentile(FC_tr_eq, 50)
CAR_50 = 100 * (((TWR_50/initial_equity) ** (1.0/years_in_forecast)) - 1.0)

TWR_75 = stats.scoreatpercentile(FC_tr_eq, 75)
CAR_75 = 100 * (((TWR_75/initial_equity) ** (1.0/years_in_forecast)) - 1.0)

print(f'CAR25:\t\t\t{CAR_25:.2f}')
print(f'CAR50:\t\t\t{CAR_50:.2f} ')
print(f'CAR75:\t\t\t{CAR_75:.2f}')

# Save equity curve to disc
np.savetxt('account_balance.csv', account_balance, delimiter= ',')

# Save CDF data to disc
np.savetxt('FC_maxIT_DD.csv', FC_max_IT_DD, delimiter= ',')
np.savetxt('FCTr.csv', FC_tr_eq, delimiter= ',')

# Plot maximum drawdown
for i in range(a1):
    pltx[i] = i
    plty[i] = max_IT_DD[i]
plt.plot(pltx, plty)
plt.show()
# end