from src.heston_model.heston_model import HestonModel


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

        greek_values = []
        for i in range(self.start, self.finish + self.step, self.step):
            new_parameter_value = i
            self.parameter_update(new_parameter_value)

            Hest = HestonModel(self.s, self.k, self.t, self.v, self.r, self.theta, self.kappa, self.sigma, self.rho)

            if self.greek == "delta":
                greek_values.append(Hest.greek_delta())

        return greek_values


hest_list = [154.08, 147, 1/365, 0.0105, 0.1, 0.0837, 74.32, 3.4532, -0.8912]
Class_Test = GraphGreeksHeston(greek='delta', initial_condition= hest_list, model_parameter = 's', start=150, finish=160, step=1)







