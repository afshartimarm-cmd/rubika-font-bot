import json
import time
import urllib.request
import os
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer


# ============================================================
# تنظیمات
# ============================================================

TOKEN = os.getenv("CGACAE0KAWIWSHTBRSGNZHJGZZBQCPTZGFFEWGIPLJBLLDXNGJDUGVKWIOXOCXSI")

if not TOKEN:
    raise ValueError("❌ متغیر TOKEN در Render تنظیم نشده است.")

BASE_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"
offset_id = None


# ============================================================
# HTTP SERVER مخصوص Render
# ============================================================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path in ("/", "/health"):

            self.send_response(200)
            self.send_header(
                "Content-Type",
                "text/plain; charset=utf-8"
            )
            self.end_headers()

            self.wfile.write(b"OK")

        else:

            self.send_response(404)
            self.end_headers()

    def log_message(self, format, *args):
        return


def start_health_server():

    port = int(os.environ.get("PORT", "10000"))

    try:

        server = ThreadingHTTPServer(
            ("0.0.0.0", port),
            HealthHandler
        )

        print(
            f"🌐 HTTP server listening on 0.0.0.0:{port}",
            flush=True
        )

        server.serve_forever()

    except Exception as e:

        print(
            f"❌ HTTP SERVER ERROR: {e}",
            flush=True
        )


health_thread = threading.Thread(
    target=start_health_server,
    daemon=True
)

health_thread.start()

time.sleep(1)


# ============================================================
# RUBIKA API
# ============================================================

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

        print(
            "❌ API ERROR:",
            e,
            flush=True
        )

        return None


# ============================================================
# ارسال پیام
# ============================================================

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
        print(
            "📤 پیام ارسال شد.",
            flush=True
        )

    return result


# ============================================================
# حروف انگلیسی
# ============================================================

UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWER = "abcdefghijklmnopqrstuvwxyz"


BOLD_U = "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"
BOLD_L = "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"

ITALIC_U = "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"
ITALIC_L = "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧"

BOLD_ITALIC_U = "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁"
BOLD_ITALIC_L = "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"

SCRIPT_U = "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
SCRIPT_L = "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"

BOLD_SCRIPT_U = "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"
BOLD_SCRIPT_L = "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"

FRAKTUR_U = "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"
FRAKTUR_L = "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"

BOLD_FRAKTUR_U = "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"
BOLD_FRAKTUR_L = "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"

DOUBLE_U = "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
DOUBLE_L = "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"

SANS_U = "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹"
SANS_L = "𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓"

SANS_BOLD_U = "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
SANS_BOLD_L = "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"

SANS_ITALIC_U = "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
SANS_ITALIC_L = "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"

SANS_BOLD_ITALIC_U = "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
SANS_BOLD_ITALIC_L = "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"

MONO_U = "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
MONO_L = "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"

FULL_U = "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
FULL_L = "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"


# ============================================================
# تبدیل فونت
# ============================================================

def unicode_font(text, upper, lower):

    result = ""

    for char in text:

        if char in UPPER:
            result += upper[UPPER.index(char)]

        elif char in LOWER:
            result += lower[LOWER.index(char)]

        else:
            result += char

    return result


def combine_style(text, mark):

    result = ""

    for char in text:

        if char.isalpha():
            result += char + mark
        else:
            result += char

    return result


# ============================================================
# Small Caps
# ============================================================

SMALL_CAPS = {
    "a": "ᴀ", "b": "ʙ", "c": "ᴄ", "d": "ᴅ",
    "e": "ᴇ", "f": "ꜰ", "g": "ɢ", "h": "ʜ",
    "i": "ɪ", "j": "ᴊ", "k": "ᴋ", "l": "ʟ",
    "m": "ᴍ", "n": "ɴ", "o": "ᴏ", "p": "ᴘ",
    "q": "ǫ", "r": "ʀ", "s": "s", "t": "ᴛ",
    "u": "ᴜ", "v": "ᴠ", "w": "ᴡ", "x": "x",
    "y": "ʏ", "z": "ᴢ"
}


def small_caps(text):

    return "".join(
        SMALL_CAPS.get(char.lower(), char)
        for char in text
    )


# ============================================================
# ۵۰ فونت انگلیسی تمیز
# ============================================================

def english_fonts(text):

    fonts = [

        unicode_font(text, BOLD_U, BOLD_L),
        unicode_font(text, ITALIC_U, ITALIC_L),
        unicode_font(text, BOLD_ITALIC_U, BOLD_ITALIC_L),
        unicode_font(text, SCRIPT_U, SCRIPT_L),
        unicode_font(text, BOLD_SCRIPT_U, BOLD_SCRIPT_L),
        unicode_font(text, FRAKTUR_U, FRAKTUR_L),
        unicode_font(text, BOLD_FRAKTUR_U, BOLD_FRAKTUR_L),
        unicode_font(text, DOUBLE_U, DOUBLE_L),
        unicode_font(text, SANS_U, SANS_L),
        unicode_font(text, SANS_BOLD_U, SANS_BOLD_L),
        unicode_font(text, SANS_ITALIC_U, SANS_ITALIC_L),
        unicode_font(text, SANS_BOLD_ITALIC_U, SANS_BOLD_ITALIC_L),
        unicode_font(text, MONO_U, MONO_L),
        unicode_font(text, FULL_U, FULL_L),
        small_caps(text),

        combine_style(text, "\u0332"),
        combine_style(text, "\u0336"),
        combine_style(text, "\u0335"),
        combine_style(text, "\u0337"),
        combine_style(text, "\u0338"),
        combine_style(text, "\u0305"),
        combine_style(text, "\u0307"),
        combine_style(text, "\u0323"),
        combine_style(text, "\u0308"),
        combine_style(text, "\u030A"),
        combine_style(text, "\u0304"),
        combine_style(text, "\u0303"),
        combine_style(text, "\u0302"),
        combine_style(text, "\u030C"),
        combine_style(text, "\u0306"),
        combine_style(text, "\u0301"),
        combine_style(text, "\u0300"),

        " ".join(text),
        f"【{text}】",
        f"『{text}』",
        f"「{text}」",
        f"〖{text}〗",
        f"〘{text}〙",
        f"〚{text}〛",
        f"《{text}》",
        f"〈{text}〉",
        f"〔{text}〕",
        f"⟦{text}⟧",
        f"⟨{text}⟩",
        f"⟪{text}⟫",
        f"⟮{text}⟯",
        f"({text})",
        f"[{text}]",
        f"{{{text}}}",
        f"<{text}>",
        f"_{text}_",
        f"-{text}-",
        f"={text}=",
        f"|{text}|",
        f"/{text}/"

    ]

    return fonts[:50]


# ============================================================
# ۵۰ استایل فارسی
# ============================================================

def persian_fonts(text):

    fonts = [

        f"『 {text} 』",
        f"〖 {text} 〗",
        f"〘 {text} 〙",
        f"〚 {text} 〛",
        f"《 {text} 》",
        f"〈 {text} 〉",
        f"「 {text} 」",
        f"【 {text} 】",
        f"〔 {text} 〕",
        f"⟦ {text} ⟧",
        f"⟨ {text} ⟩",
        f"⟪ {text} ⟫",
        f"⟮ {text} ⟯",
        f"({text})",
        f"[{text}]",
        f"{{{text}}}",
        f"<{text}>",
        f"| {text} |",
        f"/ {text} /",
        f"\\ {text} /",

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
        f"• {text} •",
        f"● {text} ●",
        f"○ {text} ○",
        f"◉ {text} ◉",
        f"◆ {text} ◆",
        f"◇ {text} ◇",
        f"⬢ {text} ⬢",
        f"⟡ {text} ⟡",
        f"❖ {text} ❖",
        f"✺ {text} ✺",
        f"✹ {text} ✹",
        f"✷ {text} ✷",
        f"✵ {text} ✵",
        f"✿ {text} ✿",
        f"༺ {text} ༻",
        f"꧁ {text} ꧂",
        f"𓆩 {text} 𓆪",
        f"╰┈➤ {text}"

    ]

    return fonts[:50]


# ============================================================
# تشخیص زبان
# ============================================================

def is_english_text(text):

    has_english = False

    for char in text:

        if char.isalpha() and char.isascii():
            has_english = True

        elif char.isalpha():
            return False

    return has_english


def make_fonts(text):

    if is_english_text(text):
        return english_fonts(text)

    return persian_fonts(text)


# ============================================================
# تشخیص دستور
# ============================================================

def get_font_name(text):

    text = text.strip()

    if text.startswith("فونت"):
        return text[4:].strip()

    if text.lower().startswith("font"):
        return text[4:].strip()

    return None


# ============================================================
# ساخت پاسخ
# ============================================================

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


# ============================================================
# پردازش پیام
# ============================================================

def process_update(update):

    if not update:
        return

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

    print(
        f"📩 پیام جدید | {text}",
        flush=True
    )

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

    response = create_response(name)

    send_message(
        chat_id,
        response,
        message_id
    )


# ============================================================
# رد کردن تمام پیام‌های قدیمی
# ============================================================

def skip_old_updates():

    global offset_id

    print(
        "🧹 در حال رد کردن پیام‌های قبلی...",
        flush=True
    )

    skipped = 0

    while True:

        data = {}

        if offset_id:
            data["offset_id"] = offset_id

        result = api(
            "getUpdates",
            data
        )

        if not result:

            time.sleep(2)
            continue

        if result.get("status") != "OK":

            print(
                "⚠️ پاسخ نامعتبر:",
                result,
                flush=True
            )

            time.sleep(2)
            continue

        response_data = result.get(
            "data",
            {}
        )

        updates = response_data.get(
            "updates",
            []
        )

        next_offset = response_data.get(
            "next_offset_id"
        )

        if next_offset:
            offset_id = next_offset

        if not updates:
            break

        skipped += len(updates)

        print(
            f"🗑️ {len(updates)} پیام قدیمی رد شد.",
            flush=True
        )

        time.sleep(0.2)

    print(
        f"✅ مجموع پیام‌های قدیمی رد شده: {skipped}",
        flush=True
    )


# ============================================================
# دریافت پیام‌های جدید
# ============================================================

def get_new_updates():

    global offset_id

    data = {}

    if offset_id:
        data["offset_id"] = offset_id

    return api(
        "getUpdates",
        data
    )


# ============================================================
# شروع
# ============================================================

print("=" * 50, flush=True)
print("       FONT MAKER RUBIKA BOT", flush=True)
print("=" * 50, flush=True)

skip_old_updates()

print(
    "🤖 ربات روشن شد.",
    flush=True
)

print(
    "📱 پیوی و گروه فعال هستند.",
    flush=True
)

print(
    "💬 مثال: فونت ARSHIA",
    flush=True
)

print(
    "💬 مثال: فونت یاسنا",
    flush=True
)


# ============================================================
# LOOP اصلی
# ============================================================

while True:

    try:

        result = get_new_updates()

        if not result:

            time.sleep(2)
            continue

        if result.get("status") != "OK":

            print(
                "⚠️ پاسخ نامعتبر:",
                result,
                flush=True
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

        next_offset = data.get(
            "next_offset_id"
        )

        if next_offset:
            offset_id = next_offset

        for update in updates:
            process_update(update)

        time.sleep(1)

    except KeyboardInterrupt:

        print(
            "\n🛑 ربات متوقف شد.",
            flush=True
        )

        break

    except Exception as e:

        print(
            "\n❌ خطای اصلی:",
            e,
            flush=True
        )

        time.sleep(3)
