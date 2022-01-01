
import telebot
from telebot import types

bot = telebot.TeleBot("%%%", parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	image = open("photo/milos.jpg", "rb")
	bot.send_photo(message.chat.id, image)
	parser = open("parser.py", 'r')
	parser1 = parser.read()
	bot.reply_to(message, parser1)

	markup = types.ReplyKeyboardMarkup(row_width=2)
	itembtn1 = types.KeyboardButton('Смело')
	itembtn2 = types.KeyboardButton('Не хочу')

	markup.add(itembtn1, itembtn2)

	bot.send_message(message.chat.id, "Сделай выбор мудро:", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def answer(message):
	if message.text == 'Смело':
		markup = types.InlineKeyboardMarkup(row_width = 2)
		oil1 = telebot.types.InlineKeyboardButton("Вазелин", callback_data = 'vaseline')
		oil2 = telebot.types.InlineKeyboardButton("Слюна", callback_data = 'saliva')
		oil3 = telebot.types.InlineKeyboardButton("Клиторовое масло", callback_data = 'clitor_oil')
		oil4 = telebot.types.InlineKeyboardButton("На сухую", callback_data = 'dry')
		markup.add(oil1, oil2, oil3, oil4)

		bot.send_message(message.chat.id, "Чем смажешь очко?", reply_markup=markup)
	elif message.text == 'Не хочу':
		bot.send_message(message.chat.id, "Тикай тогда отсюдова!")


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
	try:
		if call.message:
			if call.data == 'vaseline':
				bot.send_message(call.message.chat.id, 'Смазывай очко вазелином')
			if call.data == 'saliva':
				bot.send_message(call.message.chat.id, 'Тогда копи слюну')
			if call.data == 'clitor_oil':
				bot.send_message(call.message.chat.id, 'Неси ведрами тогда')
			if call.data == 'dry':
				bot.send_message(call.message.chat.id, 'А ты хардкорщик))')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id)
	except:
		print("Error")

bot.polling(none_stop = True)