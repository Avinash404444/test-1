# Install dependencies first: pip install numpy scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

temp = ctrl.Antecedent(np.arange(0, 41, 1), "temp")
speed = ctrl.Consequent(np.arange(0, 101, 1), "speed")
temp["cold"] = fuzz.trimf(temp.universe, [0, 0, 20])
temp["warm"] = fuzz.trimf(temp.universe, [15, 25, 35])
temp["hot"] = fuzz.trimf(temp.universe, [30, 40, 40])
speed["low"] = fuzz.trimf(speed.universe, [0, 0, 50])
speed["medium"] = fuzz.trimf(speed.universe, [30, 50, 70])
speed["high"] = fuzz.trimf(speed.universe, [60, 100, 100])
rules = [
    ctrl.Rule(temp["cold"], speed["low"]),
    ctrl.Rule(temp["warm"], speed["medium"]),
    ctrl.Rule(temp["hot"], speed["high"])
]
simulation = ctrl.ControlSystemSimulation(ctrl.ControlSystem(rules))
simulation.input["temp"] = 32
simulation.compute()
print("Fan Speed:", round(simulation.output["speed"], 2))
