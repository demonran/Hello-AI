#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 去除停用词
import codecs
import logging
import os
import sys


def del_stop_word(line, stop_key):
    word_list = line.split(' ')
    sentence = ''
    for word in word_list:
        word = word.strip()
        if word not in stop_key:
            if word != '\t':
                sentence += word + " "
    return sentence.strip()


def stop_word(source_file, target_file, stop_key):
    source = codecs.open(source_file, 'r', encoding='utf-8')
    target = codecs.open(target_file, 'w', encoding='utf-8')
    logger.info('open source file: ' + source_file)
    logger.info('open target file: ' + target_file)
    line_num = 1
    line = source.readline()
    while line:
        logger.info('---processing ' + str(line_num) + ' article---')
        sentence = del_stop_word(line, stop_key)
        # print sentence
        target.writelines(sentence + '\n')
        line_num = line_num + 1
        line = source.readline()
    logger.info('well done.')
    source.close()
    target.close()


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logger.root.setLevel(level=logging.INFO)

    stop_key = [w.strip() for w in codecs.open('data/stopWord.txt', 'r', encoding='utf-8').readlines()]

    logger.info(stop_key)

    source_file = 'tmp/2000_neg_cut.txt'
    target_file = 'tmp/2000_neg_cut_stopword.txt'
    stop_word(source_file, target_file, stop_key)

    source_file = 'tmp/2000_pos_cut.txt'
    target_file = 'tmp/2000_pos_cut_stopword.txt'
    stop_word(source_file, target_file, stop_key)
