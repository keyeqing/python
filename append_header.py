

merge_path='merge_fasttext_predict_v1.txt'
new_merge_path='new_merge_fasttext_predict_v1.txt'
path="data\\fasttext\\ads_fast_text_v1.tsv"
with open(path, 'r', encoding='utf-8') as original1:
    cols = next(original1).split("\t")
    final_header = "\t".join(cols[1:])
    print('final header is {}'.format(final_header))
original1.close()

count = 0
with open(merge_path, 'r', encoding='utf-8') as original:
    next(original)
    with open(new_merge_path, 'w', encoding='utf-8') as modified:
        modified.write(final_header)
        modified.flush()
        for line in original:
            modified.write(line)
            modified.flush()
            count +=1

modified.close()
original.close()
print('Generate {} lines.'.format(count))