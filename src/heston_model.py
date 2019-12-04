import numpy as np

class HestonModel():

    def __init__(self, s, k, t, v, r, theta, kappa, sigma, rho):
        """
        :param s: stock price
        :param k: strike price
        :param t: time to maturity in years
        :param v: volatility
        :param r: risk free rate
        :param theta: long run average of volatility
        :param kappa: mean reversion (speed) of variance to long run average
        :param sigma: volatility of volatility
        :param rho: correlation between the brownian motion of the stock price and the volatility.
        """
        self.s = s
        self.k = k
        self.t = t
        self.v = v
        self.r = r
        self.theta = theta
        self.kappa = kappa
        self.sigma = sigma
        self.rho = rho

    def charachteristic_function(self):
        if j==1:
            u = 0.5
            b = self.kappa + self.lambd - self.rho * self.sigma
        else:
            u = -0.5
            b = self.kappa

        a = (self.kappa * self.theta)

        d = np.sqrt((self.rho * self.sigma * self.phi - b)**2 - (self.sigma**2) * (2 * u * self.phi * - self.phi**2))
        g = (b - (self.rho * self.sigma * self.phi) + d) / (b - (self.rho * self.sigma * self.phi) - d)

        c = self.r * self.PHI * self.t \
            + (a / (self.v**2)) * (b - self.rho * self.sigma * self.PHI + d)*self.t \
            - 2 * np.log(1 - g * np.exp(d * self.t) / (1-g))

        d = ((b - self.rho * self.sigma * self.phi + d)/(self.sigma**2)) * ((1-np.exp(d * self.t)) / 1 - g * np.exp(d * self.t))

        f = np.exp(c + d + self.phi * self.s)

        return f




