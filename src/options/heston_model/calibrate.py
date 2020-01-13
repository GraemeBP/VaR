from scipy.optimize import minimize, differential_evolution
from src.options.heston_model.heston_model import HestonModel
from numpy import array
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

class CalibrateHeston:
    def __init__(self, initial_guess, bounds, known, optmisation_type, graph="n"):
        """
            :param v: volatility
            :param theta: long run average volatility (vbar)
            :param kappa: mean reversion (speed) of variance to long run average
            :param sigma: volatility of volatility (vvol)
            :param rho: correlation between the brownian motion of the stock price and the volatility.
        """
        self.known_s = known['s']
        self.known_r = known['r']
        self.known_t = known['t']
        self.known_k = known['k']
        self.known_c = known['c']

        self.initial_guess = initial_guess
        self.bounds = bounds
        self.optimisation_type = optmisation_type
        self.graph = graph
    def objective(self, guess):
        sum_of_relative_difference = 0
        # HestonModel(s, k, t, v, r, theta, kappa, sigma, rho)
        for i in range(0, 4):

            heston = HestonModel(self.known_s[i], self.known_k[i], self.known_t[i], guess[0], self.known_r[i],
                                 guess[1], guess[2], guess[3], guess[4])

            pred_price = heston.european_call()
            print("Predicted Price {}".format(pred_price))
            print("Predicted Params {}".format(guess))

            actual_price = self.known_c[i]
            print("Diff {}".format(actual_price - pred_price))
            trade_abs_difference = abs(actual_price - pred_price)
            trade_relative_difference = trade_abs_difference/actual_price

            sum_of_relative_difference = sum_of_relative_difference + trade_relative_difference

            print("Sum of rel difference {}".format(sum_of_relative_difference))
        return sum_of_relative_difference

    def local_optimisation(self):
        result = minimize(self.objective, self.initial_guess, bounds=self.bounds, tol=0.05)
        return result

    def global_optimisation(self):
        result = differential_evolution(self.objective, self.bounds)
        return result

    def graph_output(self, result):

        [v_calibrated, theta_calibrated, kappa_calibrated, sigma_calibrated, rho_calibrated] = result.x

        call_price = []
        strike_price = []
        maturity = []

        for i in range(0, 4):

            heston = HestonModel(self.known_s[i], self.known_k[i], self.known_t[i], v_calibrated, self.known_r[i],
                                 theta_calibrated, kappa_calibrated, sigma_calibrated, rho_calibrated)

            call_price.append(heston.european_call())
            strike_price.append(self.known_k[i])
            maturity.append(self.known_t[i])

            print(call_price)

        fig = plt.axes(projection='3d')
        fig.plot3D(strike_price, maturity, call_price, 'gray')

    def run_optimisation(self):
        if self.optimisation_type == 'local':

            result = self.local_optimisation()
            if self.graph == "y":
                self.graph_output(result)
            return result
        elif self.optimisation_type == 'global':
            result = self.global_optimisation()
            if self.graph == "y":
                self.graph_output(result)
            return result
        else:
            return print('Optimisation type should be local or global')

# initial_guess(v, theta, kappa, sigma, rho)
initial_guess = array([0.09, 0.295, 0.9, 0.7, -0.2])
bounds = array([(0, 1), (0, 1), (0, 5), (0, 5), (-1, 1)])

# s0, v0, theta, kappa, sigma, r, rho, t, k)
known = pd.read_excel(r"C:\Users\rp413vx\PycharmProjects\VaR_NEW\data\Heston_Calibration_Data.xlsx",sheet_name="Data")


cali = CalibrateHeston(initial_guess, bounds, known, 'local', graph='y')
output = cali.run_optimisation()
