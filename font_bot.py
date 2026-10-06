import json
import time
import urllib.request
import os
import threading
from http.server import BaseHTTPRequestHandler, HTTPServer


# =========================================
# تنظیمات
# =========================================

TOKEN = os.getenv("TOKEN")

if not TOKEN:
    raise ValueError("❌ متغیر TOKEN در Render تنظیم نشده است.")

BASE_URL = f"https://botapi.rubika.ir/v3/{TOKEN}"

offset_id = None


# =========================================
# HTTP HEALTH SERVER برای Render
# =========================================

class HealthHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        if self.path == "/health":

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

    port = int(os.environ.get("PORT", 10000))

    server = HTTPServer(
        ("0.0.0.0", port),
        HealthHandler
    )

    print(f"🌐 Health server running on port {port}")

    server.serve_forever()


threading.Thread(
    target=start_health_server,
    daemon=True
).start()


# =========================================
# RUBIKA API
# =========================================

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

            result = response.read().decode(
                "utf-8"
            )

            return json.loads(result)

    except Exception as e:

        print("❌ API ERROR:", e)

        return None


# =========================================
# ارسال پیام
# =========================================

def send_message(
    chat_id,
    text,
    reply_to=None
):

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


# ============================================================
# فونت‌های انگلیسی
# ============================================================

NORMAL_UPPER = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NORMAL_LOWER = "abcdefghijklmnopqrstuvwxyz"


# ------------------------------------------------------------
# Bold
# ------------------------------------------------------------

BOLD_UPPER = (
    "𝐀𝐁𝐂𝐃𝐄𝐅𝐆𝐇𝐈𝐉𝐊𝐋𝐌𝐍𝐎𝐏𝐐𝐑𝐒𝐓𝐔𝐕𝐖𝐗𝐘𝐙"
)

BOLD_LOWER = (
    "𝐚𝐛𝐜𝐝𝐞𝐟𝐠𝐡𝐢𝐣𝐤𝐥𝐦𝐧𝐨𝐩𝐪𝐫𝐬𝐭𝐮𝐯𝐰𝐱𝐲𝐳"
)


# ------------------------------------------------------------
# Italic
# ------------------------------------------------------------

ITALIC_UPPER = (
    "𝐴𝐵𝐶𝐷𝐸𝐹𝐺𝐻𝐼𝐽𝐾𝐿𝑀𝑁𝑂𝑃𝑄𝑅𝑆𝑇𝑈𝑉𝑊𝑋𝑌𝑍"
)

ITALIC_LOWER = (
    "𝑎𝑏𝑐𝑑𝑒𝑓𝑔ℎ𝑖𝑗𝑘𝑙𝑚𝑛𝑜𝑝𝑞𝑟𝑠𝑡𝑢𝑣𝑤𝑥𝑦𝑧"
)


# ------------------------------------------------------------
# Bold Italic
# ------------------------------------------------------------

BOLD_ITALIC_UPPER = (
    "𝑨𝑩𝑪𝑫𝑬𝑭𝑮𝑯𝑰𝑱𝑲𝑳𝑴𝑵𝑶𝑷𝑸𝑹𝑺𝑻𝑼𝑽𝑾𝑿𝒀𝒁"
)

BOLD_ITALIC_LOWER = (
    "𝒂𝒃𝒄𝒅𝒆𝒇𝒈𝒉𝒊𝒋𝒌𝒍𝒎𝒏𝒐𝒑𝒒𝒓𝒔𝒕𝒖𝒗𝒘𝒙𝒚𝒛"
)


# ------------------------------------------------------------
# Script
# ------------------------------------------------------------

SCRIPT_UPPER = (
    "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
)

SCRIPT_LOWER = (
    "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
)


# ------------------------------------------------------------
# Bold Script
# ------------------------------------------------------------

BOLD_SCRIPT_UPPER = (
    "𝓐𝓑𝓒𝓓𝓔𝓕𝓖𝓗𝓘𝓙𝓚𝓛𝓜𝓝𝓞𝓟𝓠𝓡𝓢𝓣𝓤𝓥𝓦𝓧𝓨𝓩"
)

BOLD_SCRIPT_LOWER = (
    "𝓪𝓫𝓬𝓭𝓮𝓯𝓰𝓱𝓲𝓳𝓴𝓵𝓶𝓷𝓸𝓹𝓺𝓻𝓼𝓽𝓾𝓿𝔀𝔁𝔂𝔃"
)


# ------------------------------------------------------------
# Fraktur
# ------------------------------------------------------------

FRAKTUR_UPPER = (
    "𝔄𝔅ℭ𝔇𝔈𝔉𝔊ℌℑ𝔍𝔎𝔏𝔐𝔑𝔒𝔓𝔔ℜ𝔖𝔗𝔘𝔙𝔚𝔛𝔜ℨ"
)

FRAKTUR_LOWER = (
    "𝔞𝔟𝔠𝔡𝔢𝔣𝔤𝔥𝔦𝔧𝔨𝔩𝔪𝔫𝔬𝔭𝔮𝔯𝔰𝔱𝔲𝔳𝔴𝔵𝔶𝔷"
)


# ------------------------------------------------------------
# Bold Fraktur
# ------------------------------------------------------------

BOLD_FRAKTUR_UPPER = (
    "𝕬𝕭𝕮𝕯𝕰𝕱𝕲𝕳𝕴𝕵𝕶𝕷𝕸𝕹𝕺𝕻𝕼𝕽𝕾𝕿𝖀𝖁𝖂𝖃𝖄𝖅"
)

BOLD_FRAKTUR_LOWER = (
    "𝖆𝖇𝖈𝖉𝖊𝖋𝖌𝖍𝖎𝖏𝖐𝖑𝖒𝖓𝖔𝖕𝖖𝖗𝖘𝖙𝖚𝖛𝖜𝖝𝖞𝖟"
)


# ------------------------------------------------------------
# Double
# ------------------------------------------------------------

DOUBLE_UPPER = (
    "𝔸𝔹ℂ𝔻𝔼𝔽𝔾ℍ𝕀𝕁𝕂𝕃𝕄ℕ𝕆ℙℚℝ𝕊𝕋𝕌𝕍𝕎𝕏𝕐ℤ"
)

DOUBLE_LOWER = (
    "𝕒𝕓𝕔𝕕𝕖𝕗𝕘𝕙𝕚𝕛𝕜𝕝𝕞𝕟𝕠𝕡𝕢𝕣𝕤𝕥𝕦𝕧𝕨𝕩𝕪𝕫"
)


# ------------------------------------------------------------
# Sans
# ------------------------------------------------------------

SANS_UPPER = (
    "𝖠𝖡𝖢𝖣𝖤𝖥𝖦𝖧𝖨𝖩𝖪𝖫𝖬𝖭𝖮𝖯𝖰𝖱𝖲𝖳𝖴𝖵𝖶𝖷𝖸𝖹"
)

SANS_LOWER = (
    "𝖺𝖻𝖼𝖽𝖾𝖿𝗀𝗁𝗂𝗃𝗄𝗅𝗆𝗇𝗈𝗉𝗊𝗋𝗌𝗍𝗎𝗏𝗐𝗑𝗒𝗓"
)


# ------------------------------------------------------------
# Sans Bold
# ------------------------------------------------------------

SANS_BOLD_UPPER = (
    "𝗔𝗕𝗖𝗗𝗘𝗙𝗚𝗛𝗜𝗝𝗞𝗟𝗠𝗡𝗢𝗣𝗤𝗥𝗦𝗧𝗨𝗩𝗪𝗫𝗬𝗭"
)

SANS_BOLD_LOWER = (
    "𝗮𝗯𝗰𝗱𝗲𝗳𝗴𝗵𝗶𝗷𝗸𝗹𝗺𝗻𝗼𝗽𝗾𝗿𝘀𝘁𝘂𝘃𝘄𝘅𝘆𝘇"
)


# ------------------------------------------------------------
# Sans Italic
# ------------------------------------------------------------

SANS_ITALIC_UPPER = (
    "𝘈𝘉𝘊𝘋𝘌𝘍𝘎𝘏𝘐𝘑𝘒𝘓𝘔𝘕𝘖𝘗𝘘𝘙𝘚𝘛𝘜𝘝𝘞𝘟𝘠𝘡"
)

SANS_ITALIC_LOWER = (
    "𝘢𝘣𝘤𝘥𝘦𝘧𝘨𝘩𝘪𝘫𝘬𝘭𝘮𝘯𝘰𝘱𝘲𝘳𝘴𝘵𝘶𝘷𝘸𝘹𝘺𝘻"
)


# ------------------------------------------------------------
# Sans Bold Italic
# ------------------------------------------------------------

SANS_BOLD_ITALIC_UPPER = (
    "𝘼𝘽𝘾𝘿𝙀𝙁𝙂𝙃𝙄𝙅𝙆𝙇𝙈𝙉𝙊𝙋𝙌𝙍𝙎𝙏𝙐𝙑𝙒𝙓𝙔𝙕"
)

SANS_BOLD_ITALIC_LOWER = (
    "𝙖𝙗𝙘𝙙𝙚𝙛𝙜𝙝𝙞𝙟𝙠𝙡𝙢𝙣𝙤𝙥𝙦𝙧𝙨𝙩𝙪𝙫𝙬𝙭𝙮𝙯"
)


# ------------------------------------------------------------
# Monospace
# ------------------------------------------------------------

MONO_UPPER = (
    "𝙰𝙱𝙲𝙳𝙴𝙵𝙶𝙷𝙸𝙹𝙺𝙻𝙼𝙽𝙾𝙿𝚀𝚁𝚂𝚃𝚄𝚅𝚆𝚇𝚈𝚉"
)

MONO_LOWER = (
    "𝚊𝚋𝚌𝚍𝚎𝚏𝚐𝚑𝚒𝚓𝚔𝚕𝚖𝚗𝚘𝚙𝚚𝚛𝚜𝚝𝚞𝚟𝚠𝚡𝚢𝚣"
)


# ------------------------------------------------------------
# Fullwidth
# ------------------------------------------------------------

FULLWIDTH_UPPER = (
    "ＡＢＣＤＥＦＧＨＩＪＫＬＭＮＯＰＱＲＳＴＵＶＷＸＹＺ"
)

FULLWIDTH_LOWER = (
    "ａｂｃｄｅｆｇｈｉｊｋｌｍｎｏｐｑｒｓｔｕｖｗｘｙｚ"
)


# ------------------------------------------------------------
# Circled
# ------------------------------------------------------------

CIRCLED_UPPER = (
    "ⒶⒷⒸⒹⒺⒻⒼⒽⒾⒿⓀⓁⓂⓃⓄⓅⓆⓇⓈⓉⓊⓋⓌⓍⓎⓏ"
)

CIRCLED_LOWER = (
    "ⓐⓑⓒⓓⓔⓕⓖⓗⓘⓙⓚⓛⓜⓝⓞⓟⓠⓡⓢⓣⓤⓥⓦⓧⓨⓩ"
)


# ------------------------------------------------------------
# Negative Circled
# ------------------------------------------------------------

NEG_CIRCLED_UPPER = (
    "🅐🅑🅒🅓🅔🅕🅖🅗🅘🅙🅚🅛🅜🅝🅞🅟🅠🅡🅢🅣🅤🅥🅦🅧🅨🅩"
)

NEG_CIRCLED_LOWER = NEG_CIRCLED_UPPER


# ------------------------------------------------------------
# Squared
# ------------------------------------------------------------

SQUARED_UPPER = (
    "🄰🄱🄲🄳🄴🄵🄶🄷🄸🄹🄺🄻🄼🄽🄾🄿🅀🅁🅂🅃🅄🅅🅆🅇🅈🅉"
)

SQUARED_LOWER = SQUARED_UPPER


# ------------------------------------------------------------
# Negative Squared
# ------------------------------------------------------------

NEG_SQUARED_UPPER = (
    "🅰🅱🅲🅳🅴🅵🅶🅷🅸🅹🅺🅻🅼🅽🅾🅿🆀🆁🆂🆃🆄🆅🆆🆇🆈🆉"
)

NEG_SQUARED_LOWER = NEG_SQUARED_UPPER


# ------------------------------------------------------------
# Parenthesized
# ------------------------------------------------------------

PAREN_UPPER = (
    "⒜⒝⒞⒟⒠⒡⒢⒣⒤⒥⒦⒧⒨⒩⒪⒫⒬⒭⒮⒯⒰⒱⒲⒳⒴⒵"
)

PAREN_LOWER = PAREN_UPPER


# ------------------------------------------------------------
# Small Caps
# ------------------------------------------------------------

SMALL_CAPS = {
    "a": "ᴀ",
    "b": "ʙ",
    "c": "ᴄ",
    "d": "ᴅ",
    "e": "ᴇ",
    "f": "ꜰ",
    "g": "ɢ",
    "h": "ʜ",
    "i": "ɪ",
    "j": "ᴊ",
    "k": "ᴋ",
    "l": "ʟ",
    "m": "ᴍ",
    "n": "ɴ",
    "o": "ᴏ",
    "p": "ᴘ",
    "q": "ǫ",
    "r": "ʀ",
    "s": "s",
    "t": "ᴛ",
    "u": "ᴜ",
    "v": "ᴠ",
    "w": "ᴡ",
    "x": "x",
    "y": "ʏ",
    "z": "ᴢ"
}


# ------------------------------------------------------------
# تبدیل حروف
# ------------------------------------------------------------

def unicode_font(
    text,
    upper,
    lower
):

    result = ""

    for char in text:

        if char in NORMAL_UPPER:

            index = NORMAL_UPPER.index(char)

            result += upper[index]

        elif char in NORMAL_LOWER:

            index = NORMAL_LOWER.index(char)

            result += lower[index]

        else:

            result += char

    return result


# ============================================================
# استایل‌های ترکیبی تمیز
# ============================================================

def combine_style(
    text,
    mark
):

    result = ""

    for char in text:

        if char.isalpha():

            result += char + mark

        else:

            result += char

    return result


def reverse_text(text):

    return text[::-1]


def spaced_text(text):

    return " ".join(list(text))


def boxed_text(text):

    return "【" + text + "】"


def bracket_text(text):

    return "『" + text + "』"


def parenthesis_text(text):

    return "(" + text + ")"


def angle_text(text):

    return "〈" + text + "〉"


def double_angle_text(text):

    return "《" + text + "》"


def curly_text(text):

    return "{" + text + "}"


# ============================================================
# ۵۰ فونت تمیز انگلیسی
# ============================================================

def english_fonts(text):

    fonts = []

    # 1
    fonts.append(
        unicode_font(
            text,
            BOLD_UPPER,
            BOLD_LOWER
        )
    )

    # 2
    fonts.append(
        unicode_font(
            text,
            ITALIC_UPPER,
            ITALIC_LOWER
        )
    )

    # 3
    fonts.append(
        unicode_font(
            text,
            BOLD_ITALIC_UPPER,
            BOLD_ITALIC_LOWER
        )
    )

    # 4
    fonts.append(
        unicode_font(
            text,
            SCRIPT_UPPER,
            SCRIPT_LOWER
        )
    )

    # 5
    fonts.append(
        unicode_font(
            text,
            BOLD_SCRIPT_UPPER,
            BOLD_SCRIPT_LOWER
        )
    )

    # 6
    fonts.append(
        unicode_font(
            text,
            FRAKTUR_UPPER,
            FRAKTUR_LOWER
        )
    )

    # 7
    fonts.append(
        unicode_font(
            text,
            BOLD_FRAKTUR_UPPER,
            BOLD_FRAKTUR_LOWER
        )
    )

    # 8
    fonts.append(
        unicode_font(
            text,
            DOUBLE_UPPER,
            DOUBLE_LOWER
        )
    )

    # 9
    fonts.append(
        unicode_font(
            text,
            SANS_UPPER,
            SANS_LOWER
        )
    )

    # 10
    fonts.append(
        unicode_font(
            text,
            SANS_BOLD_UPPER,
            SANS_BOLD_LOWER
        )
    )

    # 11
    fonts.append(
        unicode_font(
            text,
            SANS_ITALIC_UPPER,
            SANS_ITALIC_LOWER
        )
    )

    # 12
    fonts.append(
        unicode_font(
            text,
            SANS_BOLD_ITALIC_UPPER,
            SANS_BOLD_ITALIC_LOWER
        )
    )

    # 13
    fonts.append(
        unicode_font(
            text,
            MONO_UPPER,
            MONO_LOWER
        )
    )

    # 14
    fonts.append(
        unicode_font(
            text,
            FULLWIDTH_UPPER,
            FULLWIDTH_LOWER
        )
    )

    # 15
    fonts.append(
        unicode_font(
            text,
            CIRCLED_UPPER,
            CIRCLED_LOWER
        )
    )

    # 16
    fonts.append(
        unicode_font(
            text,
            NEG_CIRCLED_UPPER,
            NEG_CIRCLED_LOWER
        )
    )

    # 17
    fonts.append(
        unicode_font(
            text,
            SQUARED_UPPER,
            SQUARED_LOWER
        )
    )

    # 18
    fonts.append(
        unicode_font(
            text,
            NEG_SQUARED_UPPER,
            NEG_SQUARED_LOWER
        )
    )

    # 19
    fonts.append(
        unicode_font(
            text,
            PAREN_UPPER,
            PAREN_LOWER
        )
    )

    # 20
    small = ""

    for char in text:

        low = char.lower()

        if low in SMALL_CAPS:
            small += SMALL_CAPS[low]
        else:
            small += char

    fonts.append(small)

    # 21
    fonts.append(
        combine_style(
            text,
            "\u0332"
        )
    )

    # 22
    fonts.append(
        combine_style(
            text,
            "\u0336"
        )
    )

    # 23
    fonts.append(
        combine_style(
            text,
            "\u0335"
        )
    )

    # 24
    fonts.append(
        combine_style(
            text,
            "\u0337"
        )
    )

    # 25
    fonts.append(
        combine_style(
            text,
            "\u0338"
        )
    )

    # 26
    fonts.append(
        combine_style(
            text,
            "\u0305"
        )
    )

    # 27
    fonts.append(
        combine_style(
            text,
            "\u0307"
        )
    )

    # 28
    fonts.append(
        combine_style(
            text,
            "\u0323"
        )
    )

    # 29
    fonts.append(
        combine_style(
            text,
            "\u0308"
        )
    )

    # 30
    fonts.append(
        combine_style(
            text,
            "\u030A"
        )
    )

    # 31
    fonts.append(
        combine_style(
            text,
            "\u0304"
        )
    )

    # 32
    fonts.append(
        combine_style(
            text,
            "\u0303"
        )
    )

    # 33
    fonts.append(
        combine_style(
            text,
            "\u0302"
        )
    )

    # 34
    fonts.append(
        combine_style(
            text,
            "\u030C"
        )
    )

    # 35
    fonts.append(
        combine_style(
            text,
            "\u0306"
        )
    )

    # 36
    fonts.append(
        combine_style(
            text,
            "\u0301"
        )
    )

    # 37
    fonts.append(
        combine_style(
            text,
            "\u0300"
        )
    )

    # 38
    fonts.append(
        spaced_text(text)
    )

    # 39
    fonts.append(
        boxed_text(text)
    )

    # 40
    fonts.append(
        bracket_text(text)
    )

    # 41
    fonts.append(
        parenthesis_text(text)
    )

    # 42
    fonts.append(
        angle_text(text)
    )

    # 43
    fonts.append(
        double_angle_text(text)
    )

    # 44
    fonts.append(
        curly_text(text)
    )

    # 45
    fonts.append(
        "【" + text + "】"
    )

    # 46
    fonts.append(
        "[" + text + "]"
    )

    # 47
    fonts.append(
        "<" + text + ">"
    )

    # 48
    fonts.append(
        "_" + text + "_"
    )

    # 49
    fonts.append(
        "-" + text + "-"
    )

    # 50
    fonts.append(
        "=" + text + "="
    )

    return fonts[:50]


# ============================================================
# فونت‌های فارسی
# ============================================================

def persian_fonts(text):

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

    return fonts[:50]


# ============================================================
# تشخیص فارسی / انگلیسی
# ============================================================

def is_english_text(text):

    has_english = False

    for char in text:

        if char.isalpha() and char.isascii():

            has_english = True

        elif char.isalpha():

            return False

    return has_english


# ============================================================
# ساخت خروجی
# ============================================================

def make_fonts(text):

    if is_english_text(text):

        return english_fonts(text)

    return persian_fonts(text)


# ============================================================
# تشخیص دستور فونت
# ============================================================

def get_font_name(text):

    text = text.strip()

    # فارسی

    if text.startswith("فونت"):

        name = text[4:].strip()

        return name

    # انگلیسی

    lower = text.lower()

    if lower.startswith("font"):

        name = text[4:].strip()

        return name

    return None


# ============================================================
# ساخت پیام
# ============================================================

def create_response(name):

    fonts = make_fonts(name)

    result = (
        f"✨ فونت‌های {name}\n"
        f"━━━━━━━━━━━━━━\n\n"
    )

    for i, font in enumerate(
        fonts,
        1
    ):

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

    message = update.get(
        "new_message"
    )

    if not message:
        return

    text = message.get("text")

    if not text:
        return

    chat_id = update.get(
        "chat_id"
    )

    message_id = message.get(
        "message_id"
    )

    print()
    print("==============================")
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


# ============================================================
# رد کردن تمام پیام‌های قدیمی
# ============================================================

def skip_old_updates():

    global offset_id

    print(
        "🧹 در حال رد کردن پیام‌های قبلی..."
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

            print(
                "⚠️ دریافت صف اولیه ناموفق بود."
            )

            time.sleep(2)

            continue

        if result.get("status") != "OK":

            print(
                "⚠️ پاسخ نامعتبر:"
            )

            print(result)

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

        skipped += len(updates)

        if not updates:

            break

        print(
            f"🗑️ {len(updates)} پیام قدیمی رد شد."
        )

        time.sleep(0.2)

    print(
        f"✅ مجموع پیام‌های قدیمی رد شده: {skipped}"
    )

    print(
        "➡️ Offset:",
        offset_id
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
# شروع ربات
# ============================================================

print("=" * 50)

print(
    "          FONT MAKER RUBIKA BOT"
)

print("=" * 50)

print()

skip_old_updates()

print()

print(
    "🤖 ربات روشن شد."
)

print(
    "📱 پیوی و گروه فعال هستند."
)

print(
    "💬 مثال: فونت ARSHIA"
)

print(
    "💬 مثال: فونت یاسنا"
)

print()


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
            "\n🛑 ربات متوقف شد."
        )

        break

    except Exception as e:

        print(
            "\n❌ خطای اصلی:",
            e
        )

        time.sleep(3)
