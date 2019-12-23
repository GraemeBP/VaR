from src.processes.heston_process import HestonProcess
from numpy import mean, exp, maximum, arange
from matplotlib import pyplot as plt


class DiffusionHestonModel:
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

    def diffusion_model(self, simulations, time_steps, option_type, graph='No'):
        model_inputs = HestonProcess(s=self.s,
                                     k=self.k,
                                     t=self.t,
                                     v=self.v,
                                     r=self.r,
                                     theta=self.theta,
                                     kappa=self.kappa,
                                     sigma=self.sigma,
                                     rho=self.rho)
        (s, v) = model_inputs.diffusion(simulations, time_steps)

        if graph == 'Yes':
            plt.figure()
            plt.plot(arange(0, self.t * 365, self.t / time_steps * 365), mean(s, axis=0), label='Stock Price')
            plt.legend()
            plt.ylabel("Stock Price")
            plt.xlabel("Time (Days)")
            plt.title("Heston's Stock Price Diffusion")
            plt.grid()
            plt.show()

            plt.figure()
            plt.plot(arange(0, self.t * 365, self.t / time_steps * 365), mean(v, axis=0), label='Volatility')
            plt.legend()
            plt.ylabel("Volatility")
            plt.xlabel("Time (Days)")
            plt.title("Heston Volatility Diffusion")
            plt.grid()
            plt.show()


        expected_value = s[time_steps-1]
        if option_type == 'call':
            return mean((maximum(expected_value - self.k, 0)) * exp(-self.r * self.t), axis=0)
        elif option_type == 'put':
            return mean((maximum(expected_value - self.k, 0)) * exp(-self.r * self.t), axis=0)





hest = DiffusionHestonModel(s=150,
                            k=155,
                            t=15/365,
                            v=0.0105,
                            r=0.1,
                            theta=0.0837,
                            kappa=74.32,
                            sigma=3.4532,
                            rho=-0.8912)




