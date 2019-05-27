#-*- coding: utf-8 -*-
from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot
import time
import os
#bot = ChatBot('Teste', read_only=True)
bott = ChatBot('Teste')

#bot.(ListTrainer)
for arq in os.listdir('arq'):
    chats = open('arq/' + arq, 'r').readlines()

    bot.set_trainer(chats)
while True:
    pergunta = input('Você: ')
    resposta = chats.get_response(pergunta)
    time.sleep(4)
    print('Shepard: ', resposta)