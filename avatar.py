# import sda
# import scipy.io.wavfile as wav
# from PIL import Image
# import pyttsx3
# import io

# # Initialize the text-to-speech engine
# engine = pyttsx3.init()

# # Function to convert text to speech and save as a .wav file
# def text_to_speech(text):
#     audio_stream= io.BytesIO()
#     engine.save_to_file(text, audio_stream)
#     engine.runAndWait()
#     audio_stream.seek(0)
#     return audio_stream

# # Instantiate the animator
# va = sda.VideoAnimator(gpu=-1,model_path='crema')

# # Real-time speech input (replace this with your own speech input mechanism)
# speech_text = "Hello, how are you?"

# # Convert speech to audio and save as a .wav file
# audio_stream=text_to_speech(speech_text)

# # Load still frame image
# still_frame = Image.open("assets\suyash.bmp")

# # Load audio clip
# # fs, audio_clip = wav.read(audio_output_file)

# # Generate video using the talking head model
# vid, aud = va(still_frame, audio_stream)

# # Display or save the generated video (vid)
# va.save_video(vid,aud,"avatar_vids/generated.mp4")