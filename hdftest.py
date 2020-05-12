import h5py
import numpy as np
print("Check negative one")
import os

print("Check zero")
sample1 = np.random.randint(low = 0, high = 20, size = (4, 4))
sample2 = np.random.randint(low = 0, high = 20, size = (5, 5))
print("Check one")

with h5py.File(os.path.join(os.getcwd(), 'hdf5_data.h5'), 'w') as hdf:
    print("Check two")
    hdf.create_dataset('dataset1', data = sample1)
    hdf.create_dataset('dataset2', data = sample2)
    print("Check three")
    hdf.close()

with h5py.File(os.path.join(os.getcwd(), 'hdf5_data.h5'), 'r') as hdf:
    print("Check four")
    dataSetNames = list(hdf.keys())
    data1 = np.array(hdf.get(dataSetNames[0]))
    data2 = np.array(hdf.get(dataSetNames[1]))
    print("Check five")
    hdf.close()

print("\nFirst Matrix")
print(data1)
print("Second Matrix")
print(data2)
