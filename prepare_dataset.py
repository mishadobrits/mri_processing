import numpy as np
import yaml
 

with open("params.yaml") as f:
    config = yaml.safe_load(f)

np.random.seed(42)
dataset = np.random.normal(config["stage1"]["mean"], config["stage1"]["std"]**2, size=config["stage1"]["shape"])
np.save("dataset.npy", dataset)
