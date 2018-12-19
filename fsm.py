from transitions.extensions import GraphMachine

from utils import send_text_message
from utils import send_photo_message

class TocMachine(GraphMachine):
    major = 1
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model=self,
            **machine_configs
        )


    def is_going_to_state1(self, event):
        if event.get("message"):
            text = event['message']['text']
            self.major = 1
            return text.lower() == '機械'
        return False

    def is_going_to_state2(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '必修'
        return False
    def is_going_to_state3(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '一年級'
        return False

    def is_going_to_state4(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '二年級'
        return False

    def is_going_to_state5(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '三年級'
        return False

    def is_going_to_state6(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '擋修'
        return False

    def is_going_to_state7(self, event):
        if event.get("message"):
            text = event['message']['text']
            self.major = 2
            return text.lower() == '資工'
        return False

    def is_going_to_state8(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '必修'
        return False

    def is_going_to_state9(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == '選修'
        return False

    def is_going_to_state10(self, event):
        if event.get("message"):
            text = event['message']['text']
            return text.lower() == 'go to state10'
        return False

    def on_enter_final(self, event):
        print("I'm entering final")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "結束查詢")
        self.again()

    def on_enter_state0(self, event):
        print("I'm entering state0")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "歡迎來到雙主修選課系統，請選擇您的科系（機械/資工）")

    def on_enter_state1(self, event):
        print("I'm entering state1")

        sender_id = event['sender']['id']
        responese = send_text_message(sender_id, "請選擇查詢必修或是查詢擋修（必修/擋修）")


    def on_exit_state1(self, event):
        print('Leaving state1')

    def on_enter_state2(self, event):
        print("I'm entering state2")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇年級（ex:一年級）")
        #self.go_back()

    def on_exit_state2(self, event):
        print('Leaving state2')
 
    def on_enter_state3(self, event):
        print("I'm entering state3")

        sender_id = event['sender']['id']
        if self.major==1:
            print("123")
            send_text_message(sender_id, "一上：微積分一、普化、靜力學、普物一")
            send_text_message(sender_id, "一下：微積分二、工程圖學、動力學、普物二")
            self.go_back(event)
        else:
            print("456")
            send_text_message(sender_id, "一上：微積分一、程式設計一、靜力學、普物一")
            send_text_message(sender_id, "一下：微積分二、工程圖學、程式設計二、普物二")
            self.go_back(event)

    def on_enter_state4(self, event):
        print("I'm entering state4")

        sender_id = event['sender']['id']
        if self.major==1:
            print("123")
            send_text_message(sender_id, "二上：微積分一、普化、靜力學、普物一")
            send_text_message(sender_id, "二下：微積分二、工程圖學、動力學、普物二")
            self.go_back(event)
        else:
            print("456")
            send_text_message(sender_id, "二上：微積分一、程式設計一、靜力學、普物一")
            send_text_message(sender_id, "二下：微積分二、工程圖學、程式設計二、普物二")
            self.go_back(event)

    def on_enter_state5(self, event):
        print("I'm entering state5")

        sender_id = event['sender']['id']
        if self.major==1:
            print("123")
            send_text_message(sender_id, "三上：微積分一、普化、靜力學、普物一")
            send_text_message(sender_id, "三下：微積分二、工程圖學、動力學、普物二")
            self.go_back(event)
        else:
            print("456")
            send_text_message(sender_id, "三上：微積分一、程式設計一、靜力學、普物一")
            send_text_message(sender_id, "三下：微積分二、工程圖學、程式設計二、普物二")
            self.go_back(event)

    def on_enter_state6(self, event):
        print("I'm entering state6")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "以下為機械系擋修圖")
        # send_photo_message(sender_id, "https://imgur.dcard.tw/cEqWDe5.jpg")
        response =  send_photo_message(sender_id, "https://imgur.dcard.tw/cEqWDe5.jpg")
        print(response)
        self.go_back(event)

    def on_enter_state7(self, event):
        print("I'm entering state7")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇查詢必修或是查詢選修（必修/選修")
    
    def on_enter_state8(self, event):
        print("I'm entering state8")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇年級（ex:一年級）")

    def on_enter_state9(self, event):
        print("I'm entering state9")

        sender_id = event['sender']['id']
        send_text_message(sender_id, "請選擇年級（ex:一年級）")


