import json
import random

class Chatbot:
    def __init__(self, responses_file):
        with open(responses_file, "r", encoding="utf-8") as f:
            self.responses =json.load(f)
        
    def run(self, user_input):        
        if user_input.lower() in self.responses:
            return random.choice(self.responses[user_input.lower()])
        else:
            return "对不起，我不理解你在说什么。"


if __name__ == '__main__':
    chatbot = Chatbot("C:/Users/gold7/Desktop/qingyun-main/responses.json")
    user_input = "你好"
    response = chatbot.run(user_input)
    print( response)




