## PIL: Python Imaging Library (còn gọi là Pillow) là thư viện dùng cho xử lý ảnh
from PIL import Image, ImageDraw 
import face_recognition

# Load the jpg file into a numpy array
image = face_recognition.load_image_file("biden.jpg")

# Find all facial features in all the faces in the image
## face_landmarks: tìm kiếm tất cả các đặc trưng có trên khuôn mặt như mắt, mũi, miệng, ... và trả về một list chứa những dict(), với mỗi dict() chứa vị trí của các đặc trưng tìm được trên mỗi khuôn mặt
face_landmarks_list = face_recognition.face_landmarks(image)

for face_landmarks in face_landmarks_list:
    ## Tạo object hình ảnh từ mảng các pixel
    pil_image = Image.fromarray(image)
    ## Tạo draw object để vẽ lên hình ảnh 'pil_image' với mode màu để vẽ là 'RGBA'
    d = ImageDraw.Draw(pil_image, 'RGBA')

    ## polygon(): hàm phác thảo đa giác giữa các vị trí trong list được truyền vào
    ## line(): hàm vẽ đường thẳng giữa các vị trí trong list được truyền vào
    ## fill: 4 màu cho 4 channels RGBA
    ## width: độ dày của đường
    # Make the eyebrows into a nightmare
    d.polygon(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 128)) 
    d.polygon(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 128))
    d.line(face_landmarks['left_eyebrow'], fill=(68, 54, 39, 150), width=5) 
    d.line(face_landmarks['right_eyebrow'], fill=(68, 54, 39, 150), width=5)

    # Gloss the lips
    d.polygon(face_landmarks['top_lip'], fill=(150, 0, 0, 128))
    d.polygon(face_landmarks['bottom_lip'], fill=(150, 0, 0, 128))
    d.line(face_landmarks['top_lip'], fill=(150, 0, 0, 64), width=8)
    d.line(face_landmarks['bottom_lip'], fill=(150, 0, 0, 64), width=8)

    # Sparkle the eyes
    d.polygon(face_landmarks['left_eye'], fill=(255, 255, 255, 30))
    d.polygon(face_landmarks['right_eye'], fill=(255, 255, 255, 30))

    # Apply some eyeliner
    d.line(face_landmarks['left_eye'] + [face_landmarks['left_eye'][0]], fill=(0, 0, 0, 110), width=6)
    d.line(face_landmarks['right_eye'] + [face_landmarks['right_eye'][0]], fill=(0, 0, 0, 110), width=6)

    pil_image.show()
