import numpy as np
import scipy.integrate as integrate
import scipy.pi as pi

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

    def characteristic_function(self, j, phi):
        if j == 1:
            u = 0.5
            b = self.kappa - self.rho * self.sigma
        else:
            u = -0.5
            b = self.kappa

        a = (self.kappa * self.theta)

        d = np.sqrt((self.rho * self.sigma * phi - b)**2 - (self.sigma**2) * (2 * u * phi * - phi**2))
        g = (b - (self.rho * self.sigma * phi) + d) / (b - (self.rho * self.sigma * phi) - d)

        c = self.r * phi * self.t \
            + (a / (self.v**2)) * (b - self.rho * self.sigma * phi + d)*self.t \
            - 2 * np.log(1 - g * np.exp(d * self.t) / (1-g))

        d = ((b - self.rho * self.sigma * phi + d)/(self.sigma**2)) * ((1-np.exp(d * self.t)) / 1 - g * np.exp(d * self.t))

        f = np.exp(c + d + phi * self.s)

        return f

    def integrand(self, j, phi):

        f = self.characteristic_function(j, phi)

        integrand = np.real(((np.exp(-phi * np.log(self.k))) * f)/phi)
        return integrand

    def probability_function(self, j):

        integrated = integrate.quad(self.integrand, 0, np.inf, args=j)

        p = 0.5 * (1/pi) * integrated
        return p

    def european_call(self):
        call_price = self.t * (self.probability_function(1)) - self.k * np.exp(-self.r * self.t) * (self.probability_function(2))
        return call_price

    def european_put(self):
        put_price = - self.t * (self.probability_function(1, phi)) + self.k * (self.probability_function(2, phi))
        return put_price



