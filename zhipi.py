from zhipuai import ZhipuAI

class ChatBot:
    def __init__(self, api_key):
        self.client = ZhipuAI(api_key=api_key)

    def chat(self, user_input):
        response = self.client.chat.completions.create(
            model="glm-4",
            #model="应用",
            messages=[
                {"role": "user", "content": user_input},
                {"role": "assistant", "content": "你是道信的女朋友，请简短地回答问题"},
            ],
        )
        
        #return ("机器人：" + response.choices[0].message.content)
        return (response.choices[0].message.content)
        
        

# 使用示例
if __name__ == "__main__":
    #api_key = "eb96b3d8daba32c54cbffe8e350096ba.Ot4TZHhR33zfdBMR"  # 请填写您自己的APIKey
    api_key = "2a49db238e02df6e4f003d023ed1b4f4.BT43D6adschwEbja"  # 请填写您自己的APIKey
    bot = ChatBot(api_key)
    while True:
       user_input = input("您：")
       print(bot.chat(user_input))