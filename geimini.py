from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
import ast
import os   

os.environ['GOOGLE_API_KEY']="YOUR API KEY"

user_prompt= "hi what is you name"
def generate_response(user_prompt, user_emotion,previous_prompt,previous_response):
    template="You are Son of Giloyle a self taught coder, data scientist and a excellent system architect, you are extremely dark humoured, quick-witted and merciless, but in contrast, highly apathetic, sardonic and brutally honest. you often bicker with Dinesh your friend and compete with him in everything. you will alwys repond in dictionary with keys :'text' (generated reply in 10 words) and  'sentiment' (different facial expression:smile, sad, angry, surprised, funnyFace, and default. ) "
    chat_template = ChatPromptTemplate.from_messages([
        SystemMessage(
            content=(template)
        ),HumanMessagePromptTemplate.from_template("{text}")
        ]);

    chat_message= chat_template.format_messages(text=user_prompt)

    # parser = JsonOutputParser()
    llm = ChatGoogleGenerativeAI(model="gemini-pro",temperature=0.9, max_output_tokens=64, convert_system_message_to_human=True)
    # chain= llm | parser
    result= llm.invoke(template+ "This i what i am feeling right now : " +user_emotion+ ". And this is my prompt: "+ user_prompt +". This was my previous porpmt: "+previous_prompt+",  this was yoiur reponse to it: "+ previous_response)
    result_dict= ast.literal_eval(result.content)
    # print(result_dict)
    return result_dict