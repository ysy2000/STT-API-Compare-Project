import Levenshtein as Lev 
import pandas as pd
import csv
'''
cer 계산 시 문장부호는 모두 제거하여 계산
'''


def cal_CER(ori_str, eval_str):
    dist, length, _ = get_distance(ori_str, eval_str)
    cer = float(dist / length)
    return cer

def get_distance(ref, hyp):
    total_dist = 0
    total_length = 0
    transcripts = []

    transcripts.append('{ref}\n>>{hyp}'.format(hyp=hyp, ref=ref))
    dist, length = char_distance(ref, hyp)
    total_dist += dist
    total_length += length 

    return total_dist, total_length, transcripts

def char_distance(ref, hyp):
    ref = ref.replace(' ', '') 
    hyp = hyp.replace(' ', '') 

    dist = Lev.distance(hyp, ref)
    length = len(ref.replace(' ', ''))

    return dist, length 
     
if __name__ == "__main__":
    # # test
    # ref = '시범으로 저희 그 저기 GUI 외주 줄 때 작성한 문건 있잖아요 그거 그냥 그대로 보여드리고'
    # hyp = '지원으로 그냥 저희 저 gi 외주주 때 작성한 문건 있잖아요. 그거 그냥 그대로 보여드리고'
    # print('CER: %f ' % cal_CER(ref,hyp))
    
    labels = []
    clovas = []

    with open('text.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\n',quotechar = "|")
        for i, row in enumerate(spamreader):
            labels.append(''.join(row))    

    with open('ETRI.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter = '\n',quotechar = "|")
        for i, row in enumerate(spamreader):
            clovas.append(''.join(row))    

    # pandas로 해보고싶은데,, 잘 안되네
    # Label_list = pd.read_csv("text.csv")
    # Data_list = pd.read_csv("clova.csv")
    # for i in range(len(Label_list)):
    #     print(str(Label_list[i].text))
    #     fdhjf
    #     labels.append(Label_list[i].text)
    #     clovas.append(Data_list[i].text)
    
    for i in range(len(labels)):
        print('CER: %f' % cal_CER(labels[i], clovas[i]))