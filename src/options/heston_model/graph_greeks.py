from src.options.heston_model.heston_model import HestonModel
from matplotlib import pyplot as plt
from numpy import arange


class GraphGreeksHeston:
    def __init__(self, greek, initial_condition, model_parameter, start, finish, step, step_floats, option_type):

        self.greek = greek
        self.s = initial_condition[0]
        self.k = initial_condition[1]
        self.t = initial_condition[2]
        self.v = initial_condition[3]
        self.r = initial_condition[4]
        self.theta = initial_condition[5]
        self.kappa = initial_condition[6]
        self.sigma = initial_condition[7]
        self.rho = initial_condition[8]

        self.model_parameter = model_parameter
        self.start = start
        self.finish = finish
        self.step = step
        self.step_floats = step_floats

        self.option_type = option_type

    def parameter_update(self, new_parameter_value):
        if self.model_parameter == "s":
            self.s = new_parameter_value
        elif self.model_parameter == "k":
            self.k = new_parameter_value
        elif self.model_parameter == "t":
            self.t = new_parameter_value
        elif self.model_parameter == "v":
            self.v = new_parameter_value
        elif self.model_parameter == "r":
            self.r = new_parameter_value
        elif self.model_parameter == "theta":
            self.theta = new_parameter_value
        elif self.model_parameter == "kappa":
            self.kappa = new_parameter_value
        elif self.model_parameter == "sigma":
            self.sigma = new_parameter_value
        elif self.model_parameter == "rho":
            self.rho = new_parameter_value

    def greek_simulation(self):
        new_parameter_value_list = []
        greek_values = []
        # Arange is used rather than range because it allows for decimal steps
        for i in arange(self.start, self.finish + self.step, self.step):
            # I have rounded it because it sometimes leads to not exact results
            new_parameter_value = round(i, self.step_floats)
            new_parameter_value_list.append(new_parameter_value)
            self.parameter_update(new_parameter_value)

            heston_inputs = HestonModel(self.s, self.k, self.t, self.v, self.r, self.theta, self.kappa, self.sigma, self.rho)
            if self.greek == "delta":
                greek_values.append(heston_inputs.greek_delta(self.option_type))
            elif self.greek == "gamma":
                greek_values.append(heston_inputs.greek_gamma(self.option_type))
            elif self.greek == "vega":
                greek_values.append(heston_inputs.greek_vega(self.option_type))
            elif self.greek == "rho":
                greek_values.append(heston_inputs.greek_rho(self.option_type))
            elif self.greek == "volga":
                greek_values.append(heston_inputs.greek_volga(self.option_type))
            elif self.greek == "vanna":
                greek_values.append(heston_inputs.greek_vanna(self.option_type))
            elif self.greek == "theta":
                greek_values.append(heston_inputs.greek_theta(self.option_type))

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
        elif self.model_parameter == "v":
            plt.xlabel("initial volatility")
        elif self.model_parameter == "r":
            plt.xlabel("interest rate")
        elif self.model_parameter == "theta":
            plt.xlabel("long run average volatility")
        elif self.model_parameter == "kappa":
            plt.xlabel("speed on conversation")
        elif self.model_parameter == "sigma":
            plt.xlabel("volatility of volatility")
        elif self.model_parameter == "rho":
            plt.xlabel("correlation of wiener process")
        plt.grid()
        plt.show()


# HestonModel(s,      k,     t,     v,     r,  theta, kappa, sigma,   rho)
hest_list = [154.08, 155, 15/365, 0.0105, 0.1, 0.0837, 74.32, 3.4532, -0.8912]
Class_Test = GraphGreeksHeston(greek='delta',
                               initial_condition=hest_list,
                               model_parameter='s',
                               start=120,
                               finish=190,
                               step=0.1,
                               step_floats=1,
                               option_type='put')
Class_Test.greek_plot()







