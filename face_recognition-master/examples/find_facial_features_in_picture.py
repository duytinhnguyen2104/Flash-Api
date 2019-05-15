## PIL: Python Imaging Library (còn gọi là Pillow) là thư viện dùng cho xử lý ảnh
from PIL import Image, ImageDraw
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("two_people_1.jpg")

# Find all facial features in all the faces in the image
## face_landmarks: tìm kiếm tất cả các đặc trưng có trên khuôn mặt như mắt, mũi, miệng, ... và trả về một list chứa những dict(), với mỗi dict() chứa vị trí của các đặc trưng tìm được trên mỗi khuôn mặt
face_landmarks_list = face_recognition.face_landmarks(image)

print("I found {} face(s) in this photograph.".format(len(face_landmarks_list)))

# Create a PIL imagedraw object so we can draw on the picture
## Tạo object hình ảnh từ array các pixel
pil_image = Image.fromarray(image)

## Tạo draw object để vẽ lên hình ảnh 'pil_image'
d = ImageDraw.Draw(pil_image)

## Lặp trên mỗi dict() các đặc trưng của từng khuôn mặt
for face_landmarks in face_landmarks_list:

    ## Lặp trên mỗi đặc trưng của 1 dict()
    # Print the location of each facial feature in this image
    for facial_feature in face_landmarks.keys():
        print("The {} in this face has the following points: {}".format(facial_feature, face_landmarks[facial_feature]))

    # Let's trace out each facial feature in the image with a line!
    for facial_feature in face_landmarks.keys():
        ## line(): hàm vẽ đường thẳng giữa các vị trí trong list được truyền vào
        ## width: độ dày của đường
        d.line(face_landmarks[facial_feature], width=5)

# Show the picture
pil_image.show()
