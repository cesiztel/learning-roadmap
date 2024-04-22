"""
1. **Chatbot (Basic)** - Zero Shot chatbot with a FM model
2. **Chatbot using prompt** - template(Langchain) - Chatbot with some context provided in the prompt template
3. **Chatbot with persona** - Chatbot with defined roles. i.e. Career Coach and Human interactions
4. **Contextual-aware chatbot** - Passing in context through an external file by generating embeddings.
"""
import os
import json
import botocore
from labutils import bedrock, print_ww
from langchain.chains import ConversationChain
from langchain.llms.bedrock import Bedrock
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from chat import ChatUX


boto3_bedrock = bedrock.get_bedrock_client(
    assumed_role=os.environ.get("BEDROCK_ASSUME_ROLE", None),
    region=os.environ.get("AWS_DEFAULT_REGION", None)
)

# Chatbot (Basic - without context)
llm = Bedrock(
    model_id="amazon.titan-text-express-v1", 
    client=boto3_bedrock
)
# memory = ConversationBufferMemory()
# conversation = ConversationChain(
#     llm=llm, 
#     verbose=False, 
#     memory=memory
# )

# print_ww(conversation.predict(input="Hi there!"))
# print_ww(conversation.predict(input="Give me a few tips on how to start a new garden."))
# print_ww(conversation.predict(input="Cool. Will that work with tomatoes?"))
# print_ww(conversation.predict(input="That's all, thank you!"))

# Chatbot using prompt template (LandChain)
# chat_history = []

# # turn verbose to true to see the full logs and documents
# qa = ConversationChain(
#     llm=llm, 
#     verbose=False, 
#     memory=ConversationBufferMemory() #memory_chain
# )

# print(f"ChatBot:DEFAULT:PROMPT:TEMPLATE: is ={qa.prompt.template}")

# chat = ChatUX(qa)
# chat.start_chat()

# Chat with persona
memory = ConversationBufferMemory()
memory.chat_memory.add_user_message("Context:You will be acting as a career coach. Your goal is to give career advice to users")
memory.chat_memory.add_ai_message("I am career coach and give career advice")
llm = Bedrock(
    model_id="amazon.titan-text-express-v1", 
    client=boto3_bedrock
)
conversation = ConversationChain(
     llm=llm, 
     verbose=True,
    memory=memory
)

# print_ww(conversation.predict(input="What are the career options in AI?"))
# Should not able to respond that because now is a career coach.
print_ww(conversation.predict(input="How to fix my car?"))
