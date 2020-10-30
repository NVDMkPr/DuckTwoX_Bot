from time import sleep,localtime,struct_time
from datetime import datetime
from json import loads,dumps
from sqlite3 import connect
from os import system
from re import findall
from requests import *
from telegram import (
    InlineKeyboardMarkup as IKM,
    InlineKeyboardButton as IKB,
    Bot,Chat,
    Update)
from telegram.ext import (
    Updater,CommandHandler,CallbackQueryHandler)
from payeer_api import PayeerAPI

bot = Updater("1324303472:AAGC1wjHcMzlhRzTGqjoL7D0ybYkani2_oI",use_context=True)
Bot = Bot("1324303472:AAGC1wjHcMzlhRzTGqjoL7D0ybYkani2_oI")
disp= bot.dispatcher
channel = "t.me/DuckTwoXChannel"
chan_id = "@DuckTwoXChannel"
PA = PayeerAPI("P1031638149",1191393731,"None")
TransactionID = None
a = localtime()
b = datetime(a[0],a[1],a[2],a[3],a[4],a[5])

def Start(update,context):
    bot     = context.bot
    chat_id = update.effective_chat.id
    text    = '''<b><i>Deposit Now And Receive 120% Profits In 20 Days</i>\n<u>Minium 10$ Maximum 500$</u>
🔥 <i>Bonus Up To 140% Profits From Now To <u>15/11/2020</u></i></b>'''
    reply_markup = IKM([[IKB("Account",None,1),IKB("Support",None,2)],[IKB("Stat",None,3)]])
    bot.send_message(chat_id,text,"HTML",True,True,None,reply_markup)
def Account(bot,chat_id):
    text    = '''👤 <b>Account Balance:
    💵 Withdrawable Balance: {function}$
    💎 Active Investment: {function}$
    🚧 Pending Withdraw: {function}$
    ✔️ Total Withdrawn: {function}$</b>'''
    reply_markup = IKM([[IKB("Invest",None,11),IKB("Auto Withdraw",None,12)],[IKB("Back",None,0)]])
    bot.send_message(chat_id,text,"HTML",True,True,None,reply_markup)
def Support(bot,chat_id):
    text    = '''<b>Send Message To Admin For Support!</b>'''
    reply_markup = IKM([[IKB("Telegram Admin","t.me/nvdmkpr")],[IKB("Back",None,0)]])
    bot.send_message(chat_id,text,"HTML",True,False,None,reply_markup)
def Stat(bot,chat_id):
    text    = '''<b>Bot Statistics
    👥 Total User: {function}
    ➕ Total Investments: {function}$
    ➖ Total Withdrawals: {function}$
    ⬆️ Total Profit To Admin From All Investor: {function}$</b>
    <u>Version: {function}</u>'''
    reply_markup = IKM([[IKB("Back",None,0)]])
    bot.send_message(chat_id,text,"HTML",True,True,None,reply_markup)
def Deposit(bot,chat_id):
    text = '''<b>Choose One Currency Type Available For Deposit<i>
❗ Auto Withdraw Will Send Your Profit To Deposit Address|Account!</i>
Payeer: <code>P1031638149</code>
BTC: <code>1LxudDaPdWjdp8RW7xyNpjdWL4J1AZZdQe</code>
ETH: <code>0x94f29C62DaDea7fB6a34E65C4446fE54E94151CF</code>
LTC: <code>LY6iiqXWv1njZFtay5BKjgeMVJsyvpCLC4</code></b>'''
    reply_markup = IKM([[IKB("Back",None,1)]])
    bot.send_message(chat_id,text,"HTML",True,False,None,reply_markup)
    
def CallbackHandler(update,context):
    query   = update.callback_query
    chat_id = update.effective_chat.id
    msg_id  = update.effective_message.message_id
    msg_txt = update.effective_message.text
    user_id = update.effective_user.id
    bot     = context.bot
    data    = int(query.data)
    query.answer()
    if data == 0    : Start(update,context)
    if data == 1    : Account(bot,chat_id)
    if data == 2    : Support(bot,chat_id)
    if data == 3    : Stat(bot,chat_id)
    if data == 11   : Deposit(bot,chat_id)
    if data == 12   : Withdraw(bot,chat_id)
    

disp.add_handler(CallbackQueryHandler(CallbackHandler))
disp.add_handler(CommandHandler("start",Start))
bot.start_polling(clean=True)
while False:
    history = PA.history("count=1000&type=incoming&from=2020/08/14 00:00:00&to=2020/10/30 23:59:59")
    toStr = dumps(history)
    print(history)
    i = 0
    if len(toStr) > 2:
        pattern = "[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"
        id_ = findall(pattern,toStr)[0]
        data = history[id_]
        date = data["date"]
        transid = data["id"]
        sender = data["from"]
        amount = data["creditedAmount"]
        curr = data["creditedCurrency"]
        fee = data["payeerFee"]
        text = f'''🔼🔼🔼 New Deposit 🔼🔼🔼

🕛 Date: {date}
🆔 Transaction ID: <code>{transid}</code>
❤️ Sender: <code>{sender}</code>
💲 Amount: {amount} {curr}
➖ Payeer Fee: {fee}{curr}'''
        #Bot.send_message(chan_id,text,"HTML")
def requests(**kwargs):
    data = {'account':'P1031638149','apiId':1191393731,'apiPass':'None'}
    if kwargs:
        try:
            if kwargs['from_']:
                kwargs['from'] = kwargs['from_']
                kwargs.pop('from_')
        except: pass
        data.update(kwargs)
    url = "https://payeer.com/ajax/api/api.php"
    resp = post(url,data).json()
    errors = resp.get('errors')
    if errors:
        raise TypeError(errors)
    else:
        return resp
print(requests(action='history',append=1191436161))