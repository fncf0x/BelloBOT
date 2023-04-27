import os

import discord
from dotenv import load_dotenv
from random import choice

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


hello = ["wach", "kifech", "saha", "ya"]
hello_response = ["saha ejeun", "wach kho", "yaaaw wch khasek", "wiii esoo7baa ghaya?"]
question_answers = [
    (
        ["wach", "kifech", "saha"],
        ["saha ejeun", "wach kho", "yaaaw wch khasek", "wiii esoo7baa ghaya?"]
    ),
    (
        ["ghani ghonya", "sing a song", "goli haja", "ech3er"],
        ["Jiboli les fruit", "Ketrouli mel kiwi", "roho tkowedo", "yaw welah manwelli"]
    ),
    (
        ["send nudes"],
        ["baghyin tchofo zebi ?", "ahachmo malkom", "malkom a zebi"]
    ),
    (
        ["weri nchofek", "baghi nchofek", "eb3at tswira", 'photo', 'chof'],
        [("ha werani", "pictures/1.jpg"), ("ih omri", "pictures/2.jpg") ,("pa de bghoblem", "pictures/3.jpg") ,("ouiii ezin", "pictures/4.jpg") ,("lik ki rani dayer", "pictures/5.jpg") ,("ok bb", "pictures/6.jpg")]
    ),
    (
        ["attack", "ezdem"],
        ["nik mok", "kowdo", "waaaa3"]
    ),
    (
        ['rak hna', 'jit', "mazalaek hna", 'u here', "here"],
        ["wah ni hna", "cha khasek omri", "ouiiii biensour", "rana daymen hna", "wah wah hna jamais la nroho"]
    ),
    (
        ["love you", "na3che9 fik", "nhabek", "omri"],
        ["moi aussi nebghik", "nbhghik rebek", "nhabek cheuri", "malek?", "aya privé nahki m3ak", 'kwdo rani za3fan'],
    ),
    (
        ["chbeb", "li zomme", "bogoss", "tawe3na", "te3na"],
        ["merciiiii hafdek", "ooooh li zomme", "hafdk hafdek", "sa77aa 3ayniya", "mchi we9tha manich mlih"],
    )
]

def answer(msg):
    for questions, answers in question_answers:
        if any(question in msg.content.lower() for question in questions) and "bello" in msg.content.lower():
            return choice(answers)
    if "bello" in msg.content.lower():
        return choice(["not implemented ya kho dir PR", "mafhatmch mazalni net3alem", "khatini mana3refch", "?"])

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        msg = answer(message)
        if msg:
            if type(msg) == tuple:
                await message.channel.send(msg[0], file=discord.File(msg[1]))
            else:
                await message.channel.send(msg)

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(TOKEN)