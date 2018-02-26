
import sys
import re
import io

#remove prunction and to lower case
def preprocess(line):
    punctuation = re.compile(u"[-~!@#$%^&*()_+`=/\[\]\\\{\}\"|;':,./<>?·！@#￥%……&*（）——+【】、；‘：“”，。、《》？「『」』®]")
    line = punctuation.sub(' ', line)
    return line.lower()

def preprocess_v2(line):
    return line.lower()

def process_url(line):
    punctuation = re.compile(u"[.]")
    line = punctuation.sub('', line)
    line = re.compile(u"[/]").sub(' ',line)
    return line.lower()

raw_line = "www.hotels.com/free"
pre_line = process_url(raw_line)
print('raw_line:{}, pre_line:{}'.format(raw_line, pre_line))