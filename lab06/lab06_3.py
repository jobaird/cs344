'''
@author: John Baird
@created: March 9, 2019
@copied from numbpy.ipynb
'''
#I was unable to get this to work due to weird tensorflow problems on my machine, but I believe this should function.
from keras.datasets import boston_housing

(train_images, train_labels), (test_images, test_labels) = boston_housing.load_data()

def print_structures():
    print(
        f'training images \
            \n\tcount: {len(train_images)} \
            \n\tdimensions: {train_images.ndim} \
            \n\tshape: {train_images.shape} \
            \n\tdata type: {train_images.dtype}\n\n',
        f'testing images \
            \n\tcount: {len(test_labels)} \
            \n\tdimensions: {train_labels.ndim} \
            \n\tshape: {test_labels.shape} \
            \n\tdata type: {test_labels.dtype} \
            \n\tvalues: {test_labels}\n',
    )
print_structures()