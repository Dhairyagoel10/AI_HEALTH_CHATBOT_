from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from data.health_data import health_conversations

def create_chatbot():
    # Create the chatbot
    chatbot = ChatBot(
        'HealthBot',
        logic_adapters=[
            'chatterbot.logic.BestMatch',
            'chatterbot.logic.TimeLogicAdapter'
        ]
    )

    # Create a trainer
    trainer = ListTrainer(chatbot)

    # Train each conversation individually
    for conversation in health_conversations:   
        trainer.train(conversation)  # Train one conversation at a time

    return chatbot
