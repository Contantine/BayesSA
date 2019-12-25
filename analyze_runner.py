#!usr/bin/python

# -*- coding: utf-8 -*-
import sys
import os



# 配置环境变量
sys_path = ['E:/workspace/python/douban-spider', 'E:/workspace/python/douban-spider',
            'D:/Program Files/pycharm/PyCharm 2019.3/plugins/python/helpers/pycharm_display',
            'E:/workspace/pycharm/venv/Scripts/python37.zip', 'C:/Program Files/python/DLLs',
            'C:/Program Files/python/lib', 'C:/Program Files/python', 'E:/workspace/pycharm/venv',
            'E:/workspace/pycharm/venv/lib/site-packages',
            'E:/workspace/pycharm/venv/lib/site-packages/setuptools-39.0.1-py3.7.egg',
            'D:/Program Files/pycharm/PyCharm 2019.3/plugins/python/helpers/pycharm_matplotlib_backend',
            'E:/workspace', 'E:/workspace/python']
for path in sys_path:
    sys.path.append(path)
from analyzer import SentimentAnalyzer

model_path = 'E:\\workspace\\python\\douban-spider\\models\\model_1225_01.pkl'
userdict_path = 'E:\\workspace\\python\\douban-spider\\userdict.txt'
stopword_path = 'E:\\workspace\\python\\douban-spider\\stop_words.txt'

# 预测器
analyzer = SentimentAnalyzer(model_path=model_path, stopword_path=stopword_path, userdict_path=userdict_path)


if __name__ == '__main__':
#     print(analyzer.analyze('真的辣鸡'))
# print(sys.argv)

    text = sys.argv[1]
    emotion = analyzer.analyze(text)
    if emotion >= 0.88:
        print("正面情绪")
    else:
        print("负面情绪")
