import utils
corpus_file = "D:\\workspace\\adsdata\\adsGloveCorpus.tsv"
all_ad_copy_training_file = "data\\rnn\\all_rnn_adcopy_training_v4.txt"
lp_training_file = "data\\rnn\\rnn_lp_training_v4.txt"
query_file = "data\\rnn\\rnn_query_set_annotation_v4.txt"

adCopyJudgment_set = set()
adLpJudgment_set = set()
query_set = set()

lp_training_file_f = open(lp_training_file, 'w', encoding='utf-8')
query_file_f = open(query_file, 'w', encoding='utf-8')
all_ad_copy_training_file_f = open(all_ad_copy_training_file, 'w', encoding='utf-8')

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
        query = utils.preprocess_v2(arr[2].strip())
        query_set.add(query)
        keyword = utils.preprocess_v2(arr[3])
        adText = utils.preprocess_v2(arr[4])
        adTitle = utils.preprocess_v2(arr[5])
        ad_url = utils.process_url(arr[6])
        lp_title = utils.preprocess_v2(arr[7])
        if((ac_label=='Perfect')|(ac_label=='Excellent')|(ac_label=='Good')):
           all_ad_copy_training_file_f.write('{}\t{} {} {} {}\t1\n'.format(query, ad_url, keyword, adTitle, adText))
        elif(ac_label=='Bad'):
           all_ad_copy_training_file_f.write('{}\t{} {} {} {}\t0\n'.format(query, ad_url, keyword, adTitle, adText))
        all_ad_copy_training_file_f.flush()

        if ((lp_label == 'Perfect') | (lp_label == 'Excellent') | (lp_label == 'Good')| (lp_label == 'same') | (lp_label == 'subset') | (lp_label=='overlap') | (lp_label == 'superset')):
           lp_training_file_f.write(utils.preprocess_v2('{}\t{}\t1\n'.format(query, lp_title)))
        elif((lp_label == 'disjoint')|(lp_label=='Bad')|(lp_label=='VeryBad')|(lp_label=='Very Bad')):
           lp_training_file_f.write(utils.preprocess_v2('{}\t{}\t0\n'.format(query, lp_title)))
        lp_training_file_f.flush()
query_file_f.write('\n'.join(query_set))
query_file_f.flush()
print('adCopy:{}'.format(' '.join(adCopyJudgment_set)))
print('adLp:{}'.format(' '.join(adLpJudgment_set)))
print('total query count:{}'.format(len(query_set)))

lp_training_file_f.close()
all_ad_copy_training_file_f.close()