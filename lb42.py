def insertion(list_nums):
    for i in range(1, len(list_nums)):
        item = list_nums[i]
        i2 = i - 1
        while i2 >= 0 and list_nums[i2] > item:
            list_nums[i2 + 1] = list_nums[i2]
            i2 -= 1
        list_nums[i2 + 1] = item

def remove_element(arr, index):
    if 0 <= index < len(arr):
        arr[index] = 0
    else:
        print("Ошибка, неверный индекс")