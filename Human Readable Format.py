# https://www.codewars.com/kata/human-readable-duration-format/train/python

def format_duration(seconds):
    print(seconds)
    if seconds == None or seconds == 0:
        return "now"
    sec = 1
    min = 60
    hour = min * 60
    day = 24 * hour
    year = 365 * day

    output = []
    for time_unit in [year, day, hour, min, sec]:
        # print(time_unit)
        num_units = seconds // time_unit
        seconds%=time_unit
        output.append(num_units)

    string_output = []
    name_of_units = [("year", "years"), ("day", "days"), ("hour", "hours"),
                     ("minute", "minutes"), ("second", "seconds")]


    for i in range(len(output)):
        if output[i] == 1:
            string_output.append(str(output[i]) + " " + name_of_units[i][0])

        elif output[i] == 0:
            pass

        else:
            string_output.append(str(output[i]) + " " + name_of_units[i][1])


    final_output = ""
    for i in range(len(string_output)):
        component = string_output[i]
        final_output += component

        if i == len(string_output)-2:
            symbol = " and "

        elif i == len(string_output) -1:
            symbol = ""

        else:
            symbol = ", "

        final_output += symbol


    return final_output

print(format_duration(1))