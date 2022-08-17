# 名字好酷喔，只有你耶
from email.message import Message
from line import reply_message
from message_queue import RequestTimeout, ask
from overlap_name import overlap
from afterselection import final
from unique_name import PlayerNotFound, unique


def individual(event):
    try:
        event = ask(event, "請輸入姓名")
        name = event.message.text
        print(name)
        options = overlap(name)
        if not options:
            response = unique(name)
            reply_message(event, response)
        else:
            event = ask(event, ", ".join(options))
            birthday = event.message.text
            name_birth = [p for p in options if birthday in p]
            print(name_birth)
            if len(name_birth) != 1:
                reply_message(
                    event, '使用者你好!你所輸入的出生年月不符合使用規範，請你先去看一下使用說明，點擊圖文選單右下角就會在聊天室出現了。Buen dia~')
                raise Exception("name birth is not 1", name_birth)
            reply_message(event, final(name_birth[0]))
    except PlayerNotFound:
        reply_message(event, '查無此人')

    except RequestTimeout:
        reply_message(event, 'Thread dismissed!')
        print("Timeout!")
        #alt_text = '名字有重複囉，請選擇下方Flex Message中自己的生日'
        # line_bot_api.reply_message(
        # event.reply_token,
        # FlexSendMessage(alt_text, overlap(name)))
        # class SameName(Exception):
        #     def __str__(self) -> str:
        #         return super().__str__()
        # print(unique('陳昕'))
        # unique('周昱翔')
