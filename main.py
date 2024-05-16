import streamlit as st
from stt_speechTtext import record_text
from geimini import generate_response
import pyttsx3
from fer import face_emotion_recogniton
import webbrowser
import os
# speaker for text to speech section
speaker =None

previous_response="Empty"
previous_prompt="Empty"

def init_speaker():
    global speaker
    if speaker is None:
        speaker = pyttsx3.init()

def Speak(text):
    init_speaker()
    speaker.startLoop(False)
    speaker.say(text)
    speaker.iterate()
    speaker.stop()
    speaker.endLoop()

# sectio for llm setup for generating reponse
def run_generate(user_emotion):
    # if not recording and session_state.user_speech:
    #     st.write("Generating response...")
    #     response_total = generate_response(session_state.user_speech,user_emotion=user_emotion)
    #     response_given =response_total['text']
    #     previous_prompt=
    #     st.write("Response:", response_given)
    #     Speak(response_given)

    # elif session_state.user_input:
    #     st.write("Generating response...")
    #     response_total = generate_response(session_state.user_input,user_emotion=user_emotion)
    #     response_given =response_total['text']
    #     st.write("Response:", response_given)
    #     Speak(response_given)
    st.write("Generating response...")
    global previous_prompt, previous_response
    response_total = generate_response(query,user_emotion=user_emotion,previous_prompt=previous_prompt, previous_response=previous_response)
    response_given =response_total['text']
    previous_prompt=query
    previous_response=response_given
    print(previous_response,previous_prompt)
    st.write("Response:", response_given)
    Speak(response_given)
    

st.title("Son of Gilfoyle, CAI assistant")


recording = False
session_state = st.session_state
if not hasattr(session_state, "user_speech"):
    session_state.user_speech = ""


user_emotion_string='I am smiling right now!'
close_fr=False

start_button_pressed= st.button('Start the emotion detection')
emotion='neutral'
if start_button_pressed:
    if st.button('move to guilfoyle'):
        close_fr=True
    frame_holder= st.empty()
    frame_gen= face_emotion_recogniton()
    for frame, current_emotion in frame_gen:
        frame_holder.image(frame,channels=('RGB'))
        emotion= current_emotion
        if close_fr:
            break

if emotion=='happy':
    user_emotion_string='I am feeling very happy right now! '
elif emotion=='angry':
    user_emotion_string='i am feeling very angry right now! '
elif emotion=='fear':
    user_emotion_string== "I am feeling scared right now! "
elif emotion=='sad':
    user_emotion_string== "I am feeling very sad right now! "
else:
    user_emotion_string='i am feeling happy'



if not recording:
    if st.button('start recording', key='1'):
        recording = True
if recording:
    if st.button('stop recording', key='2'):
        session_state.user_speech = record_text(False)

# user speech
if recording:
    st.write("Recording...")
    session_state.user_speech = record_text(True)
    st.write(session_state.user_speech)
else:
    st.write("You said:", session_state.user_speech)


session_state.user_input = st.text_input('Enter text input:', '')

if session_state.user_speech:
    query=session_state.user_speech
elif session_state.user_input:
    query=session_state.user_input
else:
    query=''
print("user query :" + query)
print("user emotion"+user_emotion_string)

if not query=='':
    if query.startswith('activate'):
        if "open youtube" in query:
            webbrowser.open_new("youtube.com")
        elif "open google" in query:
            webbrowser.open_new("google.com")
        elif 'song'in query:
            music_dir= r'E:\new videos\suyash mumbai\songs'
            # print(os.listdir(music_dir))
            os.startfile(os.path.join(music_dir,'birthday.mp3'))
        elif 'code' in query:
            code_dir= r"C:\Users\HP\AppData\Local\Programs\Microsoft VS Code"
            os.startfile(code_dir)
            
        print(query , user_emotion_string)
    else:
        run_generate(user_emotion=user_emotion_string)

elif not user_emotion_string=='':
    run_generate(user_emotion=user_emotion_string)
# run_generate(user_emotion=user_emotion_string)

# Generate response
# if not recording and session_state.user_speech:
#     st.write("Generating response...")
#     response_total = generate_response(session_state.user_speech)
#     response_given=response_total['text']
#     st.write("Response:", response_given)
#     # speaker.say(response_given)
#     Speak(response_given)