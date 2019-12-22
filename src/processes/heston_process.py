from numpy import zeros, random, sqrt, arange, abs
import matplotlib.pyplot as plt


class HestonProcess:

    def __init__(self, s, k, t, v, r, theta, kappa, sigma, rho):
        """
        :param s: stock price
        :param k: strike price
        :param t: time to maturity in years
        :param v: volatility
        :param r: risk free rate
        :param theta: long run average volatility (vbar)
        :param kappa: mean reversion (speed) of variance to long run average
        :param sigma: volatility of volatility (vvol)
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

    def diffusion(self, time_steps, simulations):
        dt = self.t / time_steps

        s = zeros((simulations, time_steps))
        s[:, 0] = self.s

        v = zeros((simulations, time_steps))
        v[:, 0] = self.v

        w1 = random.standard_normal((simulations, time_steps))

        z2 = random.standard_normal((simulations, time_steps))
        w2 = self.rho * w1 + (sqrt(1-self.rho**2)) * z2

        for i in range(0, time_steps-1):
            v[:, i + 1] = abs(
                                v[:, i] +
                                self.kappa * (self.theta - v[:, i]) * dt +
                                self.sigma * sqrt(v[:, i]) * w2[:, i] * sqrt(dt)
            )

            s[:, i + 1] = s[:, i] + \
                          self.r * self.s * dt + \
                          self.sigma * sqrt(v[:, i + 1]) * w2[:, i]

        return s, v, w1, w2


hest = HestonProcess(s=150,
                     k=155,
                     t=15/365,
                     v=0.0105,
                     r=0.1,
                     theta=0.0837,
                     kappa=74.32,
                     sigma=3.4532,
                     rho=-0.8912)
