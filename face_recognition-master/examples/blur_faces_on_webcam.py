import face_recognition
import cv2

# This is a demo of blurring faces in video.

# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read from your webcam.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Get a reference to webcam #0 (the default one)
video_capture = cv2.VideoCapture(0)

# Initialize some variables
face_locations = []

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()

    # Resize frame of video to 1/4 size for faster face detection processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

    # Find all the faces and face encodings in the current frame of video
    # Hàm face_locations(img, number_of_times_to_upsample=1, model="hog"):
    ## Xác định khung giới hạn của tất cả khuôn mặt trong ảnh
    ## Input:
        ## img: numpy array của ảnh
        ## number_of_times_to_upsample: số lần upsample ảnh để tìm kiếm khuôn mặt. Số lần lớn sẽ tìm kiếm được nhiều khuôn mặt nhỏ nhưng tốn nhiều chi phí xử lý. Mặc định = 1
                    ## (Upsample ảnh là thực hiện tăng kích thước của ảnh theo một tỷ lệ nào đó. Khi đó, ta có thể phát hiện được những khuôn mặt nhỏ do ở xa, ...)
        ## model: mô hình nhận dạng khuôn mặt để sử dụng. Các mô hình có thể sử dụng "hog" (ít chính xác, chạy nhanh trên CPUs) và "cnn" (chính xác hơn "hog" nhưng cần GPU/CUDA để tăng tốc độ)
    ## Output: danh sách các face locations (top, right, bottom, left)
    face_locations = face_recognition.face_locations(small_frame, model="cnn")

    # Display the results
    for top, right, bottom, left in face_locations:
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4

        # Extract the region of the image that contains the face
        face_image = frame[top:bottom, left:right]

        # Blur the face image
        face_image = cv2.GaussianBlur(face_image, (99, 99), 30)

        # Put the blurred face region back into the frame image
        frame[top:bottom, left:right] = face_image

    # Display the resulting image
    cv2.imshow('Video', frame)

    # Hit 'q' on the keyboard to quit!
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release handle to the webcam
video_capture.release()
cv2.destroyAllWindows()
