import argparse
from train_data import GraphDataSet
import numpy as np
from sklearn.model_selection import KFold


def split_data():
    dataset = GraphDataSet()
    num_of_data = dataset.__len__()
    kf = KFold(n_splits=num_folds, shuffle=True)
    indices = []
    for i, (_, index) in enumerate(kf.split(np.arange(num_of_data))):
        np.random.shuffle(index)
        indices.append(index)
    indices = np.array(indices)
    return indices

def extract_graph_data(out_file_path, indices):
    np.savez_compressed(out_file_path, indices = indices)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--folds', type=int, default=10)
    given_args = parser.parse_args()
    num_folds = given_args.folds
    indices = split_data()
    out_file_path = 'indices.npz'
    extract_graph_data(out_file_path, indices = indices)