import numpy as np

def majority_classifier(y_train, X_test):
    """
    Predict the most frequent label in training data for all test samples.
    """
    unique_labels, counts = np.unique(y_train, return_counts=True)
    majority_index = np.argmax(counts)
    majority_class = unique_labels[majority_index]
    predictions = np.full(len(X_test), fill_value=majority_class)
    return predictions.tolist()