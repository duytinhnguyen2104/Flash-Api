import face_recognition

# Often instead of just checking if two faces match or not (True or False), it's helpful to see how similar they are.
# You can do that by using the face_distance function.

# The model was trained in a way that faces with a distance of 0.6 or less should be a match. But if you want to
# be more strict, you can look for a smaller face distance. For example, using a 0.55 cutoff would reduce false
# positive matches at the risk of more false negatives.

# Note: This isn't exactly the same as a "percent match". The scale isn't linear. But you can assume that images with a
# smaller distance are more similar to each other than ones with a larger distance.

# Load some images to compare against
## Hàm load_image_file(file, mode='RGB'): dùng chuyển đổi ảnh (.jpg, .png, ...) thành numpy array
## Input:
    ## file: tên file ảnh
    ## mode: chỉ hỗ trợ dạng ảnh Red Green Blue 'RGB' (8-bit RGB, 3 channels) và Greyscale 'L' (black and white). Mặc định = 'RGB'
## Output: numpy array
## known_obama_image là numpy array được chuyển đổi từ ảnh "obama.jpg"
known_obama_image = face_recognition.load_image_file("obama.jpg")
known_biden_image = face_recognition.load_image_file("biden.jpg")

# Get the face encodings for the known images
## Hàm face_encodings(face_image, known_face_locations=None, num_jitters=1):
    ## Dùng chuyển đổi numpy array thành mảng gồm một hoặc nhiều danh sách.
    ## Mỗi danh sách tương ứng với một khuôn mặt trong ảnh và có 128 phần tử mã hóa khuôn mặt (128-dimension face encoding). Được gọi là face_encoding
## Input:
    ## face_image: numpy array của ảnh (ảnh có thể chứa một hoặc nhiều khuôn mặt)
    ## known_face_locations: Khung giới hạn của mỗi khuôn mặt trong trường hợp bạn đã biết trước rồi. Mặc định = None
    ## num_jitters: số lần lấy mẫu lại khi tính toán các phần từ mã hóa. Trường hợp num_jitters > 1 sẽ lấy mẫu nhiều lần, sau đó tính trung bình. Mặc định = 1
## Output: mảng các danh sách phần tử mã hóa khuôn mặt
## Do ảnh "obama.jpg" chỉ có 1 khuôn mặt nên sử dụng cú pháp [0] để lấy như bên dưới
obama_face_encoding = face_recognition.face_encodings(known_obama_image)[0]
biden_face_encoding = face_recognition.face_encodings(known_biden_image)[0]

known_encodings = [
    obama_face_encoding,
    biden_face_encoding
]

# Load a test image and get encondings for it
image_to_test = face_recognition.load_image_file("obama2.jpg")
image_to_test_encoding = face_recognition.face_encodings(image_to_test)[0]

# See how far apart the test image is from the known faces
## Hàm face_distance(face_encodings, face_to_compare): Dùng tính khoảng cách Euclid giữa face encoding của ảnh đã biết và ảnh test
## Input:
    ## face_encodings: mảng face_encoding của các ảnh đã biết
    ## face_to_compare: face_encoding của ảnh test
## Output: Mảng các khoảng cách
face_distances = face_recognition.face_distance(known_encodings, image_to_test_encoding)

for i, face_distance in enumerate(face_distances):
    print("The test image has a distance of {:.2} from known image #{}".format(face_distance, i))
    print("- With a normal cutoff of 0.6, would the test image match the known image? {}".format(face_distance < 0.6))
    print("- With a very strict cutoff of 0.5, would the test image match the known image? {}".format(face_distance < 0.5))
    print()
