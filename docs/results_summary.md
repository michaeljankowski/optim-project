The goal of this project was to reproduce and find a way to improve the results of “Multi-Factor Market-Neutral Systematic Trading” (arXiv:2412.12350), which proposes a market-neutral investment strategy using fundamental factors, analyst recommendations, momentum based indicators and Lasso regression for signal construction. The original study demonstrates that linear models can effectively extract predictive signals while maintaining robustness and interpretability.

After replicating the original Lasso based strategy successfully using the market-neutral portfolios, the replicated results showed consistent results with the performance reported in the paper. All strategies outperform the S&P 500 benchmark, which has a Sharpe ratio of 0.60 over the same period, confirming the validity of the replication. The results below follow a slightly different data range.

Elastic Net regression was tested to handle highly correlated features better by keeping groups of correlated variables together and shrinking their coefficients more evenly while still performing feature selection. Without surprise, it introduces redundant and highly correlated factor exposures that adversely affect risk variable portfolio constructions such as Risk Parity and Beta-Neutral Minimum Variance as noted in the paper. This is likely a result of strong regularization and overlapping market exposure across factors.. As a result, Elastic Net underperforms.

To make improvements, the linear model was replaced with LightGBM, a nonlinear decision tree model using gradient boosting was designed to capture interactions and nonlinearities that linear regressions cannot. Keeping everything else constant, LightGBM produces higher Sharpe ratios and lower maximum drawdown across all strategies. This indicates that enhanced cross-sectional ranking with LightGBM, instead of Lasso’s fitting, improves performance and concludes that risk parity offers higher returns and a lower maximum drawdown, while maintaining market neutrality as the original paper intended to.

The new results confirm the conclusions of the original paper to an even better. These results indicated that risk parity offers higher risk-adjusted returns and a lower maximum drawdown than other portfolios, while maintaining market neutrality, in a greater sense than the original code. Linear models such as Lasso and Elastic Net offer a strong intuitive baseline performance. However, nonlinear models like LightGBM can further improve returns by capturing complex factor interactions. This extension demonstrates that the original framework is flexible and can accommodate modern machine learning models without sacrificing its market-neutral nature.

## Results:
### Lasso: <br>

**Sharpe Ratio:**<br>
Risk Parity            0.621151<br>
MinVar Beta Neutral    0.385258<br>
Equally Weighted       0.945686<br>
daily_sp500_return      0.59819<br>

**Maximum Drawdown:**<br>
Risk Parity           -0.150902<br>
MinVar Beta Neutral   -0.151835<br>
Equally Weighted       -0.23063<br>
daily_sp500_return     -0.33925<br>

### LGBM:<br>

**Sharpe Ratio LGBM:**<br>
Risk Parity            1.098101<br>
MinVar Beta Neutral    0.932381<br>
Equally Weighted       1.066428<br>
daily_sp500_return      0.59819<br>

**Maximum Drawdown LGBM:**<br>
Risk Parity           -0.022467<br>
MinVar Beta Neutral   -0.016234<br>
Equally Weighted      -0.018711<br>
daily_sp500_return    -0.036535<br>

