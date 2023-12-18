calibrations = []
with open("input.txt", "r") as input_file:
    calibrations = input_file.readlines()[:-1]
    calibrations = [line.strip() for line in calibrations]

sum = 0
for calibration in calibrations:
    first_digit = 0
    second_digit = 0

    for c in calibration:
        if c.isdigit():
            first_digit = int(c)
            break

    for c in calibration[::-1]:
        if c.isdigit():
            second_digit = int(c)
            break

#    print(calibration, first_digit, second_digit)
    sum += first_digit * 10 + second_digit

print(sum)

numbers = ["zero","one","two","three","four","five","six","seven","eight","nine"]
digits = ["0","1","2","3","4","5","6","7","8","9"]
sum = 0

def get_first_number(s):
    first_number = ""
    first_number_index = 999

    for number in numbers:
        if (i := s.find(number)) < first_number_index and i != -1:
            first_number = number
            first_number_index = i

    return (first_number, first_number_index)

def get_last_number(s):
    last_number = ""
    last_number_index = -1

    for number in numbers:
        if (i := s.rfind(number)) > last_number_index:
            last_number = number
            last_number_index = i

    return (last_number, last_number_index)

def get_digit_positions(s):
    first_digit = ("", 999)
    for digit in digits:
        if (i := s.find(digit)) < first_digit[1] and i != -1:
            first_digit = (digit, i)

    last_digit  = ("", -1)
    for digit in digits:
        if (i := s.rfind(digit)) > last_digit[1]:
            last_digit = (digit, i)

    return (first_digit, last_digit)


for calibration in calibrations:
    print(calibration)

    first_number = get_first_number(calibration)
    last_number  = get_last_number(calibration)
    print(first_number, last_number)

    first_digit, last_digit = get_digit_positions(calibration)
    print(first_digit, last_digit)

    num_or_digit = ""

    first_value = -1
    if first_number[1] < first_digit[1]:
        first_value = numbers.index(first_number[0])
        num_or_digit = "n"
    else:
        first_value = int(first_digit[0])
        num_or_digit = "d"

    last_value = -1
    if last_number[1] > last_digit[1]:
        last_value = numbers.index(last_number[0])
        num_or_digit += "n"
    else:
        last_value = int(last_digit[0])
        num_or_digit += "d"

    print(f"{num_or_digit}: {first_value*10 + last_value}")
    sum += first_value*10 + last_value

print(sum)

