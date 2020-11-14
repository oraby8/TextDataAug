import textblob

class BackTranselate:
	def __init__(self):
		pass
	def translate(self,sent,from_lang,to_lang):
		return(str(textblob.TextBlob(sent).translate(to=to_lang,from_lang=from_lang)))

	def backtranselate(self,sent,from_lang,to_lang):
		if type(sent)=='str':
			target_translate=self.translate(sent,from_lang,to_lang)
			back_translate=self.translate(target_translate,to_lang,from_lang)
			return back_translate
		else:
			return sent

	def lang_codes(self):
		try:
			with open('lang_codes.txt') as file:
				print(file.readlines())
		except:
			print('lang_codes is missing')


