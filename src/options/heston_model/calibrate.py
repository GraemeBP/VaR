from scipy.optimize import minimize
from src.options.heston_model.heston_model import HestonModel
from numpy import array


class CalibrateHeston:
    def __init__(self, initial_guess, bounds, known):
        """
            :param v: volatility
            :param theta: long run average volatility (vbar)
            :param kappa: mean reversion (speed) of variance to long run average
            :param sigma: volatility of volatility (vvol)
            :param rho: correlation between the brownian motion of the stock price and the volatility.
        """

        self.initial_guess = initial_guess
        self.bounds = bounds
        self.known = known

    def objective(self, guess):
        # HestonModel(s, k, t, v, r, theta, kappa, sigma, rho)
        heston = HestonModel(self.known[0], self.known[1], self.known[2], guess[0], self.known[3],
                             guess[1], guess[2], guess[3], guess[4])

        pred_price = heston.european_call()
        print("Predicted Price")
        print(pred_price)
        print("Predicted Params")
        print(guess)

        actual_price = self.known[4]
        print("Diff")
        print(actual_price - pred_price)
        return abs(actual_price - pred_price)

    def local_optimisation(self):
        result = minimize(self.objective, self.initial_guess, bounds=self.bounds)
        return result


# initial_guess(v, theta, kappa, sigma, rho)
initial_guess = array([0.09, 0.295, 0.9, 0.7, -0.2])
bounds = array([(0, 1), (0, 1), (0, 5), (0, 5), (-1, 1)])
# known = array([328.29, 275, 0.1753424, 0.000553778, 56.9])
known = array([[328.29, 275, 0.1753424, 0.000553778, 56.9], [328.29, 300, 0.1753424, 0.000553778, 36.3]])

cali = CalibrateHeston(initial_guess, bounds, known)
output = cali.local_optimisation()
