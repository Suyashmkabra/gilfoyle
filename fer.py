import cv2
from deepface import DeepFace

# Disable OpenCV optimizations for better compatibility
cv2.setUseOptimized(False)

def face_emotion_recogniton():
    # Load pre-trained face classifier
    face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

    # Initialize video capture (use index 0 for the default camera)
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open video stream")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video capture has ended")
            break

        # Convert frame to grayscale for better face detection
        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(frame_gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

        dominant_emotion = 'Unknown'

        for (x, y, w, h) in faces:
            face_region = frame[y:y+h, x:x+w]

            try:
                response = DeepFace.analyze(face_region, actions=["emotion"], enforce_detection=False)

                # Extract the dominant emotion
                dominant_emotion = response[0]['dominant_emotion']

                # Handle neutral emotion with low confidence
                if dominant_emotion == 'neutral' and response[0]['emotion']['neutral'] < 30:
                    sorted_emotions = sorted(response[0]['emotion'].items(), key=lambda x: x[1], reverse=True)
                    dominant_emotion = sorted_emotions[1][0]  # Pick the second most dominant emotion

            except Exception as e:
                print(f"Error analyzing face: {e}")
                dominant_emotion = "Error"

            # Draw a rectangle around the detected face
            cv2.rectangle(frame, (x, y), (x + w, y + h), (130, 0, 75), 1)

            # Display the detected emotion on the frame
            cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (130, 0, 75), 2)

        # Yield the processed frame (RGB format for Streamlit compatibility)
        yield cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), dominant_emotion

    cap.release()
    cv2.destroyAllWindows()
