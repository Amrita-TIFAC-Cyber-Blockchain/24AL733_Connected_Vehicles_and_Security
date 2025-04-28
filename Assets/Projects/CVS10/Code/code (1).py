#!/usr/bin/env python
# coding: utf-8

# In[31]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt  
import plotly.express as px
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error

file_path = r"TripA01.csv"

# Try reading the file with a different encoding
df = pd.read_csv(file_path, sep=";", encoding="ISO-8859-1", on_bad_lines='skip')

df.head()  # Display first few rows


# In[32]:


plt.figure(figsize=(12, 8))
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", fmt=".1f")
plt.title("Feature Correlation Heatmap")
plt.show()


# In[33]:


df.columns


# In[34]:


def mean_absolute_percentage_error(y_true, y_pred):
    y_true, y_pred = np.array(y_true), np.array(y_pred)
    return np.mean(np.abs((y_true - y_pred) / y_true)) * 100


# In[35]:


# Assuming 'df' is already loaded in your environment
selected_features = ['Time [s]',"Battery Voltage [V]",'Elevation [m]', 
                     "max. Battery Temperature [°C]", "Velocity [km/h]", 
                     "Ambient Temperature [°C]", 'Heat Exchanger Temperature [°C]', 'Cabin Temperature Sensor [°C]']

# Splitting into features (X) and target (y)
X = df[selected_features]
y = df["SoC [%]"]  # Ensure this column exists

# Train-test split (80-20)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Training size:", X_train.shape, "Testing size:", X_test.shape)

# Model initialization and training
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Predictions and evaluation
y_pred = model.predict(X_test)
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
mape = mean_absolute_percentage_error(y_test, y_pred)

print(f"MAE: {mae:.3f}")
print(f"MSE: {mse:.3f}")
print(f"RMSE: {rmse:.3f}")
print(f"MAPE: {mape:.2f}%")

# Feature Importance
feature_importance = pd.Series(model.feature_importances_, index=selected_features).sort_values(ascending=False)
print("\nFeature Importance:")
print(feature_importance)


# In[37]:


# Create a DataFrame for better visualization
df_res = pd.DataFrame({"Actual": y_test, "Predicted": y_pred})

df_res = df_res.reset_index(drop = True)

# Plot
fig = px.line(df_res, x=df_res.index, y=["Actual", "Predicted"], 
              markers=True, title="Actual vs. Predicted Values",
              labels={"value": "Values", "variable": "Legend"})

fig.show()


# In[ ]:




