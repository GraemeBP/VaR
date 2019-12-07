import numpy as np
import scipy.integrate as integrate

class HestonModel():

    def __init__(self, s, k, t, v, r, theta, kappa, sigma, rho):
        """
        :param s: stock price
        :param k: strike price
        :param t: time to maturity in years
        :param v: volatility
        :param r: risk free rate
        :param theta: long run average volatility
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

    def characteristic_function(self, phi, j):
        if j == 1:
            u = 0.5
            b = self.kappa - self.rho * self.sigma

        else:
            u = -0.5
            b = self.kappa

        a = (self.kappa * self.theta)
        x = np.log(self.s)

        d = np.sqrt((self.rho * self.sigma * phi * complex(0, 1) - b)**2
                    - self.sigma ** 2 * (2 * u * phi * complex(0, 1) - phi**2))

        # The below is actually 1/g. This is because when g is used it gives unstable prices. This is fixed with 1/g.
        # And changing the signs of d later on.
        g = (b - self.rho * self.sigma * phi * complex(0, 1) - d) / \
            (b - self.rho * self.sigma * phi * complex(0, 1) + d)

        c = self.r * phi * complex(0, 1) * self.t \
            + a / self.sigma ** 2 * ((b - self.rho * self.sigma * phi * complex(0, 1) - d)*self.t
                                     - 2 * np.log((1 - g * np.exp(-d * self.t)) / (1-g)))

        dd = (b - self.rho * self.sigma * phi * complex(0, 1) - d) / \
            self.sigma ** 2 * ((1 - np.exp(-d * self.t)) / (1 - g * np.exp(-d * self.t)))

        f = np.exp(c + dd * self.v + complex(0, 1) * phi * x)
        return f

    def integrand(self, phi, j):

        f = self.characteristic_function(phi, j)

        integrand = np.real(np.exp(-phi * complex(0, 1) * np.log(self.k)) * f / (phi * complex(0, 1)))
        return integrand

    def probability_function(self, j):

        integrated = integrate.quad(self.integrand, 0, np.inf, epsabs=0, args=j, full_output=0)
        # integrate.quad(self.integrand, lower limit, upper limit, args= extra arguments to pass through function )
        p = 0.5 + (1 / np.pi) * integrated[0]
        return p

    def european_call(self):
        call_price = self.s * (self.probability_function(1)) - self.k * np.exp(-self.r * self.t) * (self.probability_function(2))
        return call_price

    def european_put(self):
        put_price = - self.s * (self.probability_function(1)) + self.k * (self.probability_function(2))
        return put_price


hest = HestonModel(s=154.08, k=147, t=1/365, v=0.0105, r=0.1, theta=0.0837, kappa=74.32, sigma=3.4532, rho=-0.8912)

