import face_recognition
import cv2

# This code finds all faces in a list of images using the CNN model.
#
# This demo is for the _special case_ when you need to find faces in LOTS of images very quickly and all the images
# are the exact same size. This is common in video processing applications where you have lots of video frames
# to process.
#
# If you are processing a lot of images and using a GPU with CUDA, batch processing can be ~3x faster then processing
# single images at a time. But if you aren't using a GPU, then batch processing isn't going to be very helpful.
#
# PLEASE NOTE: This example requires OpenCV (the `cv2` library) to be installed only to read the video file.
# OpenCV is *not* required to use the face_recognition library. It's only required if you want to run this
# specific demo. If you have trouble installing it, try any of the other demos that don't require it instead.

# Open video file
video_capture = cv2.VideoCapture("short_hamilton_clip.mp4")

frames = []
frame_count = 0

while video_capture.isOpened(): ## Trả về True nếu quá trình capture đã được khởi tạo
    # Grab a single frame of video
    ## Hàm .read() trả về 1 giá trị bool 'ret' = True/False cho biết khung hình có được đọc hay không và 'frame' là array các pixel của khung hình đó
    ret, frame = video_capture.read()

    # Bail out when the video file ends
    if not ret:
        break

    # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
    frame = frame[:, :, ::-1]

    # Save each frame of the video to a list
    frame_count += 1
    frames.append(frame)

    # Every 128 frames (the default batch size), batch process the list of frames to find faces
    if len(frames) == 128:
        ## batch_face_locations: trả về array 2-dimension chứa các bounding boxes của các khuôn mặt tìm được
        ## number_of_times_to_upsample: phóng to hình ảnh lên số lần bằng  number_of_times_to_upsample
        ## batch_size: số lượng hình ảnh trong mỗi lần xử lý, default=128
        batch_of_face_locations = face_recognition.batch_face_locations(frames, number_of_times_to_upsample=0)

        # Now let's list all the faces we found in all 128 frames
        for frame_number_in_batch, face_locations in enumerate(batch_of_face_locations):
            
            ## Số lượng khuôn mặt tìm được trong hình
            number_of_faces_in_frame = len(face_locations)
          
            ## Lấy ra thứ tự của khung hình đang xét trong tổng số hình cắt được từ video
            frame_number = frame_count - 128 + frame_number_in_batch
            print("I found {} face(s) in frame #{}.".format(number_of_faces_in_frame, frame_number))

            for face_location in face_locations:
                # Print the location of each face in this frame
                ## top, right, bottom, left: vị trí các đỉnh của bounding boxes
                top, right, bottom, left = face_location
                print(" - A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

        # Clear the frames array to start the next batch
        frames = []
