import utils
click_corpus_file = "data\\glove\\topk_data.tsv"
ad_copy_training_file = "data\\glove\\glove_adcopy_click_training_v3.txt"
all_ad_copy_training_file = "data\\glove\\all_glove_adcopy_click_training_v3.txt"
query_file = "data\\glove\\glove_query_set_v3.txt"

query_set = set()

ac_training_file_f = open(ad_copy_training_file, 'w', encoding='utf-8')
all_ac_training_file_f = open(all_ad_copy_training_file, 'w', encoding='utf-8')
query_file_f = open(query_file, 'w', encoding='utf-8')

ac_cnt = 0
with open(click_corpus_file,'r', encoding='utf-8') as f:
    for line in f:
        arr = line.strip('\n').split('\t')
        ac_label = int(arr[12].strip())
        ad_url = utils.process_url(arr[14])
        adText = utils.preprocess(arr[15])
        adTitle = utils.preprocess(arr[16])
        keyword = utils.preprocess(arr[17]).strip()
        query = utils.preprocess(arr[18]).strip()
        query_set.add(query)
        print('{} : {} :{} :{} :{} :{}, url:{}'.format(ac_label, ad_url, adText, adTitle, keyword, query, ad_url))
        if(ac_label>2):
           ac_training_file_f.write('{} {}\n'.format(query, adText))
           ac_training_file_f.write('{} {}\n'.format(query, adTitle))
           ac_training_file_f.write('{} {}\n'.format(query, keyword))
           ac_training_file_f.write('{} {}\n'.format(adText, keyword))
           ac_training_file_f.write('{} {}\n'.format(adTitle, keyword))
           ac_training_file_f.write('{} {}\n'.format(adTitle, adText))
           ac_training_file_f.write('{} {}\n'.format(query, ad_url))
           ac_training_file_f.write('{} {}\n'.format(keyword, ad_url))
           ac_training_file_f.write('{} {}\n'.format(adTitle, ad_url))
           ac_training_file_f.write('{} {}\n'.format(adText, ad_url))
           all_ac_training_file_f.write('{} {} {} {} {}\n'.format(query, ad_url, keyword, adTitle, adText))
           ac_cnt +=10
           ac_training_file_f.flush()
           all_ac_training_file_f.flush()
query_file_f.write('\n'.join(query_set))
query_file_f.flush()
print('ac_cnt:{}'.format(ac_cnt))
print('total query count:{}'.format(len(query_set)))

ac_training_file_f.close()
all_ac_training_file_f.close()
