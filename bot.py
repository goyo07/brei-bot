from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, Dispatcher
from telegram import ParseMode
import logging

import os
import random
import time

PORT = int(os.environ.get('PORT', 3978))
TOKEN = os.environ.get('TOKEN')

logging.basicConfig(format='%(levelname)s - %(message)s',
                    level=logging.DEBUG)
logger = logging.getLogger(__name__)

command_fun = """
😂 *Fun \(\/fun \[command\]\)*
\- 8ball \<insert question\> \: _ask a yes or no question_
\- jeje \<insert message\> \: _translates simple text in jejemon_
\- dice \: _roll a dice_
\- coin \: _flip a coin_
\- fortunecookie \: _get a wisdom from fortune cookie_
\- sing \: _brei sings a song for you from her [channel](https://www.youtube.com/channel/UCGDnSYJdZ4fZerm7Syz9ZXA)_
"""

command_react = """
❤️ *React \(\/react \[command\]\)*
\- hug \<username\> \: _sends a virtual hug_
\- slap \<username\> \: _slap someone you hate_
\- cheerup \<username\> \: _cheer up someone sad_
\- kiss \<username\> \: _kiss someone you love_
\- cry \: _sends a crying reaction_
\- cringe \: _send this when something is cringy_
\- happy \: _sends a happy reaction_
\- dance \: _send if you are hyped up_
"""

def start(update, context):
    msg = f"""
eLloW guiSzx\! *I am Brei\.* \(\/about\)

You can control me using these commands\:
"""
    context.bot.send_message(chat_id = update.message.chat_id,
        text = msg + command_fun + command_react,
        parse_mode = ParseMode.MARKDOWN_V2
    )

def fun(update, context):
    try:
        command = context.args[0].lower()

        if command == "8ball":
            if len(context.args) == 1:
                msg = "That's invalid. Ask a yes or no question after 8ball. Example: /fun 8ball Am I cute?"
                update.message.reply_text(msg)
            else:
                answers = [
                    "It is certain.",
                    "Reply hazy, try again.",
                    "Don’t count on it.",
                    "It is decidedly so.",
                    "Ask again later.",
                    "My reply is no.",
                    "Without a doubt.",
                    "Better not tell you now.",
                    "My sources say no.",
                    "Yes – definitely.",
                    "Cannot predict now.",
                    "Outlook not so good.",
                    "You may rely on it.",
                    "Concentrate and ask again.",
                    "Very doubtful.",
                    "As I see it, yes.",
                    "Most likely.",
                    "Outlook good.",
                    "Yes.",
                    "Signs point to yes."
                ]
                msg = "Shaking the 8ball 🎱..."
                edit = update.message.reply_text(msg)
                time.sleep(2)
                context.bot.editMessageText(
                    chat_id = update.message.chat_id,
                    message_id = edit.message_id,
                    text = random.choice(answers)
                )

        elif command == "jeje":
            sentence = context.args[1:]

            words = sentence

            words_dict={
                ':)': 'xD',
        		'💔': '</3',
        		'❤️': '<3',
        		'for': '4',
        		'the': 'D',
        		'be': 'B',
        		'with': 'w/',
        		'haha': 'jejeje',
        		'hahaha': 'lolz',
        		'love': 'luv',
        		'ko': 'quo',
        		'tayo': 'tau',
        		'guys': 'guisz',
        		'you': 'u',
        		'are': 'r',
                'evening': 'PM',
                'good': 'gud'
        	}

            output = ""

            for word in words:
                output += words_dict.get(word, word) + " "

            sentence = output

            letters = [char for char in sentence]

            letters_dict = {
                '.': [',.', "''", '~ ', '..', 'xD..', 'JEjeje!', ',..', 'poh..', '~~ ', 'xD.,', 'Jeje~', 'Jejeje!!', '..,,', '~~', '..!!'],
        		',': [',,', ",'", ','],
        		'?': ["??'", '????', '.??'],
        		'a': ['4', 'A', 'uH', 'a', '', '@', 'ah', 'â', 'ä', 'a', 'à', 'å'],
        		'b': ['b', 'B', 'b'],
        		'd': ['d', 'D', 'd'],
        		'e': ['e', 'é', 'E', 'é', 'e', '3', 'e'],
        		'g': ['g', '9', '6', 'g', 'G'],
        		'i': ['!', 'I', '1', 'i', '!', 'I', '1', 'i'],
        		'k': ['k', 'K', 'k'],
        		'l': ['l', 'L', 'l', '7'],
        		'm': ['m', 'M', 'm'],
        		'n': ['n', 'N', 'n'],
        		'o': ['0', 'Owz', '0', 'oe', '0w', '0eH', '0', '0h'],
        		'p': ['p', 'P','p'],
        		's': ['x', 'S', 'z', 's', 'z', '$', 'X'],
        		't': ['t', '+', 'T', 't'],
        		'u': ['u', 'U', 'u', 'ü'],
        		'x': ['x', 'X', 'x'],
        		'y': ['y', 'Y', 'y'],
        	}

            output = ""
            for letter in letters:
                output += random.choice(letters_dict.get(letter, letter))

            update.message.reply_text(output)

        elif command == "dice":
            msg = "You throw the dice 🎲 and roll a..."
            edit = update.message.reply_text(msg)
            time.sleep(1)
            context.bot.editMessageText(
                chat_id = update.message.chat_id,
                message_id = edit.message_id,
                text = f"You throw the dice 🎲 and roll a {str(random.randint(1, 17))}."
            )
        elif command == "coin":
            msg = "You flip the coin 🪙 and lands on..."
            edit = update.message.reply_text(msg)
            time.sleep(1)
            context.bot.editMessageText(
                chat_id = update.message.chat_id,
                message_id = edit.message_id,
                text = "You flip the coin 🪙 and lands on {}.".format(random.choice(["heads", "tails", "heads", "tails"]))
            )
        elif command == "fortunecookie":
            fortunecookie_gifs = [
                "https://media.giphy.com/media/fnEcPcY9KaSLBu2VEB/giphy.gif",
                "https://media.giphy.com/media/mJRtyFJp5JNbayiSH4/giphy.gif",
                "https://media.giphy.com/media/1lvvtpIbLtlQyx9g4v/giphy.gif",
                "https://media.giphy.com/media/l2Je0Ponz50mddbfa/giphy.gif",
                "https://media.giphy.com/media/3o7btMQWOgjbJrTqBa/giphy.gif",
                "https://media.giphy.com/media/3ohjV9zxmkMnaTD1lK/giphy.gif",
                "https://media.giphy.com/media/3ohjV5ARy0xROYT6i4/giphy.gif",
                "https://66.media.tumblr.com/a2391d625b9a44459e96b022fc0a6ccd/tumblr_piqxjjxjXN1t7i4f6o6_400.gif",
            ]

            fortunecookie_sayings = [
                "Do not be afraid of competition.",
                "An exciting opportunity lies ahead of you.",
                "You love peace.",
                "Get your mind set…confidence will lead you on.",
                "You will always be surrounded by true friends.",
                "Sell your ideas-they have exceptional merit.",
                "You should be able to undertake and complete anything.",
                "You are kind and friendly.",
                "You are wise beyond your years.",
                "Your ability to juggle many tasks will take you far.",
                "A routine task will turn into an enchanting adventure.",
                "Beware of all enterprises that require new clothes.",
                "Be true to your work, your word, and your friend.",
                "Goodness is the only investment that never fails.",
                "A journey of a thousand miles begins with a single step.",
                "Forget injuries; never forget kindnesses.",
                "Respect yourself and others will respect you.",
                "A man cannot be comfortable without his own approval.",
                "Always do right. This will gratify some people and astonish the rest.",
                "It is easier to stay out than to get out.",
                "Sing everyday and chase the mean blues away.",
                "You will receive money from an unexpected source.",
                "Attitude is a little thing that makes a big difference.",
                "Plan for many pleasures ahead.",
                "Experience is the best teacher.",
                "You will be happy with your spouse.",
                "Expect the unexpected.",
                "Stay healthy. Walk a mile.",
                "The family that plays together stays together.",
                "Eat chocolate to have a sweeter life.",
                "Once you make a decision the universe conspires to make it happen.",
                "Make yourself necessary to someone.",
                "The only way to have a friend is to be one.",
                "Nothing great was ever achieved without enthusiasm.",
                "Dance as if no one is watching.",
                "Live this day as if it were your last.",
                "Your life will be happy and peaceful.",
                "Reach for joy and all else will follow.",
                "Move in the direction of your dreams.",
                "Bloom where you are planted.",
                "Appreciate. Appreciate. Appreciate.",
                "Happy News is on its way.",
                "A closed mouth gathers no feet.",
                "He who throws dirt is losing ground.",
                "Borrow money from a pessimist. They don't expect it back.",
                "Life is what happens to you while you are busy making other plans.",
                "Help! I'm being held prisoner in a fortune cookie factory.",
                "Paradise is always where love dwells.",
                "The one you love is closer than you think.",
                "Love is like wildflowers… it is often found in the most unlikely places.",
                "In dreams and in love there are no impossibilities.",
                "Love isn't something you find. Love is something that finds you.",
                "True love is not something that comes everyday, follow your heart, it knows the right answer.",
            ]

            edit = context.bot.send_animation(chat_id = update.message.chat_id,
                animation = random.choice(fortunecookie_gifs),
                caption = "You cracked the fortune cookie 🥠 and it says..."
            )
            time.sleep(1)
            context.bot.editMessageCaption(chat_id = update.message.chat_id,
                message_id = edit.message_id,
                caption = "You cracked the fortune cookie 🥠 and it says, \"{}\"".format(random.choice(fortunecookie_sayings)),
            )

        elif command == "sing":
            songs = [
                "songs/Brei - Having You Near Me.ogg",
                "songs/Brei - When I Met You.ogg",
                "songs/Brei - With a Smile.ogg"
            ]
            context.bot.send_voice(chat_id = update.message.chat_id, voice = open(random.choice(songs), 'rb'))

        else:
            msg = f'"{command}" is an invalid command. Type /fun to see the command list.'
            update.message.reply_text(msg)
    except IndexError:
        context.bot.send_message(chat_id = update.message.chat_id,
            text = command_fun,
            parse_mode = ParseMode.MARKDOWN_V2
        )

def react(update, context):
    try:
        command = context.args[0].lower()

        if command == "hug":
            hug_list = [
                "https://media.giphy.com/media/3bqtLDeiDtwhq/giphy.gif",
                "https://media.giphy.com/media/DjczAlIcyK1Co/giphy.gif",
                "https://media.giphy.com/media/wSY4wcrHnB0CA/giphy.gif",
                "https://media.giphy.com/media/PHZ7v9tfQu0o0/giphy.gif",
                "https://media.giphy.com/media/yziFo5qYAOgY8/giphy.gif",
                "https://media.giphy.com/media/45Lg3ECIw25Fe/giphy.gif",
                "https://media.giphy.com/media/rSNAVVANV5XhK/giphy.gif",
            ]
            user = context.args[1]
            context.bot.send_animation(chat_id = update.message.chat_id,
                caption = f"*hugs {user}*",
                animation = random.choice(hug_list),
            )

        elif command == "slap":
            slap_list = [
                "https://media.giphy.com/media/Gf3AUz3eBNbTW/giphy.gif",
                "https://media.giphy.com/media/10DRaO76k9sgHC/giphy.gif",
                "https://media.giphy.com/media/ewHSMEx2TtEo8/giphy.gif",
                "https://media.giphy.com/media/uqSU9IEYEKAbS/giphy.gif",
                "https://media.giphy.com/media/uG3lKkAuh53wc/giphy.gif",
                "https://media.giphy.com/media/mJWDiMyXuWG8U/giphy.gif",
                "https://media.giphy.com/media/LD8TdEcyuJxu0/giphy.gif",
                "https://media.giphy.com/media/xUNd9HZq1itMkiK652/giphy.gif",
            ]
            user = context.args[1]
            context.bot.send_animation(chat_id = update.message.chat_id,
                caption = f"*slaps {user}*",
                animation = random.choice(slap_list),
            )

        elif command == "cheerup":
            cheer_up_list = [
                "https://media.giphy.com/media/m8Z2UqDYU20SY/giphy.gif",
                "https://media.giphy.com/media/tI880EKd2rxq8/giphy.gif",
                "https://media.giphy.com/media/9o9MxN7wtaIK4GawF9/giphy.gif",
                "https://media.giphy.com/media/1YdcfRvXYXkfIbQtbM/giphy.gif",
                "https://media.giphy.com/media/xuXzcHMkuwvf2/giphy.gif"
            ]
            user = context.args[1]
            context.bot.send_animation(chat_id = update.message.chat_id,
                caption = f"Cheer up, {user}.",
                animation = random.choice(cheer_up_list),
            )

        elif command == "kiss":
            kiss_list = [
                "https://media.giphy.com/media/bGm9FuBCGg4SY/giphy.gif",
                "https://media.giphy.com/media/l0ErGjnSKbCcNVoZi/giphy.gif",
                "https://media.giphy.com/media/AIDv87fiokBva/giphy.gif",
                "https://media.giphy.com/media/uSHX6qYv1M7pC/giphy.gif",
                "https://media.giphy.com/media/YO5Wks9N6xSPq2UHPl/giphy.gif"
            ]
            user = context.args[1]
            context.bot.send_animation(chat_id = update.message.chat_id,
                caption = f"kisses {user}",
                animation = random.choice(kiss_list),
            )

        elif command == "cry":
            cry_list = [
                "https://media.giphy.com/media/ROF8OQvDmxytW/giphy.gif",
                "https://media.giphy.com/media/8YutMatqkTfSE/giphy.gif",
                "https://media.giphy.com/media/4NuAILyDbmD16/giphy.gif",
                "https://media.giphy.com/media/1lpEsTFMRiGfS/giphy.gif",
                "https://media.giphy.com/media/11TN3gkseh4Vos/giphy.gif",
            ]
            context.bot.send_animation(chat_id = update.message.chat_id,
                animation = random.choice(cry_list),
            )

        elif command == "cringe":
            cringe_list = [
                "https://media.giphy.com/media/2nnD2zpuOsxSE/giphy.gif",
                "https://media.giphy.com/media/RJAjTowsU0K1a/giphy.gif",
                "https://media.giphy.com/media/j4Yzy0PwXSnok/giphy.gif",
                "https://media.giphy.com/media/nmKBaZgcH8h20sQQI2/giphy.gif",
                "https://media.giphy.com/media/YJgITXsrogeM8/giphy.gif",
                "https://media.giphy.com/media/3ohzdTG3cg9eIjBdy8/giphy.gif",
            ]
            context.bot.send_animation(chat_id = update.message.chat_id,
                animation = random.choice(cringe_list),
            )

        elif command == "happy":
            happy_list = [
                "https://media.giphy.com/media/1xVfHenZgbysbdumIP/giphy.gif",
                "https://media.giphy.com/media/anDhBXwgvIa7m/giphy.gif",
                "https://media.giphy.com/media/QzxONYL3xbj6E/giphy.gif",
                "https://media.giphy.com/media/ree8xCap5nHi/giphy.gif",
                "https://media.giphy.com/media/JWGgsu82QDoEE/giphy.gif",
            ]
            context.bot.send_animation(chat_id = update.message.chat_id,
                animation = random.choice(happy_list),
            )

        elif command == "dance":
            dance_list = [
                "https://media.giphy.com/media/mJIa7rg9VPEhzU1dyQ/giphy.gif",
                "https://media.giphy.com/media/6k6iDdi5NN8ZO/giphy.gif",
                "https://media.giphy.com/media/RLJxQtX8Hs7XytaoyX/giphy.gif",
                "https://media.giphy.com/media/vTqhQldEfAY6c/giphy.gif",
                "https://media.giphy.com/media/zgSWpnMeK7dCM/giphy.gif",
            ]
            context.bot.send_animation(chat_id = update.message.chat_id,
                animation = random.choice(dance_list),
            )

        else:
            msg = f'"{command}" is an invalid command. Type /react to see the command list.'
            update.message.reply_text(msg)

    except IndexError:
        context.bot.send_message(chat_id = update.message.chat_id,
            text = command_react,
            parse_mode = ParseMode.MARKDOWN_V2
        )

def about(update, context):
    msg = """
Brei is based on an MNL48 member, Brei \(https\:\/\/instagram\.com\/brei\.mnl48official\)\.
I created this bot to improve my coding and I am planning this to
be a multi purpose bot\.
"""
    context.bot.send_message(chat_id = update.message.chat_id,
        text = msg,
        parse_mode = ParseMode.MARKDOWN_V2
    )

def start_bot():
    global updater
    updater = Updater(TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('fun', fun))
    dispatcher.add_handler(CommandHandler('react', react))
    dispatcher.add_handler(CommandHandler('about', about))

    updater.start_webhook(listen="0.0.0.0", port=PORT, url_path=TOKEN)
    updater.bot.set_webhook("https://brei.herokuapp.com/" + TOKEN)

    #updater.start_polling()
    updater.idle()

start_bot()
