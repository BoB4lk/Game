import random as rd

numbers = 0
while numbers < 1 :  # Компьютер загадывает четырехзначное число, все цифры которого различны
                     # (первая цифра числа отлична от нуля)
    nums1 = list(range(0,10))
    nums1 = rd.sample(nums1,4)
    if nums1[0] != 0:
        numbers += 1
        nums1 = list(map(str,nums1))


def check_number():  #проверить_число
    nums = nums1
    user = input("Введите 4х значное число: ")
    user = list(user)
    global bulls
    bulls = 0
    cows = 0
    if nums[0] == user[0]:
        bulls += 1
    if nums[1] == user[1]:
        bulls += 1
    if nums[2] == user[2]:
        bulls += 1
    if nums[3] == user[3]:
        bulls += 1

    for i in nums:
        for a in user:
            if a == i:
                cows += 1

    cows -= bulls
    print("Быки - {}".format(bulls),",","Коровы - {}".format(cows))
    return bulls


def bul():
    return (bulls)
