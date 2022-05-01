from skimage.io import imread, imsave
import pyclesperanto_prototype as cle
import os

def batch_segmentation(input_folder_path, output_folder_path):
    file_names = os.listdir(input_folder_path)
    for file_name in file_names:
        if file_name.endswith('.tif'):
            image = imread(os.path.join(input_folder_path, file_name))
            labels = segmentation(image)
            labels_name = os.path.splitext(file_name)[0] + '_labels.tif'
            output_labels_path = os.path.join(output_folder_path, labels_name)
            imsave(output_labels_path, labels)
            print('Saving labels...' + labels_name)
    return
