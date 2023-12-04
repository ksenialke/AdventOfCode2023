with open('input.txt') as f:
    lines = f.readlines()

total_sum = 0
remove_these = " "

for line in lines:
    points = 0
    count = 0
    numbers = line.split(":")[1]

    lucky_numbers = numbers.split("|")[0]
    draw_numbers = numbers.split("|")[1]

    lucky_numbers_list = lucky_numbers.split(remove_these)
    draw_numbers_list = draw_numbers.split(remove_these)

    while("" in lucky_numbers_list):
        lucky_numbers_list.remove("")
    while("" in draw_numbers_list):
        draw_numbers_list.remove("")

    modified_draw_list = [element.replace("\n", '') for element in draw_numbers_list]

    for element in lucky_numbers_list:
        if element in modified_draw_list:
            count += 1

    if count != 0:
        if count == 1:
            points = 1
        else:
            points = 2**(count-1)
        total_sum += points

print(total_sum)