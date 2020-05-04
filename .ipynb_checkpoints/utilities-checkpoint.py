# Functions file

from sklearn import metrics
from sklearn.metrics import (auc, confusion_matrix, roc_curve, 
                             accuracy_score, precision_score)
import matplotlib.pyplot as plt
import numpy as np
from itertools import product
import pandas as pd

# Function to print accuracy, precision and AUC

def print_metrics(X_test, y_test, pred_clf, proba_clf, classifier_name, return_values = True):
    
    """
    This function prints accuracy, precision and AUC
    
    Inputs:
    
    y_test is a series with the labels of the test data
    
    pred_clf is a numpy.ndarray with the predictions of the model
    
    proba_clf is a numpy.ndarray with the probabilities calculated by the model
    
    classifier_name is the name of the classifier which will appear in the text
    
    No outputs
    
    """
    
    # Print accuracy and precision
    tn, fn, fp, tp = confusion_matrix(y_test, pred_clf).ravel()
    
    acc = round((tp + tn) / X_test.shape[0], 3) * 100
    print('{0} accuracy: {1:.2f}%'.format(classifier_name, acc))
    
    precision = round((tp / (tp + fp)), 2) * 100
    print('{0} precision: {1:.2f}%'.format(classifier_name, precision))
    
    # Print AUC
    auc = metrics.roc_auc_score(y_test, proba_clf[:,1])
    print("{0} AUC: {1:.4f}".format(classifier_name, auc))
    
    if return_values == True:
        return acc, precision, auc
    else:
        return None



# Function to display the confusion matrix

def plot_conf_matrix(cm,
                          normalize=False,
                          axis=1,
                          figsize=(5,4), 
                          fontsize=14,
                          cmap='Blues'):
    """
    This function prints and plots the confusion matrix.
    Normalization can be applied by setting `normalize=True`.
    Note that normalization here by default occurs across axis=1, or across each row (true class). 
    (QQ: which metric does this correspond to, precision or recall?)
    """
    classes = ['Benign', 'Malignant']
    
    if normalize:
        if axis == 1:
            cm = cm.astype('float') / cm.sum(axis=axis)[:, np.newaxis]
        elif axis == 0:
            cm = cm.astype('float') / cm.sum(axis=axis)[np.newaxis, :]
        else:
            raise ValueError("axis must be 0 or 1")
        print("Normalized confusion matrix")
    else:
        print('Confusion matrix, without normalization')

    print(cm)
    
    fig = plt.figure(figsize=figsize)
    plt.grid(b=None)
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45, fontsize = fontsize)
    plt.yticks(tick_marks, classes, fontsize = fontsize)

    q_labels = ['TN', 'FP', 'FN', 'TP']
    quad_font_size = fontsize
    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    q_i = 0
    for i, j in product(range(cm.shape[0]), range(cm.shape[1])):
        
        q = plt.text(j, i-0.2, q_labels[q_i], horizontalalignment='center', fontsize=quad_font_size)
        q_i += 1
        q.set_bbox(dict(facecolor='white', alpha=0.6, edgecolor='white'))
        
        t = plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                     verticalalignment="center",
                 color="#002781",
                    fontsize=fontsize)
        t.set_bbox(dict(facecolor='white', alpha=0.6, edgecolor='white'))
        

    plt.tight_layout(h_pad=10, w_pad=0)
    plt.ylabel('True label', fontsize = fontsize)
    plt.xlabel('Predicted label', fontsize = fontsize)
    return None



# Function to plot feature importance

def plot_feature_importance(clf, colour, classifier_name, one_hot_df_indep):
    
    """
    This function plots feature importance
    
    Inputs:
    
    clf is the classifier
    
    colour is a string describing the colour the bars should be
    
    classifier_name is the name of the classifier which will appear in the title
    
    No outputs
    
    """
    
    features_log = pd.DataFrame(clf.feature_importances_, index = one_hot_df_indep.columns.tolist(), 
                            columns = ['Importance'])
    features_log = features_log.sort_values(by='Importance', ascending=True)

    features_log.plot(kind='barh', figsize=(10,8), color = colour)
    plt.xlabel('Feature importance')
    plt.title('Feature importance for {}'.format(classifier_name))
    
    return None