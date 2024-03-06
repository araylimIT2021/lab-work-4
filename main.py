import random as rand

phoneNumber_duration = dict()

with open("lab4_data.txt", 'r') as file:
    lines = file.readlines()

    for line in lines:
        phone_number_1, phone_number_2, call_duration, date, time = line.split(" ")
        call_duration = int(call_duration)

        if phone_number_1 not in phoneNumber_duration:
            phoneNumber_duration[phone_number_1] = 0

        if phone_number_2 not in phoneNumber_duration:
            phoneNumber_duration[phone_number_2] = 0

        phoneNumber_duration[phone_number_1] += call_duration
        phoneNumber_duration[phone_number_2] += call_duration

with open('output.txt', 'w') as f:
    for phone_number, call_duration in phoneNumber_duration.items():
        f.write(str(f"{phone_number} {call_duration} \n"))

