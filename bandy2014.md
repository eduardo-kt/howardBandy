> Bandy, H. B. (2014). Quantitative technical analysis: An integrated approach to trading system development and trade management (1st edition). Blue Owl Press, Inc; bandy14.

**Quantitative Technical Analysis**<br>
_Howard Bandy_

- [Contents](#contents)
- [Chapter 01. Introduction](#chapter-01-introduction)
  - [The Goal](#the-goal)
  - [The Process](#the-process)
  - [Two Components of Trading](#two-components-of-trading)
  - [Position Sizing](#position-sizing)
  - [Development (trading system development)](#development-trading-system-development)
    - [The Model](#the-model)
    - [The Data](#the-data)
    - [Patterns](#patterns)
    - [Non-stationary](#non-stationary)
    - [Synchronization](#synchronization)
    - [Signal and Noise](#signal-and-noise)
    - [Learning](#learning)
    - [Subjectivity and Objective Functions](#subjectivity-and-objective-functions)
    - [Estimate Distributions of Performance](#estimate-distributions-of-performance)
  - [Trading Management](#trading-management)
  - [Risk Tolerance](#risk-tolerance)
  - [Why Traders Stop Trading](#why-traders-stop-trading)
  - [Why is so Hard](#why-is-so-hard)
- [Chapter 02. Risk and Risk Tolerance](#chapter-02-risk-and-risk-tolerance)
  - [Measurement and Management](#measurement-and-management)
  - [Drawdown Defined](#drawdown-defined)
  - [Frequency of Action](#frequency-of-action)
  - [Maximum Adverse Excursion (MAE)](#maximum-adverse-excursion-mae)
    - [MAE for a single day](#mae-for-a-single-day)
    - [MAE for a two-day trade](#mae-for-a-two-day-trade)
    - [MAE for a multi-day trade](#mae-for-a-multi-day-trade)
    - [MAE for a Series of Trades](#mae-for-a-series-of-trades)
    - [Accumulated MAE (AMAE)](#accumulated-mae-amae)
  - [Mark-to-Market Equivalence](#mark-to-market-equivalence)
  - [Risk Tolerance](#risk-tolerance-1)
  - [Position Size - safe-f](#position-size---safe-f)
  - [Using Final Equity as a Metric](#using-final-equity-as-a-metric)
  - [Evaluating Market-to-Market Equivalence](#evaluating-market-to-market-equivalence)
  - [Technique for Risk Management](#technique-for-risk-management)
  - [Trade Quality](#trade-quality)
- [Chapter 03. Programming Environments](#chapter-03-programming-environments)
- [Chapter 04. Data](#chapter-04-data)
- [Chapter 05. Issue Selection](#chapter-05-issue-selection)
  - [Market Research](#market-research)
  - [Risk and Profit Potential](#risk-and-profit-potential)
  - [Simulation Outline](#simulation-outline)
  - [Calculating CAR](#calculating-car)
  - [Drawdown as a Function of Holding Period](#drawdown-as-a-function-of-holding-period)
  - [Profit Potential](#profit-potential)
  - [Risk of being Short](#risk-of-being-short)
  - [What the Prospector Found (extend the analysis)](#what-the-prospector-found-extend-the-analysis)
  - [Holding Longer](#holding-longer)
  - [Portfolios](#portfolios)
  - [Estimating Profit Potential](#estimating-profit-potential)
- [Chapter 06. Model Development](#chapter-06-model-development)
  - [Introduction](#introduction)
  - [Two Processes to be Modeled](#two-processes-to-be-modeled)
  - [Aspects of Trading System Model Development](#aspects-of-trading-system-model-development)
    - [Goal](#goal)
    - [Pattern Recognition](#pattern-recognition)
    - [Data](#data)
    - [Trend Following](#trend-following)
    - [Indicators](#indicators)
    - [Entries and Exits](#entries-and-exits)
    - [Trading Signals](#trading-signals)
    - [Model Constraints](#model-constraints)
    - [Fitting and Overfitting](#fitting-and-overfitting)
    - [Objective Function](#objective-function)
    - [Backtesting](#backtesting)
    - [Optimization](#optimization)
    - [Stationarity and Synchronization](#stationarity-and-synchronization)
    - [Validation](#validation)
      - [These conditions are required for walk forward to work:](#these-conditions-are-required-for-walk-forward-to-work)
    - [Some Other Way](#some-other-way)
  - [Next Chapters](#next-chapters)
- [Chapter 07. Model Development Indicator Based](#chapter-07-model-development-indicator-based)
  - [Objective Function](#objective-function-1)
  - [Select Data Series](#select-data-series)
  - [System Overview](#system-overview)
  - [Indicator Selection](#indicator-selection)
    - [Chart Patterns](#chart-patterns)
  - [Discovering Tradable Systems](#discovering-tradable-systems)
  - [Summary](#summary)
- [Chapter 08. Model Development Machine Learning](#chapter-08-model-development-machine-learning)
- [Chapter 09. Trading Management](#chapter-09-trading-management)
- [Chapter 10. Summary and Random Thoughts](#chapter-10-summary-and-random-thoughts)
- [Bibliography](#bibliography)


# Contents
Chapter 1: [Introduction](#chapter-01-introduction)<br>
Chapter 2: [Risk and Risk Tolerance](#chapter-02-risk-and-risk-tolerance)<br>
Chapter 3: [Programming Environments](#chapter-03-programming-environments)<br>
Chapter 4: [Data](#chapter-04-data)<br>
Chapter 5: [Issue Selection](#chapter-05-issue-selection)<br>
Chapter 6: [Model Development](#chapter-06-model-development)<br>
Chapter 7: [Indicator-based Model Development](#chapter-07-model-development-indicator-based)<br>
Chapter 8: [Machine-Learning-based Model Development](#chapter-08-model-development-machine-learning)<br>
Chapter 9: [Trading Management](#chapter-09-trading-management)<br>
Chapter 10: [Summary and Random Thoughts](#chapter-10-summary-and-random-thoughts)<br>

<div style="page-break-before: always;"></div>

# Chapter 01. Introduction
This book is about trading using quantitative techniques together with technical analysis.

Chapter 1 begins with the statement of a goal, briefly discusses a number of topics that provide some background for the development and trading quantitative systems, and concludes with some reasons why this is so hard.

## The Goal
The goal is for the trader to have confidence that the signals generated by the trading system precede trades that provide rewards adequate to compensate for the risk.

## The Process
This is a classical example of fitting a model to a set of data, intending to use the model for prediction. 

In order to have a system that generates signals that we have confidence in, that is profitable, and that has acceptable risk, we need several things:

|Reference| Item Thing|
|-|-|
|| Data series that have enough variation so that buying and selling produces profit in excess of risk-free alternative uses of the money.|
|| The same data series must not have so much volatility that the resulting system has risk of drawdown that exceeds the trader's personal risk tolerance.|
|| Existence of patterns in the data that precede profitable trading opportunities.|
|| Existence of a set of rules and parameters, call it a model, that recognizes the patterns and issues trading signals.|
|| Our ability to discover the model and verify that it works for historical data, creating a trading system.|
|| Our ability to monitor the performance of the trades generated by the system over time to verify that the system has learned to recognize the patterns and that the patterns continue.|
|| Our ability to compute the correct position size for each trade so that we maximize account growth while holding drawdown within personal limits of risk tolerance.|
|| Our ability to recognize system breakdown and take the system offline before excessive loss of trading capital.|
|||

## Two Components of Trading
The trading system has two distinct components:
* **Trading System Development**: Development handles issue and data selection; and design, testing, and validation of the trading model. That includes calculation of indicators, establishment of rules for trade entry and trade exit, searching to detect patterns, metrics for measuring success, testing to validate the pattern recognition, and establishing a baseline with which to compare future performance. Detailed in [chapter 6](#chapter-06-model-development), [chapter 7](#chapter-07-model-development-indicator-based), and [chapter 8](#chapter-08-model-development-machine-learning). 
* **Trading System Management**: Trading management focuses on monitoring the health of the system being traded, estimating risk, determining position size, estimating profit potential, and making the trades. Detailed in [chapter 9](#chapter-09-trading-management).

The two components share a common element - the set of trades that, during development, is the _best estimate_ of future performance, and, during trading, is that best set of trades augmented by trades actually taken.

## Position Sizing
Position sizing is determining the number of shares or contracts for the next trade. Including position size while evaluating the data series prior to trading model development (see [chapter 5](#chapter-05-issue-selection)) and again in trading management (see [chapter 9](#chapter-09-trading-management)) is correct and important. But position size should not be a component of the trading model itself. Including it there causes two problems:
1. During development of the trading system, using position size other than a fixed number of contracts or dollars introduces a bias that favors specific models that benefit from specific order of trades that happen to occur in the historical data used for development but are unlikely to be repeated in the future, as compared with models whose trades are evaluated independent of order.
2. The trading system has a large number of rules and parameters that can be varied in the search for the best system. The management system has only one - position size. Including position size in the trading system removes it from the management system, leaving no variable that can be used for objective trading management.

## Development (trading system development)

A trading system is a combination of a model and some data (<span style="color:red;font-weight: bold">_System = Model + Data_</span>).

### The Model
The purpose of the model is to recognize patterns that precede profitable trading opportunities. The output from the model is a list of trades for the time period being tested, together with a summary of performance. [Chapet 6](#chapter-06-model-development) discusses general issues related to development of the model. [Chapter 7](#chapter-07-model-development-indicator-based) and [Chapter 8](#chapter-08-model-development-machine-learning) discuss issues related to model development using indicator-based techniques and machine learning based techniques, respectively.

### The Data
The primary data series is a time-ordered sequence of quotations. Each quotation represents the price of the issue being traded. The data format assumed throughout this book is bars (a set of OHLC values that provide the range of prices for some period of time).

> It is important to accept the data as it is without making additional assumptions as to being normal, log-normal, or any other distribution.

The purpose of developing trading systems is to learn as much as possible about the population of trades that will occur in the future and make estimates of future performance. The results of testing trading systems form the sample that is used to make those estimates. The information content that describes a trading system over a given period of time can be described in many ways. The following list is in decreasing order of information:
1. Reality. Trades, in sequence, that actually result from applying the system. Reality cannot be known in advance. Estimating reality, the population, is the purpose of system validation. Reality is the logic of the system processing the future data series.
2. List of trades, in time sequence. The list of trades, in time sequence, that results from processing a data series that is similar to the future data, is the best estimate we can obtain of reality. 
3. Set of trades. The set of trades, ignoring time sequence, relaxes the assumption of the trades occurring in a particular sequence. Selecting trades from this set in random order gives an opportunity to evaluate the effects of similar conditions, but in different time sequence.
4. Distribution of trades. A distribution can be formed using any of the metrics of the individual trades. For example, the probability mass function (aka probability density function) of the distribution of percentage gain per trade.
5. Four moments describing the distribution of trades (mean, variance, skewness, and kurtosis).
6. Mean and standard deviation.
7. Mean.
8. Direction.

### Patterns
We will be examining data looking for patterns, for profitable trades, and the relationship between the patterns and the trades. The patterns will be described as a set of rules and coded into the model. 

### Non-stationary
Stationarity is a feature of data that refers to how a particular metric of the data remains relatively constant or changes as different subsets of the data are analyzed.

The techniques discussed in this book extend the concept of stationarity to whatever metric is being analyzed. We want that relationship to remain stationary. <span style="color:magenta; font-weight:bold">Be cautious, financial time series data is never stationary.</span>

### Synchronization
The model specifies the logic, rules, and parameters. The data is the price history of the issue being traded, perhaps augmented by other data series. A trading system is profitable as long as the logic identifies patterns in the data that precede profitable trading opportunities.

The logic of a typical trading system is relatively fixed. It is designed to detect a particular set of patterns. The data change, following changes in areas that affect the issue - economics, politics, weather, etc. As the data changes, the patterns in the data move in and out of synchronization with the logic.

### Signal and Noise
The data consists of two components - signal and noise. The signal consists of the patterns we hope to identify. What constitutes signal is determined by the model. Everything that a particular model does not explicitly consider to be signal is noise and interferes with identification of the signal patterns.

### Learning
Learning is the process of examining data, recognizing some patterns, observing related patterns, and hoping there is a generalization. Learning is not possible unless there is data to be examined and patterns to find. It is a data mining activity. The data mined is called the _in-sample_ data.

We cannot learn a feature that has not been seen. The in-sample data must include examples of the patterns to be learned.

Identifying patterns in the in-sample data is necessary for learning, but not sufficient. There must be generalization. **The test for generalization is validation**. That is, testing previously unused data to estimate the success of detecting the patterns and defining the rules. The data tested for validation is called the _out-of-sample_ data.

### Subjectivity and Objective Functions
Systematic traders use objective functions designed to identify important decision criteria and quantify them. An objective function is alternatively called a loss function, cost function, utility function, fitness function, or optimization metric. An objective function is a formula that includes terms for each of the criteria or variables important to the decision.

The developer needs to decide which is best, and best is subjective. The purpose of the objective function is to provide an objective metric that represents the subjectivity of the developer's definition of best.

### Estimate Distributions of Performance
The trading system that results from the design, testing, and validation provides a single set of trades with single mean, single standard deviation, single terminal wealth, single maximum drawdown. In order to estimate profit potential and risk it is important to consider the distribution of potential results.

Beginning with determining the maximum safe position size that normalizes risk associated with a set of trades to keep it within your personal risk tolerance, an objective function based on the Compound Annual Rate of Return (CAR) at some confidence level (say the 25th percentile) is nearly universal objective function. The process is outlined in [chapter 2](#chapter-02-risk-and-risk-tolerance).

## Trading Management
The trading management sections fo this book discuss a new and unique technique, _dynamic position sizing_, and introduce a new metric of system health, _safe-f_.

Dynamic position sizing monitors system performance trade-by-trade. Using Monte Carlo simulation and Bayesian analysis, it determines risk of drawdown, assesses the personal risk tolerance of the trader, computes safe-f - the maximum safe position size for the next trade - and estimates profit potential. All on a trade-by-trade basis. Safe-f gives you a clear indication of system health, including when the system should be taken offline. [Chapter 9](#chapter-09-trading-management) discusses trading management.

## Risk Tolerance
Everyone has a personal tolerance for risk. Every trading system has some risk. In [chapter 2](#chapter-02-risk-and-risk-tolerance) we give some techniques for assessing and quantifying personal risk tolerance, for assessing the risk associated with a data series, and for a trading system.

## Why Traders Stop Trading
1. ~~The results are too good~~. Keep trading until one of the other reasons to stop happens.
2. The results are not worth the effort.
3. The results are not worth the stress.
4. You make enough money. No matter how good a system is, there is always a risk of serious loss. <span style="color:#9db288; font-weight: bold">When you has reached your goal, you should retire.</span>
5. There is a serious drawdown. The primary reason people stop trading a system.

Do not continue to trade a system that has entered a serious drawdown expecting that it will recover. It may recover on its own; it may require readjustment; or may be permanently broken and never work again. Take it offline and either observe it until recent paper-trade results demonstrate that it is healthy again, or send it back to development. **The correct position size for a system that is broken is zero.**

## Why is so Hard
* The data is very noisy.
* The data is non-stationary.
* The market is nearly efficient.
* There are many potential solutions to reach the same profitable trades.
* Competition is agressive.

<div style="page-break-before: always;"></div>

# Chapter 02. Risk and Risk Tolerance
Risk is the risk of drawdown in the balance of the account. The primary reason traders stop trading is that they experience a drawdown larger than they anticipated, larger than they can afford, larger than their risk tolerance.

## Measurement and Management
Measurement of risk and management of risk are related. Management of risk has two components: system design and position sizing.

**System design** affects risk in issue selection, trade selection, entry, and exit (See issue selection in [chapter 5](#chapter-05-issue-selection) and trade selection, entry, and exit in [chapter 6](#chapter-06-model-development)).

**Position sizing** is adjusting trade size as the model and data move in and out of synchronization. It enables us to take advantage of periods of good performance and reduce exposure during periods of poor performance. See [chapter 9](#chapter-09-trading-management) for dynamic position sizing.

Measurement of risk helps us understand the risk inherent with the combination of:
* the issue being traded
* accuracy of the trading system
* holding period
* intra-trade visibility

## Drawdown Defined
**Drawdown** is defined as the drop in account equity, measured as a percentage relative to the highest equity achieved prior to the drawdown. The gain needed to recover from a drawdown is greater than the loss that caused the drawdown. <span style="color:magenta; font-weight:bold"> Drawdown is related to equity curve.</span>

![Drawdown](resources\drawdown.png)

## Frequency of Action
A system's equity is either at a new high, or it is in a drawdown. Most systems are in drawdowns most of time (70 to 90% of the time is not unusual).

Continuing to trade a system that is in a drawdown requires that you have confidence in your system. In order to apply the pattern recognition, risk control, and position sizing techniques described in later chapters, you must be prepared to hold your open positions until the system issues the exit. What does that imply?

Drawdown can increase rapidly over a multi-day market decline, so, the minimum holding period must be short enough that price changes, including drawdown, within it can be ignored. I recommend the minimum period between potential changes to position be no longer than one trading day.

## Maximum Adverse Excursion (MAE)
Maximum Adverse Excursion (MAE) is a measure of the most unfavorable point in a trade, or in a period of time. MAE is a measure of risk we acknowledge. <span style="color:magenta; font-weight:bold"> MAE is related to trades.</span>

Similar to MAE, maximum favorable excursion (MFE) records the most favorable price. In a long trade, it is the highest high. When using mark-to-market, whenever there is a new MFE and it establishes a new high for the account equity, adjust the equity to reflect that gain. 

### MAE for a single day
**The MAE for a single period of time in isolation, such as daily bar, is the most adverse position relative to the beginning of the that period and with respect to the direction**. The MAE for a long position entered Market-on-Open (MOO) is the low relative to the open.

$$MAE=\frac{(Open-Low)}{Open}$$

If entry is mae at some other intra-day price than the open, we cannot determine (without access to shorter, intra-day bars) whether the low came before or after the entry. **The conservative analysis** is to assume the worst case and compute MAE as the low relative to the entry.

$$MAE=\frac{(Entry-Low)}{Entry}$$

> The MAE for a short position entered MOO is the high relative to the open. For an intra-day entry, it is the high relative to the entry.

### MAE for a two-day trade

Consider a system that enter a long position market-on-close (MOC), holds one day, and exits MOC the next day, with intra-day low  visible. The intra-trade MAE is the low on the second day relative to the entry.

$$MAE=\frac{Ref(Close, 0)-Ref(Low, 1)}{Ref(Close, 0)}$$
where $Ref(Low, 1)$ is the low one day into the future.

If intra-day prices are invisible, then only the two closing prices matter. If the trade is a winner, MAE is zero; if it is a loser, MAE is the loss of the trade.

$$MAE=max \left(\frac{Ref(Close, 0)-Ref(Close, 1)}{Ref(Close, 0)},\;0\right)$$

### MAE for a multi-day trade

For a multi-day trade, the MAE of the trade depends on how much of the intra-trade price we want to acknowledge. With **intra-day prices visible**, the adverse excursion for a long trade is the difference between the highest intra-trade equity, marked-to-market each day at some price (e.g. the day's close), and that day's low.

<img src=resources\mae.png>

If **intra-day prices are invisible**, each day's price is a single value. The adverse excursion is the difference between the highest close, marked-to-market daily, and the day's close.

<img src=resources\mae_intra_invisible.png>

<div style="color:red; font-weight:bold">Um dia sempre fecha com nova máxima ou com adverse excursion. Se o preço de fechamento for novo fechamento máximo o adverse excursion é zero. Se não for, conta um adverse excursion do máximo (que ocorreu no passado) até o mínimo do dia de hoje. Se for o maior percentual de toda a série será MAE</div>

### MAE for a Series of Trades
There is a similarity between a price bar, say a daily bar, and a trade. Each has an open, high, low, and close. Imagine that the opening price of the bar is the entry price of a trade and the closing price is the exit price. In this interpretation, the trade's high is its MFE and the trade's low is its MAE. 
|Trade|Daily Bar|
|-|-|
|Entry|Open|
|High|High|
|Low|Low|
|Exit|Close|

Each trade is a series of days, each of which has its own high and low. Drawdown for a series of trades could be measured relative to:
* Intra-day high and low prices. Use intra-day high to MFE and subsequent low prices to measure MAE (relative difference between MFE and MAE). Not tradable.
* Intra-trade high equity. Marked-to-market closing prices define the highest bankable equity and maximum adverse excursion from that price. Point **A** is the highest close. You could have liquidated the position, banked the profit, and withdrawn the funds at the closing price that day. That is your money, and drawdown is calculated relative to it. Point **B** is the MAE. It is the deepest intra-trade drawdown at a marked-to-market closing price. The difference between B and A is the amount you had lost at the close of day B. 

<img src=resources\intra_trade_mae.png>

* Closed-trade high equity. Ignores all intra-trade equity changes and compare current closed equity with maximum closed equity.

### Accumulated MAE (AMAE)
Every trade has its own MAE, computed and reported daily. The accumulated drawdown spans trades and measures the highest marked-to-market bankable equity to lowest market-to-market equity. Your goal in trading the system is to determine the proper maximum safe position size, on a trade-by-trade basis, so the accumulated MAE rarely exceeds your risk tolerance. 
<span style="color:magenta; font-weight:bold;"> AMAE is related to the equity account. </span>


## Mark-to-Market Equivalence
From a mathematical perspective, the net equity change from a sequence of trades is identical whether the trades are considered as complete trades or as sequences of marked-to-market days (the cumulative gain for the sequence of days for the entire trade sequence). From a trading management perspective, marking-to-market daily gives finer resolution to the performance of the system and the opportunity to make subjective trading decisions, should they become necessary (e.g. taken the system offline). From a trading system design perspective, marking-to-market daily transforms every system, no matter how often it buys and sells, into a system that has 252 daily results every year. [Chapter 06](#chapter-06-model-development) describe how convert impulse signals to state signals.

Although the trades extend over multiple days, the system design and system management focus is on the mark-to-market period - daily.

This does not imply changing positions every day. It does imply evaluating every day, and willingness to change positions daily. **In terms of changes to account equity and drawdown, an n-day trade is equivalent to n one-day trades**.

## Risk Tolerance
Risk tolerance is the level of drawdown that, when reached or exceeded, causes the trader to accept that the system is broken and must be taken offline.

A statement of risk tolerance has four parameters:
* Account size (the initial balance)
* Forecast Horizon (how far into the future we look. Pick a length of time that fits your business plan and trading activity).
* Maximum Drawdown (level at which the system is taken offline. Individual traders might be willing to accept 20% or less. Trades preferring longer holding periods must be prepared to either accept higher risk or trade at a smaller position size).
* Degree of certainty (change level of having maximum drawdown)

Illustrating the case: a trading system was designed, coded, and tested using daily end-of-day data for the period 01/01/1999 through 01/01/2012. **Validation** produced a set of 506 trades for the 13 year period. That set of trades was used as the _best estimate_ of future performance. Assuming that future performance is similar to that of the best estimate, a two year forecast horizon will have about 78 trades. A monte carlo simulation was coded. 

The fixed fraction technique was used for position sizing (recommended technique). The fraction value is determined interactively (with monte carlo simulation). The fraction was adjusted in order to find the value where there was a 5% change (degree of certainty) that the maximum drawdown would exceed 20%.

The maximum drawdown for each try in a monte carlo simulation (e.g. each of 1000 tries) was recorded, then sorted into bins 0.5% wide. Then we design the cumulative distribution function (**CDF**). To form the CDF, beginning t the leftmost bin of the histogram of the pmf, compute the running sum of percentages. 

![risk](resources\risktolerance.png)

## Position Size - safe-f

There are many alternative methods of determining position size. I recommend using fixed fraction as the position sizing technique. For a given set of trades, maximum drawdown is highly dependent on position size. As the fraction of the account used for each trade is increased, maximum drawdown also increases. 

**Safe-f** is position size. It is recalculated after every trade and used to determine the size of the next trade. If the set of trades change the risk of drawdown changes, and safe-f changes. 

When using mark-to-market evaluation, safe-f is computed at that same frequency - daily. Daily intra-trade changes are added to the set of trades. If an intra-trade drawdown develops, safe-f will drop, indicating to the trader to lighten position. **This is a dynamic position sizing technique.**

Equity of the trading account also depends on position size. Final equity is relative to initial equity. Also note that as the probability of a large final equity account increases with position size, the magnitude of the potential loss of account equity also increases.

## Using Final Equity as a Metric
Final equity increases with position size. It is tempting to use final equity, terminal wealth, or compound annual rate of return (CAR) - all equivalent metris - to evaluate system performance. The difficulty is that the distribution of final equity expands quite rapidly as position size increases.

## Evaluating Market-to-Market Equivalence

We saw the mark-to-market equivalence between a sequence of multi-day trades and a sequence of single-days, each marked-to-market. We can, and should, test whether mark-to-market equivalence holds for risk, calculation of safe-f, and profit potential. 

The trading system code was modified so its output included a series of daily price changes along wiht the trade listing. The 506 trades covered 1151 days. The simulation to forecast a two year period used 177 days. Nothing else was changed.

We should hope for results that are close, but we should not expect perfect agreement. For one thing, replacing trades by days destroyed whatever serial correlation existed between the days in trades. For another, simulations usually produce results thar differ slightly from run to run.

The advantages of marking to market daily - increased control over changes in position, increased number of data points per year, less distortion at the boundaries of evaluation periods - easily compensate for slight differences in forecast of safe-f, drawdown, and final equity.

## Technique for Risk Management
The statement of risk tolerance is a personal statement. If the drawdown reaches the maximum level, that is an indication that the system is broken, and the system is taken offline.

The _dynamic position sizing_ (see [Chapter 9](#chapter-09-trading-management)) uses recent trading results, together with the best estimate set of trades and a Monte Carlo simulation, to estimate the distribution of the drawdown that can be expected in the future. <span style="color:#dfc76c">Properly implemented, dynamic position sizing will reduce the position size when trading results are poor.</span>

## Trade Quality
We periodically read articles that recommend holding long positions for long periods of time. The argument revolves around an analysos of equity gain related to missing a very few of the best days in a period, suggesting it is essential to remain invested in order to benefit from those few special days. <span style="color:magenta">Losing trades are clearly more important than winning trades in determining risk.</span>

Recall that safe-f (position sizing) is computed so that the risk of a 20% drawdown is 5%. We can describe this as normalizing for risk. When normalized for risk, the profit potential of alternative trading systems can be compared directly. <span style="color:#dfc76c"> Normalized for risk, performance is significantly better for the set of trades that do not include the losing trades. </span>

# Chapter 03. Programming Environments
Quantitative technical analysts use precisely defined logical and  mathmatical expressions to identify signals and trades. There is no alternative. You must understand the techniques and the associated math. You must be able to read, write, and execute computer programs. 

As we approach quantitative analysis from two different perspectives, we need two different programming environments. One for traditional trading system development, computation of indicators, and generation of buy and sell signals. The other for data science and machine learning.

# Chapter 04. Data
The final step in developmen and use of a trading system is trading. Every trade is because the rules have identified a pattern in the data. Fisrt in data used to develop the system; them in the current, as yet unseen, data used to trade. Development data must have sequences of patterns followed by price changes similar to those being sought in the trading data.

In order to be useful in training, data must contain instances of the pattern. 

# Chapter 05. Issue Selection
It an issue tradable? The answer is in three parts:
* How much **risk** is there?
* How much **profit** is available?
* Can we develop a **system** to extract the profit?

## Market Research
The best issues to trade combine four characteristics:
* Adequate profit potential (some price variation)
* Absence of extreme adverse price changes (not to much price variation)
* Existence of detectable signal patterns (not too efficient)
* Sufficiently liquid so you can exit your entire position any minute of any day without substantially affecting the bid-ask spread.

The complete trading system consists of the model and the data series. Even before we begin model development, we can determine how much profit is potentially available by analyzing the data series itself.

## Risk and Profit Potential
There is quantifiable risk inherent in any data series. All trades, winners as well as losers, have adverse excursions that contribute to the drawdown.
* Given a data series and two variables - holding period and system accuracy - we can estimate the risk inherent in the series.
* Given the risk inherent in the series and your personal statement of risk tolerance, we can determine safe-f.
* Given safe-f, we can estimate profit potential.

## Simulation Outline
The analysis is done using a monte carlo simulator. We are choosing trades that sum a total of two years of long exposure, however many trades that requires and however much time that covers.

> Imagine you are alternately long and flat, then squeeze out the flat periods, resulting in two years of long trades. This is the **forecast horizon**.

The major control variables:
* Your [risk tolerance](#risk-tolerance-1) (say a maximum 5% chance of drawdown greater than 20% over a 2 year horizon)
* The issue being tested (Say SPY. We need daily closing prices data)
* Any time period longer than the **forecast horizon** can be used (more is better. Say 1999 through 2014)
* The holding period of each trade in days (any value up to the length of the forecast is valid. Say 5 days).
* Accuracy of the trading system (say 0.65).
* The number of simulation runs (say 1000).

The simulation works as follows:
1. Set the control variables.
2. Select a daily price series.
3. Given the holding period, examine every day as an entry day. Positions will be taken market on close, at the closing price. Look ahead the number of days of the holding period. That will be the exit day. If the closing price on the exit day is higher, mark this entry day as a "gainer" entry day; otherwise it is a "loser" entry day. 
4. Divide the number of days in the forecast horizon by the holding period, giving the number of trades.
5. Set the fraction used for each trade to 1.00.

For each of the required number of simulations runs, repeat the following sequence for as many trades as are needed to complete the forecast horizon: 
1. Pick a random number (uniform, 0.00 to 1.00) to determine whether the next trade will be a winner of a loser. Over the course of many runs, the proportion of winning trades matches the trade accuracy you want to study. 
2. From whichever list (gainers or losers) was chosen, select a trade entry day at random. Note the entry price. Buy as many shares as you can with the fraction of equity allowed.
3. In the sequence they occur in the historical price series, process the trade day-by-day. Keep daily track of:
    * Intra-day drawdown, measured using daily high and low.
    * Intra-trade drawdown, measured using mark-to-market daily closing price.
    * Trade drawdown, measured from the trade open to trade close.
    * Account equity (value of shares held plus cash)

At the completion of those trades, the simulator reports the three drawdown metrics and the final equity. 

<img src=resources\monte_carlo_metrics.png>

**Legend**: maximum intra-day drawdown (Max IDDD); maximum intra-trade drawdown (Max ITDD) this is the metric we want to hold to 20%; maximum trade drawdown (Max TRDD); final equity (EqAtClose); compound annual rate of return (CAR).

## Calculating CAR
Terminal Wealth Relative (TWR), Final equity, compound annual rate of return (CAR), and number of years (N), are related by these formulas:
$$TWR = \frac{Final\;Equity}{Initial\;Equity}$$
$$TWR = (1+CAR)^{N}$$
$$CAR=exp\left(\frac{ln(TWR)}{N}\right)-1$$

The risk tolerance requires intra-trade marked-to-market daily drawdown at the 95th percentile to be no greater than 20 percent.
> If results for all 1000 runs (monte carlo simulation) were listed and sorted by Max ITDD, we want the first 950 to have values less than 0.20 (max drawdown risk tolerance) and the final 50 to be greater. There is no advantage in having the final 50 be less than 0.20, a situation that would occur only if the fraction of available equity used for each trade was lower than the maximum safe-f. Intentionaly using a lower fraction does lower risk, but it lowers profit even more. 

You do want to coordinate your risk tolerance with the fraction used and take the largest positions that are safe (a.k.a. safe-f). **We are not judging the system profitability. We are just setting the position size according to the accepted risk tolerance level**.

> This does not mean that a system that is 65% accurate and holds trades five days cannot be profitably traded. It does mean that, in order to avoid unaceptable drawdowns, only a fraction of the available funds can be safely used (**not the full fraction**). The remainder must remain in a risk free account to act as a ballast.

## Drawdown as a Function of Holding Period
* Drawdown increases as holding period increases.
    * Profit potential increases as holding period is reduced.
* Drawdown increases as trade accuracy decreases.
    * Profit potential increases as trade accuracy increases.

## Profit Potential
Given the parameters (system accuracy, holding period, maximum intra-trade drawdown, and maximum safe fraction) we can estimate the potential profit. That is, tranding the selected issue for two years of exposure, using a yet-to-be-defined model that results in trades that are held for the holding period of which the tested system accuracy, we can compute the distribution of final equity and associated CAR.;


<img src=resources\cdf_spy.png>

The CAR actually experienced will depend on the specific trades, but if the future resembles the past, estimates can be read from the distribution of CAR. 

The 50th percentile is the median. The interquartile range is another useful metric. It is the difference between the values at the 25th percentile and those at the 75th percentile. Results are equally likely to be within this range as to be outside it to one extreme or the other. It is typical for CAR75 to be 1 or 2 times CAR25 with CAR50 about at their midpoint. Any large differences should be checked.

CAR25 is the compound annual rate of return at the 25th percentile of the cumulative distribution of profit. CAR25 of the risk-normalized distribution of profit is as close to a universal objective function as I have found.

## Risk of being Short
We hear that being short is dangerous. That is riskier than being long.
> There may be other reasons for not taking short positions, but riskiness is not one of them. Being short is inherently safer than being long. 

## What the Prospector Found (extend the analysis)
Before spending the effort trying to develop a model to use with a data series, we want some assurance the resulting system has the possibility of satisfactory performance. Recall that we want a combination of:
* Enough variability to give opportunity for profitable trades (CAR25 above risk free return).
* Enough stability that sharp price changes are infrequent (risk tolerance threshold).
* Enough history to assess performance in rinsing and falling markets (analize available data).
* Enough liquidity to be able to exit a position easily.

## Holding Longer
There are many reasons for holding positions longer than a few days. You may have read or heard an anecdote where a large profit was made as a result of holding a position for a long time. Large profits improve any trading system. But limiting losses is more critical than achieving gains. As holding periods increase, adverse price movements increase in proportion to the square root of the relative increasing in hodling period, just from the random changes in price. For example: with a 5 day holding period and 4% risk of drawdown, increasing the holding period in 4 times (20 days) will increase intra-trade drawdown to 8% ($\sqrt{4}\times4=8$).

## Portfolios
The ideas on which portfolios are based are:
* diversification
* mean-variance optimization
* rotate to whatever is rising in price

My preference is shifting from portfolios to more focused systems. Each system taking a single direction in a single issue. Select a few issues that have attractive risk and profit potential base on your criteria, develop a system for each, then manage trading of each separately. Allocate most of your trading account to the system that is performing best.

## Estimating Profit Potential
For a given set of trades, risk (as measured by drawdown) depends on the sequence of trades. The position size - the fraction of the doolar amount allocated to a system that is used to take a position for each of that system's trade - affects both equity growth and drawdown. Assuming the system has a positive expectation, increasing position size results in faster equity growth, a higher final equity balance, and higher drawdown. If the position size is too high, drawdown will cause bankruptcy and end trading. We want to estimate the highest position size - the largest fraction - that can be used while keeping drawdown within tolerable limits.

A monte carlo simulation will give that estimate.

The technique described in [Chapter 2](#chapter-02-risk-and-risk-tolerance) - monitoring and accumulating adverse price excursions - is used to compute the drawdown of a sequence fo trades.

Drawdown can be recognized at three levels:
* intra-day
* intra-trade
* trade

Using daily price bars and marking to market at the close of every day, intra-trade drawdown is the level this program uses to determine safe-f.

The simulation is straight-forward:
1. State risk tolerance. 
2. Choose a data series and date range.
3. State holding period and trading accuracy.
4. Create or import a "best estimate" set of trades.
5. Search for safe-f:
    1. Pick an initial estimate of the fraction.
    2. Generate many trade sequences.
    3. Compare estimated risk from the trades with risk tolerance from the statement.
    4. Adjust the fraction and repeat until the estimated risk matches the risk tolerance.

The program listed here generates the set of trades based on trading accuracy and holding period. Alternatively, a set of real or hypothetical trades could be imported.

Begin with a statement of risk tolerance. Say it is a limit of a 5% chance of a drawdown of equity greater than 20%, measured from highest equity to date, marked-to-market using daily closing prices, over the period of a 2 year forecast. 

Choose the holding period, say 5 days. Specify a desired trading accuracy, say 65 percent.

The trade generation and trade-by-trade performance process is as follows:

For every possible entry day, note the entry and exit prices. Look into the future and note the exit price at the end of the holding period. Assign a label f either "gainer" or "loser" to the entry day.

If you are working with 10 years of daily data, there are 2520 possible entry days. Adjust for the boundary at the end of the test period. Either use 2515 entry days to ensure that every trade entered will be completed within the test data; or use all 2520 entry days, and allow the final 5 days to look into the subsequent period.

Divide the lenght of the forecast period by the length of the holding period, returning an integer. That result is the number of trades needed to cover the forecast period. You will need 100 5-day trades to cover the 504 days in two years. 

Each trade sequence / equity curve will be a sequence of 100 trades, each trade drawn at random using "sampling with replacement" from the best estimate set.

Add trades (winners or losers) to the sequence randomly based on the trading accuracy (is the percent of winners). Determine the size of the trade by the fraction being used.

For a system that is long or flat, a winning trade is one where the exit price is higher than the entry price - a "gainer".

Whenever you need a trade to add to the sequence, begin with a random choice of "gainer" or "loser" with "gainer" chosen 65% of the time. Given the resulting category, select any entry day at random. Determine the size of the trade by the fraction being used.

Generate many (say 1000 runs) such trade sequences, each covering two years of long exposure (chosen forecast period). For each sequence, compute and remember the metrics: final equity, maximum drawdown, and whatever else is of interest. Sort by maximum drawdown and note the value at the 95th percentile. If it is about 20%, the fraction is safe-f. If it is not, adjust the fraction and repeat generating a new set of 1000 sequences. 

When the fraction is correct so that the 95th percentile maximum drawdown matches the stated risk tolerance, use the final equity value from each sequence to construct the distribution of final equity. Report the values for the 25th, 50th, and 75th percentile. 


# Chapter 06. Model Development 
## Introduction
There are two approaches to trading system development:
* **Indicator-based:** compute an indicator, then observe price changes that follow.
* **Machine learning:** observe a notable price change, then identify patterns that precede.

The purpose of the model is to accept time series data that represent trades, proces that data searching for patterns that precede profitable trading opportunities, learn those patterns, and issue orders to buy, sell, short, and cover in response to live real-time or end-of-day data.

> The quality of the model is judge by its usefulness in live trading.

The two approaches share a considerable amount. From the perspective of trading management, there is no difference.

> _Developing or discovering high quality models is difficult. The markets are nearly efficient. The barriers to entry are low. Everyone is looking for the same profitables trades. Every profitable trade removes some of the inefficiency the system was designed to find._ 

## Two Processes to be Modeled


There are two modeling processes involved in trading system development: 
* **Developing the trading system:** it is developing the rules, identifying the patterns, analyzing the trades found in historical data, and validating the system.
* **Managing trading:** that is deciding whether the system is working or broken, and what size position is best for the next trade.

## Aspects of Trading System Model Development
### Goal
The goal of the model - its sole purpose - is to identify profitable trades. Nothing else. 

We definitely need to simplify. We began quantifying our own risk tolerance and quantifying the risk inherent in a data series. The simplifications allow us to work with a limited pool of data series that we know to have reasonable risk and profit potential. But while the number of data series is reduced to a reasonable size, the number of possible models remains nearly uncountable. Simplifications may help limit the scope of the development problem, but they do not address the central questions:
* Are we finding the best models?
* Are the signals predictive?
* What performance can be reasonably expected in the future?
* Are metrics of system health available?

### Pattern Recognition
Every series of trade prices is a combination of signals and noise. The signal portion of the data contains the patterns our model is designed to recognize. As seen by our model, everything that is not signal is noise - even if it contains profitable signals that could be identified by some other model. 

> If it is easy to pick the signals out of the surrounding noise, we say there is a <span style="color: sienna; font-size:20px">high signal-to-noise ratio</span>.

The stronger the signal-to-noise ratio, the easier it is to identify the patterns, and the more profitable the trades. We are looking for non-stationary, weak signals in a noisy background (read _Signal and the Noise_, by Nate Silver).

### Data
When daily data, often described as end-of-day data, is being used, one bar represents the trades made for an entire day. A daily data bar typically has four prices - OHLC.
### Trend Following
No matter which entry technique is used, no matter which patterns are found to be predictive, the trades sought are always trend following. To be profitable, the price at which the position is sold must be higher than the price at which it is bought.
### Indicators
Indicators can be based on anything. They are most useful when they have significant events, such as crossing or bottoms.
### Entries and Exits

> My preference is fro trades that <span style="font-size:20px; color:sienna">occur frequently and hold one to three days.</span> You may be for something different. Whatever it is, a useful development practice is:
1. Identify the best entry point.
2. Identify he best exit point.
3. Evaluate the risk.
4. Evaluate the profit.
5. Explore patterns that precede entry and exit.
6. analyze results when either the entry or exit is not perfect.

The classical lookahead indicator is ZigZag:
```python
# zigzag function: True if Bottom. Buy signals.
z = zigzag(p, n)
Bottom[0] = 0
Bottom[-1] = 0
for i in range(1,len(Bottom) - 1):
    Bottom[i] = z[i] < z[i-1] and z[i] < z[i+1] # inverte para sell signals
```

The outline of the analysis:
1. Identify trades with daily prices: Compute zigzag or some other indicator of your choice, Identify entry/exit, Identify trade and store it in an array.
2. Analyze performance. Using the array of trades, perform Monte Carlo analysis to assess risk, normalize for risk, determine safe-f, estimate profit, including CAR25.

This procedure defines an upper limit to profitability. 

### Trading Signals
* **Impulse signals** mark transitions, such as the beginning or end of a trade. Using impulse signals, one trade is one data point - however many days that trade lasts.
* **State signals** identify condiions (long, flat, or short). Using state signals, marking to market daily, each day is one data point. 

> One aadvantage to state signals is providing opportunity for finer control of trade management throughout the trade. The health of the system is reevaluated every day at the same time it is marked-to-market. More on this in [Chapter 9](#chapter-09-trading-management).

### Model Constraints
Much of the discussion among traders focuses on the definition of the pattern that signals the trades. People describe themselves, or their technique through themselves, as being trend following, mean reverting, seasonal, or pattern traders. To my thinking, we can develop better system if we relax our insistence that entries conform to particular categories. If we want the determining factor of systemm acceptability to be results, rather than the constraints, we must be willing to relax tradition-bound requirements.

### Fitting and Overfitting

> Accuracy refers to errors in missing the center of the target (between-sample error). Precision refers to the distance between shots (within-sample error). Overfitting can be defined as an overly precise solution to a general problem based on a limited sample. Overfitting s emphasizing precision over accuracy. 

The test of whether the model is properly fit or is overfit - whether it has learned or memorized - is testing with previously unseen data.

### Objective Function
In order to manage the fitting process, there must be an appropriate metric of goodness of fit that can be measured. For quantitative technical analysis, it is an objective function.

The purpose of the objective function is to provide a single-valued score for each alternative, where the ranking of the alternatives is in the same order as our subjective preferences.

>_We are using the objective function to quantify subjectivity._

The best alternative, seem from trading results, is subjective. It includes positive growth of the trading account, limited drawdowns to the trading account, and conformity of results to real or artificially imposed constraints such as trading frequency and holding period.

> _CAR25 is the credible value of expected equity growth associated with the risk-normalized forecast of a trading system. It is the most universal objective function for trading system development and trading management I have found._

What characteristics of the series of trades give high CAR25?
* trade frequently
* trade accurately
* hold a short period
* have a high gain per trade
* penalize drawdown (specially large losses)

### Backtesting
A backtest is an evaluation of a system using data previously collected - historical data. 

### Optimization
The optimization is a search through a search space. Each indicator (or other feature being searched) defines a dimension in a seach space. We are searching for the highest stable area of that surface.

If run times are acceptable, use exhaustive search. Check for spikes in the response surface. Preferred solutions are located in "plateaus" with smooth slopes. 
>_Do not obsess over perfection. A good local optimum may be satisfactory. Prefer a robust system with lower performance to a fragile system with higher performance._

### Stationarity and Synchronization
To be profitable, a system must:
* learn the predictive patterns by analysis of the training data.
* identify those patterns in the validation data, and eventully in live-trading data.

Training data is in-sample data. Validation data is out-of-sample data.

Stationarity is a feature of data that refers to how a particular metric of the data remains relatively constant or changes as different subsets of the data are analyzed.

The trading system - the combination of model and data - is not stationary. Applying techniques that are appropriate for stationary processes to models that are not stationary produces inaccurate and unreliable results. 

The signal or pattern component of the data must be stationary thoughout the in-sample traning period. The in-sample period may be shorter than the period of synchronization, but avoid longer periods. The issue is not the length of the period in days so much as it is the length of the period of stationarity.

Naive developers are sometimes heard to recommend using as much data and as long a period as possible for each test period. Their reasoning is that the model will be exposed to as many different conditions as possible and will be able to perform well in all of them. My view is quite the opposite. I recommend that the test periods - particularly the in-sample periods over which the model is fit to the data - be as short as practical. Using data that includes an different conditions decreases the fit to an of the conditions. 

In my opinion, there is no minimum length for the out-of-sample period. It is, or at least can be, appropriate to treat each day as a one-day long out-of-sample period, with parameter values readjusted daily. 

In general, the lengths of the in-sample and out-of-sample periods are related only to the extent that the system must remain synchronized for the total length of those two periods. 

One thing you can expect is that longer holding periods require longer periods of stationarity in order to indentify and vlaidadte signal recognition. That implies boh longer in-sample periods, and longer out-of-sample periods. Increasing the length of time increases the probability that conditions change, stationarity is lost, and profitability drops. 

Additionally, drawdown increases as holding period increases. Longer holding periods imply greater risk, smaller safe-f, and lower CAR25.

Again, we have a familiar tradeoff. We want more data points for finer granularity, better precision, and easier statistical significance. But not so many data points that some of them represent conditions that are no longer current. 

Each data point is a trade that is both opened and closed within the test period. The longer positions are held, the longer the test period must be to span several trades; and the greater the intra-trade drawdown.

> The longer the test period, the more likely the model and the data will lose synchronization. 


### Validation

The gold standard of validation is walk forward testing. 

WF is a sequence o steps. Each step consists of finding the best model using the in-sample data, then using that model to test the out-of-sample data. The search for the best model is an optimization. You do not have an opportunity to evaluate the top choice. The optimization is applied to in-sample then the selected model is applied to out-of-sample data and stored. This process is repeated several times. After each step, the beginning and ending dates of both periods are stepped forward by the length of the out-of-sample period. 

The results from all of the out-of-sample tests are accumulated and analyzed. The decision to pass to real trading is based on analysis of these trades. 

After passing to real trade, the process continues. Periodically, either according to the walk forward schedule, or whenever trading results are deteriorating, resynchronize the model to the data using the same process. 

#### These conditions are required for walk forward to work:
* the suystem is stationary for the combined length of the insample and out-of-sample periods.
* you are confident that the model selectedby your objective function as best based on in-sample optimization.
* There are several, preferably many, trades in each test period. 

### Some Other Way
If satisfactory walk forward results cannot be obtained, weaker validation techniques can be used:
* testing on other data series.
* testing on earlier time periods (weak technique)

## Next Chapters
There is a logical sequence of operations that model development follows:
* set goal and performance metrics
* choose the primary data series
* choose auxiliary data series
* date and time align the data series
* select and compute functions and indicators
* select the target
* reduce dimensions or change basis
* determine lengths of in-sample and out-of-sample periods
* learn
* test
* evaluate performance
* predict and trade

# Chapter 07. Model Development Indicator Based

## Objective Function
One of he first steps in indicator-based development is choice of the objective function. It must encapsulates and quantifies the subjective preferences of the developer, and assign a single-valued score to each set of trades evaluated (reward desirable characteristics and penalize underirable characteristics).

Important metrics to use in objective functions:
* Percentage gained per trade.
* Number of bars held.
* Number of trades per year.
* Percentage of trades that are winners.
* Percentage of time a position is held.
* Magnitude of losing trades.

Because **they are sequence dependent**, these metrics should be avoided:
* Maximum drawdown for the test period.
* Maximum losers in a row.
* Time between new highs.

> If available, CAR25 would be the preferred objective function.

You can use **'decathlon'** scoring: select, compute, scale, then add or multiply the metrics.

## Select Data Series
Begin with those series that have passed the risk and profit screen, are very liquid, and easily traded. Prefer those with high safe-f scores and high CAR25 scores. You can use any data series you want, but is easier to develop profitable, safe, tradable system with those characteristics.

## System Overview
While there may be a short/flat system for the same data series, I recommend developing long/flat separately first because:
* It is easier to identify bottoms and entries for long trades than tops and entries for short trades.
* Long/flat has fewer rules and parameters than long/flat/short.
* There is an upward bias in price related to factors such inflation, population growth, and productivity increase that favor being long equities.
* The characteristics of profitable long trades and profitable short trades are different for most issues. If a short/flat system does exist, it is probably not a reversal or symmetrical system.

## Indicator Selection
* We expect there about 15 to 50 ideal trades per year. To pick a specific number for discussion, say 24 trades per year.
* Signals generated by indicators are crossings or turnings. One indicator crosses another indicator, an indicator crosses a critical level, an indicator changes direction, or something similar.
* The indicator cycle (aka frequency of trade events/signals) must fit to price data and generates the desirable number of trades. For the trades we hope to identify, choosing a loockback (period between buy and sell) that is shorter than ideal (for example, to identify 24 trades in a year, the lookback period must be about 10 days) is more forgiving than choosing one that is longer than ideal. 
  
### Chart Patterns
Patterns in the sequence and relationship of OHLC for a few bars are easily identified and sometimes reliably precede price changes (for example, three consecutive higher closing prices are often followed by a fall in prices). Be aware that patterns are highly susceptible to overfitting.   

## Discovering Tradable Systems
There is some subjectivity, and it will require some experimentation on your part, to determine the best lengths to use for in-sample and out-of-sample periods. Try one year out-of-sample and 1-6 year in sample periods. Adjust as you learn the characteristics of the system. The lengths that work depend on the strength of the trading signal within the data's noise, stationarity of the signal, and robustness of the model to changes in synchronization.

## Summary
* Develop a statement of personal risk tolerance.
* Analyze potential data series to determine the risk and profit potential in each. 
* Using relatively simple entry rules, develop and backtest a series of odels to see if those issues have profitable trades that follow persistent patterns.
* Using an objective function to rank alternative systems, use the walk forward process to objectively choose systems.
* The final result is a set of trades, produced as objectively as possible, that are the best estimate of future performance of the system. 

# Chapter 08. Model Development Machine Learning

# Chapter 09. Trading Management

# Chapter 10. Summary and Random Thoughts
* Abandon Financial Astrology
* Become a competent programmer
* Bad data is worse than no data
* Think probabilistically
* Forecasts can change (improve with experience and new information)
* A simple algorithm with refined data usually outperforms a complex algorithm with raw data
* Trading systems are like blackjack. There is a model that works under some conditions
* Learn the mathmatics
* Nothing about financial data or trading systems is stationary.
* There are no physical laws governing the behavior of financial markets. If there were, new information would not matter much, and there would be little profit opportunity.
* Quantify your risk tolerance.
* The system results in an equity curve. Analysis of the equity curve determines the goodness of the system. That is, what is the terminal wealth and what is the drawdown.
* Financial data does not follow Normal distribution. Do not assume that it does, nor try to force it to be, nor naively use techniques that assume Normality.
* When you have enough, Quit. There is always a non-zero probability of an account destroying black swan event.

# Bibliography

Derman, E. (2011). Models behaving badly: Why confusing illusion with reality can lead to disaster, on Wall Street and in life. Wiley.

Savage, S. L. (2009). The flaw of averages: Why we underestimate risk in the face of uncertainty. Wiley.

Silver, N. (2021). O sinal e o ruído. Intrínseca.

Downey, A. B. (2015). Think Stats: Exploratory data analysis (2. ed). O’Reilly.

Downey, A. B. (2021). Think Bayes: Bayesian statistics in Python (Second edition). O’Reilly.

Gigerenzer, G. (2002). Calculated risks: How to know when numbers deceive you. Simon & Schuster.

Haigh, J. (2003). Taking chances: Winning with probability. Oxford University Press.

Stone, J. V. (2014). Bayes’ rule: A tutorial introduction to Bayesian analysis (First edition, third printing [with corrections]). Sebtel Press.

Connors, L. A., & Alvarez, C. (2012). How markets really work: A quantitative guide to stock market behavior (Second edition). John Wiley & Sons, Inc.








[def]: 41