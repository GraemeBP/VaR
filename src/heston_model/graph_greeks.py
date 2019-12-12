from src.heston_model.heston_model import HestonModel
from matplotlib import pyplot as plt


class GraphGreeksHeston():
    def __init__(self, greek, initial_condition, model_parameter, start, finish, step):
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
        for i in range(self.start, self.finish + self.step, self.step):
            new_parameter_value = i
            new_parameter_value_list.append(new_parameter_value)
            self.parameter_update(new_parameter_value)

            Hest = HestonModel(self.s, self.k, self.t, self.v, self.r, self.theta, self.kappa, self.sigma, self.rho)

            if self.greek == "delta":
                greek_values.append(Hest.greek_delta())
            elif self.greek == "gamma":
                greek_values.append(Hest.greek_gamma())
            elif self.greek == "vega":
                greek_values.append(Hest.greek_vega())
            elif self.greek == "rho":
                greek_values.append(Hest.greek_rho())
            elif self.greek == "volga":
                greek_values.append(Hest.greek_volga())
            elif self.greek == "vanna":
                greek_values.append(Hest.greek_vanna())
            elif self.greek == "theta":
                greek_values.append(Hest.theta_h())

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
            plt.xlabel("correlation of weiner process")
        plt.show()


# hest = HestonModel(s=154.08, k=147, t=1/365, v=0.0105, r=0.1, theta=0.0837, kappa=74.32, sigma=3.4532, rho=-0.8912)

hest_list = [154.08, 155, 15/365, 0.0105, 0.1, 0.0837, 74.32, 3.4532, -0.8912]
Class_Test = GraphGreeksHeston(greek='gamma',
                               initial_condition=hest_list,
                               model_parameter='s',
                               start=120,
                               finish=190,
                               step=1)
Class_Test.greek_plot()







