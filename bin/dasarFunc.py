import torch
import numpy as np
import matplotlib.pyplot as plt
from scipy.ndimage.filters import maximum_filter
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion
import imagepers

def randompoints(C1,N):
    C1tmp = torch.from_numpy(C1)
    possibleindex =np.reshape(np.array(range(0, torch.numel(C1tmp))),(1,torch.numel(C1tmp)))
    weighting = np.reshape(C1,(1,torch.numel(C1tmp)))
    total=sum(sum(C1))
    weighting=weighting/total
    np.random.seed(seed=1)
    chosenindex = np.random.choice(possibleindex.flatten(),(1,N),replace=True, p=weighting.flatten())
    [Y_target , X_target]=np.unravel_index(chosenindex,(np.shape(C1)))
    return Y_target, X_target