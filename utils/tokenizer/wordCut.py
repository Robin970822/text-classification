import jieba
import os

stopwords_path = os.path.normpath(os.path.dirname(__file__)) + "/stopwords.txt"


class WordCut(object):
    """docstring for WordCut"""

    def __init__(self, stopwords_path=stopwords_path):
        super(WordCut, self).__init__()
        self.stopwords_path = stopwords_path

    def addDictionary(self, dict_list):
        map(lambda x: jieba.load_userdict(x), dict_list)

    def seg_sentence(self, sentence, stopwords_path=None):
        if stopwords_path is None:
            stopwords_path = self.stopwords_path

        def stopwordslist(filepath):
            stopwords = [line.strip()
                         for line in open(filepath, 'r').readlines()]
            return stopwords
        sentence_seged = jieba.cut(sentence.strip())
        stopwords = stopwordslist(stopwords_path)
        outstr = ""
        for word in sentence_seged:
            if word not in stopwords:
                if word != '\t':
                    outstr += word
                    outstr += " "
        return outstr

    def seg_file(self, path, show=True, write=False, write_name='token.txt'):
        print("now token file...")
        if write:
            write_path = '/'.join(path.split('/')[:-1]) + '/' + write_name
            w = open(write_path, 'w')

        with open(path, 'r') as p:
            for line in p.readlines():
                line_seg = self.seg_sentence(line)
                if show:
                    print(line_seg)
                if write:
                    w.write(line_seg + '\n')
        if write:
            w.close()
