import csv
from datetime import datetime

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """

    date = datetime.fromisoformat(iso_string)

    #"Monday 05 July 2021"
    weekday_dictionary = {
        0:"Monday",
        1:"Tuesday",
        2:"Wednesday",
        3:"Thursday",
        4:"Friday",
        5:"Saturday",
        6:"Sunday"
    }

    month_dictionary = {
        1:"January",
        2:"February",
        3:"March",
        4:"April",
        5:"May",
        6:"June",
        7:"July",
        8:"August",
        9:"September",
        10:"October",
        11:"November",
        12:"December"
    }

    weekday = weekday_dictionary[date.weekday()]
    month = month_dictionary[date.month]
    year = str(date.year)

    if date.day <10:
        day = "0" + str(date.day)
    else: 
        day = str(date.day)

    formatted_date  = weekday + " " + day + " " + month + " " +  year

    return formatted_date



def convert_f_to_c(temp_in_farenheit):
    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_in_celcius = round((float(temp_in_farenheit) - 32.0) *5/9,1)
    return temp_in_celcius


    


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    my_sum = 0
    
    for number in weather_data:
        my_sum+=float(number)

    my_mean = my_sum/len(weather_data) 

    return my_mean 



def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    with open (csv_file) as file:
        csv_reader = list(csv.reader(file))
    
    csv_list = []

    for line in csv_reader [1:]:
        if line != []:
            line[1] = int(line[1])
            line[2] = int(line[2])
            csv_list.append(line)

    return csv_list


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """

    if weather_data == []:
         result = ()
    else:     
         min_value = min(weather_data)
         for i in range(len(weather_data)):
          if weather_data[i] == min_value:
            last_index = i

         min_value = float(min_value)
         result = min_value, last_index

    return result


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        result = ()
    else:     
        max_value = max(weather_data)
        for i in range(len(weather_data)):
            if weather_data[i] == max_value:
                last_index = i 
        max_value = float(max_value)
        result = max_value, last_index

    return result


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    number_of_days = str(len(weather_data))
    min_temp_list = []
    max_temp_list = []

    for line in weather_data:
        min_temp_list.append(line[1])

    for line in weather_data:
        max_temp_list.append(line[2])

    min_temp_index = find_min(min_temp_list)
    max_temp_index = find_max(max_temp_list)

    avg_min = format_temperature(convert_f_to_c(calculate_mean(min_temp_list)))
    avg_max = format_temperature(convert_f_to_c(calculate_mean(max_temp_list)))

    min_temp = format_temperature(convert_f_to_c(min_temp_index[0]))
    max_temp = format_temperature(convert_f_to_c(max_temp_index[0]))

    min_temp_line = int(min_temp_index[1])
    max_temp_line = int(max_temp_index[1])

    min_date = convert_date(weather_data[min_temp_line][0])
    max_date = convert_date(weather_data[max_temp_line][0])

    overview = number_of_days + " Day Overview\n"
    min_message = "  The lowest temperature will be " + min_temp + ", and will occur on " + min_date + ".\n"
    max_message = "  The highest temperature will be "+ max_temp + ", and will occur on " + max_date + ".\n"
    avg_min_message = "  The average low this week is " + avg_min + ".\n"
    avg_max_message = "  The average high this week is " + avg_max +".\n"

    message = overview + min_message + max_message + avg_min_message + avg_max_message
                
    # message = (number_of_days + " Day Overview\n" +
    # "The lowest temperature will be " + min_temp + ", and will occur on " + min_date + ".\n" +
    # "The highest temperature will be "+ max_temp + ", and will occur on " + max_date + ".\n" +
    # "The average low this week is " + avg_min + ".\n" +
    # "The average high this week is " + avg_max +".")

    return message

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    string_message = ""
    for line in weather_data:

        date = convert_date(line[0])
        min_temp = format_temperature(convert_f_to_c(line[1]))
        max_temp = format_temperature(convert_f_to_c(line[2]))

        string_title = "---- " + date + " ----\n"
        string_min = "  Minimum Temperature: " + min_temp + "\n"
        string_max = "  Maximum Temperature: " + max_temp + "\n\n"
        string_message += string_title + string_min + string_max

    return string_message
