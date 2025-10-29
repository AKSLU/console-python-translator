from deep_translator import GoogleTranslator

languages = ['fr', 'it', 'es', 'kk', 'en', 'ru']  

text = input("Введите текст для перевода: ")

for language in languages:
    translation = GoogleTranslator(source='auto', target=language).translate(text)
    print(f'{language}: {translation}')
