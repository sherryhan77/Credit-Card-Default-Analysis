fig, ax = plt.subplots()
ind = np.arange(7)
width = 0.3
rects1 = ax.bar(ind,res_ml['Accuracy'],width)
rects2 = ax.bar(ind+width,res_ml['f-score'],width)
rects3 = ax.bar(ind+width*2,res_ml['Precision'],width)
ax.set_xticks(ind + width)
ax.set_xticklabels(('SVM', 'NN', 'DT', 'RF', 'BNB','LOG','KNN'))
ax.legend((rects1[0], rects2[0],rects3[0]), ('Accuracy', 'f-score','Precision'))
ax.set_ylabel('Value')
ax.set_title('ML results')
def autolabel(rects):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '{:.1%}'.format(height),
                ha='center', va='bottom')

        
autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.savefig('ML_result.png', dpi=600) 
