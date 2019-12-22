from src.options.black_scholes.black_scholes import BlackScholes
from matplotlib import pyplot as plt
from numpy import arange


class GraphGreeksBS:
    def __init__(self, greek, initial_condition, model_parameter, start, finish, step, option_type):
        self.greek = greek
        self.s = initial_condition[0]
        self.k = initial_condition[1]
        self.t = initial_condition[2]
        self.sigma = initial_condition[3]
        self.d = initial_condition[4]
        self.r = initial_condition[5]

        self.model_parameter = model_parameter
        self.start = start
        self.finish = finish
        self.step = step

        self.option_type = option_type

    def parameter_update(self, new_parameter_value):
        if self.model_parameter == "s":
            self.s = new_parameter_value
        elif self.model_parameter == "k":
            self.k = new_parameter_value
        elif self.model_parameter == "t":
            self.t = new_parameter_value
        elif self.model_parameter == "sigma":
            self.sigma = new_parameter_value
        elif self.model_parameter == "d":
            self.d = new_parameter_value
        elif self.model_parameter == "r":
            self.r = new_parameter_value

    def greek_simulation(self):

        new_parameter_value_list = []
        greek_values = []
        # Arange is used rather than range because it allows for decimal steps
        for i in arange(self.start, self.finish + self.step, self.step):
            new_parameter_value = i
            new_parameter_value_list.append(new_parameter_value)
            self.parameter_update(new_parameter_value)

            bs_inputs = BlackScholes(self.s, self.k, self.t, self.sigma, self.d, self.r)

            if self.greek == "delta":
                greek_values.append(bs_inputs.greek_delta(self.option_type))
            elif self.greek == "gamma":
                greek_values.append(bs_inputs.greek_gamma(self.option_type))
            elif self.greek == "vega":
                greek_values.append(bs_inputs.greek_vega(self.option_type))
            elif self.greek == "rho":
                greek_values.append(bs_inputs.greek_rho(self.option_type))
            elif self.greek == "theta":
                greek_values.append(bs_inputs.greek_theta(self.option_type))

        return new_parameter_value_list, greek_values

    def greek_plot(self):

        (new_parameter_value_list, greek_values) = self.greek_simulation()
        plt.plot(new_parameter_value_list, greek_values)

        plt.ylabel(self.greek)
        if self.model_parameter == "s":
            plt.xlabel("stock price")
        elif self.model_parameter == "k":
            plt.xlabel("strike price")
        elif self.model_parameter == "t":
            plt.xlabel("time to maturity")
        elif self.model_parameter == "sigma":
            plt.xlabel("volatility")
        elif self.model_parameter == "r":
            plt.xlabel("interest rate")
        elif self.model_parameter == "d":
            plt.xlabel("dividends")
        plt.show()


BS = [154.08, 155, 15/365, 0.2331, 0.0, 0.1]
BSClass_Test = GraphGreeksBS(greek='theta',
                             initial_condition=BS,
                             model_parameter='s',
                             start=120,
                             finish=190,
                             step=1,
                             option_type="call")
BSClass_Test.greek_plot()







