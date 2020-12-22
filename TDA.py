from nltk.corpus import stopwords,wordnet
from random import choice,shuffle,uniform,randint
from string import punctuation,digits
from translate import BackTranselate
from langcodes import LANGCODES,WORDNETLAN

class DataAugmentation:
	def __init__(self,text_language='english'):
		'''
		>>DataAugmentation(text_language)
		>>DataAugmentation('arabic')
		>>DataAugmentation('english')
		>>DataAugmentation('Spanish')
		'''
		self.lan=text_language
		self.syn_lan=self.Lang_syn('lan')
		self.wordnet_lan=self.Lang_syn('wordnet')
		self.stopwords_list=stopwords.words(self.lan)

	def Lang_syn(self,type_):
		if type_=='lan':
			lan=LANGCODES
		else:
			lan=WORDNETLAN
		for syn,name in lan.items():
			if syn.lower()==self.lan.lower():
				return name
		print('unkown language name.')
		return 'en'

	def SentProcessing(self,sent):
		low_sent=sent.lower()
		sent_without_punc=[i for i in low_sent if i not in punctuation]
		return ''.join(sent_without_punc)

	def get_synonyms(self,word):
		''' get synonyms for wordnet data courps'''
		synonyms = set()
		for syn in wordnet.synsets(word,lang=self.wordnet_lan): 
			for l in syn.lemmas(): 
				synonym = l.name().replace("_", " ").replace("-", " ").lower()
				synonym = "".join([char for char in synonym if char in ' qwertyuiopasdfghjklzxcvbnm'])
				synonyms.add(synonym) 
		if word in synonyms:
			synonyms.remove(word)
		return list(synonyms)

	def SynonymReplacement(self,sent,num):
		'''Randomly
		choose n words from the sentence that are not
		stop words. Replace each of these words with
		one of its synonyms chosen at random.'''
		chosen_index=[]
		psent=self.SentProcessing(sent)
		pro_sent=psent.split()
		if num > len(pro_sent):
			num = len(pro_sent)-1
		for i in range(num):
			while True:
				choice_index=choice([i[0] for i in enumerate(pro_sent)])
				if choice_index not in chosen_index and pro_sent[choice_index] not in self.stopwords_list:
					break
			chosen_index.append(choice_index)
			syn_words=self.get_synonyms(pro_sent[choice_index])
			if syn_words ==[]:
				syn_word=self.SynonymReplacement(''.join([i[1] for i in enumerate(pro_sent) if i[0] != choice_index and i[0] not in chosen_index]),num-i)
			else:
				syn_word=choice(syn_words)
				pro_sent[choice_index]=syn_word
		return ' '.join(pro_sent)


	def Random_Insertion(self,sent,num):
		''' Find a random synonym of a random word in the sentence that is
		not a stop word. Insert that synonym into a random position in the sentence. Do this n times.'''
		chosen_index=[]
		psent=self.SentProcessing(sent)
		pro_sent=psent.split()
		sent_pos=[i for i in range(len(pro_sent))]
		if num > len(pro_sent):
			num = len(pro_sent)-1
		for i in range(num):
			while True:
				choice_index=choice([i[0] for i in enumerate(pro_sent)])
				if choice_index not in chosen_index and pro_sent[choice_index] not in self.stopwords_list:
					break
			chosen_index.append(choice_index)
			syn_words=self.get_synonyms(pro_sent[choice_index])
			if syn_words ==[]:
				syn_word=self.Random_Insertion(''.join([i[1] for i in enumerate(pro_sent) if i[0] != choice_index and i[0] not in chosen_index]),num-i)
			else:
				syn_word=choice(syn_words)
				random_pos=choice(sent_pos)
				pro_sent.insert(random_pos,syn_word)
		return ' '.join(pro_sent)

	def Random_Swap(self,sent):
		'''Randomly choose two
		words in the sentence and swap their positions.
		Do this n times'''
		chosen_index=[]
		psent=self.SentProcessing(sent)
		pro_sent=psent.split()
		sent_pos=[i for i in range(len(pro_sent))]
		shuffle(sent_pos)
		for i in range(2):
			while True:
				choice_index=choice([i for i in sent_pos])
				if choice_index not in chosen_index and pro_sent[choice_index]:
					break
			chosen_index.append(choice_index)
		temp0=pro_sent[chosen_index[0]]
		temp1=pro_sent[chosen_index[1]]
		pro_sent[chosen_index[0]]=temp1
		pro_sent[chosen_index[1]]=temp0
		return ' '.join(pro_sent)

	def Random_Deletion(self,sent,probability):
		'''Randomly remove
		each word in the sentence with probability p'''
		psent=self.SentProcessing(sent)
		sent_list=psent.split()
		if len(sent_list) == 1:
			return ''.join(sent_list)
		new_sents = []
		for word in sent_list:
			r = uniform(0, 1)
			if r > probability:
				new_sents.append(word)
		if len(new_sents) == 0:
			rand_int = randint(0, len(sent_list)-1)
			return ''.join([sent_list[rand_int]])

		return ' '.join(new_sents)

	def AugPipeLine(self,sent,num,probability,bktr=True,translate_to='es'):
		'''DataAugmentation pipeline has (SynonymReplacement,Random_Swap,Random_Swap,Random_Deletion).
		#how to call it 
		AugPipeLine(sent,num,probability,bktr=True,translate_to='es')
		'''
		listofeda=[]
		pro_sent=self.SentProcessing(sent)
		listofeda.append(pro_sent)
		listofeda.append(self.SynonymReplacement(sent,num))
		listofeda.append(self.Random_Insertion(sent,num))
		listofeda.append(self.Random_Swap(sent))
		listofeda.append(self.Random_Deletion(sent,probability))
		if bktr:
			tran=BackTranselate()
			listofeda.append(tran.backtranselate(pro_sent,self.syn_lan,translate_to))

		return listofeda
