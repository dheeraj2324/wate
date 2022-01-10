from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ( CommandHandler, Filters, MessageHandler, Updater)
from message import Editmessage, Sendmessage, logger
from Checks.Altbalaji import altbalaji_helper
from Checks.hoichoi import hoichoi_helper
from Checks.voot import Voot_helper
from Checks.aha import aha_helper
from Checks.zee5 import zee_helper
from Checks.sun import Sun_helper
from Miscellaneous.Scraper import pastebin, text_scraper, throwbin, ghostbin
import os


bot_token = os.environ.get('TG_BOT_TOKEN')
startmessage = [[
		InlineKeyboardButton(
			"𝓐𝓫𝓸𝓾𝓽 𝓜𝓮",
			url='https://t.me/aboutdheeraj'
		),
        InlineKeyboardButton(
			"𝕯𝖊𝖛",
			url='https://t.me/dheeraj2324'
		)
        ]]


def start(update, context):
    info = update.effective_user
    print(info)
    chat_id = info.id
    userid= info['username']
    text = f'Ｗｅｌｃｏｍｅ @{userid}, Ｔｏ Ａｃｃｏｕｎｔ Ｃｈｅｃｋ Ｂｏｔ, ｔｏ ｋｎｏｗ ｍｏｒｅ ｕｓｅ /help . 𝕋𝕙𝕚𝕤 𝕓𝕠𝕥 𝕚𝕤 𝕡𝕣𝕠𝕧𝕚𝕕𝕖𝕕 𝕗𝕠𝕣 𝕖𝕕𝕦𝕔𝕒𝕥𝕚𝕠𝕟𝕒𝕝 𝕦𝕤𝕖 𝕠𝕟𝕝𝕪, 𝕒𝕟𝕪 𝕞𝕚𝕤𝕦𝕤𝕖 𝕥𝕙𝕖𝕟 𝕪𝕠𝕦 𝕤𝕙𝕠𝕦𝕝𝕕 𝕓𝕖 𝕣𝕖𝕤𝕡𝕠𝕟𝕤𝕚𝕓𝕝𝕖'
    Sendmessage(chat_id, text, reply_markup=InlineKeyboardMarkup(startmessage))
    return

    
def combos_spilt(combos):
    split = combos.split('\n')
    return split


def help(update, context):
    chat_id = update.message.chat_id
    text = "<b>Available Sites:\n!alt~space~combo* - to check Ａｌｔｂａｌａｊｉ accounts\n!hoi~space~combo* - to check Ｈｏｉｃｈｏｉ accounts\n!aha~space~combo* - to check Ａｈａ accounts\n!sun~space~combo* - to check ＳｕｎＮｘｔ accounts\n!voot~space~combo* - to check Ｖｏｏｔ accounts\n!zee5~space~combo* - to check Ｚｅｅ５ accounts\n\nMiscellaneous:-\n!pst~space~title|text - to paste text on Throwbin.io and get paste link</b>(If you don't want to give title then skip it just send the text)\n\n*combo means Email:password combination,':' is important."
    Sendmessage(chat_id, text, reply_markup= InlineKeyboardMarkup(startmessage))

def duty(update, context):
    chat_id = update.message.chat_id
    text =  update.message.text.split(' ', 1)
    if text[0] == '!alt':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                altbalaji_helper(chat_id, i)
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            altbalaji_helper(chat_id, text[1])
    elif text[0] == '!voot':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                Voot_helper(chat_id, i)
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            Voot_helper(chat_id, text[1])
    elif text[0] == '!hoi':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                hoichoi_helper(chat_id, i)
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            hoichoi_helper(chat_id, text[1])
    elif text[0] == '!aha':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                aha_helper(chat_id, i)
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            aha_helper(chat_id, text[1])
    elif text[0] == '!zee5':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                zee_helper(chat_id, i)
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            zee_helper(chat_id, text[1])
    elif text[0] == '!sun':
        if '\n' in text[1]:
            simple = combos_spilt(text[1])
            for i in simple:
                Sun_helper(chat_id, i)
            Sendmessage(chat_id, 'Ｃｏｍｐｌｅｔｅｄ')
        else:
            Sun_helper(chat_id, text[1])
    elif text[0] == '!pst':
            try:
                throwbin(chat_id, text[1])
            except IndexError:
                Sendmessage(chat_id, "<i>Somethings wrong with your format!</i>")
    else:
        logger.info('Unknown Command')


def scraperdfnc(update, context):
    msg = update.message.text
    status_msg = update.message
    chat_id = status_msg.chat_id
    try:
        if 'pastebin' in msg:
            link = msg.split(' ')[1]
            pastebin(chat_id,link)
        elif 'ghostbin' in msg:
            link = msg.split(' ')[1]
            ghostbin(chat_id,link)
        else:
            scrape_text = status_msg['reply_to_message']['text']
            text_scraper(chat_id, scrape_text)
    except:
        Sendmessage(chat_id, 'Only Supports pastebin, please check if you send paste bin link')

def main():
    updater = Updater(
        bot_token,
        use_context=True
    )
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, duty))
    dp.add_handler(CommandHandler("scrape", scraperdfnc))
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    logger.info("Bot Started!!!")
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()
