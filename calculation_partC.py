 # import packages
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt
import seaborn as sns
 
# loading the csv file
df = pd.read_csv('raw_training.csv')
print(df.head())
 
# fitting the model
# df.columns = ['"Concrete compressive strength(MPa, megapascals) "', 'Cement (component 1)(kg in a m^3 mixture)','Blast Furnace Slag (component 2)(kg in a m^3 mixture)','Fly Ash (component 3)(kg in a m^3 mixture)','Water  (component 4)(kg in a m^3 mixture)','Superplasticizer (component 5)(kg in a m^3 mixture)','Coarse Aggregate  (component 6)(kg in a m^3 mixture)','Fine Aggregate (component 7)(kg in a m^3 mixture)','Age (day)']

df.columns = [
    "Cement", "Blast_Furnace_Slag", "Fly_Ash",
    "Water", "Superplasticizer", "Coarse_Aggregate", "Fine_Aggregate", "Age", "Concrete_compressive_strength"
]

formula = "Concrete_compressive_strength ~ Cement + Blast_Furnace_Slag + Fly_Ash + Water + Superplasticizer + Coarse_Aggregate + Fine_Aggregate + Age"

model = smf.ols(formula=formula, data=df).fit()

# https://stackoverflow.com/questions/41075098/how-to-get-the-p-value-in-a-variable-from-olsresults-in-python
p_values = model.pvalues
print(p_values)
print(model.summary())

df["Predicted_Strength"] = model.predict(df)


# https://www.geeksforgeeks.org/python-seaborn-tutorial/
sns.scatterplot(x=df["Concrete_compressive_strength"], y=df["Predicted_Strength"], alpha=0.1)
sns.regplot(x=df["Concrete_compressive_strength"], y=df["Predicted_Strength"], scatter=False, color="green")
# plt.scatter(df.index, df["Concrete_compressive_strength"], color='blue', label="Actual", alpha=0.1)
# plt.plot(df.index, df["Predicted_Strength"], color='red', label="Predicted")

plt.title("Observed vs. Predicted Concrete Compressive Strength")

plt.xlabel("Observed Concrete Compressive Strength (MPa)")
plt.ylabel("Predicted Concrete Compressive Strength (MPa)")

plt.grid(True)

plt.show()