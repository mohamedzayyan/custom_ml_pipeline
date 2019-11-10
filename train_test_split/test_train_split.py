#!/usr/bin/env python3
import numpy as np
def test_train_split(array, test_size,y=-1):
    num_classes = np.unique(array[:,y], return_counts=True)[0].shape
    unique_vals = np.unique(array[:,y], return_counts=True)[0]
    num_rows, num_cols = array.shape[0], array.shape[1]

    subclasses = []
    for i in unique_vals:
        subclasses.append(array[array[:,y] == i])
    train_ = []
    test_ = []
    
    for i in unique_vals:
        temp = array[array[:,y] == i]
        train_size = int(np.floor(test_size*temp.shape[0]))
        test_s = temp.shape[0] - train_size
        
        train_.append(temp[:train_size])
        test_.append(temp[train_size:train_size+test_s])
        
    train_ = np.random.permutation(np.vstack(train_))
    test_ = np.random.permutation(np.vstack(test_))
    
    
    return [train_, test_]

