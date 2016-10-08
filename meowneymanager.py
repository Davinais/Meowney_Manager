#Python 3.5 is Needed.

import discord
import datetime
import os
import csv
import random
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print("----------")
    print("連接成功！")
    print("登入名稱：" + client.user.name)
    print("ID:" + client.user.id)
    print("----------")

@client.event
async def on_message(message):
    prefix = "$"
    if message.content == prefix + "rewards":
        await rewards(message)

async def rewards(message):
    initial = False if os.path.exists("dailies.csv") else True
    reward = True
    if initial:
        with open("dailies.csv", "w", newline="") as dailies:
            w = csv.writer(dailies, quoting=csv.QUOTE_ALL)
            w.writeheader(["User ID", "Last Rewarded"])
            w.writerow([message.author.id, message.timestamp.strftime("%Y-%m-%d %H:%M:%S")])
    else:
        with open("dailies.csv", "r", newline="") as dailies, open(".dailies_tmp.csv", "w", newline="") as edit:
            w = csv.writer(edit, quoting=csv.QUOTE_ALL)
            usernotinrow = True
            for row in csv.reader(dailies):
                if row[0] == message.author.id:
                    usernotinrow = False
                    lastrewarded = datetime.datetime.strptime(row[1], "%Y-%m-%d %H:%M:%S") 
                    diff = datetime.timedelta(0.5) - (message.timestamp - lastrewarded) #datetime.timedelta([days])
                    if diff > datetime.timedelta(0):
                        diffminutes = int(diff.seconds/60)
                        diffhours = 0
                        while diffminutes >= 60:
                            diffhours += 1
                            diffminutes -= 60
                        nomsg = await client.send_message(message.channel, "咦咦!?不可以這麼著急哦...{0}！不是約定好再過{1}小時{2}分之後才能再來找喵妮的喵？:blush:".format(message.author.mention, diffhours, diffminutes))
                        reward = False
                        w.writerow(row)
                    else:
                        latestrow = [message.author.id, message.timestamp.strftime("%Y-%m-%d %H:%M:%S")]
                        w.writerow(latestrow)
                else:
                    w.writerow(row)
            if usernotinrow:
                w.writerow([message.author.id, message.timestamp.strftime("%Y-%m-%d %H:%M:%S")])
        os.remove("dailies.csv")
        os.rename(".dailies_tmp.csv", "dailies.csv")
    if reward:
        print("獎勵發送中...")
        rewardmeowney = random.randint(1,5)
        awardmsg = await client.send_message(message.channel, "{0}果然是溫柔又守約定的人呢...喵妮除了給你{1}喵幣做鼓勵以外...也祝你今天幸福唷！下次也約定好再來看喵妮，好喵？:blush:".format(message.author.mention, rewardmeowney))
        awardcmd = await client.send_message(message.channel, "$award {1} {0}".format(message.author.mention, rewardmeowney))
        await asyncio.sleep(0.2)
        await client.delete_message(awardcmd)
        print("已經發送{1}喵幣獎勵給 {0}".format(message.author.name, rewardmeowney))
        print("----------")    

client.run("")
