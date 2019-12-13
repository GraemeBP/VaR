
import numpy as np
import scipy.stats as si


class BlackScholes():

    def __init__(self, s, k, t, sigma, d, r):
        self.s = s
        self.k = k
        self.t = t
        self.sigma = sigma
        self.d = d
        self.r = r

    def d1_european_call(self):
        d1 = (np.log(self.s / self.k) + (self.r - self.d + 0.5 * self.sigma ** 2) * self.t) / (
                np.sqrt(self.t) * self.sigma)
        return d1

    def d1_european_put(self):
        d1 = (np.log(self.s / self.k) + (self.r - self.d + 0.5 * self.sigma**2) * self.t) /\
             (np.sqrt(self.t) * self.sigma)
        return d1

    def d2_european_call(self):
        d2 = (np.log(self.s / self.k) + (self.r - self.d - 0.5* self.sigma**2) *self.t) / (np.sqrt(self.t) * self.sigma)
        return d2

    def d2_european_put(self):
        d2 = (np.log(self.s / self.k) + (self.r - self.d - 0.5 * self.sigma**2) * self.t) / \
             (np.sqrt(self.t) * self.sigma)
        return d2

    def european_call(self):
        """
        Calculate European Call Price based on the Black-Scholes models:
            The formula can be found here: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model

        :function si.norm.cdf: The cumulative distribution function of the standard normal distribution
        :param S:       Stock price of the underlying security
        :param K:       The strike price of the option, also frequently called exercise price.
        :param T:       Time to maturity in years.
        :param Sigma:   The volatility of returns of the underlying asset
        :param d:       The dividend yield. An annual rate, expressed in terms of continuous compounding.
        :param r:       The risk free rate. An annual rate, expressed in terms of continuous compounding.
        :return:        The price of a European call option via the Black Scholes Model
        """
        call_price = (self.s * np.exp(-self. d * self.t) * si.norm.cdf(self.d1_european_call())
                      - self.k * np.exp(-self.r * self.t) * si.norm.cdf(self.d2_european_call()))
        return call_price

    def european_put(self):
        """
        Calculate European Put Price based on the Black-Scholes models:
            The formula can be found here: https://en.wikipedia.org/wiki/Black%E2%80%93Scholes_model

        :function si.norm.cdf: The cumulative distribution function of the standard normal distribution
        :param S:       Stock price of the underlying security
        :param K:       The strike price of the option, also frequently called exercise price.
        :param T:       Time to maturity in years.
        :param Sigma:   The volatility of returns of the underlying asset
        :param d:       The dividend yield. An annual rate, expressed in terms of continuous compounding.
        :param r:       The risk free rate. An annual rate, expressed in terms of continuous compounding.
        :return:        The price of a European put option via the Black Scholes Model
        """

        put_price = (self.k * np.exp(-self.r * self.t) * si.norm.cdf(-self.d2_european_put())) \
                    - (self.s * np.exp(-self. d * self.t) * si.norm.cdf(-self.d1_european_put()))
        return put_price

    def greek_delta(self, option_type):
        """
        :param option_type: this is either "call" or "put"
        :return: Delta which is a measure of the change in an option's price resulting from a change in the
        underlying asset

        It can be interpreted as the probability of the option expiring in the money.
        """
        if option_type == "call":
            delta = si.norm.cdf(self.d1_european_call())

        elif option_type == "put":
            delta = si.norm.cdf(self.d1_european_put()) - 1

        return delta

    def greek_gamma(self, option_type):
        """
        :param option_type: this is either "call" or "put"
        :return: Gamma which measures delta's rate of change
        """
        if option_type == "call":
            d1 = self.d1_european_call()

        elif option_type == "put":
            d1 = self.d1_european_put()

        gamma = si.norm.pdf(d1) / (self.s * self.sigma * np.sqrt(self.t))

        return gamma

    def greek_vega(self, option_type):
        """
        :param option_type: this is either "call" or "put"
        :return: Vega which Measures Impact of a Change in Volatility
        """
        if option_type == "call":
            d1 = self.d1_european_call()

        elif option_type == "put":
            d1 = self.d1_european_put()

        vega = self.s * si.norm.pdf(d1) * np.sqrt(self.t)
        return vega

    def greek_rho(self, option_type):
        if option_type == "call":
            rho = self.k * self.t * np.exp(-self. r * self.t) * si.norm.cdf(self.d2_european_call())

        elif option_type == "put":
            rho = -self.k * self.t * np.exp(-self.r * self.t) * si.norm.cdf(-self.d2_european_call())
        return rho

    def greek_theta(self, option_type):
        if option_type == "call":
            theta = (-np.exp(-self.d * self.t)) * (self.s * si.norm.pdf(self.d1_european_call()) * self.sigma) / \
                    2 * np.sqrt(self.t) \
                    - self.r * self.k * (np.exp(-self.r * self.t)) * si.norm.cdf(self.d2_european_call()) \
                    + self.d * self.s * (np.exp(-self.d * self.t)) * si.norm.cdf(self.d1_european_call())

        elif option_type == "put":
            theta = (-np.exp(-self.d * self.t)) * (self.s * si.norm.pdf(self.d1_european_put()) * self.sigma) / \
                    2 * np.sqrt(self.t) \
                    + self.r * self.k * (np.exp(-self.r * self.t)) * si.norm.cdf(- self.d2_european_put()) \
                    - self.d * self.s * (np.exp(-self.d * self.t)) * si.norm.cdf(- self.d1_european_put())

        return theta


BlackS = BlackScholes(154.08, 155, 15/365, 0.2331, 0.0, 0.1)
BlackS.greek_gamma('call')