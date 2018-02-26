path="data\\fasttext\\ads_fast_text_v1.tsv"

predict_path="predict_result_v2.txt"

fpredict = open("merge_fasttext_predict_v2.txt", "w",encoding="utf-8")
count=0

def convert_ms(label_id):
    id = label_id[9:]
    i1=int(id)/255
    i2=int(id)%255
    return str(int(i1)),str(int(i2))

#print('{}'.format(convert_ms('__label__123')))

with open(path, 'r', encoding="utf-8") as f:
    header = next(f)
    cols = header.split("\t")
    final_header = "\t".join(cols[1:])
    print('final header is {}'.format(final_header))
    fpredict.write(final_header)
    fpredict.flush()
    with open(predict_path, 'r', encoding='utf-8') as pf:
        text = f.readlines()
        label_line = pf.readlines()
        print('load files!')
        for i in range(len(text)):
            features = text[i].split("\t")
            texts = features[1:6]
            ms_features = features[18:]
            labels = label_line[i].split(" ")
            #print('labels line:{}'.format(label_line[i]))
            outline = "\t".join(texts)
            for j in range(len(labels)):
                if(j%2==0):
                    print(labels[j])
                    ms_a, ms_b = convert_ms(labels[j])
                    outline = outline+"\t"+ms_a+"\t"+ms_b
            outline = outline + "\t" + "\t".join(ms_features)
            fpredict.write(outline)
            fpredict.flush()
            count +=1


print('total labels:{}'.format(count))
fpredict.close()