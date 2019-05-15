## PIL: Python Imaging Library (còn gọi là Pillow) là thư viện dùng cho xử lý ảnh
from PIL import Image
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all the faces in the image using the default HOG-based model.
# This method is fairly accurate, but not as accurate as the CNN model and not GPU accelerated.
# See also: find_faces_in_picture_cnn.py

## face_locations: tìm kiếm các khuôn mặt có trong ảnh và trả về vị trí các bounding boxes cho từng khuôn mặt tìm được
face_locations = face_recognition.face_locations(image)

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
