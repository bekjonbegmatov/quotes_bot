import aiogram
import config
import requests
import logging
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
from aiogram.types import ChatActions
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
    InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(level=logging.INFO)
 
# from bot import category as bot_categoriy_list

bot = Bot(token=config.token)
dp = Dispatcher(bot)
bot_categoriy_list = [
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
def random_image():
    img_url = "https://random.imagecdn.app/500/500"
    img = requests.get(img_url).content
    with open('img.png' , 'wb') as handler :
        handler.write(img)
def draw(cate):
    img = Image.open('img.png')
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
    # print('text1 ==> ' , text1)
    # print('text2 ==> ' , text2)
    I1 = ImageDraw.Draw(img)
    myFont = ImageFont.truetype('fonts/Cabin/Cabin-VariableFont_wdth,wght.ttf', 20)
    # Add Text to an image
    I1.text((10, 400), text1 , font=myFont, fill=(255, 255, 255))
    I1.text((10, 430), text2 , font=myFont, fill=(255, 255, 255))

    img.save('img.jpg')
    return img

markup3 = ReplyKeyboardMarkup()
markup3.add(KeyboardButton("MENU🏠"))
for i in bot_categoriy_list:
    markup3.add(KeyboardButton(i.upper()))

all_category = KeyboardButton('All Category 🧾')
random_quotes = KeyboardButton('Random Quotes 🎲')
hello = ReplyKeyboardMarkup().add(
    random_quotes).add(all_category)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Hello " + message.chat.first_name + " !\n I'm Quotes bot , I generate for you Quotes with picture." , reply_markup=hello)

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.reply('I\'m a quote bot and I can generate quotes with categories \nWrite /quote')

@dp.message_handler(commands=['quote'])
async def help_command(message: types.Message):
    await message.reply("Choose one from the category !" , reply_markup=markup3)
@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'MENU🏠':
        await message.reply("Hello " + message.chat.first_name + "OK" , reply_markup=hello)
    if message.text == 'Random Quotes 🎲':
        category = bot_categoriy_list[round(random.uniform(0 , len(bot_categoriy_list)))]
        random_image()
        photo = draw(category)
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_PHOTO)
        await bot.send_photo(message.chat.id, photo=open('img.jpg' , 'rb'))
        return 
    test = False
    for i in bot_categoriy_list:
        if i.lower() == (message.text).lower():
            test = True
            break
    if message.text == 'All Category 🧾':
        await message.reply("Choose one from the category !" , reply_markup=markup3)
    elif test:
        category = (message.text).lower()
        random_image()
        photo = draw(category)
        # await bot.send_chat_action('upload_photo')
        await bot.send_chat_action(message.chat.id, ChatActions.UPLOAD_PHOTO)
        await bot.send_photo(message.chat.id, photo=open('img.jpg' , 'rb'))
    else :
        await message.reply("Choose one from the category !" , reply_markup=markup3)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)