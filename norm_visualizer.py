import matplotlib.pyplot as plt
import numpy as np
import streamlit as st


# Define the norm Np function
def norm_Np(x, p):
    return np.power(np.sum(np.abs(x) ** p), 1 / p)


# Streamlit UI
st.title("Np norm visualization in R2")

# User input for p (slider)
p = st.slider("Choose a value for p (between 0 and 10):", 0.1, 10.0, 2.0, 0.1)

# Generate a grid of points for visualization
n_points = 400
x = np.linspace(-2, 2, n_points)
y = np.linspace(-2, 2, n_points)
X, Y = np.meshgrid(x, y)

# Calculate the set E using vectorized computation
Z = np.power(np.abs(X) ** p + np.abs(Y) ** p, 1 / p)

# Create a binary mask for the set E
E_mask = Z <= 1

# Plotting the set E
fig, ax = plt.subplots()
ax.imshow(
    E_mask,
    extent=[-2, 2, -2, 2],
    origin="lower",
    cmap="Blues",
    alpha=1.0,
    aspect="auto",
)

# Add zero axes
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)

# Add dots at (-1, 0), (0, -1), (0, 1), and (1, 0)
dots = np.array([[-1, 0], [0, -1], [0, 1], [1, 0]])
ax.scatter(dots[:, 0], dots[:, 1], color="red", s=30, zorder=5)

ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_title(f"p={p}")
st.pyplot(fig)
