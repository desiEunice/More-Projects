##  Appling Principal Components Analysis on the Interest Rate Term Structure.

Essentially, term structure of interest rates is the relationship between interest rates or bond yields and different terms or maturities. When graphed, the term structure of interest rates is known as a yield curve, and it plays a crucial role in identifying the current state of an economy. (Investopedia)


### PCA

Principal Component Analysis (PCA) technique is used to reduce the dimensionality of a data set, finding the causes of variability and sorting them by importance. Its general objective is extract signal from data by finding the least amount of variables that explain the largest proportion of the data making it easier to interpret.


### Yield Curve

The yield curve shows the interest rates the government must pay to borrow money across different maturites.
According to the expectations theory of interest rates, the yield curve is made up of two aspects:
- An average of market expectations concerning future short-term interest rates.
- The term premium — the extra compensation an investor receives for holding a
longer-term bond. This is essentially because of the time value of money — $100 is worth more today than it is worth tomorrow, due to its potential earning capacity due to interest. Therefore, for a fixed-income investment to be worth the extra time the investor must part with their cash, the bond issuer must pay the investor some extra amount.


### Project Objective

- To model the yield curve dynamics to identify the fundamental yield curve movements. 
- To determine the number of principal components required to sufficiently explain the yield curve for ...  data.

To illustrate PCA on interest rates movements, we consider the multivariate time series of daily [U.S. Treasury Interest Rate](https://home.treasury.gov/policy-issues/financing-the-government/interest-rate-statistics?data=yield) over a 10-year period from 2011 to 2020.

![plot](More-Projects/Applying PCA to the Yield Curve /README.md/yield_curve.png)








