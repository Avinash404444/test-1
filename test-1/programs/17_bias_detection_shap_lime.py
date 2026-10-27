# Install: pip install shap lime scikit-learn pandas
import pandas as pd
import shap
from lime.lime_tabular import LimeTabularExplainer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

df = pd.DataFrame({
    "Age": [22, 25, 30, 35, 40, 45, 50, 55, 28, 38, 48, 60],
    "Gender": [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0],
    "Education": [1, 2, 2, 3, 3, 4, 4, 4, 1, 3, 4, 5],
    "Income": [0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1]
})
X = df[["Age", "Gender", "Education"]]
y = df["Income"]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=1, stratify=y
)
model = RandomForestClassifier(random_state=1)
model.fit(X_train, y_train)

test = X_test.copy()
test["Prediction"] = model.predict(X_test)
print("Prediction rate by gender:")
print(test.groupby("Gender")["Prediction"].mean())

explainer = shap.TreeExplainer(model)
print("\nSHAP values:")
print(explainer.shap_values(X_test))

lime = LimeTabularExplainer(
    X_train.values, feature_names=list(X.columns),
    class_names=["Low Income", "High Income"], mode="classification"
)
explanation = lime.explain_instance(
    X_test.iloc[0].values, model.predict_proba, num_features=3
)
print("\nLIME explanation:")
print(explanation.as_list())
