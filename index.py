from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('AhozhCqRqPY29p3ZJN1x/JGo88ioGFM1lcWXJq0w6WxNQtsr1SPCpV2vPBiOLBX0iHGpC2rXlLiLlDFp/5LUmc9vTNeoa3IeynD2n7EIqPsS8svT+EW0UZf+41OjOajh+H8GqdedCWA969NZbX20kwdB04t89/1O/w1cDnyilFU=')
handler1 = WebhookHandler('
d3e326b7dc8bf84b18aafe1ac47465d4 D3E326B7dc8BF84B18aafe1ac47465d4')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler1.handle(body, signature)
    except InvalidSignatureError:
        print("Invalid signature. Please check your channel access token/channel secret.")
        abort(400)

    return 'OK'


@handler1.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()
