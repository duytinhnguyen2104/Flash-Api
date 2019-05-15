## PIL: Python Imaging Library (còn gọi là Pillow) là thư viện dùng cho xử lý ảnh
from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all the faces in the image using a pre-trained convolutional neural network.
# This method is more accurate than the default HOG model, but it's slower
# unless you have an nvidia GPU and dlib compiled with CUDA extensions. But if you do,
# this will use GPU acceleration and perform well.
# See also: find_faces_in_picture.py

## face_locations: tìm kiếm các khuôn mặt có trong ảnh và trả về vị trí các bounding boxes cho từng khuôn mặt tìm được
## number_of_times_to_upsample: phóng to hình ảnh lên số lần bằng  number_of_times_to_upsample
face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=0, model="cnn")

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    ## top, right, bottom, left: vị trí các đỉnh của bounding boxes
    top, right, bottom, left = face_location
    print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))

    # You can access the actual face itself like this:
    face_image = image[top:bottom, left:right]
    ## Tạo lại object hình ảnh từ array các pixel
    pil_image = Image.fromarray(face_image)
    pil_image.show()
