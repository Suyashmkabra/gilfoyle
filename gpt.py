import streamlit as st
from stt_speechTtext import record_text
from geimini import generate_response
import pyttsx3
from fer import face_emotion_recogniton
import webbrowser
import os

# speaker for text to speech section
speaker =None


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
    st.text("Generating response...")
    response_total = generate_response(query,user_emotion=user_emotion)
    response_given =response_total['text']
    st.write("Response:", response_given)
    Speak(response_given)


st.title("Son of Gilfoyle, CAI assistant")


recording = False
session_state = st.session_state
if not hasattr(session_state, "user_speech"):
    session_state.user_speech = ""

query=''

user_emotion_string=''
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
    user_emotion_string='I am happy right now!'




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

# Generate response
# if not recording and session_state.user_speech:
#     st.write("Generating response...")
#     response_total = generate_response(session_state.user_speech)
#     response_given=response_total['text']
#     st.write("Response:", response_given)
#     # speaker.say(response_given)
#     Speak(response_given)


# import streamlit as st
# from stt_speechTtext import record_text
# from geimini import generate_response
# import pyttsx3
# from fer import face_emotion_recogniton
# import threading

# # Initialize the text-to-speech engine globally
# speaker = None
# emotion_frames=[]
# emotion=[]
# session_state= st.session_state
# close_fr=False
# recording = False
# def init_speaker():
#     global speaker
#     if speaker is None:
#         speaker = pyttsx3.init()

# def Speak(text):
#     init_speaker()
#     speaker.say(text)
#     speaker.runAndWait()

# # Function to run emotion detection in a separate thread
# def run_emotion_detection():
#     global emotion_frames
#     global emotion
#     emotion_frames = []
#     emotion = []
#     frame_gen = face_emotion_recogniton()
#     for frame, emo in frame_gen:
#         emotion_frames.append(frame)
#         emotion.append(emo)

# # Function to display emotion frames in Streamlit
# def display_emotion_frames():
#     global emotion_frames
#     frame_gen= st.empty()
#     for frame in emotion_frames:
#         frame_gen.image(frame, channels='RGB')

# # Function to get user emotion string based on detected emotion
# def get_user_emotion_string():
#     global emotion
#     for cur_emotion in emotion:
#         if cur_emotion == 'happy':
#             return 'I am feeling very happy right now!'
#         elif cur_emotion == 'angry':
#             return 'I am feeling very angry right now!'
#         elif cur_emotion == 'fear':
#             return 'I am feeling scared right now!'
#         elif cur_emotion == 'sad':
#             return 'I am feeling very sad right now!'
#         else:
#             return 'I am happy right now!'

# # Function to run the main part of the Streamlit app

# def run_main():
#     global recording, emotion_frames, close_fr
#     user_emotion_string=''

#     st.title("Son of Gilfoyle, CAI assistant")
#     global session_state
#     if not hasattr(session_state, "user_speech"):
#         session_state.user_speech = ""

#     start_button_pressed = st.button('Start the emotion detection')
#     if start_button_pressed:
#         close_fr = False
#         thread = threading.Thread(target=run_emotion_detection)
#         thread.start()
        
#     display_emotion_frames()
#     user_emotion_string = get_user_emotion_string()

#     if close_fr and user_emotion_string=='' :
#         user_emotion_string = ''


#     if not recording:
#         if st.button('Start recording', key='1'):
#             recording = True
#     if recording:
#         if st.button('Stop recording', key='2'):
#             recording=False

#     # User speech input
#     if recording:
#         st.write("Recording...")
#         session_state.user_speech = record_text(True)
#         st.write(session_state.user_speech)
#     else:
#         st.write("You said:", session_state.user_speech)

#     session_state.user_input = st.text_input('Enter text input:', '')

#     # Generate response and speak it
#     run_generate(user_emotion=user_emotion_string)


# def run_generate(user_emotion):
#     global session_state
#     if not recording and session_state.user_speech:
#         st.write("Generating response...")
#         response_total = generate_response(session_state.user_speech, user_emotion=user_emotion)
#         response_given = response_total['text']
#         st.write("Response:", response_given)
#         Speak(response_given)

#     elif session_state.user_input:
#         st.write("Generating response...")
#         response_total = generate_response(session_state.user_input, user_emotion=user_emotion)
#         response_given = response_total['text']
#         st.write("Response:", response_given)
#         Speak(response_given)

# run_main()
