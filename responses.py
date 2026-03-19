import random
pongresponses = ["https://tenor.com/xAPKvJgLSr.gif", "https://tenor.com/eG2AiNFW7sK.gif", "https://tenor.com/rT4KSQiWYFq.gif"]
cataresponses = ["https://tenor.com/ekjQkXWDZN5.gif", "https://tenor.com/ntwr2EZpUAB.gif", " https://tenor.com/pPuoGy1htU6.gif"]
waifuresponses = ["https://tenor.com/bVCiJ.gif", "https://tenor.com/peWPjVIQMUi.gif", "https://tenor.com/i1mRZdUX6kp.gif"]
responses = {
        "hi catapi": lambda m: f"Hello {m.author.display_name}!",
        "💀" : "💀",
        "<:Pepe_Business:940594983390568519>" : "<:Pepe_Business:940594983390568519>",
        "<:treu:970263511202668545>" : "<:flase:970263232214356038>",
        "<:thenerdismo:967652138723450900>" : "<:thebotysmo:987194644599308308>",
        "ping" : "pong",
        "pong" : lambda m: random.choice(pongresponses),
        "bad bot": "https://tenor.com/bkmB206JnPH.gif",
        "ride" : "https://tenor.com/qXA6XNn6pxl.gif",
        "w.claim" : lambda m: random.choice(waifuresponses),
        "<@797232493131857951>" : lambda m: random.choice(cataresponses), 
        "hawk": "tuah",
        }
