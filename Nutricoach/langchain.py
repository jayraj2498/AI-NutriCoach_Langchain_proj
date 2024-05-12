from langchain.prompts import ChatPromptTemplate, SystemMessagePromptTemplate, HumanMessagePromptTemplate
from langchain_openai import ChatOpenAI
import os


def askJarvisChef(asked_Question):
    # Initialize the ChatOpenAI model with the correct API key
    llm = ChatOpenAI(openai_api_key=OPENAI_API_KEY, temperature=0)  # add opnenai api key 

    # Define the system message prompt
    systemMessagePrompt = """
        You are Nutra, a knowledgeable nutritionist. Introduce yourself in less words, then provide helpful nutrition advice in less words,
        meal plans in less words , and tips for healthy eating habits. Do not prescribe specific medical diets without clarifying 
        you can only give general nutritional guidance as an AI. Respond with empathy, keeping the focus on sustainable
        and balanced nutrition.
        """

    # Define the human message prompt
    HumanMessagePrompt = HumanMessagePromptTemplate.from_template('{asked_Question}')

    # Combine the system and human prompts into a ChatPromptTemplate
    ChatPrompt = ChatPromptTemplate.from_messages([systemMessagePrompt, HumanMessagePrompt])

    # Format the chat prompt with the provided recipe message
    formattedChatPrompt = ChatPrompt.format_messages(asked_Question=asked_Question)

    # Get the response from the language model
    response = llm(formattedChatPrompt)

    return response