import face_recognition
import cv2

# This is a super simple (but slow) example of running face recognition on live video from your webcam.
# There's a second example that's a little more complicated but runs faster.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Load a sample picture and learn how to recognize it.
## Hàm load_image_file(file, mode='RGB'): dùng chuyển đổi ảnh (.jpg, .png, ...) thành numpy array
## Input:
    ## file: tên file ảnh
    ## mode: chỉ hỗ trợ dạng ảnh Red Green Blue 'RGB' (8-bit RGB, 3 channels) và Greyscale 'L' (black and white). Mặc định = 'RGB'
## Output: numpy array
obama_image = face_recognition.load_image_file("obama.jpg")
## Hàm face_encodings(face_image, known_face_locations=None, num_jitters=1):
    ## Dùng chuyển đổi numpy array thành mảng gồm một hoặc nhiều danh sách.
    ## Mỗi danh sách tương ứng với một khuôn mặt trong ảnh và có 128 phần tử mã hóa khuôn mặt (128-dimension face encoding). Được gọi là face_encoding
## Input:
    ## face_image: numpy array của ảnh (ảnh có thể chứa một hoặc nhiều khuôn mặt)
    ## known_face_locations: Khung giới hạn của mỗi khuôn mặt trong trường hợp bạn đã biết trước rồi. Mặc định = None
    ## num_jitters: số lần lấy mẫu lại khi tính toán các phần từ mã hóa. Trường hợp num_jitters > 1 sẽ lấy mẫu nhiều lần, sau đó tính trung bình. Mặc định = 1
## Output: mảng các danh sách phần tử mã hóa khuôn mặt
## Do ảnh "obama.jpg" chỉ có 1 khuôn mặt nên sử dụng cú pháp [0] để lấy như bên dưới
obama_face_encoding = face_recognition.face_encodings(obama_image)[0]

# Load a second sample picture and learn how to recognize it.
biden_image = face_recognition.load_image_file("biden.jpg")
biden_face_encoding = face_recognition.face_encodings(biden_image)[0]

trungdv_image = face_recognition.load_image_file("trungdv.jpg")
trungdv_face_encoding = face_recognition.face_encodings(trungdv_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding,
    trungdv_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden",
    "Vinh Trung"
]

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face enqcodings in the frame of video
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop through each face in this frame of video
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # See if the face is a match for the known face(s)
        ## Hàm compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
            ## So sánh danh sách các face encoding đã biết với face encoding cần test xem chúng có khớp nhau hay không
        ## Input:
            ## known_face_encodings: danh sách các face encoding đã biết
            ## face_encoding_to_check: face encoding cần test
            ## tolerance: ngưỡng khoảng cách được xem là khớp. Khoảng cách giữa 2 face encodings <= ngưỡng này. tolerance = 0.6 cho hiệu suất tốt nhất.
        ## Output: danh sách True/False cho biết known_face_encodings khớp với face_encoding_to_check
        matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

        name = "Unknown"

        # If a match was found in known_face_encodings, just use the first one.
        if True in matches:
            first_match_index = matches.index(True)
            name = known_face_names[first_match_index]

        # Draw a box around the face
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
