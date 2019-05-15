import face_recognition

# Load the jpg files into numpy arrays
biden_image = face_recognition.load_image_file("biden.jpg")
obama_image = face_recognition.load_image_file("obama.jpg")
unknown_image = face_recognition.load_image_file("obama2.jpg")

# Get the face encodings for each face in each image file
# Since there could be more than one face in each image, it returns a list of encodings.
# But since I know each image only has one face, I only care about the first encoding in each image, so I grab index 0.
try:
    ## Hàm face_encodings(face_image, known_face_locations=None, num_jitters=1):
        ## Dùng chuyển đổi numpy array thành mảng gồm một hoặc nhiều danh sách.
        ## Mỗi danh sách tương ứng với một khuôn mặt trong ảnh và có 128 phần tử mã hóa khuôn mặt (128-dimension face encoding). Được gọi là face_encoding
    ## Input:
        ## face_image: numpy array của ảnh (ảnh có thể chứa một hoặc nhiều khuôn mặt)
        ## known_face_locations: Khung giới hạn của mỗi khuôn mặt trong trường hợp bạn đã biết trước rồi. Mặc định = None
        ## num_jitters: số lần lấy mẫu lại khi tính toán các phần từ mã hóa. Trường hợp num_jitters > 1 sẽ lấy mẫu nhiều lần, sau đó tính trung bình. Mặc định = 1
    ## Output: mảng các danh sách phần tử mã hóa khuôn mặt
    ## Do ảnh "biden.jpg" chỉ có 1 khuôn mặt nên sử dụng cú pháp [0] để lấy như bên dưới
    biden_face_encoding = face_recognition.face_encodings(biden_image)[0]
    obama_face_encoding = face_recognition.face_encodings(obama_image)[0]
    unknown_face_encoding = face_recognition.face_encodings(unknown_image)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

known_faces = [
    biden_face_encoding,
    obama_face_encoding
]

# results is an array of True/False telling if the unknown face matched anyone in the known_faces array
## Hàm compare_faces(known_face_encodings, face_encoding_to_check, tolerance=0.6):
    ## So sánh danh sách các face encoding đã biết với face encoding cần test xem chúng có khớp nhau hay không
## Input:
    ## known_face_encodings: danh sách các face encoding đã biết
    ## face_encoding_to_check: face encoding cần test
    ## tolerance: ngưỡng khoảng cách được xem là khớp. Khoảng cách giữa 2 face encodings <= ngưỡng này. tolerance = 0.6 cho hiệu suất tốt nhất.
## Output: danh sách True/False cho biết known_face_encodings khớp với face_encoding_to_check
results = face_recognition.compare_faces(known_faces, unknown_face_encoding)

print("Is the unknown face a picture of Biden? {}".format(results[0]))
print("Is the unknown face a picture of Obama? {}".format(results[1]))
print("Is the unknown face a new person that we've never seen before? {}".format(not True in results))
