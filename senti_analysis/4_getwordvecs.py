#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 从词向量模型中提取文本特征向量
import logging
import os
import sys

if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
    logger.info("running %s" % ' '.join(sys.argv))

    # load word2vec model
    fdir = '/Users/sy/Desktop/pyRoot/SentimentAnalysis/'
    inp = fdir + 'wiki.zh.text.vector'
    model = gensim.models.KeyedVectors.load_word2vec_format(inp, binary=False)
