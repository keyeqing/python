import utils
corpus_file = "D:\\workspace\\adsdata\\adsGloveCorpus.tsv"
ad_copy_training_file = "data\\glove\\glove_adcopy_training_v3.txt"
all_ad_copy_training_file = "data\\glove\\all_glove_adcopy_training_v3.txt"
lp_training_file = "data\\glove\\glove_lp_training_v3.txt"
query_file = "data\\glove\\glove_query_set_annotation_v3.txt"

adCopyJudgment_set = set()
adLpJudgment_set = set()
query_set = set()

ac_training_file_f = open(ad_copy_training_file, 'w', encoding='utf-8')
lp_training_file_f = open(lp_training_file, 'w', encoding='utf-8')
query_file_f = open(query_file, 'w', encoding='utf-8')
all_ad_copy_training_file_f = open(all_ad_copy_training_file, 'w', encoding='utf-8')

ac_cnt = 0
lp_cnt = 0
all_ac_cnt = 0
#0 Unsure Adult Perfect Excellent Fair Good Bad
#NoJudgment:0 Excellent same overlap Good NJ:PageDidNotLoad NJ:Login Detrimental subset Very Bad disjoint NoJudgment:Foreign NJ:Foreign NoJudgment:Login NoJudgment:PageDidNotLoad superset VeryBad Fair Bad Perfect
with open(corpus_file,'r', encoding='utf-8') as f:
    header = next(f)
    print('header is {}.'.format(header))
    for line in f:
        arr = line.strip('\n').split('\t')
        ac_label = arr[0].strip()
        lp_label = arr[1].strip()
        adCopyJudgment_set.add(ac_label)
        adLpJudgment_set.add(lp_label)
        query = utils.preprocess(arr[2].strip())
        query_set.add(query)
        keyword = utils.preprocess(arr[3])
        adText = utils.preprocess(arr[4])
        adTitle = utils.preprocess(arr[5])
        ad_url = utils.process_url(arr[6])
        lp_title = utils.preprocess(arr[7])
        if((ac_label=='Perfect')|(ac_label=='Excellent')|(ac_label=='Good')):
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
           ac_cnt +=10
           all_ac_cnt +=1
           all_ad_copy_training_file_f.write('{} {} {} {} {}\n'.format(query, ad_url, keyword, adTitle, adText))
           ac_training_file_f.flush()
           all_ad_copy_training_file_f.flush()
        if ((lp_label == 'Perfect') | (lp_label == 'Excellent') | (lp_label == 'Good')| (lp_label == 'same') | (lp_label == 'subset') | (lp_label=='overlap') | (lp_label == 'superset')):
           lp_training_file_f.write(utils.preprocess('{} {}\n'.format(query, lp_title)))
           lp_cnt +=1
           lp_training_file_f.flush()
query_file_f.write('\n'.join(query_set))
query_file_f.flush()
print('adCopy:{}'.format(' '.join(adCopyJudgment_set)))
print('adLp:{}'.format(' '.join(adLpJudgment_set)))
print('ac_cnt:{}, lp_cnt:{}, all_ac_cnt:{}'.format(ac_cnt,lp_cnt, all_ac_cnt))
print('total query count:{}'.format(len(query_set)))

ac_training_file_f.close()
lp_training_file_f.close()
all_ad_copy_training_file_f.close()