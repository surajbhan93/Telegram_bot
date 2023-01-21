import telegram.ext


Token="5500005070:AAEpKd3F6_unKgbWs8_LVkNW79NMZjiWMGI"
updater=telegram.ext.updater("5500005070:AAEpKd3F6_unKgbWs8_LVkNW79NMZjiWMGI",use_context=True)
dispatcher=updater.dispatcher

def start(update,context):
    update.message.reply_text("Hello users ! Welcome to Coder$Tech")

def help(update,context):
    update.message.reply_text(
        """/start->Welcome to the channel
           /help->This particular message
           /content->About Various playlists of Simplilearn
           /python->The first video from python playlist
           /SQL->The first video from SQL Playlist
           /Java->The first video from Java playlist
           /content->content information"""

    )
def content(update,context):
    update.message.reply_text("We have various playlist and articles available")

def python(update,context):
    update.message.reply_text("tutorial link : https://youtu.be/aqvDTCpNRek")

def SQL(update,context):
    update.message.reply_text("tutorial link : https://youtu.be/pVKT4N-Cgb8")

def Java(update,context):
    update.message.reply_text("tutorial link : https://youtu.be/1kkvalOcSog")

def contect(update,context):
    update.message.reply_text("you can contact on the ragistred mail id proided on the website")    


dispatcher.add_handler(telegram.ext.commandHandler('start',start))

dispatcher.add_handler(telegram.ext.commandHandler('python',python))
dispatcher.add_handler(telegram.ext.commandHandler('SQL',SQL))
dispatcher.add_handler(telegram.ext.commandHandler('java',java))
dispatcher.add_handler(telegram.ext.commandHandler('contect',contect))
dispatcher.add_handler(telegram.ext.commandHandler('help',help))

updater.start_polling()
updater.idle()



