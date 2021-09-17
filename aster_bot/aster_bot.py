import telebot
import mySearchNumber
token = '1966342656:AAEikQMfVsuHureW2I8fJhPJtx4zG64rVvc'
user_info=[]
bot = telebot.TeleBot(token)
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if len(message.text) == 4 and message.text.isdigit():
        user_info = mySearchNumber.getSearchNumber(message.text)
        bot.send_message(message.from_user.id, "Номер = "+str(user_info['extension']))
        bot.send_message(message.from_user.id, "ФИО = "+str(user_info['name']))
        bot.send_message(message.from_user.id, "Пароль = "+str(user_info['password']))
        markup=telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(text='Изменить пароль', callback_data=3))
        markup.add(telebot.types.InlineKeyboardButton(text='Изменить ФИО', callback_data=3))
        bot.send_message(message.chat.id, text='Что сделать с данным номером?', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, 'не подходит')
@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    bot.answer_callback_query(callback_query_id=call.id, text='Команда принята!!!')
    answer = ''
    if call.data == '1':
        answer = 'Вы троечник!'
    elif call.data == '2':
        print('1')
    elif call.data == '3':
        answer = 'Вы отличник!'
    bot.send_message(call.message.chat.id, answer)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)
bot.polling(none_stop=True, interval=0)