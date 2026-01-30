# Multi-Factor Market-Neutral Trading



## Overview
This project replicates and extends the results from the paper  
“Multi-Factor Market-Neutral Systematic Trading” (arXiv:2412.12350)
using WRDS/Compustat equity data from 2013–2024.  

The objective was to reproduce the original paper’s baseline (linear factor model)
and test alternative approaches, such as Elastic Net and nonlinear models such as LightGBM, to evaluate whether
nonlinear methods improve risk-adjusted returns while maintaining market neutrality.

### Key Findings
- LightGBM consistently outperforms LASSO by capturing nonlinear relationships and feature interactions that linear models miss.

- Elastic Net, while effective at handling correlated features, can retain overlapping market exposures that negatively affect diversification in certain portfolio frameworks.

- Portfolio construction choices play a critical role in determining whether predictive signals translate into robust performance.

### Technology and Tools

Python

NumPy / pandas

Optimizaiton tools

#### Author

Michael Jankowski  
Computer Science & Applied Mathematics  
University of Connecticut
