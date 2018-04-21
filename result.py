def result(y_test, y_prediction):
    tp=0
    fp=0
    tn=0
    fn=0
    for i in range(len(y_test)):
        if y_test[i]==1 and y_prediction[i]==1:
            tp+=1
        elif y_test[i]==0 and y_prediction[i]==1:
            fp+=1
        elif y_test[i]==0 and y_prediction[i]==0:
            tn+=1
        else:
            fn+=1
    tpr = tp/(tp+fn)
    tnr = tn/(tn+fp)
    fpr = fp/(fp+tn)
    precision = tp/(tp+fp)
    f = 2 * precision*tpr/(precision+tpr)
    accuracy = (tp+tn)/(tp+tn+fp+fn)
    misclassification_rate = (fp + fn)/(tp+fp+tn+fn)
    print("Precision:\t\t%1.2f identified as mines are mines"%precision)
    print("Recall:\t\t\t%1.2f proportion of actual mines identified"%tpr)
    print("Specificity:\t\t%1.2f proportion of rocks identified as rocks"%tnr)
    print("False Positive Rate:\t%1.2f proportion of rocks identified as mines"%fpr)
    print("f-score:\t\t%1.2f tradeoff between precision and recall"%f)
    print("Accuracy:\t\t%1.2f how well the model has classified"%accuracy)
    # print("Misclassification Rate:\t\t%1.2f how well the model has classified"%accuracy)
    print("tp:\t\t\t{}\nfp:\t\t\t{}\ntn:\t\t\t{}\nfn:\t\t\t{}".format(tp,fp,tn,fn))
        
