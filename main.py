import pandas as pd
import numpy as np
from uiautomation import WindowControl
import uiautomation as ui
import time
from datetime import datetime
from chatbot import Chatbot
import re

from zhipi import ChatBot
from config import api_key,  response_file, csv_file  # 导入配置文件中的变量

def wxuser():
    ui.SetGlobalSearchTimeout(0)
    info = {}
    WX = WindowControl(Name='微信')
    print(WX)
    WX.SwitchToThisWindow()
    hw = WX.ListControl(Name='会话')
    print('寻找会话控件绑定', hw)
    df = pd.read_csv(csv_file, encoding='gbk')
    print(WX)
    we = hw.TextControl(searchDepth=4)
    if we.Exists(0):
        print('查找未读消息', we)
        if we.Name:
            fame = we.GetParentControl().GetParentControl()
            famel = fame.Name
            print("聊天对象:" + famel)
            we.Click(simulateMove=False)
            last_msg = WX.ListControl(Name='消息').GetChildren()[-1].Name
            print('读取最后一条消息', last_msg)
            msg = df.apply(lambda x: x['回复内容'] if x['关键字'] in last_msg else None, axis=1)
            msg.dropna(axis=0, how='any', inplace=True)
            ar = np.array(msg).tolist()
            if ar:
                WX.SendKeys(ar[0].replace('{br}','{Shift}{Enter}'), waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=ar[0][:5]).RightClick()
            elif "菲菲" in last_msg:
                chatbot = Chatbot(response_file)
                msge = last_msg.rstrip("菲菲").rstrip('""')
                response = chatbot.run(msge)
                print(response)
                reply = response
                WX.SendKeys(reply, waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=last_msg[:5]).RightClick()
            
            elif "wifi" in last_msg:
                response = "名称:CMMC-mkVE"+"密码:YvkDmqzp"
                print(response)
                reply = response
                WX.SendKeys(reply, waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=last_msg[:5]).RightClick()
            else:
                sparkdesk = ChatBot(api_key)
                prompt = last_msg
                response = sparkdesk.chat(prompt)
                reply = response
                print(reply)
                WX.SendKeys(reply, waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=last_msg[:5]).RightClick()

def grouop():
    ui.SetGlobalSearchTimeout(0)
    info = {}
    WX = WindowControl(Name='微信')
    print(WX)
    WX.SwitchToThisWindow()
    hw = WX.ListControl(Name='会话')
    print('寻找会话控件绑定', hw)
    df = pd.read_csv(csv_file, encoding='gbk')
    print(WX)
    we = hw.TextControl(SubName="@菲菲", searchDepth=5)
    if we.Exists(0):
        print('查找未读消息', we)
        if we.Name:
            fame = we.GetParentControl().GetParentControl()
            famel = fame.Name
            print("聊天对象:" + famel)
            we.Click(simulateMove=False)
            last_msg = WX.ListControl(Name='消息').GetChildren()[-1].Name
            print('读取最后一条消息', last_msg)
            msg = df.apply(lambda x: x['回复内容'] if x['关键字'] in last_msg else None, axis=1)
            msg.dropna(axis=0, how='any', inplace=True)
            ar = np.array(msg).tolist()
            if ar:
                WX.SendKeys(ar[0].replace('{br}','{Shift}{Enter}'), waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=ar[0][:5]).RightClick()
            elif "运势" in last_msg:
                getalmanacrun = GetAlmanacRun()
                response = getalmanacrun.run(appkey)
                print(response)
                reply = response
                WX.SendKeys(reply, waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=last_msg[:5]).RightClick()
            elif "wifi" in last_msg:
                response = "名称:CMMC-mkVE"+"密码:YvkDmqzp"
                print(response)
                reply = response
                WX.SendKeys(reply, waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=last_msg[:5]).RightClick()
            else:
                sparkdesk = ChatBot(api_key)
                prompt = last_msg
                response = sparkdesk.chat(prompt)
                reply = response
                WX.SendKeys(reply, waitTime=0)
                WX.SendKeys('{Enter}', waitTime=5)
                WX.TextControl(SubName=last_msg[:5]).RightClick()

def main():
    try:
        WX = WindowControl(Name='微信')
        print(WX)
        while True:
            wxuser()
            grouop()
            time.sleep(0.2)
    except Exception as e:
        print("抱歉，我不明白你说什么", str(e))
        WX.SendKeys("抱歉，我不明白你说什么", waitTime=0)
        WX.SendKeys('{Enter}', waitTime=5)
        main()

if __name__ == "__main__":
    main()