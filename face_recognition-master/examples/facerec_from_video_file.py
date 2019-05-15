import face_recognition
import cv2

# This is a demo of running face recognition on a video file and saving the results to a new video file.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open the input movie file
input_movie = cv2.VideoCapture("hamilton_clip.mp4")

## Lấy ra số lượng khung hình chụp được từ video
length = int(input_movie.get(cv2.CAP_PROP_FRAME_COUNT))

# Create an output movie file (make sure resolution/frame rate matches input video!)
## FourCC is a 4-byte code used to specify the video codec
fourcc = cv2.VideoWriter_fourcc(*'XVID')
## cv2.VideoWriter(output_file_name, FourCC code, number_of_frames_per_second(fps), frame size)
output_movie = cv2.VideoWriter('output.avi', fourcc, 29.97, (640, 360))

# Load some sample pictures and learn how to recognize them.
## Hàm 'face_encodings' trả về mỗi array 128-dimension encoding cho mỗi khuôn mặt.
lmm_image = face_recognition.load_image_file("lin-manuel-miranda.png")
lmm_face_encoding = face_recognition.face_encodings(lmm_image)[0]

al_image = face_recognition.load_image_file("alex-lacamoire.png")
al_face_encoding = face_recognition.face_encodings(al_image)[0]

## List các khuôn mặt đã được encoding
known_faces = [
    lmm_face_encoding,
    al_face_encoding
]

# Initialize some variables
face_locations = []
face_encodings = []
face_names = []
frame_number = 0

while True:
    # Grab a single frame of video
    ## Hàm .read() trả về 1 giá trị bool 'ret' = True/False cho biết khung hình có được đọc hay không và 'frame' là array các pixel của khung hình đó
    ret, frame = input_movie.read()
    frame_number += 1

    # Quit when the input video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    rgb_frame = frame[:, :, ::-1]

    # Find all the faces and face encodings in the current frame of video
    ## face_locations: tìm kiếm các khuôn mặt có trong ảnh và trả về vị trí các bounding boxes
    face_locations = face_recognition.face_locations(rgb_frame)
    ## face_encodings: trả về mỗi array 128-dimension encoding cho mỗi khuôn mặt, trong trường hợp đã biết face_locations
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    face_names = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        ## Tính khoảng cách (độ khác nhau) giữa khuôn mặt đã biết với khuôn mặt tìm được trong khung hình, với ngưỡng <= tolerance được xem là cùng 1 người
        ## compare_faces: trả về giá trị True hoặc False
        match = face_recognition.compare_faces(known_faces, face_encoding, tolerance=0.50)

        # If you had more than 2 faces, you could make this logic a lot prettier
        # but I kept it simple for the demo
        name = None
        if match[0]:
            name = "Lin-Manuel Miranda"
        elif match[1]:
            name = "Alex Lacamoire"

        face_names.append(name)

    # Label the results
    ## (top, right, bottom, left): tọa độ 4 điểm của bounding boxes
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        if not name:
            continue

        # Draw a box around the face
        ## cv2.rectangle(image, tọa_độ_đỉnh, tọa_độ_đỉnh_đối_diện, color, thickness)
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Draw a label with a name below the face
        cv2.rectangle(frame, (left, bottom - 25), (right, bottom), (0, 0, 255), cv2.FILLED)
        font = cv2.FONT_HERSHEY_DUPLEX
        ## Hiển thị chữ trong hình ảnh
        ## cv2.putText(image, text, bottom-left_corner_of_text, font_style, font_scale, color, thickness)
        cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.5, (255, 255, 255), 1)

    # Write the resulting image to the output video file
    print("Writing frame {} / {}".format(frame_number, length))
    output_movie.write(frame)

# All done!
## close video file
input_movie.release()
## Đóng tất cả các cửa sổ đã tạo
cv2.destroyAllWindows()
