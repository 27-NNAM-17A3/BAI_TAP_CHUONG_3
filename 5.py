import numpy as np

with open('heights_1.txt', 'r') as f:
    height = [float(line.strip()) for line in f]

with open('weights_1.txt', 'r') as f:
    weight = [float(line.strip()) for line in f]

# Câu 1: Tạo numpy array arr_height từ list height
arr_height = np.array(height)
print("Array arr_height:", arr_height)

# Câu 2: Tạo numpy array arr_weight từ list weight
arr_weight = np.array(weight)
print("Array arr_weight:", arr_weight)

# Câu 3: Tạo arr_height_m bằng cách chuyển đổi chiều cao từ inch sang mét
conversion_factor_inch_to_m = 0.0254
arr_height_m = arr_height * conversion_factor_inch_to_m
print("Array arr_height_m (m):", arr_height_m)

# Câu 4: Tạo arr_weight_kg bằng cách chuyển đổi cân nặng từ pound sang kg
conversion_factor_pound_to_kg = 0.453592
arr_weight_kg = arr_weight * conversion_factor_pound_to_kg
print("Array arr_weight_kg (kg):", arr_weight_kg)

# Câu 5: Tính BMI
arr_bmi = arr_weight_kg / (arr_height_m ** 2)
print("Array arr_bmi:", arr_bmi)

# Câu 6: Cân nặng tại vị trí index = 50 trong arr_weight_kg
weight_at_index_50 = arr_weight_kg[50]
print("Cân nặng tại index 50 (kg):", weight_at_index_50)

# Câu 7: Tạo arr_height_m_100 từ arr_height_m với các phần tử từ index 100 đến 110
arr_height_m_100 = arr_height_m[100:111]
print("Array arr_height_m_100 (index 100-110):", arr_height_m_100)

# Câu 8: Các cầu thủ có bmi < 21 trong arr_bmi
players_bmi_under_21 = arr_bmi[arr_bmi < 21]
print("Cầu thủ có BMI < 21:", players_bmi_under_21)

# Câu 9: Chiều cao trung bình và cân nặng trung bình của các cầu thủ
mean_height = np.mean(arr_height_m)
mean_weight = np.mean(arr_weight_kg)
print("Chiều cao trung bình (m):", mean_height)
print("Cân nặng trung bình (kg):", mean_weight)

# Câu 10: Chiều cao và cân nặng lớn nhất của các cầu thủ
max_height = np.max(arr_height_m)
max_weight = np.max(arr_weight_kg)
print("Chiều cao lớn nhất (m):", max_height)
print("Cân nặng lớn nhất (kg):", max_weight)

# Câu 11: Chiều cao và cân nặng nhỏ nhất của các cầu thủ
min_height = np.min(arr_height_m)
min_weight = np.min(arr_weight_kg)
print("Chiều cao nhỏ nhất (m):", min_height)
print("Cân nặng nhỏ nhất (kg):", min_weight)