import numpy as np
import scipy.stats as si

def BSCall(S, K, T, Sigma, d, r):

    """
    Calculate European Call Price based on the Black-Scholes models:
        The formula can be found here: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model

    :function si.norm.cdf: The cumulative distribution function of the standard normal distribution
    :param S:       Stock price
    :param K:       The strike price of the option, also frequently called exercise price.
    :param T:       Time to maturity in years.
    :param Sigma:   The volatility of returns of the underlying asset
    :param d:       The dividend yield. An annual rate, expressed in terms of continuous compounding.
    :param r:       The risk free rate. An annual rate, expressed in terms of continuous compounding.
    :return:        The price of a European call option via the Black Scholes Model
    """
    d1 = (np.log(S / K) + (r - d + 0.5*Sigma**2)*T) / (np.sqrt(T)*Sigma)
    d2 = (np.log(S / K) + (r - d - 0.5*Sigma**2)*T) / (np.sqrt(T)*Sigma)

    call_price = (S * np.exp(-d*T) * si.norm.cdf(d1, 0.0, 1.0) - K * np.exp(-r * T) * si.norm.cdf(d2, 0.0, 1.0))
    return call_price
graeme  = BSCall(100,100,1,0.1,0,0.05)

def BSPut(S, K, T, Sigma, d, r):
    d1 = (np.log(S / K) + (r - d + 0.5*Sigma**2)*T) / (np.sqrt(T)*Sigma)
    d2 = (np.log(S / K) + (r - d - 0.5*Sigma**2)*T) / (np.sqrt(T)*Sigma)

    put_price = (K * np.exp(-r * T) * si.norm.cdf(-d2, 0.0, 1.0)) - (S * np.exp(-d*T) * si.norm.cdf(-d1, 0.0, 1.0))
    return put_price