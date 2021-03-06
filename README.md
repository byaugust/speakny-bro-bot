# SpeaknyBro Bot

This is a telegram bot that turns a word or text up to 300 characters into lifelike speech and send it back as a voice message.

It doesn't translate one language to another one. For now. It just converts text to a voice message.

## Why?

This bot is useful for those who learn a foreign language. Sometimes it could be tricky to find out how to pronounce some words or phrases.

So this bot can help with that.

Currently the bot has 8 languages. And every language has native speakers. And in settings one can change the language and choose the native speaker for it.

For some languages native speakers are from different countries. For example, English has native speakers from Australia, United States, UK. Or Portuguese has natives from Brazil and Portugal.

And it might help to understand how a word is pronounced by people from different countries.

## How does it work?

It uses a service called Amazon Polly that turns text into lifelike speech with neural network. So it basically sounds real close to how people talk in real life.

It even understands the question mark and natives change the intonation.

## Development process

Creating a telegram bot there are 2 ways to get updates.
- Using a method `getUpdates`
- Using a webhook

I choose to use a webhook. But telegram requires to always use https over http. So it could be tricky on the local machine. And there's a service called [ngrok](https://ngrok.com/) which can help with that.

The whole process would like that
- Initialising ngrok to get https url
```bash

ngrok http 8000

```

- Put that url into `config.py` to `Dev/webhook_url`
- And then we can launch it

```bash

python3 -m venv venv

. venv/bin/activate

python -m src.dev

```

## Languages

| Language      | Natives                                                                     |
| ------------- | --------------------------------------------------------------------------- |
| πΊπΈ English    | πΊπΈ Kimberly, πΊπΈ Mathew, π¬π§ Brian, π¬π§Emma, π¦πΊ Nicole, π¦πΊ Russell               |
| πͺπΈ EspaΓ±ol    | πͺπΈ Lucia, πͺπΈ Enrique, πͺπΈ Conchita, π²π½ Mia, πΊπΈ Miguel, πΊπΈ Lupe                 |
| π©πͺ Deutsch    | π©πͺ Hans, π©πͺ Vicki, π©πͺ Marlene                                                |
| π«π· FranΓ§ais   | π«π· Lea, π«π· Celine, π«π· Mathieu, π¨π¦ Chantal                                    |
| π?πΉ Italiano   | π?πΉ Carla, π?πΉ Giorgio, π?πΉ Bianca                                              |
| π§π· PortuguΓͺs  | π§π· Camila, π§π· Vitoria, π§π· Ricardo, π΅πΉ Ines, π΅πΉ Cristiano                      |
| π¦πͺ ΨΉΨ±Ψ¨Ω       | π¦πͺ Zeina                                                                    |
| π·πΊ Π ΡΡΡΠΊΠΈΠΉ    | π·πΊ Tatyana, π·πΊ Maxim                                                         |
