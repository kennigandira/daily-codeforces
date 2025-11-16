n = int(input())

ui = "1234567890"

for i in range(n):
    pin_set = input()
    seconds = 0
    last_cursor_index = 0

    for pin_index in range(len(pin_set)):
        curr_pin = pin_set[pin_index]
        diff = 0
        if(curr_pin == ui[last_cursor_index]):
            seconds += 1
        else:
            if(curr_pin == "0"):
                if(last_cursor_index == 9):
                    seconds += 1
                else:
                    diff = last_cursor_index + 1 - 10
                    last_cursor_index = 9
            else:
                diff = int(curr_pin) - (last_cursor_index + 1)
                last_cursor_index = diff + last_cursor_index

            seconds += (abs(diff) + 1)

    print(seconds)