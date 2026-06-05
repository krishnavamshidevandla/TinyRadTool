# %%
import numpy as np
import matplotlib.pyplot as plt

# Load matrix
M = np.load("C:/Users/EMI_user1/Desktop/radar/matrix_256x128.npy")

# Show matrix values
print("FULL MATRIX:")
print(M)

# Show matrix shape
print("\nMatrix Shape:")
print(M.shape)

# Show matrix size in bytes
print("\nMatrix Size (bytes):")
print(M.nbytes)

# Show heatmap
plt.figure(figsize=(10, 6))
plt.imshow(M, aspect='auto', cmap='jet')

plt.title("Radar Matrix")
plt.xlabel("Columns")
plt.ylabel("Rows")

plt.colorbar(label="Amplitude")

plt.show()