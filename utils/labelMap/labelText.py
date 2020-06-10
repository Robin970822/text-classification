import os
import numpy as np


class LabelText(object):
    """docstring for LabelText"""

    def __init__(self, label_list, ori_path):
        super(LabelText, self).__init__()
        self.label_list = label_list
        self.ori_path = ori_path

    def arrageLabelText(self, show=True, write=False):
        abs_path = os.path.abspath(self.ori_path)
        if write:
            write_path = '/'.join(abs_path.split('/')[:-1]) + '/labelText.csv'
            print('new file saved in' + write_path)
            w = open(write_path, 'w')
        with open(self.ori_path, 'r') as o:
            for l, s in zip(self.label_list, o.readlines()):
                try:
                    line = str(l) + '\t' + str(s.strip())
                    if show:
                        print(line)
                    if write:
                        w.write(line + '\n')
                except(Exception):
                    print('------Exception------')
                    continue
            if write:
                w.close()

    def sortByLabel(self, show=True, write=False):
        abs_path = os.path.abspath(self.ori_path)
        if write:
            write_path = '/'.join(abs_path.split('/')
                                  [:-1]) + '/sortedLabelText.csv'
            print('new file saved in' + write_path)
            w = open(write_path, 'w')
        with open(self.ori_path, 'r') as o:
            index = np.argsort(self.label_list)
            ori_lines = o.readlines()
            for i in range(len(index)):
                try:
                    line = str(self.label_list[index[i]]) + \
                        '\t' + str(ori_lines[index[i]].strip())

                    if show:
                        print(line)
                    if write:
                        w.write(line)
                        w.write('\n')
                except(Exception):
                    print('------Exception------')
                    continue
            if write:
                w.close()
