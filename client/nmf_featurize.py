from __future__ import print_function
from time import time
from os import listdir
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import NMF
import numpy as np
import glob
import scipy.io

"""
Custom TFIDF NMF featurizer for the landmark classification dataset.
Built during HackMIT 2015.
Author: Can Koc <cankoc@berkeley.edu>, Brian Su <bsu@berkeley.edu>, Cem Koc <cemkoc@berkeley.edu>
Connects to Clarifai API to extract textual corpus from landmark images using Deep Learning Image Classification methods.

License: BSD
"""

NUM_TRAINING_EXAMPLES = 2620
NUM_TEST_EXAMPLES = 1

GOLDEN_GATE_DIR = "client/ggb_text/"
STONEHENGE_DIR = "client/stonehenge_text/"
EIFFEL_DIR = "client/eiffel_text/"
ROME_DIR = "client/rome_text/"

TEST_DIR = "client/test/"


n_samples = NUM_TRAINING_EXAMPLES + NUM_TEST_EXAMPLES
n_features = 1000
n_topics = 20
n_top_words = 1000

def vectorize_and_featurize(all_paths):
    t0 = time()
    print("Loading dataset and extracting TF-IDF features...")

    vectorizer = TfidfVectorizer(max_df=0.95, min_df=2, max_features=n_features,
                             stop_words='english')

    documents = []
    counter = 0
    for path in all_paths:
        if counter == n_samples:
            break
        counter += 1
        with open(path, 'r') as f:
            try:
                content = f.read().lower()
                text_string = ''
                for c in content:
                    if c in '+abcdefghijklmnopqrstuvwxyz ':
                        text_string += c
                    else:
                        text_string += ''
                content = text_string.encode(errors='ignore').strip()
                documents.append(content)
            except Exception as e:
                print(e)
                continue

    # print(documents)
    # Pre-processing is done
    tfidf = vectorizer.fit_transform(documents)
    print("done in %0.3fs." % (time() - t0))

    #Fit NMF Model
    print("Fitting the NMF model with n_samples=%d and n_features=%d..." % (n_samples, n_features))

    # Using fit_transform method because in the end I want to get the data matrix
    nmf = NMF(n_components=n_topics, random_state=1).fit_transform(tfidf)
    print("done in %0.3fs." % (time() - t0))

    feature_names = vectorizer.get_feature_names()

    print()
    print("NMF Data Matrix")
    print(nmf.shape)
    return nmf

def run():
    ggb_filenames = glob.glob(GOLDEN_GATE_DIR + '*.txt')
    stonehenge_filenames = glob.glob(STONEHENGE_DIR + '*.txt')
    eiffel_filenames = glob.glob(EIFFEL_DIR + '*.txt')
    rome_filenames = glob.glob(ROME_DIR + '*.txt')

    test_filenames = [TEST_DIR + str(x) + '.txt' for x in range(NUM_TEST_EXAMPLES)]

    giant_document_paths = ggb_filenames + stonehenge_filenames + eiffel_filenames + rome_filenames
    giant_document_paths += test_filenames

    all_features = vectorize_and_featurize(giant_document_paths)

    indices = list(xrange(NUM_TRAINING_EXAMPLES + NUM_TEST_EXAMPLES))
    training_indices = indices[0:NUM_TRAINING_EXAMPLES]

    test_indices = indices[NUM_TRAINING_EXAMPLES:]

    X = all_features[np.array(training_indices), :]
    test_features = all_features[np.array(test_indices), :]
    Y = [0]*len(ggb_filenames) + [1]*len(stonehenge_filenames) + [2]*len(eiffel_filenames) + [3]*len(rome_filenames)

    file_dict = {}
    file_dict['training_data'] = X
    file_dict['training_labels'] = Y
    file_dict['test_data'] = test_features
    print("Printing Final File Sizes")
    print("X is: {0} | Y is: {1} | Test Size is: {2}\n".format(len(X), len(Y), len(test_features)))
    scipy.io.savemat('client/landmark_data.mat', file_dict)


if __name__ == '__main__':
    run()
