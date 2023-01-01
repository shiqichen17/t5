import math
import argparse
import pandas as pd
from time import sleep
from transformers import T5Tokenizer, T5ForConditionalGeneration
import pdb
xsumeval_2shot="Document: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statement be inferred from the above document?\nAndros Townsend scored for England against Italy on Wednesday . Paul Merson criticised Townsend's call-up to the England squad . Merson said Townsend should not have been in Roy Hodgson's squad . Townsend hit back at Merson on Twitter after scoring for England . \n\nA: No\n\nDocument: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statement be inferred from the above document?\npaul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . ' paul merson had another dig at andros townsend after his appearance for tottenham against burnley . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley .\n\nA: Yes\n"
xsumeval_2shotsbs="Document: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statement be inferred from the above document?Yes or No?\n1. Andros Townsend scored for England against Italy on Wednesday . \n2. Paul Merson criticised Townsend's call-up to the England squad . \n3. Merson said Townsend should not have been in Roy Hodgson's squad . \n4. Townsend hit back at Merson on Twitter after scoring for England . \n\nA: \n1. No, the document states it' s on Tuesday night. \n2. Yes.\n3. Yes.\n4. Yes.\n\nDocument: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Are the following statements correct according to the above document? Yes or No?\n1. paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . \n2. ' paul merson had another dig at andros townsend after his appearance for tottenham against burnley .\n3. townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley .\n\nA: \n1. Yes.\n2. Yes.\n3. Yes.\n\n"

from transformers import T5Tokenizer, T5ForConditionalGeneration
import pdb
cache_dir='checkpoints/hf_model'

def parse_args():
    parse=argparse.ArgumentParser()
    parse.add_argument('--n',type=int,help='data number feeded each iteration')
    parse.add_argument('--data',type=str,help='dataset name')
    args = parse.parse_args()  
    return args

def method(data,dataset_name,n,method):
    result={}
    tokenizer = T5Tokenizer.from_pretrained("google/flan-t5-xxl",cache_dir=cache_dir)
    model = T5ForConditionalGeneration.from_pretrained("google/flan-t5-xxl",cache_dir=cache_dir, device_map="auto")

    for i,row in data.iterrows():
        _id=str(i)
        doc=' '.join(row[3].split( )[0:1024])

        res=1
        if method=='direct':
            a="Document: "+doc+"\n\nQ: Can the following statement be inferred from the above document?\n"+ row[4]+"\n\nA:"
        elif method=='twoshot_direct':
            if dataset_name=='Xsum-Sota':
                a=''
            elif dataset_name=='Xsumfaith':
                a=''
            elif dataset_name=='SummEval':
                a=''
            a+="Document: "+doc+"\n\nQ: Can the following statement be inferred from the above document?"+ row[4]+"\n\nA:"
        elif method=='cot':
            a="Document: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\n"+ row[4]+"\n\nA:"
        elif method=='twoshot_cot':
            if dataset_name=='Xsum-Sota':
                a=''
            elif dataset_name=='Xsumfaith':
                a=''
            elif dataset_name=='SummEval':
                a=''
            a+="Document: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\n"+ row[4]+"\n\nA:"
        input_ids = tokenizer(a, return_tensors="pt").input_ids.to("cuda")
        outputs = model.generate(input_ids)
        print(tokenizer.decode(outputs[0]))

        if method=='direct' or 'twoshot_direct' :
            res=max(0,res-('No' in tokenizer.decode(outputs[0])))
        elif method=='cot' or 'twoshot_cot':
            res=max(0,res-('2. No' in tokenizer.decode(outputs[0])))
        if res==row[6]==1:
            print("TP")
        elif res==row[6]==0:
            print("TN")
        elif res==1 and row[6]==0:
            print("FP")
        else:
            print('FN')
        result[_id] = {'pred': res, 'raw': tokenizer.decode(outputs[0]), 'prompt': a}
        if i%n==0:
            sleep(10) 
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

if __name__=='__main__':
    args=parse_args()
    pdb.set_trace()
    n=args.n
    data_name=args.data
    data=pd.read_csv('ori_data/aggre_fact_final.csv')
    data=data.loc[data['cut']=='test']
    if data_name=='SummEval':
        data=data.loc[data['dataset']=='SummEval']
        data=data.loc[data['model_name']!='LEAD3']
        print(data_name,len(data))
    elif data_name=='Xsum-Sota':
        data=pd.read_csv('ori_data/aggre_fact_sota.csv')
        data=data.loc[data['cut']=='test']
        data=data.loc[data['origin']=='xsum']
        data=data.loc[data['dataset'].isin(['CLIFF','Goyal21'])]
        print(data_name,len(data))
    elif data_name=='XsumFaith':
        data=data.loc[data['origin']=='xsum']
        data=data.loc[data['dataset']=='XSumFaith']
        data=data.loc[~data['model_name'].isin (['Gold'])]
        print(data_name,len(data))
    result=method(data,data_name,n,'direct')
    print('ALL'+str(compute_accuracy(data, result)))
    
    print('Wang20'+str(compute_accuracy(data.loc[data['dataset']=='Wang20'], result)))
    print('Cao22'+str(compute_accuracy(data.loc[data['dataset']=='Cao22'], result)))
    print('CLIFF'+str(compute_accuracy(data.loc[data['dataset']=='CLIFF'], result)))
    print('Goyal21'+str(compute_accuracy(data.loc[data['dataset']=='Goyal21'], result))) 
    
    '''
    print('Former'+str(compute_accuracy(data.loc[data['model_name'].isin(['BERTS2S','TranS2S'])], result)))
    print('Old'+str(compute_accuracy(data[~data['model_name'].isin(['BERTS2S','TranS2S'])], result)))  
    '''
    time_=time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    output='result/'+time_+'_'+str(len(data))+'.csv'
    save_exp(data, result, output)    
    
    
        



