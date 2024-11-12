animals_list = ["dog", "cat", "mouse", "bird", "monkey", "honeyBadger",  "cheetah", "deer"]

index = 0
while (index < len(animals_list)):
    if(index == 3):
        animals_list[3] = "dog"
    print(animals_list[index])
    index += 1