import face_recognition
from PIL import Image, ImageDraw

# This is an example of running face recognition on a single image
# and drawing a box around each person that was identified.

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

# Create arrays of known face encodings and their names
known_face_encodings = [
    obama_face_encoding,
    biden_face_encoding
]
known_face_names = [
    "Barack Obama",
    "Joe Biden"
]

# Load an image with an unknown face
unknown_image = face_recognition.load_image_file("two_people.jpg")

# Find all the faces and face encodings in the unknown image
## Hàm face_locations(img, number_of_times_to_upsample=1, model="hog"):
    ## Xác định khung giới hạn của tất cả khuôn mặt trong ảnh
## Input:
    ## img: numpy array của ảnh
    ## number_of_times_to_upsample: số lần upsample ảnh để tìm kiếm khuôn mặt. Số lần lớn sẽ tìm kiếm được nhiều khuôn mặt nhỏ nhưng tốn nhiều chi phí xử lý. Mặc định = 1
                ## (Upsample ảnh là thực hiện tăng kích thước của ảnh theo một tỷ lệ nào đó. Khi đó, ta có thể phát hiện được những khuôn mặt nhỏ do ở xa, ...)
    ## model: mô hình nhận dạng khuôn mặt để sử dụng. Các mô hình có thể sử dụng "hog" (ít chính xác, chạy nhanh trên CPUs) và "cnn" (chính xác hơn "hog" nhưng cần GPU/CUDA để tăng tốc độ)
## Output: danh sách các face locations (top, right, bottom, left)
face_locations = face_recognition.face_locations(unknown_image)
face_encodings = face_recognition.face_encodings(unknown_image, face_locations)

# Convert the image to a PIL-format image so that we can draw on top of it with the Pillow library
# See http://pillow.readthedocs.io/ for more about PIL/Pillow
pil_image = Image.fromarray(unknown_image)
# Create a Pillow ImageDraw Draw instance to draw with
draw = ImageDraw.Draw(pil_image)

# Loop through each face found in the unknown image
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

    # Draw a box around the face using the Pillow module
    draw.rectangle(((left, top), (right, bottom)), outline=(0, 0, 255))

    # Draw a label with a name below the face
    text_width, text_height = draw.textsize(name)
    draw.rectangle(((left, bottom - text_height - 10), (right, bottom)), fill=(0, 0, 255), outline=(0, 0, 255))
    draw.text((left + 6, bottom - text_height - 5), name, fill=(255, 255, 255, 255))


# Remove the drawing library from memory as per the Pillow docs
del draw

# Display the resulting image
pil_image.show()

# You can also save a copy of the new image to disk if you want by uncommenting this line
# pil_image.save("image_with_boxes.jpg")
