import cv2
from deepface import DeepFace


def face_emotion_recogniton():
    face_classifier = cv2.CascadeClassifier()
    face_classifier.load(cv2.samples.findFile('haarcascade_frontalface_default.xml'))

    cap = cv2.VideoCapture(0)
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Video capture has ended")
            break

        frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(frame_gray)
        dominant_emotion=''
        for face in faces:
            x, y, w, h = face
            face_region = frame[y:y+h, x:x+w]
            response = DeepFace.analyze(face_region, actions=("emotion"), enforce_detection=False)
            # print(response[0])
            
            dominant_emotion=response[0]['dominant_emotion']

            if dominant_emotion=='neutral' and response[0]['emotion']['neutral']<30:
                sorted_dict = sorted(response[0]['emotion'].items(), key=lambda x: x[1], reverse=True)
                dominant_emotion= sorted_dict[1][0]


            cv2.rectangle(frame, (x, y), (x+w, y+h), (130, 0, 75), 1)
            cv2.putText(frame, dominant_emotion, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (130, 0, 75), 1)

            # print(dominant_emotion +" || "+ response[0]['dominant_emotion'])

        yield cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), dominant_emotion

    cap.release()
    cv2.destroyAllWindows()

