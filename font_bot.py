import json
import time
import urllib.request


# ==================================================
# تنظیمات ربات
# ==================================================

TOKEN = "CGACAE0KAWIWSHTBRSGNZHJGZZBQCPTZGFFEWGIPLJBLLDXNGJDUGVKWIOXOCXSI"

BASE_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"

offset_id = None


# ==================================================
# ارتباط با روبیکا
# ==================================================

def api(method, data=None):

    if data is None:
        data = {}

    url = f"{BASE_URL}/{method}"

    try:

        request = urllib.request.Request(
            url,
            data=json.dumps(
                data,
                ensure_ascii=False
            ).encode("utf-8"),
            headers={
                "Content-Type": "application/json"
            }
        )

        with urllib.request.urlopen(
            request,
            timeout=30
        ) as response:

            result = response.read().decode("utf-8")

            return json.loads(result)

    except Exception as e:

        print("❌ API ERROR:", e)

        return None


# ==================================================
# ارسال پیام
# ==================================================

def send_message(chat_id, text, reply_to=None):

    data = {
        "chat_id": chat_id,
        "text": text
    }

    if reply_to:
        data["reply_to_message_id"] = reply_to

    result = api(
        "sendMessage",
        data
    )

    if result:
        print("📤 پیام ارسال شد.")

    return result


# ==================================================
# حروف انگلیسی
# ==================================================

NORMAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


# ==================================================
# چند خانواده Unicode واقعی
# ==================================================

BOLD = "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"

ITALIC = "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"

BOLD_ITALIC = "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁"

SCRIPT = "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"

BOLD_SCRIPT = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"

FRAKTUR = "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"

DOUBLE = "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"

BOLD_FRAKTUR = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"

SANS = "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹"

SANS_BOLD = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"

SANS_ITALIC = "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"

SANS_BOLD_ITALIC = "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"

MONO = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"

MONO_BOLD = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"


# ==================================================
# تبدیل متن انگلیسی
# ==================================================

def unicode_font(text, alphabet):

    result = ""

    for char in text:

        upper = char.upper()

        if upper in NORMAL:

            index = NORMAL.index(upper)

            converted = alphabet[index]

            if char.islower():
                result += converted.lower()
            else:
                result += converted

        else:

            result += char

    return result


# ==================================================
# فونت‌های تزئینی
# ==================================================

def decorated_fonts(text):

    fonts = [

        f"『 {text} 』",
        f"【 {text} 】",
        f"〖 {text} 〗",
        f"〘 {text} 〙",
        f"〚 {text} 〛",
        f"《 {text} 》",
        f"〈 {text} 〉",
        f"「 {text} 」",
        f"『{text}』",
        f"【{text}】",

        f"꧁ {text} ꧂",
        f"꧁༺ {text} ༻꧂",
        f"༺ {text} ༻",
        f"༺༻ {text} ༺༻",
        f"𓆩 {text} 𓆪",
        f"𓆩♡{text}♡𓆪",
        f"𓆩 {text} 𓆪",
        f"✦ {text} ✦",
        f"✧ {text} ✧",
        f"★ {text} ★",

        f"☆ {text} ☆",
        f"☾ {text} ☽",
        f"☽ {text} ☾",
        f"♡ {text} ♡",
        f"♥ {text} ♥",
        f"♛ {text} ♛",
        f"♕ {text} ♕",
        f"⚡ {text} ⚡",
        f"🔥 {text} 🔥",
        f"💎 {text} 💎",
        f"👑 {text} 👑",

        f"• {text} •",
        f"● {text} ●",
        f"○ {text} ○",
        f"◉ {text} ◉",
        f"◆ {text} ◆",
        f"◇ {text} ◇",
        f"⬢ {text} ⬢",
        f"⟡ {text} ⟡",
        f"⟢ {text} ⟣",
        f"╰┈➤ {text}",

        f"➤ {text}",
        f"➳ {text}",
        f"➵ {text}",
        f"➸ {text}",
        f"❖ {text} ❖",
        f"✺ {text} ✺",
        f"✹ {text} ✹",
        f"✷ {text} ✷",
        f"✵ {text} ✵",
        f"✿ {text} ✿"

    ]

    return fonts


# ==================================================
# ساخت ۵۰ خروجی
# ==================================================

def make_fonts(text):

    results = []

    # ----------------------------------------------
    # فونت‌های واقعی Unicode
    # ----------------------------------------------

    unicode_fonts = [

        ("Bold", BOLD),
        ("Italic", ITALIC),
        ("Bold Italic", BOLD_ITALIC),
        ("Script", SCRIPT),
        ("Bold Script", BOLD_SCRIPT),
        ("Fraktur", FRAKTUR),
        ("Double", DOUBLE),
        ("Bold Fraktur", BOLD_FRAKTUR),
        ("Sans", SANS),
        ("Sans Bold", SANS_BOLD),
        ("Sans Italic", SANS_ITALIC),
        ("Sans Bold Italic", SANS_BOLD_ITALIC),
        ("Monospace", MONO),
        ("Monospace Bold", MONO_BOLD)

    ]

    for name, alphabet in unicode_fonts:

        converted = unicode_font(
            text,
            alphabet
        )

        results.append(converted)

    # ----------------------------------------------
    # استایل‌های تزئینی
    # ----------------------------------------------

    results.extend(
        decorated_fonts(text)
    )

    # فقط ۵۰ مورد
    return results[:50]


# ==================================================
# تشخیص درخواست فونت
# ==================================================

def get_font_name(text):

    text = text.strip()

    # حالت اصلی
    if text.startswith("فونت"):

        name = text[4:].strip()

        return name

    # حالت انگلیسی
    lower = text.lower()

    if lower.startswith("font"):

        name = text[4:].strip()

        return name

    return None


# ==================================================
# ساخت پاسخ
# ==================================================

def create_response(name):

    fonts = make_fonts(name)

    result = (
        f"✨ فونت‌های {name}\n"
        f"━━━━━━━━━━━━━━\n\n"
    )

    for i, font in enumerate(fonts, 1):

        result += f"{i}. {font}\n"

    result += (
        "\n━━━━━━━━━━━━━━\n"
        "🤖 Font Maker"
    )

    return result


# ==================================================
# پردازش پیام
# ==================================================

def process_update(update):

    if not update:
        return

    # فقط پیام جدید
    if update.get("type") != "NewMessage":
        return

    message = update.get("new_message")

    if not message:
        return

    text = message.get("text")

    if not text:
        return

    chat_id = update.get("chat_id")

    message_id = message.get("message_id")

    print("\n==============================")
    print("📩 پیام جدید")
    print("Chat:", chat_id)
    print("Text:", text)
    print("==============================")

    name = get_font_name(text)

    if name is None:

        return

    if not name:

        send_message(
            chat_id,
            "❌ اسم موردنظرت رو بعد از فونت بنویس.\n\n"
            "مثال:\n"
            "فونت ARSHIA\n\n"
            "یا:\n"
            "فونت یاسنا"
        )

        return

    print("🔤 Name:", name)

    response = create_response(name)

    send_message(
        chat_id,
        response,
        message_id
    )


# ==================================================
# رد کردن پیام‌های قدیمی
# ==================================================

def skip_old_updates():

    global offset_id

    print("🧹 در حال رد کردن پیام‌های قبلی...")

    result = api(
        "getUpdates",
        {}
    )

    if not result:

        print("⚠️ دریافت صف اولیه ناموفق بود.")
        return

    if result.get("status") != "OK":

        print("⚠️ پاسخ نامعتبر:")
        print(result)
        return

    data = result.get("data", {})

    next_offset = data.get(
        "next_offset_id"
    )

    updates = data.get(
        "updates",
        []
    )

    if next_offset:

        offset_id = next_offset

        print(
            f"✅ {len(updates)} آپدیت قدیمی رد شد."
        )

        print(
            "➡️ Offset:",
            offset_id
        )

    else:

        print(
            "✅ پیام قدیمی وجود نداشت."
        )


# ==================================================
# دریافت پیام‌های جدید
# ==================================================

def get_new_updates():

    global offset_id

    data = {}

    if offset_id:

        data["offset_id"] = offset_id

    return api(
        "getUpdates",
        data
    )


# ==================================================
# شروع ربات
# ==================================================

print("=" * 50)
print("          FONT MAKER RUBIKA BOT")
print("=" * 50)
print()

skip_old_updates()

print()
print("🤖 ربات روشن شد.")
print("📱 پیوی و گروه فعال هستند.")
print("💬 مثال: فونت ARSHIA")
print("💬 مثال: فونت یاسنا")
print()


# ==================================================
# حلقه اصلی
# ==================================================

while True:

    try:

        result = get_new_updates()

        if not result:

            time.sleep(2)

            continue

        if result.get("status") != "OK":

            print(
                "⚠️ پاسخ نامعتبر:",
                result
            )

            time.sleep(3)

            continue

        data = result.get(
            "data",
            {}
        )

        updates = data.get(
            "updates",
            []
        )

        # خیلی مهم:
        # offset بعدی را از خود روبیکا می‌گیریم

        next_offset = data.get(
            "next_offset_id"
        )

        if next_offset:

            offset_id = next_offset

        for update in updates:

            process_update(update)

        time.sleep(1)

    except KeyboardInterrupt:

        print("\n🛑 ربات متوقف شد.")

        break

    except Exception as e:

        print(
            "\n❌ خطای اصلی:",
            e
        )

        time.sleep(3)