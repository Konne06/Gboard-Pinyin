# -*-coding=utf8-*-

import sys
from pypinyin import lazy_pinyin

File_input = sys.argv[1]
f = open("output.txt", mode='w')
f.write('# Gboard Dictionary version:1\n')
for line in open(File_input):
    line = line.strip('\n')
    res = ''.join(lazy_pinyin(line.strip('\r')))
    f.write(res+'\t'+line+'\t'+'zh-CN\n')
f.close()
