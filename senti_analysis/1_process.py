#!/usr/bin/env python
# -*- coding: utf-8  -*-
# 将原始数据合并到一个txt文件

import codecs
import logging
import os
import sys


# 读取文件内容
def getContent(fullname):
    content = ''
    logger.info("处理：" + fullname)
    try:
        f = open(fullname, 'r', encoding='GB2312')
        content = f.readline()
        f.close()
    except:
        try:
            f = open(fullname, 'r', encoding='UTF8')
            content = f.readline()
            f.close()
        except:
            pass
    return content


if __name__ == '__main__':
    program = os.path.basename(sys.argv[0])
    logger = logging.getLogger(program)
    logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
    logger.root.setLevel(level=logging.INFO)

    inp = 'data/ChnSentiCorp_htl_ba_2000'
    folders = ['neg', 'pos']

    for folder in folders:
        logger.info("running " + folder + " files.")
        outp = 'tmp/2000_' + folder + '.txt'  # 输出文件
        output = codecs.open(outp, 'w')

        i = 0
        rootdir = inp + '/' + folder
        for parent, dirnames, filenames in os.walk(rootdir):
            for filename in filenames:
                content = getContent(rootdir + '/' + filename)
                output.writelines(content)
                i = i + 1

        output.close()
        logger.info("Saved " + str(i) + " files.")
