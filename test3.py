import h5py 
f1 = h5py.File('keras_model.h5', 'r') 
print(list(f1.keys()))