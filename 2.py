import numpy as np


arr = np.arange(10)
print("Array ban đầu (arr):", arr)
print("Kiểu dữ liệu của arr:", arr.dtype)
print("Kích thước của arr:", arr.shape)

arr_odd = arr[arr % 2 != 0]  
arr_even = arr[arr % 2 == 0]  
print("Các phần tử lẻ (arr_odd):", arr_odd)
print("Các phần tử chẵn (arr_even):", arr_even)

arr_update_1 = np.where(arr % 2 == 0, arr, -1)  
print("Array sau khi cập nhật (arr_update_1):", arr_update_1)