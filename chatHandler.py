from telebot.types import ReplyKeyboardMarkup, KeyboardButton

texts = {
    'onstart': 'Здравсвуйте. Пожалуйста выберите язык. Assalomu aleykum. Iltimos, hohlagan tilingizni tanlang.',
    
}

#The dictionary consisting key-value QA's
chat_logic_ru = {
    'Привет':'Привет!',
    'Как дела?':'Хорошо! Как у тебя?',
}
chat_logic_uz = {
    'Salom':'Salom!',
    'Ishla qale?':'Yaxmale!',
}
stages = {
    
}
#Language menu
markup = ReplyKeyboardMarkup()
set_to_russian = KeyboardButton(text="Русский")
set_to_uzbek = KeyboardButton(text="O'zbekcha")
markup.add(set_to_russian)
markup.add(set_to_uzbek)
stages['language_pref'] = markup
#After the language was chosen comes main menu (Russian)
markup = ReplyKeyboardMarkup()
products = KeyboardButton(text='Продукты')
support = KeyboardButton(text='Поддержка')
markup.add(products)
markup.add(support)
stages['main_ru'] = markup
