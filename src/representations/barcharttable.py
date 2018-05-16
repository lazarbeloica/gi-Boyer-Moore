import numpy as np
import matplotlib.pyplot as plt

BAR_GROUP_WIDTH = 0.2

class BarChartTable:

    @staticmethod
    def show_results(title, x_label, y_label, dictionary_values, tick_labels):
        '''
        dictionary_values - dictionary i.e. {'men':[25,35,50,80],'women':[55,15,50,100]}
        '''

        bar_labels = [bar_label for bar_label in dictionary_values] #for previous example : ['men','women']
        values = [dictionary_values[bar_label] for bar_label in dictionary_values] # array of arrays ;for previous example : [[25,35,50,80],[55,15,50,100]]
        
        
        temp_set = set([len(one_label_values) for one_label_values in values])
        if len(temp_set) != 1:
            raise Exception("Each label has to have the same number of values")
        
        if list(temp_set)[0] != len(tick_labels):
            raise Exception("Tick labels and every label must have the same number of items")

        n_rects = len(bar_labels)
        n_groups = len(values[0])



        fig, ax = plt.subplots(nrows=2)

        index = np.arange(n_groups)
        bar_width = BAR_GROUP_WIDTH/n_rects

        rects = [ax[0].bar(index + i*bar_width, values[i], bar_width, label=bar_labels[i]) for i in range(n_rects)]
        

        ax[0].set_xlabel(x_label)
        ax[0].set_ylabel(y_label)
        ax[0].set_title(title)
        ax[0].set_xticks(index - bar_width / 2 + bar_width * n_rects / 2)
        ax[0].set_xticklabels(tick_labels)

        ax[0].legend()

        row_colors = [rect[0]._facecolor for rect in rects]        
        the_table = plt.table(cellText=values,
                      rowLabels=bar_labels,
                      colLabels=tick_labels,
                      loc='center', cellLoc='center',
                      rowColours=row_colors )

        the_table.scale(1, 2)
    
        ax[1].add_table(the_table)
        ax[1].set_axis_off()

        fig.tight_layout()
        #fig.set_size_inches(5,5)
        plt.show()


    @staticmethod
    def show_results_boyer_moore(dictionary_values, tick_labels_text_size, tick_labels_pattern_size):

        if len(tick_labels_pattern_size) != len(tick_labels_text_size):
            raise Exception("tick_labels_pattern_size and tick_labels_text_size must be equal")

        tick_labels = ['text: ' + str(tick_labels_text_size[i]) + '\n' + 'pattern: ' + str(tick_labels_pattern_size[i]) for i in range(len(tick_labels_pattern_size)) ] 
        BarChartTable.show_results("Graphical representation for performance testing", "Text and pattern size", "Time", dictionary_values, tick_labels)
