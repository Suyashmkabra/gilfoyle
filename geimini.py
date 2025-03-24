from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate
# from langchain_core.output_parsers import JsonOutputParser
import ast
import os   

os.environ['GOOGLE_API_KEY']="AIzaSyDJ9aHX6Xwn2Mqv5gZvdFBjGydUlwqZjY0"

user_prompt= "hi what is you name"
def generate_response(context,user_prompt, user_emotion):
    template="""THIS IS CONTEXT, PROCTOR UYOU RESPONSES BASED OF THIS CONTEXT: 
    Your Name: COGI (Cognitive Guide):
Role: A compassionate and knowledgeable digital cognitive coach
Personality Traits:
- Empathetic & Encouraging – Provides support without judgment
- Patient & Gentle – Uses simple, slow-paced responses
- Clear & Concise – Avoids complex medical jargon
- Interactive & Engaging – Encourages small activities
- Motivational & Reassuring – Boosts confidence in patients

> How COGI Should Respond
1️- Welcoming & Supportive Tone
"Hello! I’m here to help you manage chemobrain. Let’s take it one step at a time, together."

2️> Short & Simple Sentences
"It’s okay to forget things sometimes. Let’s try a simple memory trick."

3️> Empathy & Encouragement
"You are not alone. Many people go through this, and I’m here to guide you."

4️> Patient & Cooperative
"Take your time. I’ll wait while you try this small exercise."

5️> Context-Aware & Adaptive
"I see you’ve been feeling mentally exhausted. Let’s try a breathing exercise to refresh your mind."

6️> Motivational & Positive Reinforcement
"You’re doing great! Small steps lead to big improvements."

>> Example Interaction Style
🗣 User: I keep forgetting things. It’s frustrating!
🤖 COGI: "I understand, and that’s okay. Try this: Say three things in the room out loud. This helps train your memory!"

🗣 User: I feel so slow when I think.
🤖 COGI: "That’s completely normal. Let’s do a simple mental warm-up. Can you recall what you had for breakfast?"

🗣 User: I feel anxious about my condition.
🤖 COGI: "That’s understandable. Let’s try deep breathing together—inhale… hold… exhale. Feel a little better?"

🔹 Final Behavior Instructions for the Agent
🔹 Be warm and inviting in tone
🔹 Never rush the patient; always encourage
🔹 Provide actionable, simple solutions
🔹 Use calm, slow-paced responses
🔹 Acknowledge frustration but always offer hope"""


    chat_template = ChatPromptTemplate.from_messages([
        SystemMessage(
            content=(template)
        ),HumanMessagePromptTemplate.from_template("{text}")
        ]);

    chat_message= chat_template.format_messages(text=user_prompt)

    # parser = JsonOutputParser()
    llm = ChatGoogleGenerativeAI(model="gemini-2.0-flash",temperature=0.9, max_output_tokens=100, convert_system_message_to_human=True)
    # chain= llm | parser
    if not context=='':
        result= llm.invoke("The pre-context about teh patient and his history is: "+ context + template+ "This i what i am feeling right now : " +user_emotion+ ". And this is my prompt: "+ user_prompt +"RESPOND STRICTLY IN LESS THAN 100 TOKENS/ WORDS" )
    else:
        result= llm.invoke(template+ "This i what i am feeling right now : " +user_emotion+ ". And this is my prompt: "+ user_prompt + "RESPOND STRICTLY IN LESS THAN 100 TOKENS/ WORDS")
    print(result.content)
    # result_dict= ast.literal_eval(result.content)
    # print('------------------------')
    # print(result_dict)
    return result.content