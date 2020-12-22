# TextDataAug

TextDataAug is pipeline has implemnted for Boosting Performance on
Text Classification tasks by using "Easy Data Augmentation" Technique and "Back-Translation" Technique.

The pipeline has been implemented based on [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/pdf/1901.11196.pdf) and [Low Resource Text Classification with ULMFit and Backtranslation](https://arxiv.org/pdf/1903.09244.pdf).

TextDataAug supports 22 languages:
--
Arabic , Catalan , Danish , English , Basque , Persian , Finnish , French , Galician , Hebrew , Indonesian , Italian , Japanese , Norwegian Nynorsk , Norwegian Bokmål , Polish , Polish , Spanish , Thai , Mal

Requirements
--

Python 3
The following software packages are dependencies and will be installed automatically.
''' bash
$ pip install numpy nltk gensim textblob googletrans 
'''
The following code downloads stopwords amd wordnet data

'''bash
nltk.download('stopwords')
nltk.download('omw')
nltk.download('wordnets')
'''

Usage
--
'''bash
tda=DataAugmentation('english')
text_out=tda.AugPipeLine("Great movie. This is the type of movie you just want to watch time and time again. A real classic.)
'''
'''bash
tda=DataAugmentation('english')
print(tda.AugPipeLine("Great movie. This is the type of movie you just want to watch time and time again. A real classic.",num=2,probability=0.2,bktr=True,translate_to='es'))
'''
