import math
import argparse
import pandas as pd
from transformers import T5Tokenizer, T5ForConditionalGeneration
import pdb
cache_dir='checkpoints/hf_model'
import argparse
import pandas as pd
from time import sleep
import time
import os
from tenacity import (
    retry,
    stop_after_attempt,
    wait_random_exponential,
)
from collections import OrderedDict

def parse_args():
    parse=argparse.ArgumentParser()
    parse.add_argument('--data',type=str,help='dataset name')
    args = parse.parse_args()  
    return args
 
def sentence_seg(paragraph):
    paragraph = paragraph.lower()
    #加载punkt句子分割器
    sen_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle') 
    sentences = sen_tokenizer.tokenize(paragraph)
    return sentences
def make_print_to_file(path='logger/'):
    import sys
    import os
    import sys
    import datetime
 
    class Logger(object):
        def __init__(self, filename="Default.log", path="./"):
            self.terminal = sys.stdout
            self.path= os.path.join(path, filename)
            self.log = open(self.path, "a", encoding='utf8',)
            print("save:", os.path.join(self.path, filename))
 
        def write(self, message):
            self.terminal.write(message)
            self.log.write(message)
 
        def flush(self):
            pass
 
 
 
 
    #fileName = datetime.datetime.now().strftime('day'+'%Y_%m_%d_%H_%M_%S')
    fileName = datetime.datetime.now().strftime('day'+'%Y_%m_%d')

    sys.stdout = Logger(fileName + '.log', path=path)
 
    print(fileName.center(60,'*'))



def method(data,dataset_name,method):
    max_length=4000
    max_new_tokens=300
    result={}

    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl",max_length=max_length,cache_dir=cache_dir)
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl",cache_dir=cache_dir, device_map="auto")

    for i,row in data.iterrows():
        _id=str(i)
        # a=512-(200+len(row[4].split()))
        # doc=' '.join(row[3].split( )[0:a])
        doc=' '.join(row[3].split( )[0:512])

        res=1
        if method=='direct':
            a="Document: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Yes or No?\n"+ row[4]+"\n\nA:"
        
        elif method=='cot':
            a="\n\nDocument: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\n"+ row[4]+"\n\nA: 1."
        
        elif method=='sbs':
            sumsentence=sentence_seg(row[4])
            a="Document: "+doc+"\n\n"
            a+="Q: Can the following statement be inferred from the above document? Yes or No?\n"
            for j in range(len(sumsentence)):
                b=str(j+1)+". "+sumsentence[j]+"\n"
                a+=b
            a+="\nA: 1."
            #print(a)
            #print(a)

        input_ids = tokenizer(a, return_tensors="pt").input_ids.to("cuda")
        outputs = model.generate(input_ids,max_new_tokens=max_new_tokens,do_sample=True,temperature=0.7)
        print(tokenizer.decode(outputs[0]))
        generate=tokenizer.decode(outputs[0])
        if method=='direct' or method=='twoshot_direct' or method=='sbs' or method=='twoshot_sbs':
            res=max(0,res-('No' in generate))
        elif method=='cot' or method=='twoshot_cot':
            res=max(0,res-('2. No' in generate))
        
        if res==row[6]==1:
            print("TP")
        elif res==row[6]==0:
            print("TN")
        elif res==1 and row[6]==0:
            print("FP")
        else:
            print('FN')
        result[_id] = {'pred': res, 'raw': generate, 'prompt': a}

    return result

def compute_accuracy(data, res):
    TP=0
    TN=0
    FP=0
    FN=0
    for i, row in data.iterrows():
        id_, label = str(i), row['label']
        if res[id_]['pred'] == 1:
            if label == 1:
                TP += 1
            elif label == 0:
                FP += 1
            else:
                raise ValueError
        elif res[id_]['pred'] == 0:
            if label == 0:
                TN += 1
            elif label == 1:
                FN += 1
            else:
                raise ValueError
        else:
            raise ValueError

    return {
        'class 1': TP/(TP+FN) if TP+FN!=0 else None,
        'class 0': TN/(TN+FP) if TN+FP!=0 else None,
        'true num': TP + FN,
        'false num': TN + FP,
        'balanced': 0.5*(TP/(TP+FN)+TN/(TN+FP)) if TP+FN!=0 and TN+FP!=0 else None
    }
def print_saveresult(data,data_name,result):
    print('ALL'+str(compute_accuracy(data, result)))
    if data_name=='Xsum-Sota':
        print('---xsumsota---')
        print('Wang20'+str(compute_accuracy(data.loc[data['dataset']=='Wang20'], result)))
        print('Cao22'+str(compute_accuracy(data.loc[data['dataset']=='Cao22'], result)))
        print('CLIFF'+str(compute_accuracy(data.loc[data['dataset']=='CLIFF'], result)))
        print('Goyal21'+str(compute_accuracy(data.loc[data['dataset']=='Goyal21'], result))) 
        print('---xsumsota---')
    elif data_name=='XsumFaith':
        print('---xsumfaith---')
        print('Former'+str(compute_accuracy(data.loc[data['model_name'].isin(['BERTS2S','TranS2S'])], result)))
        print('Old'+str(compute_accuracy(data[~data['model_name'].isin(['BERTS2S','TranS2S'])], result)))  
        print('---xsumfaith---')
    elif data_name=='SummEval':
        print('---summeval---')
        print('Sota'+str(compute_accuracy(data.loc[data['model_name'].isin(['BART','Pegasus','PegasusDynamic','T5'])], result)))
        print('Former'+str(compute_accuracy(data.loc[data['model_name'].isin (['GPT2'])], result)))
        print('Old'+str(compute_accuracy(data[~data['model_name'].isin (['BART','Pegasus','PegasusDynamic','T5','GPT2'])], result)))
        print('---summeval---')
    time_=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    if not os.path.exists('new_result2'):
        os.makedirs('new_result2') 
    output='new_result2/'+time_+'_'+str(len(data))+'.csv'
    save_exp(data, result, output)

def save_exp(data, result, output):
    print(f'save results to {output}')
    init = (('dataset',[]),('doc', []), ('sum', []), ('model_name',[]),('label', []), ('prompt', []), ('gen', []), ('res', []), ('true or false', []))
    save = OrderedDict(init)
    for i, row in data.iterrows():
        id_, dataset,doc, sum, model_name, label = str(i), row['dataset'],row['doc'], row['summary'], row['model_name'],row['label']
        prompt = result[id_]['prompt']
        gen = result[id_]['raw']
        res = result[id_]['pred']
        t_or_f = int(res == label)

        save['dataset'].append(dataset)
        save['doc'].append(doc)
        save['sum'].append(sum)
        save['model_name'].append(model_name)
        save['label'].append(label)
        save['prompt'].append(prompt)
        save['gen'].append(gen)
        save['res'].append(res)
        save['true or false'].append(t_or_f)

    df = pd.DataFrame(data=save)
    df.to_csv(output)
def do(data,data_name):
    # result=method(data,data_name,'direct')
    # print_saveresult(data,data_name,result)
    result=method(data,data_name,'cot')
    print_saveresult(data,data_name,result)
    if data_name=='SummEval':    
        result=method(data,data_name,'sbs')
        print_saveresult(data,data_name,result)
        




if __name__ =='__main__':
    time_=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    if not os.path.exists('new_result2'):
        os.makedirs('new_result2')
    make_print_to_file(path='new_result2/')
    args=parse_args()
    data_name=args.data
    data=pd.read_csv('ori_data/aggre_fact_final.csv')
    data=data.loc[data['cut']=='test']
    if data_name=='SummEval':
        data=data.loc[data['dataset']=='SummEval']
        data=data.loc[data['model_name']!='LEAD3']
        print(data_name,len(data))
        do(data,data_name)
    elif data_name=='Xsum-Sota':
        data=pd.read_csv('ori_data/aggre_fact_sota.csv')
        data=data.loc[data['cut']=='test']
        data=data.loc[data['origin']=='xsum']
        data=data.loc[data['dataset'].isin(['CLIFF','Goyal21'])]
        print(data_name,len(data))
        do(data,data_name)
       
    elif data_name=='XsumFaith':
        data=data.loc[data['origin']=='xsum']
        data=data.loc[data['dataset']=='XSumFaith']
        data=data.loc[~data['model_name'].isin (['Gold'])]
        print(data_name,len(data))
        do(data,data_name)



        





        



   
    
    
        



