#%matplotlib inline
from scipy.io import loadmat
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt
import numpy as np
import random
import sys
import io

# DATA_DIR = "../../data/spam-dataset/"
DATA_DIR = "client/"
TOTAL_TRAINING_SIZE = 2620

def get_accuracy(true_labels, predicted_labels):
    return accuracy_score(true_labels, predicted_labels)

def sample_random_indices(training_size, validation_size):
    total_size = training_size + validation_size
    return random.sample(xrange(total_size), total_size)

def extract_arrays(X_array, Y_array, indices_list):
    Y_array = np.swapaxes(Y_array, 0, 1)
    return X_array[np.array(indices_list), :], Y_array[np.array(indices_list), :]

def classify_kaggle(C_param=100.0):
    landmark_data = loadmat(DATA_DIR + "landmark_data.mat")
    training_data = landmark_data['training_data']
    training_labels = landmark_data['training_labels']
    test_data = landmark_data['test_data']

    training_size = TOTAL_TRAINING_SIZE
    classifier = svm.LinearSVC(C=C_param)
    classifier.fit(training_data, np.ravel(training_labels))
    predicted_labels = classifier.predict(test_data)

    print "Training Size: {0} || Testing Size: {1}\n".format(training_data.shape[0], test_data.shape[0])
    return predicted_labels[0]
    # with open('testing_labels.csv', 'w') as writefile:
    #     writefile.write("Id,Category\n")
    #     i = 1
    #     for label in predicted_labels:
    #         writefile.write("{0},{1}\n".format(i, label))
    #         i += 1

def classify_and_validate_training(training_data, training_labels, training_size, C_param=1.0):
    validation_size = TOTAL_TRAINING_SIZE - training_size
    indices_list = sample_random_indices(training_size, validation_size)
    train_features, train_labels = extract_arrays(training_data, training_labels, indices_list[0:-validation_size])
    validation_features, validation_labels = extract_arrays(training_data, training_labels, indices_list[-validation_size:])

    classifier = svm.LinearSVC(C=C_param)
    classifier.fit(train_features, np.ravel(train_labels))
    predicted_labels = classifier.predict(validation_features)

    accuracy = get_accuracy(np.ravel(validation_labels), predicted_labels)
    print "Training Size: {0} || Validation Size: {1} || Accuracy: {2}\n".format(training_size, validation_size, accuracy)

def find_best_C(training_size):
    k_value = 4
    chunk_size = 655
    landmark_data = loadmat(DATA_DIR + "landmark_data.mat")
    training_data = landmark_data['training_data']
    training_labels = landmark_data['training_labels']
    training_size = training_size

    indices_list = random.sample(xrange(TOTAL_TRAINING_SIZE), TOTAL_TRAINING_SIZE)
    C_trials_list =[1000.0, 100.0, 90.0, 50.0, 10.0, 1.0, 1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8]
    for C_param in C_trials_list:
        sum_accuracy = 0.0
        classifier = svm.LinearSVC(C=C_param)
        for i in xrange(4):
            #First chunk is the validation indices and it iterates
            train_features, train_labels = extract_arrays(training_data, training_labels, indices_list[0:(i*chunk_size)-0]+
                indices_list[(i*chunk_size)+chunk_size:-1])

            validation_features, validation_labels = extract_arrays(training_data, training_labels, indices_list[i*chunk_size:(i*chunk_size)+
                chunk_size])

            classifier.fit(train_features, np.ravel(train_labels))
            predicted_labels = classifier.predict(validation_features)
            sum_accuracy += get_accuracy(np.ravel(validation_labels), predicted_labels)
        print "C value: {0} || Cross Validation Accuracy: {1} || Chunk Size: {2}".format(C_param, sum_accuracy/float(k_value),chunk_size)

def run(training_size):


    if "-kaggle" in sys.argv:
        classify_kaggle(training_data, training_labels, test_data, C_param=100.0)
    else:
        classify_and_validate_training(training_data, training_labels, training_size, C_param=100.0)

if __name__ == '__main__':
    if len(sys.argv) > 1:
        if sys.argv[1] == '-kaggle':
            run(TOTAL_TRAINING_SIZE)
        elif sys.argv[1] == '-size':
            training_size = int(sys.argv[2])
            run(training_size)
        elif sys.argv[1] == '-find_C':
            training_size = TOTAL_TRAINING_SIZE
            find_best_C(training_size)
        else:
            print "Not enough arguments to begin program"
            exit(0)
    else:
        run(1834)
