## timeit: Đo thời gian thực thi các đoạn code, chạy đoạn code nhiều lần (mặc định là 1000000 lần) để thống kê ra thời gian chính xác nhất
import timeit

# Note: This example is only tested with Python 3 (not Python 2)

# This is a very simple benchmark to give you an idea of how fast each step of face recognition will run on your system.
# Notice that face detection gets very slow at large image sizes. So you might consider running face detection on a
# scaled down version of your image and then running face encodings on the the full size image.

TEST_IMAGES = [
    "obama-240p.jpg",
    "obama-480p.jpg",
    "obama-720p.jpg",
    "obama-1080p.jpg"
]


def run_test(setup, test, iterations_per_test=5, tests_to_run=10):
    ## timeit.Timer().repeat(): tính tốc độ thực thi của đoạn code với thời gian chạy 'setup' 1 lần duy nhất và thời gian chạy 'test' sau khi setup là 'iterations_per_test' lần cho mỗi lần test (tổng số lần test là 'tests_to_run')
    ## min(): lấy thời gian chạy nhanh nhất
    fastest_execution = min(timeit.Timer(test, setup=setup).repeat(tests_to_run, iterations_per_test))
    ## Tính thời gian chạy 1 lần test bằng cách chia cho số lần chạy (iterations_per_test) của mỗi 1 lần test
    execution_time = fastest_execution / iterations_per_test
    ## Tính số lượng khung hình chạy được trong 1 giây
    fps = 1.0 / execution_time
    return execution_time, fps

## Truyền chuỗi gọi hàm load hình ảnh, trả về numpy array các pixel
setup_locate_faces = """
import face_recognition

image = face_recognition.load_image_file("{}")
"""

## Truyền chuỗi gọi hàm 'face_locations' tìm kiếm mặt người có trong ảnh ( trả về array chứa các bounding boxes)
test_locate_faces = """
face_locations = face_recognition.face_locations(image)
"""

## Truyền chuỗi gọi hàm load hình ảnh, trả về numpy array các pixel
## Truyền chuỗi gọi hàm 'face_locations' tìm kiếm mặt người có trong ảnh ( trả về array chứa các vị trí của bounding boxes)
setup_face_landmarks = """
import face_recognition

image = face_recognition.load_image_file("{}")
face_locations = face_recognition.face_locations(image)
"""

## Truyền chuỗi gọi hàm 'face_landmarks' để tìm tất cả các features có trên khuôn mặt (mắt, mũi, ...) trong trường hợp đã tìm được face_locations
test_face_landmarks = """
landmarks = face_recognition.face_landmarks(image, face_locations=face_locations)[0]
"""

## Truyền chuỗi gọi hàm load hình ảnh, trả về numpy array các pixel
## Truyền chuỗi gọi hàm 'face_locations' tìm kiếm mặt người có trong ảnh ( trả về array chứa các bounding boxes)
setup_encode_face = """
import face_recognition

image = face_recognition.load_image_file("{}")
face_locations = face_recognition.face_locations(image)
"""

## Truyền chuỗi gọi hàm 'face_encodings' trả về mỗi array 128-dimension encoding cho mỗi khuôn mặt trong trường hợp đã biết face_locations
test_encode_face = """
encoding = face_recognition.face_encodings(image, known_face_locations=face_locations)[0]
"""

## Truyền chuỗi gọi hàm load hình ảnh, trả về numpy array các pixel
setup_end_to_end = """
import face_recognition

image = face_recognition.load_image_file("{}")
"""

## Truyền chuỗi gọi hàm 'face_encodings' trả về array 128-dimension encoding cho mỗi khuôn mặt
test_end_to_end = """
encoding = face_recognition.face_encodings(image)[0]
"""

print("Benchmarks (Note: All benchmarks are only using a single CPU core)")
print()

## Tính toán thời gian thực thi test cho mỗi size ảnh khác nhau
for image in TEST_IMAGES:
    ## Lấy ra kích thước ảnh trong tên file 
    size = image.split("-")[1].split(".")[0]
    print("Timings at {}:".format(size))
    
    ## Gọi hàm run_test để tính thời gian thực thi cho mỗi loại test
    print(" - Face locations: {:.4f}s ({:.2f} fps)".format(*run_test(setup_locate_faces.format(image), test_locate_faces)))
    print(" - Face landmarks: {:.4f}s ({:.2f} fps)".format(*run_test(setup_face_landmarks.format(image), test_face_landmarks)))
    print(" - Encode face (inc. landmarks): {:.4f}s ({:.2f} fps)".format(*run_test(setup_encode_face.format(image), test_encode_face)))
    print(" - End-to-end: {:.4f}s ({:.2f} fps)".format(*run_test(setup_end_to_end.format(image), test_end_to_end)))
    print()
