import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(42)

normal_times = np.round(np.random.normal(loc=32, scale=8, size=97), 1)
late_times = np.array([68, 71, 75])
delivery_times = np.concatenate([normal_times, late_times])

data = {
    "OrderID": np.arange(1, 101),
    "DeliveryTime(min)": delivery_times
}
pd.DataFrame(data).to_csv("delivery_times.csv", index=False)

df = pd.read_csv("delivery_times.csv")
times = df["DeliveryTime(min)"]

# TASK A
real_mean = times.mean()
real_std = times.std()
print("Real delivery times -- Mean:", round(real_mean, 1), "min Std:", round(real_std, 1), "min")

# TASK B
simulated_times = np.random.normal(loc=real_mean, scale=real_std, size=100)
print("Simulated 100 values from Normal(mean=" + str(round(real_mean, 1)) + ", std=" + str(round(real_std, 1)) + ")")

# TASK C
plt.figure(figsize=(7, 4))
plt.hist(times, bins=15, alpha=0.6, color="steelblue", label="Real")
plt.hist(simulated_times, bins=15, alpha=0.6, color="indianred", label="Simulated")
plt.xlabel("Delivery Time (min)")
plt.ylabel("Number of Deliveries")
plt.title("Real vs. Simulated Delivery Times")
plt.legend()
plt.tight_layout()
plt.savefig("delivery_comparison_histogram.png")

# TASK D
print("Missing values:", df["DeliveryTime(min)"].isnull().sum())

plt.figure(figsize=(4, 4))
plt.boxplot(times.dropna())
plt.ylabel("Delivery Time (min)")
plt.title("Delivery Time Boxplot")
plt.tight_layout()
plt.savefig("delivery_boxplot.png")

q1 = times.quantile(0.25)
q2 = times.quantile(0.50)
q3 = times.quantile(0.75)
print("Percentiles -- 25th:", round(q1, 2), "50th:", round(q2, 2), "75th:", round(q3, 2))

# TASK E
iqr = q3 - q1
lower_bound = q1 - 1.5 * iqr
upper_bound = q3 + 1.5 * iqr
print("IQR outlier bounds:", round(lower_bound, 1), "-", round(upper_bound, 1))

outliers = df[times > upper_bound]
outlier_values = outliers["DeliveryTime(min)"].tolist()
print("Outliers detected:", len(outliers), "deliveries (" + str(outlier_values) + " minutes)")
print(outliers)

percent_flagged = len(outliers) / len(df) * 100
print("Percentage flagged as outliers:", str(percent_flagged) + "%")

print("Saved delivery_comparison_histogram.png, delivery_boxplot.png")