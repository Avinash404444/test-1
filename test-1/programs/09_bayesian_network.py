# Install dependency first: pip install pgmpy
from pgmpy.models import DiscreteBayesianNetwork
from pgmpy.factors.discrete import TabularCPD
from pgmpy.inference import VariableElimination

model = DiscreteBayesianNetwork([("Rain", "Traffic"), ("Accident", "Traffic")])
cpd_rain = TabularCPD("Rain", 2, [[0.7], [0.3]])
cpd_accident = TabularCPD("Accident", 2, [[0.9], [0.1]])
cpd_traffic = TabularCPD(
    "Traffic", 2,
    [[0.9, 0.6, 0.7, 0.3], [0.1, 0.4, 0.3, 0.7]],
    evidence=["Rain", "Accident"], evidence_card=[2, 2]
)
model.add_cpds(cpd_rain, cpd_accident, cpd_traffic)
print("Model is valid:", model.check_model())
result = VariableElimination(model).query(
    variables=["Traffic"], evidence={"Rain": 1, "Accident": 1}
)
print(result)
