import discord
import io
import pandas as pd

client = discord.Client()


df = pd.read_csv("secrets.csv").values.tolist()


cl = [] #Get thing from gitignored csv
for l in df:
    cl.append([x for x in l if str(x) != 'nan'])

@client.event
async def on_ready():
    unicodeSkips = 0
    osSkips = 0

    with io.open("Output.txt", "w", encoding="utf-8") as f: #change this

        for ch in cl[0]:
            print("\n")
            print("Starting on channel: %s" % (ch))  
            channel = client.get_channel(int(ch))

            messages = await channel.history(limit=None).flatten()
            print("Total nr of messages: " + str(len(messages)))

            for msg in messages:
                processedMsg = ""

                curAuthor = str(msg.author)[:-5]

                if curAuthor in cl[1]:
                    pass
                else:
                    processedMsg = curAuthor + ": " + str(msg.content) + "\n"
                    f.write(processedMsg)

            print(str(ch))    
            print("Unicode skips: " + str(unicodeSkips))
            print("OS skips: " + str(osSkips))

client.run(cl[2][0])