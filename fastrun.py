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

summeval_2shot="Document: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statement be inferred from the above document? Yes or No?\nAndros Townsend scored for England against Italy on Wednesday . Paul Merson criticised Townsend's call-up to the England squad . Merson said Townsend should not have been in Roy Hodgson's squad . Townsend hit back at Merson on Twitter after scoring for England . \n\nA: No\n\nDocument: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statement be inferred from the above document? Yes or No?\npaul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . ' paul merson had another dig at andros townsend after his appearance for tottenham against burnley . townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley .\n\nA: Yes"
summeval_2shotcot="Document: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday.  'Just been watching the game, did you miss the coach?  #RubberDub #7minutes,' Merson put on Twitter.  Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.'  Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley .  Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley .  Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night .  The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake.  'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said.  'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad.  'When I'm wrong, I hold my hands up.  I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.'  Townsend hit back at Merson on Twitter after scoring for England against Italy .  Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week .  Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?'  Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor. \n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\nAndros Townsend scored for England against Italy on Wednesday .  Paul Merson criticised Townsend's call-up to the England squad .  Merson said Townsend should not have been in Roy Hodgson's squad .  Townsend hit back at Merson on Twitter after scoring for England .  \n\nA: 1. The document does not mention the date Andros Townsend scored for England against Italy is on Wednesday.\n2. No.\n\nDocument: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday.  'Just been watching the game, did you miss the coach?  #RubberDub #7minutes,' Merson put on Twitter.  Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.'  Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley .  Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley .  Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night .  The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake.  'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said.  'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad.  'When I'm wrong, I hold my hands up.  I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.'  Townsend hit back at Merson on Twitter after scoring for England against Italy .  Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week .  Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?'  Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor. \n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\npaul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday .  ' paul merson had another dig at andros townsend after his appearance for tottenham against burnley .  townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley .\n\nA: 1. The document does mention these content. \n2. Yes."
summeval_2shotsbs="Document: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statements be inferred from the above document? Yes or No?\n1. Andros Townsend scored for England against Italy on Wednesday . \n2. Paul Merson criticised Townsend's call-up to the England squad . \n3. Merson said Townsend should not have been in Roy Hodgson's squad . \n4. Townsend hit back at Merson on Twitter after scoring for England . \n\nA: 1. No, the document states it' s on Tuesday night. \n2. Yes.\n3. Yes.\n4. Yes.\n\nDocument: Paul Merson has restarted his row with Andros Townsend after the Tottenham midfielder was brought on with only seven minutes remaining in his team's 0-0 draw with Burnley on Sunday. 'Just been watching the game, did you miss the coach? #RubberDub #7minutes,' Merson put on Twitter. Merson initially angered Townsend for writing in his Sky Sports column that 'if Andros Townsend can get in (the England team) then it opens it up to anybody.' Paul Merson had another dig at Andros Townsend after his appearance for Tottenham against Burnley . Townsend was brought on in the 83rd minute for Tottenham as they drew 0-0 against Burnley . Andros Townsend scores England's equaliser in their 1-1 friendly draw with Italy in Turin on Tuesday night . The former Arsenal man was proven wrong when Townsend hit a stunning equaliser for England against Italy and he duly admitted his mistake. 'It's not as though I was watching hoping he wouldn't score for England, I'm genuinely pleased for him and fair play to him – it was a great goal,' Merson said. 'It's just a matter of opinion, and my opinion was that he got pulled off after half an hour at Manchester United in front of Roy Hodgson, so he shouldn't have been in the squad. 'When I'm wrong, I hold my hands up. I don't have a problem with doing that - I'll always be the first to admit when I'm wrong.' Townsend hit back at Merson on Twitter after scoring for England against Italy . Sky Sports pundit  Merson (centre) criticised Townsend's call-up to the England squad last week . Townsend hit back at Merson after netting for England in Turin on Wednesday, saying 'Not bad for a player that should be 'nowhere near the squad' ay @PaulMerse?' Any bad feeling between the pair seemed to have passed but Merson was unable to resist having another dig at Townsend after Tottenham drew at Turf Moor.\n\nQ: Can the following statements be inferred from the above document? Yes or No?\n1. paul merson has restarted his row with andros townsend after the tottenham midfielder was brought on with only seven minutes remaining in his team 's 0-0 draw with burnley on sunday . \n2. ' paul merson had another dig at andros townsend after his appearance for tottenham against burnley .\n3. townsend was brought on in the 83rd minute for tottenham as they drew 0-0 against burnley .\n\nA: 1. Yes.\n2. Yes.\n3. Yes."
xsumsota_2shot="Document: On Monday, the BBC's Panorama programme uncovered several safety concerns, from staffing levels to waste storage.\nThe Mannin Branch of the Celtic League has called on the Manx government to campaign for a full, independent inspection of the plant in Cumbria.\nSellafield says the site is safe and has been improved with significant investment in recent years.\nA spokesman added: \"Safety is our priority and we are managing a very complex site which has got a great deal of hazardous radioactive materials on it.\"\nThe Isle of Man is located about 34 miles (55km) from the nuclear fuel reprocessing plant.\nDue to its potential impact on the Manx fishing industry, the Manx government began monitoring radioactivity levels in the Irish Sea in 1989.\nA government spokesman said: \"Seafood fished in Manx waters can contain traces of radio-nuclides associated with effluent discharges from Sellafield to the Irish Sea, therefore these are monitored regularly to confirm that they remain well below maximum safe limits.\"\nThe BBC investigation was prompted by a whistle-blower - a former senior manager who was worried by conditions at the plant.\nHe said his biggest fear was a fire in one of the nuclear waste silos or in one of the processing plants.\nThe Manx government said it was particularly concerned about \"the structural integrity of ageing waste storage ponds and silos\".\nA spokesman added: \"However we are content that Sellafield Ltd and the nuclear regulators are trying to improve the safety situation.\n\"The government has asked questions about the technical solutions being developed to decommission these redundant structures and representatives have visited the site to look at the work under way\".\n\nQ: Can the following statement be inferred from the above document? Yes or No?\nCeltic football fans have called for an independent inspection of the sellafield nuclear site.\n\nA: No\n\nDocument: Thai officials said the event, which was halted minutes before it was due to start, could have affected relations between the two countries.\nThe HRW report focuses on the treatment of a Christian group in Vietnam.\nThe group said the Thai response showed how freedom of speech had been eroded since the army seized power last year.\nThai police said the event at the Foreign Correspondents Club of Thailand could \"have an impact on the country's security or could affect the friendship and cooperation between Thailand and Vietnam\".\nIt is the third human rights event at the venue that has been halted by authorities in the past month.\nThe HRW report describes what it says is the persecution of Montagnard Christians in Vietnam's central highlands. Their religious practices have been described by the Vietnamese government as \"evil\".\nSunai Phasuk, Human Rights Watch's senior researcher in Asia, said the decision to cancel the report's launch was \"very disappointing\".\n\"Thailand is now going to be known as the defender of human rights violators in [Southeast Asia], which adds more damage to Thailand's already tarnished international reputation under the military rule,\" he added.\nThai authorities have launched a crackdown on critics since the military seized power from a civilian government in May 2014.\n\nQ: Can the following statement be inferred from the above document? Yes or No?\nThai police have cancelled the launch of a human rights watch ( hrw ) report at a foreign journalists' club in bangkok.\n\nA: Yes"
xsumsota_2shotcot="Document: On Monday, the BBC's Panorama programme uncovered several safety concerns, from staffing levels to waste storage.\nThe Mannin Branch of the Celtic League has called on the Manx government to campaign for a full, independent inspection of the plant in Cumbria.\nSellafield says the site is safe and has been improved with significant investment in recent years.\nA spokesman added: \"Safety is our priority and we are managing a very complex site which has got a great deal of hazardous radioactive materials on it.\"\nThe Isle of Man is located about 34 miles (55km) from the nuclear fuel reprocessing plant.\nDue to its potential impact on the Manx fishing industry, the Manx government began monitoring radioactivity levels in the Irish Sea in 1989.\nA government spokesman said: \"Seafood fished in Manx waters can contain traces of radio-nuclides associated with effluent discharges from Sellafield to the Irish Sea, therefore these are monitored regularly to confirm that they remain well below maximum safe limits.\"\nThe BBC investigation was prompted by a whistle-blower - a former senior manager who was worried by conditions at the plant.\nHe said his biggest fear was a fire in one of the nuclear waste silos or in one of the processing plants.\nThe Manx government said it was particularly concerned about \"the structural integrity of ageing waste storage ponds and silos\".\nA spokesman added: \"However we are content that Sellafield Ltd and the nuclear regulators are trying to improve the safety situation.\n\"The government has asked questions about the technical solutions being developed to decommission these redundant structures and representatives have visited the site to look at the work under way\".\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\nCeltic football fans have called for an independent inspection of the sellafield nuclear site.\n\nA: 1. The document does not mention about the Celtic football fans.\n2. No.\n\nDocument: Thai officials said the event, which was halted minutes before it was due to start, could have affected relations between the two countries.\nThe HRW report focuses on the treatment of a Christian group in Vietnam.\nThe group said the Thai response showed how freedom of speech had been eroded since the army seized power last year.\nThai police said the event at the Foreign Correspondents Club of Thailand could \"have an impact on the country's security or could affect the friendship and cooperation between Thailand and Vietnam\".\nIt is the third human rights event at the venue that has been halted by authorities in the past month.\nThe HRW report describes what it says is the persecution of Montagnard Christians in Vietnam's central highlands. Their religious practices have been described by the Vietnamese government as \"evil\".\nSunai Phasuk, Human Rights Watch's senior researcher in Asia, said the decision to cancel the report's launch was \"very disappointing\".\n\"Thailand is now going to be known as the defender of human rights violators in [Southeast Asia], which adds more damage to Thailand's already tarnished international reputation under the military rule,\" he added.\nThai authorities have launched a crackdown on critics since the military seized power from a civilian government in May 2014.\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\nThai police have cancelled the launch of a human rights watch ( hrw ) report at a foreign journalists' club in bangkok.\n\nA: 1. The document mentions that \"Thai police said the event at the Foreign Correspondents Club of Thailand could \"have an impact on the country's security or could affect the friendship and cooperation between Thailand and Vietnam\". It is the third human rights event at the venue that has been halted by authorities in the past month.\". We can infer that the statement is correct.\n2. Yes."
xsumfaith_2shot="Document: The Cherries went down 2-1 at Sunderland on Saturday, becoming the first team to lose to the Black Cats in the Premier League this season.\nDan Gosling's goal, which gave them the lead, was their first for three games.\n\"It shouldn't be down to a lack of confidence,\" Howe told BBC Radio Solent. \"We scored six goals against Hull prior to these two games.\"\nHe continued: \"A couple of weeks later, if you were to put the chances we've created together into a clip sequence, the fact that we haven't even scored one goal is difficult to take.\"\nBournemouth were stunned by goals for Sunderland from Victor Anichebe and a Jermain Defoe penalty and they were unable to find an equaliser, even against 10 men following Steven Pienaar's dismissal.\n\"We've had enough chances to win three games today,\" Howe added.\n\"Sometimes football pans out that way and you have to accept it. It's how you move on from that which is key.\"\n\nQ: Can the following statement be inferred from the above document? Yes or No?\nbournemouth manager eddie howe says his side are \" struggling \" after losing 2-0 to hull on saturday.\n\nA: No\n\nDocument: The man died in Inverness on 27 October this year.\nThe Police Investigations and Review Commissioner (Pirc), Kate Frame, has been asked to scrutinise the initial police response to the man's call.\nPolice Scotland said it was \"fully engaging\" with the investigation and awaited its findings.\nA spokesman for Pirc said: \"The Crown Office and Procurator Fiscal Service (COPFS) has instructed the Police Investigations and Review Commissioner to undertake an investigation into the initial police response to a call from a 72-year-old man who was later found dead at a sheltered housing complex in Inverness.\n\"A report on the commissioner's findings will be submitted to the COPFS in due course.\"\n\nQ: Can the following statement be inferred from the above document? Yes or No?\na police watchdog has ordered an investigation after a 72-year-old man was found dead in a housing housing complex.\n\nA: Yes"
xsumfaith_2shotcot="Document: The Cherries went down 2-1 at Sunderland on Saturday, becoming the first team to lose to the Black Cats in the Premier League this season.\nDan Gosling's goal, which gave them the lead, was their first for three games.\n\"It shouldn't be down to a lack of confidence,\" Howe told BBC Radio Solent. \"We scored six goals against Hull prior to these two games.\"\nHe continued: \"A couple of weeks later, if you were to put the chances we've created together into a clip sequence, the fact that we haven't even scored one goal is difficult to take.\"\nBournemouth were stunned by goals for Sunderland from Victor Anichebe and a Jermain Defoe penalty and they were unable to find an equaliser, even against 10 men following Steven Pienaar's dismissal.\n\"We've had enough chances to win three games today,\" Howe added.\n\"Sometimes football pans out that way and you have to accept it. It's how you move on from that which is key.\"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\nbournemouth manager eddie howe says his side are \" struggling \" after losing 2-0 to hull on saturday.\n\nA: 1. The document does not mention eddie howe is bournemouth manager. And the document also does not mention his side lost to hull.\n2. No.\n\nDocument: The man died in Inverness on 27 October this year.\nThe Police Investigations and Review Commissioner (Pirc), Kate Frame, has been asked to scrutinise the initial police response to the man's call.\nPolice Scotland said it was \"fully engaging\" with the investigation and awaited its findings.\nA spokesman for Pirc said: \"The Crown Office and Procurator Fiscal Service (COPFS) has instructed the Police Investigations and Review Commissioner to undertake an investigation into the initial police response to a call from a 72-year-old man who was later found dead at a sheltered housing complex in Inverness.\n\"A report on the commissioner's findings will be submitted to the COPFS in due course.\"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\na police watchdog has ordered an investigation after a 72-year-old man was found dead in a housing housing complex.\n\nA: 1. The document mentions a 72-year-old man was found dead in a housing housing complex, also mentions a police watchdog has ordered an investigation after that.\n2. Yes."
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
        #a=512-(200+len(row[4].split()))
        #doc=' '.join(row[3].split( )[0:a])
        doc=row[3][0:512]

        res=1
        if method=='direct':
            a="Document: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Yes or No?\n"+ row[4]+"\n\nA:"
        elif method=='twoshot_direct':
            if dataset_name=='Xsum-Sota':
                a=xsumsota_2shot
            elif dataset_name=='XsumFaith':
                a=xsumfaith_2shot
            elif dataset_name=='SummEval':
                a=summeval_2shot
            a+="\n\nDocument: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Yes or No?\n"+ row[4]+"\n\nA:"
        elif method=='cot':
            a="\n\nDocument: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\n"+ row[4]+"\n\nA: 1."
        elif method=='twoshot_cot':
            if dataset_name=='Xsum-Sota':
                a=xsumsota_2shotcot
            elif dataset_name=='XsumFaith':
                a=xsumfaith_2shotcot
            elif dataset_name=='SummEval':
                a=summeval_2shotcot
            a+="\n\nDocument: "+doc+"\n\nQ: Can the following statement be inferred from the above document? Please answer with the following structure. 1. Try to find the supporting evidence from the document. 2. Answer Yes or No.\n"+ row[4]+"\n\nA:"
        elif method=='sbs':
            sumsentence=sentence_seg(row[4])
            a="Document: "+doc+"\n\n"
            a+="Q: Can the following statement be inferred from the above document? Yes or No?\n"
            for j in range(len(sumsentence)):
                b=str(j+1)+". "+sumsentence[j]+"\n"
                a+=b
            a+="\nA: 1."
            #print(a)
        elif method=='twoshot_sbs':
            a=summeval_2shotsbs
            sumsentence=sentence_seg(row[4])
            a+="\n\nDocument: "+doc+"\n\n"
            a+="Q: Can the following statement be inferred from the above document? Yes or No?\n"
            for j in range(len(sumsentence)):
                b=str(j+1)+". "+sumsentence[j]+"\n"
                a+=b
            a+="\nA: 1."
            #print(a)

        input_ids = tokenizer(a, return_tensors="pt").input_ids.to("cuda")
        outputs = model.generate(input_ids,max_new_tokens=max_new_tokens)
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
    if not os.path.exists('new_result1'):
        os.makedirs('new_result1') 
    output='new_result1/'+time_+'_'+str(len(data))+'.csv'
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
    result=method(data,data_name,'direct')
    print_saveresult(data,data_name,result)
    result=method(data,data_name,'twoshot_direct')
    print_saveresult(data,data_name,result)
    result=method(data,data_name,'cot')
    print_saveresult(data,data_name,result)
    result=method(data,data_name,'twoshot_cot')
    print_saveresult(data,data_name,result)
    if data_name=='SummEval':    
        result=method(data,data_name,'sbs')
        print_saveresult(data,data_name,result)
        result=method(data,data_name,'twoshot_sbs')
        print_saveresult(data,data_name,result)
        




if __name__ =='__main__':
    time_=time.strftime("%Y-%m-%d-%H-%M-%S",time.localtime(time.time()))
    if not os.path.exists('new_result1'):
        os.makedirs('new_result1')
    make_print_to_file(path='new_result1/')
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



        





        



   
    
    
        



