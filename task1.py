import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# TASK A
rolls = np.random.randint(1, 7, size=1000)
print("First 10 rolls:", rolls[:10])

# TASK B
faces, counts = np.unique(rolls, return_counts=True)

# TASK C
theoretical_p = 1 / 6
print("Face Count Empirical P Theoretical P")
for face, count in zip(faces, counts):
    empirical_p = count / 1000
    print(face, count, round(empirical_p, 3), round(theoretical_p, 4))

# TASK D
plt.figure(figsize=(6, 4))
plt.hist(rolls, bins=np.arange(0.5, 7.5, 1), color="steelblue", edgecolor="black")
plt.xlabel("Face")
plt.ylabel("Frequency")
plt.title("Histogram of 1000 Die Rolls")
plt.savefig("die_rolls.png")
print("Saved die_rolls.png")