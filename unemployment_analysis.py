import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("unemployment_data.csv")

print("Dataset Preview:")
print(df.head())

# Basic Info
print("\nDataset Info:")
print(df.info())

# Average unemployment by region
avg_unemployment = df.groupby("Region")["Unemployment_Rate"].mean()
print("\nAverage Unemployment Rate by Region:")
print(avg_unemployment)

# Plot for each region
regions = df["Region"].unique()

for region in regions:
    data = df[df["Region"] == region]
    plt.plot(data["Year"], data["Unemployment_Rate"], marker='o', label=region)

plt.title("Unemployment Rate Trend")
plt.xlabel("Year")
plt.ylabel("Unemployment Rate")
plt.legend()
plt.grid()
plt.show()