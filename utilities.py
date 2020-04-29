def print_metrics(y_test,pred_clf,proba_clf, classifier_name):
    
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
    
    return None