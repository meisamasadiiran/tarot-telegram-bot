import telebot
import random
import os
import time
from telebot import types

# توکن ربات از environment variable
BOT_TOKEN = os.getenv('BOT_TOKEN', 'YOUR_BOT_TOKEN_HERE')

bot = telebot.TeleBot(BOT_TOKEN)

# کارت های تاروت کامل
tarot_cards = {
    "احمق (The Fool)": "🌱 شروع جدید، ماجراجویی، بی‌پروایی مثبت، آزادی از ترس. وقت ریسک کردن و قدم گذاشتن به مسیر جدیده!",
    "جادوگر (The Magician)": "✨ قدرت اراده، خلاقیت، مهارت، توانایی تحقق آرزوها. همه ابزارها در دستان شماست!",
    "کاهنه عالی (High Priestess)": "🔮 شهود، حکمت درونی، اسرار، قدرت زنانه. به صدای دل خودتون گوش بدید.",
    "امپراتورس (The Empress)": "🌸 مادری، حاصلخیزی، طبیعت، عشق بی‌قید و شرط. زمان رشد و شکوفایی است.",
    "امپراتور (The Emperor)": "👑 اقتدار، رهبری، نظم، پدر سالار. زمان تصمیم‌گیری قاطع و رهبری است.",
    "کشیش (The Hierophant)": "📿 سنت، آموزش، راهنمایی معنوی، دانش مذهبی. از تجربه دیگران یاد بگیرید.",
    "عاشقان (The Lovers)": "💕 عشق، انتخاب، رابطه، هماهنگی. تصمیم مهمی پیش روی شماست.",
    "ارابه (The Chariot)": "🏆 پیروزی، اراده قوی، کنترل، حرکت به جلو. با عزم قوی به هدف برسید.",
    "قدرت (Strength)": "🦁 شجاعت درونی، کنترل خویشتن، صبر، قدرت ملایم. قدرت واقعی از درون می‌آید.",
    "درونگرا (The Hermit)": "🕯️ جستجوی درونی، خلوت، حکمت، راهنمایی. زمان تفکر و خودشناسی است.",
    "چرخ بخت (Wheel of Fortune)": "🎡 تغییر، شانس، سرنوشت، چرخه زندگی. تغییرات مثبت در راه است!",
    "عدالت (Justice)": "⚖️ توازن، انصاف، قانون، عواقب اعمال. عدالت برقرار خواهد شد.",
    "آویخته (The Hanged Man)": "🙃 قربانی، نگاه متفاوت، صبر، رهایی. گاهی باید منتظر بمانید.",
    "مرگ (Death)": "🦋 تحول، پایان و شروع، تغییر بنیادی، تولد دوباره. پایان چیزی، شروع چیز بهتری است.",
    "اعتدال (Temperance)": "🌈 تعادل، میانه‌روی، آرامش، هماهنگی. همه چیز به تعادل نیاز دارد.",
    "شیطان (The Devil)": "⛓️ وابستگی، محدودیت، وسوسه، مادی‌گرایی. زنجیرهای خود را بشکنید.",
    "برج (The Tower)": "⚡ تغییر ناگهانی، ویرانی، آشفتگی، بیداری. تکان بزرگی در راه است.",
    "ستاره (The Star)": "⭐ امید، الهام، آرزو، شفا. امید را از دست ندهید، همه چیز بهتر می‌شود.",
    "ماه (The Moon)": "🌙 توهم، ترس، ناآگاهی، رؤیا. مراقب فریب و توهمات باشید.",
    "خورشید (The Sun)": "☀️ شادی، موفقیت، حیاتی، مثبت اندیشی. روزهای روشن در پیش است!",
    "قضاوت (Judgement)": "📯 رستگاری، بخشش، بیداری، شروع دوباره. زمان ارزیابی و تغییر فرا رسیده.",
    "جهان (The World)": "🌍 تکمیل، موفقیت، تحقق هدف، کمال. به هدف نهایی رسیده‌اید!"
}

# پیام‌های انگیزشی
motivational_messages = [
    "✨ یادت باشه که هر پایانی، شروع جدیدی هست",
    "🌟 قدرت تغییر زندگیت توی دستان خودته",
    "💫 به شهودت اعتماد کن، راه درست رو نشونت میده",
    "🌙 گاهی باید صبر کنی تا زمان مناسب فرا برسه",
    "☀️ هر چالشی فرصتی برای رشد و یادگیری است",
    "🦋 تغییر بخش طبیعی زندگی است، از آن نترسید",
    "🎯 روی هدف‌هاتون متمرکز بمونید، موفقیت نزدیکه",
    "💪 قدرت درونی شما بیشتر از اون چیزی هست که فکر می‌کنید"
]

@bot.message_handler(commands=['start'])
def send_welcome(message):
    welcome_text = f"""
🔮 سلام {message.from_user.first_name}! 
به ربات فال تاروت خوش اومدی! 

✨ برای گرفتن فال تک نیت تاروت:
/tarot - دریافت فال

📚 سایر دستورات:
/help - راهنمای کامل
/about - درباره تاروت

🌟 سوالت رو با تمرکز و قلب باز بپرس تا بهترین راهنمایی رو دریافت کنی
    """
    
    # ایجاد کیبورد
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔮 فال تاروت")
    btn2 = types.KeyboardButton("❓ راهنما")
    btn3 = types.KeyboardButton("📖 درباره تاروت")
    markup.add(btn1)
    markup.add(btn2, btn3)
    
    bot.reply_to(message, welcome_text, reply_markup=markup)

@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
📚 راهنمای کامل ربات فال تاروت:

🔮 دستورات اصلی:
• /tarot - دریافت فال تک نیت
• /help - نمایش این راهنما  
• /about - اطلاعات درباره تاروت

🎯 نحوه استفاده:
1️⃣ سوال خود را در ذهن مشخص کنید
2️⃣ با تمرکز دستور /tarot را بزنید
3️⃣ کارت تاروت و تفسیر آن را دریافت کنید
4️⃣ می‌تونید فال جدید بگیرید

💡 نکات مهم:
✅ سوالات مشخص بهترین جواب رو میدن
✅ با ذهن باز و قلب آماده فال بگیرید  
✅ از راهنمایی‌ها در زندگی استفاده کنید
⚠️ فال‌ها راهنمایی هستند، نه تعیین‌کننده سرنوشت
    """
    bot.reply_to(message, help_text)

@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
📖 درباره تاروت:

🔮 تاروت چیست؟
تاروت مجموعه‌ای از 78 کارت است که برای درک بهتر خود و راهنمایی در تصمیم‌گیری‌ها استفاده می‌شود.

🎴 آرکانا اصلی (Major Arcana):
22 کارت اصلی که نشان‌دهنده مراحل اصلی سفر روحی انسان است.

✨ هدف:
• خودشناسی بیشتر
• راهنمایی در تصمیم‌گیری‌ها  
• درک بهتر موقعیت‌های زندگی
• تقویت شهود و بصیرت درونی

🌟 یادآوری:
این ربات برای راهنمایی و تفکر ساخته شده. تصمیمات مهم را با فکر و مشورت بگیرید.
    """
    bot.reply_to(message, about_text)

@bot.message_handler(commands=['tarot'])
def tarot_reading(message):
    get_tarot_reading(message)

def get_tarot_reading(message):
    # انتخاب تصادفی کارت
    card_name = random.choice(list(tarot_cards.keys()))
    card_meaning = tarot_cards[card_name]
    motivational_msg = random.choice(motivational_messages)
    
    # ساخت پیام فال
    reading_text = f"""
🔮 **فال تک نیت شما:**

🎴 **کارت:** {card_name}

📖 **راهنمایی:** 
{card_meaning}

💫 **پیام امروز:**
{motivational_msg}

━━━━━━━━━━━━━━━━━━━━
⚡ این فال راهنمایی کلی است. تصمیمات مهم را با تفکر و مشورت بگیرید.
    """
    
    # ایجاد کیبورد inline
    markup = types.InlineKeyboardMarkup()
    new_reading_btn = types.InlineKeyboardButton("🔄 فال جدید", callback_data="new_tarot")
    share_btn = types.InlineKeyboardButton("📤 اشتراک‌گذاری", callback_data="share")
    markup.add(new_reading_btn)
    markup.add(share_btn)
    
    bot.reply_to(message, reading_text, parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "new_tarot")
def new_tarot_reading(call):
    # انتخاب کارت جدید
    card_name = random.choice(list(tarot_cards.keys()))
    card_meaning = tarot_cards[card_name]
    motivational_msg = random.choice(motivational_messages)
    
    reading_text = f"""
🔮 **فال جدید شما:**

🎴 **کارت:** {card_name}

📖 **راهنمایی:** 
{card_meaning}

💫 **پیام امروز:**
{motivational_msg}

━━━━━━━━━━━━━━━━━━━━
⚡ این فال راهنمایی کلی است. تصمیمات مهم را با تفکر و مشورت بگیرید.
    """
    
    markup = types.InlineKeyboardMarkup()
    new_reading_btn = types.InlineKeyboardButton("🔄 فال جدید", callback_data="new_tarot")
    share_btn = types.InlineKeyboardButton("📤 اشتراک‌گذاری", callback_data="share")
    markup.add(new_reading_btn)
    markup.add(share_btn)
    
    try:
        bot.edit_message_text(reading_text, call.message.chat.id, call.message.message_id, 
                             parse_mode='Markdown', reply_markup=markup)
    except:
        bot.send_message(call.message.chat.id, reading_text, parse_mode='Markdown', reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data == "share")
def share_reading(call):
    share_text = "🔮 فال تاروت گرفتم! شما هم امتحان کنید: @YourBotUsername"
    bot.answer_callback_query(call.id, "برای اشتراک‌گذاری، پیام بالا رو فوروارد کنید! 📤")

# پاسخ به پیام‌های متنی
@bot.message_handler(func=lambda message: message.text == "🔮 فال تاروت")
def handle_tarot_button(message):
    get_tarot_reading(message)

@bot.message_handler(func=lambda message: message.text == "❓ راهنما")
def handle_help_button(message):
    send_help(message)

@bot.message_handler(func=lambda message: message.text == "📖 درباره تاروت")
def handle_about_button(message):
    send_about(message)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # پاسخ به پیام‌های عادی
    responses = [
        "🔮 برای دریافت فال تاروت، دکمه 'فال تاروت' رو بزن یا /tarot تایپ کن!",
        "✨ آماده‌ای برای کشف پیام‌های جهان؟ فال تاروت بگیر! 🎴",
        "🌟 کارت‌های تاروت منتظر هستن تا راهنمایی‌ت کنن! 🔮",
        "💫 سوالت رو در ذهن مشخص کن و فال تاروت بگیر! ✨"
    ]
    
    bot.reply_to(message, random.choice(responses))

# اجرای ربات با مدیریت خطا
def main():
    print("🔮 ربات فال تاروت شروع شد...")
    while True:
        try:
            bot.polling(none_stop=True, interval=1, timeout=60)
        except Exception as e:
            print(f"خطا رخ داد: {e}")
            print("تلاش مجدد در 15 ثانیه...")
            time.sleep(15)

if __name__ == "__main__":
    main()
