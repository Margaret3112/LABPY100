numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
new1=numbers[:4]
new2=numbers[5:]
itog = sum(new1) + sum(new2)

sr = itog/len(numbers)
numbers[4]=sr

print("Измененный список:", numbers)
