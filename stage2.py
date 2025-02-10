import numpy as np

dataset = np.load("dataset.npy")
print(f"{dataset.mean() = }, {dataset.std() = }")