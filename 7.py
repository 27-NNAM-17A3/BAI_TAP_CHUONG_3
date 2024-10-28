import numpy as np

# Bước 1: Đọc dữ liệu từ tập tin baseball_2D.txt
with open('baseball_2D.txt', 'r') as f:
    baseball = [list(map(float, line.strip().split())) for line in f]

# Tạo 2D numpy array từ danh sách baseball
np_baseball = np.array(baseball)
print("Kiểu dữ liệu của np_baseball:", np_baseball.dtype)
print("Kích thước của np_baseball:", np_baseball.shape)

# Bước 2: In các giá trị của dòng thứ 50 trong np_baseball
print("\nGiá trị của dòng thứ 50 trong np_baseball:", np_baseball[49])  # Chỉ số bắt đầu từ 0

# Bước 3: Tạo numpy array np_weight với dữ liệu từ cột hai của np_baseball
np_weight = np_baseball[:, 1]
print("\nGiá trị của cột cân nặng trong np_baseball:", np_weight)

# Bước 4: Chiều cao của vận động viên thứ 124
height_of_player_124 = np_baseball[123, 0]  # Chỉ số bắt đầu từ 0
print("\nChiều cao của vận động viên thứ 124 (inch):", height_of_player_124)

# Bước 5: Chiều cao trung bình và cân nặng trung bình
mean_height = np.mean(np_baseball[:, 0])
mean_weight = np.mean(np_baseball[:, 1])
print("\nChiều cao trung bình (inch):", mean_height)
print("Cân nặng trung bình (pounds):", mean_weight)

# Bước 6: Mối tương quan giữa chiều cao và cân nặng
correlation = np.corrcoef(np_baseball[:, 0], np_baseball[:, 1])[0, 1]
print("\nMối tương quan giữa chiều cao và cân nặng:", correlation)

if correlation > 0:
    print("Có tương quan thuận giữa chiều cao và cân nặng.")
elif correlation < 0:
    print("Có tương quan nghịch giữa chiều cao và cân nặng.")
else:
    print("Không có tương quan giữa chiều cao và cân nặng.")