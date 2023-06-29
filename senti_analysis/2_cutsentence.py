#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 逐行读取文件数据进行jieba分词
import codecs
import logging
import os
import re
import string
import sys

import jieba as jieba


def prepare_data(source_file, target_file):
    f = codecs.open(source_file, 'r', encoding='utf-8')
    target = codecs.open(target_file, 'w', encoding='utf-8')
    logger.info('打开source file: ' + source_file)
    logger.info('打开target file: ' + target_file)

    lineNum = 1
    line = f.readline()
    while line:
        logger.info('---processing ' + str(lineNum) + ' article---')
        line = clearTxt(line)
        seg_line = sent2word(line)
        target.writelines(seg_line + '\n')
        lineNum = lineNum + 1
        line = f.readline()
    logger.info('well done.')
    f.close()
    target.close()


# 清洗文本
def clearTxt(line):
    if line != '':
        line = line.strip()
        # intab = ""
        # outtab = ""
        # trantab = str.maketrans(intab, outtab)
        # pun_num = string.punctuation + string.digits
        # line = line.encode('utf-8')
        # line = line.translate(trantab)
        # line = line.decode("utf8")
        # 去除文本中的英文和数字
        line = re.sub("[a-zA-Z0-9]", "", line)
        # 去除文本中的中文符号和英文符号
        line = re.sub("[\s+\.\!\/_,$%^*(+\"\'；：“”．]+|[+——！，。？?、~@#￥%……&*（）]+", "", line)
    return line


# 文本切割
def sent2word(line):
    seg_list = jieba.cut(line, cut_all=False)
    seg_sentence = ''
    for word in seg_list:
        if word != '\t':
            seg_sentence += word + " "
    return seg_sentence.strip()


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger()
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logger.root.setLevel(level=logging.INFO)

    sourceFile = 'tmp/2000_neg.txt'
    targetFile = 'tmp/2000_neg_cut.txt'
    prepare_data(sourceFile, targetFile)

    sourceFile = 'tmp/2000_pos.txt'
    targetFile = 'tmp/2000_pos_cut.txt'
    prepare_data(sourceFile, targetFile)
