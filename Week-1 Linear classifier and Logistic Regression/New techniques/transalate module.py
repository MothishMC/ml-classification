from translate import Translator
translator = Translator(from_lang='english',to_lang='french')
print(translator.translate('Hello everyone'))

dict = {"a": "123", "b": "456", "c": "789"}
string = "abc"
print(string.maketrans(dict))
