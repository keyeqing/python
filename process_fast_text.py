import pandas as pd

path="data\\fasttext\\ads_fast_text_v1.tsv"

def produceLabel(a,b):
    #print('{} {} {}'.format(a,b, type(a)))
    return a*255+b
output_dir = "output\\"
ftrain = open(output_dir+"news_fasttext_train.txt", "w",encoding="utf-8")
ftest = open(output_dir+"news_fasttext_test.txt", "w", encoding="utf-8")
final_train = open(output_dir+"final_fasttext_train.txt", "w", encoding="utf-8")
fpredict = open(output_dir+"news_fasttext_predict.txt", "w",encoding="utf-8")

count = 0
train_len = 10000000
test_len = 12000000

max_keyword_len =0
max_url_len = 0
max_ad_text_len = 0
max_ad_title_len = 0
max_lp_title_len = 0

with open(path, 'r', encoding='utf-8') as f:
    next(f)
    for line in f:
        arr = line.split('\t')
        max_keyword_len = max(max_keyword_len, len(arr[1]))
        max_url_len = max(max_url_len, len(arr[2]))
        max_ad_text_len = max(max_ad_text_len, len(arr[3]))
        max_ad_title_len = max(max_ad_title_len, len(arr[4]))
        max_lp_title_len = max(max_lp_title_len, len(arr[5]))

print('max_key_len:{}, max_url_len:{}, max_ad_text_len:{}, '
      'max_ad_title_len:{}, max_lp_title_len:{}.'.format(max_keyword_len, max_url_len, max_ad_text_len,
                                                         max_ad_title_len, max_lp_title_len))

with open(path, 'r', encoding="utf-8") as f:
    next(f)
    for line in f:
        #print(line)
        arr = line.split("\t")
        keyword = arr[1].ljust(max_keyword_len, " ")
        url = arr[2].ljust(max_url_len, " ")
        adText = arr[3].ljust(max_ad_text_len, " ")
        adTitle = arr[4].ljust(max_ad_title_len, " ")
        LpTitle = arr[5].ljust(max_lp_title_len, " ")
        #print('{} {} {} {} {}'.format(query, keyword, url, adText, adTitle))
        text_line = '{} {} {} {} {}\n'.format(keyword, url, adText, adTitle, LpTitle);
        fpredict.write(outline)
        fpredict.flush()

        for i in range(6, 17):
            if (i % 2 == 0):
                label = produceLabel(int(arr[i]), int(arr[i + 1]))
                if (label > 0):
                    outline = "__label__" + str(label) + "\t" + text_line
                    #print('{} {}'.format(i,outline))
                    count+=1
                    final_train.write(outline)
                    final_train.flush()
                    if count < train_len:
                        ftrain.write(outline)
                        ftrain.flush()
                        continue
                    elif count  < test_len:
                        ftest.write(outline)
                        ftest.flush()
                        continue




ftrain.close()
ftest.close()
final_train.close()
fpredict.close()

print('Generated {} training set and predict set totally'.format(count))

