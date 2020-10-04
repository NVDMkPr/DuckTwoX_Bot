def Color(color):
  Base = "\x1b[38;5;"
  return Base + color + "m"
Reset = "\x1b[0m"
print(Color("226"),end='',flush=True)
print("Importing Libraries . . .")
import sys,os,telegram
from telegram import InlineKeyboardMarkup as IKM
from telegram import InlineKeyboardButton as IKB
from telegram.ext import Updater,CommandHandler,CallbackQueryHandler

API = "1140798349:AAFK2Vxz8onm8Cq_A-MVfOiOZH2vV_9vedU"
Bot = Updater(API,use_context=True)
Dispatcher = Bot.dispatcher
print("Setting API . . .",Color("159"))
os.system('clear')

List = ["Deposit","Withdraw","Rules","Statistics","Bot Info","Mainmenu"]
ThankText = "Thank you for using my bot!\nAuthor: Samuel Lipoff\nTelegram: t.me/nvdmkpr"
StartMessage = "Welcome to Investment Bot!\nYou can gain profit in here and you don't need do everything, you just need to deposit and wait only!"
Start = IKM([
  [
    IKB(List[0],None,List[0]),
    IKB(List[1],None,List[1])],
  [
    IKB(List[2],None,List[2]),
    IKB(List[3],None,List[3]),
    IKB(List[4],None,List[4])]])
Mainmenu = IKM([
  [
    IKB(List[5],None,List[5])]
    ])

def Typing(update,context):
  id = update.effective_user.id
  action = telegram.ChatAction.TYPING
  context.bot.send_chat_action(id,action)
def Answer(update):
  return update.callback_query.answer()
def GetChatId(update):
  return update.effective_chat.id
def DelMsg(update,context):
  context.bot.delete_message(GetChatId(update),update.callback_query.message.message_id)
def EditMsg(msg,update,context,rm):
  query = update.callback_query
  chatid = update.effective_chat.id
  msg_id = query.message.message_id
  context.bot.edit_message_text(msg,chatid,msg_id)
  if rm != None:
    context.bot.edit_message_reply_markup(chatid,msg_id,reply_markup = rm)
def SendMsg(msg,update,context,rm):
  if rm != None:
    context.bot.send_message(GetChatId(update),msg,reply_markup=rm)
  else:
    context.bot.send_message(GetChatId(update),msg)

def start(update,context):
  Typing(update,context)
  SendMsg(StartMessage,update,context,Start)
def callbackhandler(update,context):
  callback_data = update.callback_query.data
  if callback_data == List[0]:
    Answer(update)
    Typing(update,context)
    EditMsg(ThankText,update,context,Mainmenu)
  elif callback_data == List[4]:
    Answer(update)
    Typing(update,context)
    EditMsg(ThankText,update,context,Mainmenu)
  elif callback_data == List[5]:
    Answer(update)
    Typing(update,context)
    EditMsg(StartMessage,update,context,Start)
  #context.bot.send_message(id,ThankText)
  #context.bot.edit_message_text("testing",chat_id=query.message.chat_id,message_id=query.message.message_id )

Dispatcher.add_handler(CommandHandler("start",start))
Dispatcher.add_handler(CallbackQueryHandler(callbackhandler))

Bot.start_polling(clean=True)