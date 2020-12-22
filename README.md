# TextDataAug

TextDataAug is pipeline has implemented for Boosting Performance on
Text Classification tasks by using "Easy Data Augmentation" , "Back-Translation" techniques and to support 22 languages.Given a sentence in the training set, we perform the following operations:

* **Synonym Replacement (SR)**: Randomly choose n words from the sentence that are not stop words. Replace each of these words with one of its synonyms chosen at random.
* **Random Insertion (RI)**: Find a random synonym of a random word in the sentence that is not a stop word. Insert that synonym into a random position in the sentence. Do this n times.
* **Random Swap (RS)**: Randomly choose two words in the sentence and swap their positions. Do this n times.
* **Random Deletion (RD)**: For each word in the sentence, randomly remove it with probability p.
* **Back-Translation**

The pipeline has been implemented based on [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/pdf/1901.11196.pdf) and [Low Resource Text Classification with ULMFit and Backtranslation](https://arxiv.org/pdf/1903.09244.pdf).

TextDataAug supports 22 languages:
--
Arabic , Catalan , Danish , English , Basque , Persian , Finnish , French , Galician , Hebrew , Indonesian , Italian , Japanese , Norwegian Nynorsk , Norwegian Bokmål , Polish , Polish , Spanish , Thai , Mal

Requirements
--

Python 3

The following software packages are dependencies.

````
$ pip install numpy nltk gensim textblob googletrans 
````

The following code downloads stopwords and wordnet data

````
nltk.download('stopwords')
nltk.download('omw')
nltk.download('wordnets')
````

Usage
--
````
tda=DataAugmentation('english')
text_out=tda.AugPipeLine("Great movie. This is the type of movie you just want to watch time and time again. A real classic.)
````
````
tda=DataAugmentation('english')
print(tda.AugPipeLine("Great movie. This is the type of movie you just want to watch time and time again. A real classic.",num=2,probability=0.2,bktr=True,translate_to='es'))
````
References
--
* [EDA: Easy Data Augmentation Techniques for Boosting Performance on Text Classification Tasks](https://arxiv.org/pdf/1901.11196.pdf)
* [Low Resource Text Classification with ULMFit and Backtranslation](https://arxiv.org/pdf/1903.09244.pdf)
