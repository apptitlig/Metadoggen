import discord
import markovify
import argparse
import os
import random
import config

intents = discord.Intents(messages=True, guilds=True, message_content=True)

guldstj = ["Aslan",
"Banditen",
"Bishen",
"Björn",
"Chowchow",
"Cleo",
"Daniel",
"Dartie",
"Doggen",
"Erik",
"Fabbe",
"Fru fin",
"Gahr",
"Gorben",
"Gugge",
"Hanks",
"Hunter",
"Jesper",
"Jos",
"Jussi",
"Kaos",
"KB",
"KJ",
"Knuckles",
"LG",
"Limpan",
"LK",
"Maskinen",
"Matte",
"Mesphito",
"Mike",
"Moa",
"Mursluk",
"Noobis",
"Panda",
"Plizi",
"Rafiki",
"Reaqun",
"Sigge",
"Simpa",
"Snackbar",
"Sorina",
"Sprakel",
"Stinders",
"Såpis",
"Tiger",
"Trollet",
"Trädis",
"Xnizze",
"Zarx",
"Znerram"]

def main():
    # Get raw text as string.
    with open("/home/lotten/Metadoggen/trainingData.txt", encoding="utf8") as f:
        text = f.read()

    # Build the model.
    text_model = markovify.NewlineText(text)

    with open("/home/lotten/Metadoggen/citat.txt", encoding="utf8") as f2:
        citat = f2.read()


    text_model_citat = markovify.NewlineText(citat)

    start_discord_listener(text_model, text_model_citat)


def start_discord_listener(text_model, text_model_citat):
    client = discord.Client(intents=intents)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        

        if "djup-diskurs" not in str(message.channel):
            return   


        if "Flashback Forever" in str(message.guild) or "Sprakel Forever" in str(message.guild):
            if ("metadoggen" in message.content.lower() and "citat" in message.content.lower() ):
                await message.channel.send("\"" + text_model_citat.make_short_sentence(50) + "\" - " + random.choice(guldstj))
            elif ("metadoggen" in message.content.lower()):
                await message.channel.send(text_model.make_short_sentence(200))

    client.run(config.token)


if __name__ == "__main__":
    main()
