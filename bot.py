# url = 'https://api.api-ninjas.com/v1/quotes?category=amazing'


import telebot
import config
import random
 
from telebot import types
# Importing the PIL library
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import requests

def get_img(img_name):
    img_url = "https://random.imagecdn.app/500/150"
    img = requests.get(img_url).content
    with open(img_name , 'wb') as handler :
        handler.write(img)
    return img

 
bot = telebot.TeleBot(config.token)

category = [
    'alone',
    'amazing',
    'art',
    'attitude',
    'beauty',
    'birthday',
    'business',
    'car',
    'change',
    'communications',
    'design',
    'dreams',
    'education',
    'environmental',
    'equality',
    'funny',
    'good',
    'government',
    'graduation',
    'great',
    'happiness',
    'health',
    'history',
    'home',
    'hope',
    'humor',
    'learning',
    'legal',
    'life',
    'love',
    'marriage',
    'medical',
    'money',
    'morning',
    'movies',
    'success',
]
 
def get_image_whits_text(category_q):
    
    category = category_q
    api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': '6MJhoJV2dUNo1n9+iU8zKg==zeePk0oeyQoceKv5'})
    r = response.json()[0]
    text = r['quote']
    text_l = len(text)
    text1 = ''
    text2 = ''
    test = True
    for i in range(text_l):
        if i >=(text_l/2) and text[i]== " " and test==True:
            test = False
        elif test == False:
            text2+=text[i]
        else:
            text1+=text[i]
    print('text1 ==> ' , text1)
    print('text2 ==> ' , text2)

    # Open an Image
    img = get_img('img.jpg')
    
    I1 = ImageDraw.Draw(img)

    myFont = ImageFont.truetype('fonts/Cabin/Cabin-VariableFont_wdth,wght.ttf', 20)
    
    # Add Text to an image
    I1.text((10, 400), text1 , font=myFont, fill=(255, 255, 255))
    I1.text((10, 430), text2 , font=myFont, fill=(255, 255, 255))

    img.save("img.png")
    return img
 
@bot.message_handler(commands=['start'])
def welcome(message):
    sti = open('static/salom.tgs', 'rb')
    bot.send_sticker(message.chat.id, sti)
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Random Quotes")
    item2 = types.KeyboardButton("😊 All Category")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Welcome , {0.first_name}!\nI'm  - <b>{1.first_name}</b>, I generate for you Quotes with picture.".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == '🎲 Random Quotes':

            bot.send_message(message.chat.id, str(random.randint(0,100)))
        elif message.text == '😊 All Category':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton("Alone", callback_data='alone')
            item2 = types.InlineKeyboardButton("Amazing", callback_data='amazing')
            item3 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item4 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item5 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item6 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item7 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item8 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item9 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item10 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item11 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item12 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item13 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item14 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            item15 = types.InlineKeyboardButton("Не очень", callback_data='bad')
 
            markup.add(item1, item2 , item3 , item4)
 
            bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'alone':
                get_image_whits_text('alone')
                # img = 
                bot.send_chat_action(call.message.chat.id, 'upload_photo')
                bot.send_photo(call.message.chat.id, photo=open('img.png', 'rb') , reply_to_message_id=call.message.chat.id)
                print()
                # print(call.message.chat.id , get_image_whits_text('alone') )

                # bot.send_chat_action(call.message.chat.id, 'upload_photo')
                # bot.send_photo(call.message.chat.id, get_image_whits_text('alone'), reply_to_message_id=call.message.chat.id)

                # bot.send_message(call.message.chat.id, 'Вот и отличненько 😊')
            elif call.data == 'amazing':
                img_url = "https://random.imagecdn.app/500/150"
                img = requests.get(img_url).content
                category = 'amazing'
                api_url = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
                response = requests.get(api_url, headers={'X-Api-Key': '6MJhoJV2dUNo1n9+iU8zKg==zeePk0oeyQoceKv5'})
                r = response.json()[0]
                text = r['quote']
                text_l = len(text)
                text1 = ''
                text2 = ''
                test = True
                for i in range(text_l):
                    if i >=(text_l/2) and text[i]== " " and test==True:
                        test = False
                    elif test == False:
                        text2+=text[i]
                    else:
                        text1+=text[i]
                print('text1 ==> ' , text1)
                print('text2 ==> ' , text2)

                # Open an Image
                # img = img
                
                I1 = ImageDraw.Draw(img)

                myFont = ImageFont.truetype('fonts/Cabin/Cabin-VariableFont_wdth,wght.ttf', 20)
                
                # Add Text to an image
                I1.text((10, 400), text1 , font=myFont, fill=(255, 255, 255))
                I1.text((10, 430), text2 , font=myFont, fill=(255, 255, 255))

                # img.save("img.png")
                bot.send_chat_action(call.message.chat.id, 'upload_photo')
                bot.send_photo(call.message.chat.id, img, reply_to_message_id=call.message.chat.id)

                # bot.send_message(call.message.chat.id, 'Бывает 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="😊 Как дела?",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)
