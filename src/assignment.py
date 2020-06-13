"""
COMP1730/6730 S1 2020 - Project Assignment.

Author: <201900800110吴岳东>
"""

import csv
import math

import matplotlib.pyplot as plt
from assignment_helpers import plot_volumes
from assignment_helpers import volume_to_area

def read_dataset(filepath):
    """ 
        Features:
            Takes the file path of the dataset as input, 
            reads the data,
            and returns the dataset in a suitable format. 
        Parameters:
            filepath: String. The path of the file.
        Returns:
            List of string list. The dataset.
    """
    with open(filepath) as csvfile:
        reader = csv.reader(csvfile)
        data = [line for line in reader]
    return data

def get_column(data, header):   #new
    """
        Features:
            Get the data under a specific header from the dataset.
        Parameters:
            data: List. The whole dataset.
            header: String. The header of the data that want to get.
        Returns:
            List of string. The data want to get.
    """
    headers = data[0]
    flag = 0    # to get the index of the header.
    for index in range(len(headers)):
        if headers[index] == header:
            flag = index
    result = [line[flag] for line in data[1:]]
    return result

def largest_area(data):
    """
        Features:
            Get the largest area covered by the lake from the dataset.
        Parameters:
            data: List. The whole dataset.
        Returns:
            Result: Float. The answer to largest_area.
    """
    result = 0
    area_data = [float(string) for string in get_column(data, "area")]  # convert every data to float
    for number in area_data:
        if number > result:
            result = number
    return result

def calculate_average(data, header):#new
    """ 
        Features:
            To calculate the avarage of specific header data
        Parameters:
            data: List. The whole dataset.
            header: String. The header of the data that want to get.
        Returns:
            Result: Float. The answer to calculate_average.
    """
    data = [float(string) for string in get_column(data, header)]
    sum = 0
    amount = 0
    for number in data:
        sum += number
        amount += 1
    return sum / amount

def average_volume(data):
    """
        Features:
            Get the average volume of the lake from the dataset.
        Parameters:
            data: List. The whole dataset.
        Returns:
            Result: Float. The answer to average_volume.
    """
    return calculate_average(data, "volume")

def most_average_rainfall(data):
    """
        Features:
            Get the time whose rainfall is closest to the average from the dataset.
        Parameters:
            data: List. The whole dataset.
        Returns:
            List. The answer to most_average_rainfall.
            Contains the month and year, and the rainfall during the month.
            The format is [month(integer), year(integer), rainfall(float)].
    """
    average_rainfall = calculate_average(data, "rainfall")

    rainfall_data = [float(string) for string in get_column(data, "rainfall")]  # convert every data to float
    date_data = get_column(data, "date")  # convert every data to float

    # the difference between the rainfall and average rainfall, initialized with the first data
    differ_to_average = abs(rainfall_data[0] - average_rainfall)
    closest_rainfall = rainfall_data[0]
    closest_rainfall_date = date_data[0]
    for index in range(1, len(rainfall_data)):
        if abs(rainfall_data[index] - average_rainfall) < differ_to_average:
            differ_to_average = abs(rainfall_data[index] - average_rainfall)
            closest_rainfall = rainfall_data[index]
            closest_rainfall_date = date_data[index]

    return [int(closest_rainfall_date[-2:]), int(closest_rainfall_date[:-2]), closest_rainfall]

def hottest_month(data):
    """
        Features:
            Get the hottest month on average from the dataset.
        Parameters:
            data: List. The whole dataset.
        Returns:
            List. The answer to hottest_month.
            The format is [month(string), average max temperature of the month(float)].
    """
    max_temper_data = [float(string) for string in get_column(data, "max_temperature")]
    month_data = [string[-2:] for string in get_column(data, "date")]

    month = ""
    average_degree = 0

    Jan_degree_sum = 0
    Jan_amount_sum = 0
    Feb_degree_sum = 0
    Feb_amount_sum = 0
    Mar_degree_sum = 0
    Mar_amount_sum = 0
    Apr_degree_sum = 0
    Apr_amount_sum = 0
    May_degree_sum = 0
    May_amount_sum = 0
    Jun_degree_sum = 0
    Jun_amount_sum = 0
    Jul_degree_sum = 0
    Jul_amount_sum = 0
    Aug_degree_sum = 0
    Aug_amount_sum = 0
    Sep_degree_sum = 0
    Sep_amount_sum = 0
    Oct_degree_sum = 0
    Oct_amount_sum = 0
    Nov_degree_sum = 0
    Nov_amount_sum = 0
    Dec_degree_sum = 0
    Dec_amount_sum = 0

    for index in range(len(month_data)):
        if month_data[index] == "01":
            Jan_degree_sum += max_temper_data[index]
            Jan_amount_sum += 1
            if Jan_degree_sum / Jan_amount_sum > average_degree:
                month = "January"
                average_degree = Jan_degree_sum / Jan_amount_sum
        elif month_data[index] == "02":
            Feb_degree_sum += max_temper_data[index]
            Feb_amount_sum += 1
            if Feb_degree_sum / Feb_amount_sum > average_degree:
                month = "February"
                average_degree = Feb_degree_sum / Feb_amount_sum
        elif month_data[index] == "03":
            Mar_degree_sum += max_temper_data[index]
            Mar_amount_sum += 1
            if Mar_degree_sum / Mar_amount_sum > average_degree:
                month = "March"
                average_degree = Mar_degree_sum / Mar_amount_sum
        elif month_data[index] == "04":
            Apr_degree_sum += max_temper_data[index]
            Apr_amount_sum += 1
            if Apr_degree_sum / Apr_amount_sum > average_degree:
                month = "April"
                average_degree = Apr_degree_sum / Apr_amount_sum
        elif month_data[index] == "05":
            May_degree_sum += max_temper_data[index]
            May_amount_sum += 1
            if May_degree_sum / May_amount_sum > average_degree:
                month = "May"
                average_degree = May_degree_sum / May_amount_sum
        elif month_data[index] == "06":
            Jun_degree_sum += max_temper_data[index]
            Jun_amount_sum += 1
            if Jun_degree_sum / Jun_amount_sum > average_degree:
                month = "June"
                average_degree = Jun_degree_sum / Jun_amount_sum
        elif month_data[index] == "07":
            Jul_degree_sum += max_temper_data[index]
            Jul_amount_sum += 1
            if Jul_degree_sum / Jul_amount_sum > average_degree:
                month = "July"
                average_degree = Jul_degree_sum / Jul_amount_sum
        elif month_data[index] == "08":
            Aug_degree_sum += max_temper_data[index]
            Aug_amount_sum += 1
            if Aug_degree_sum / Aug_amount_sum > average_degree:
                month = "August"
                average_degree = Aug_degree_sum / Aug_amount_sum
        elif month_data[index] == "09":
            Sep_degree_sum += max_temper_data[index]
            Sep_amount_sum += 1
            if Sep_degree_sum / Sep_amount_sum > average_degree:
                month = "September"
                average_degree = Sep_degree_sum / Sep_amount_sum
        elif month_data[index] == "10":
            Oct_degree_sum += max_temper_data[index]
            Oct_amount_sum += 1
            if Oct_degree_sum / Oct_amount_sum > average_degree:
                month = "October"
                average_degree = Oct_degree_sum / Oct_amount_sum
        elif month_data[index] == "11":
            Nov_degree_sum += max_temper_data[index]
            Nov_amount_sum += 1
            if Nov_degree_sum / Nov_amount_sum > average_degree:
                month = "November"
                average_degree = Nov_degree_sum / Nov_amount_sum
        else:
            Dec_degree_sum += max_temper_data[index]
            Dec_amount_sum += 1
            if Dec_degree_sum / Dec_amount_sum > average_degree:
                month = "December"
                average_degree = Dec_degree_sum / Dec_amount_sum

    return [month, average_degree]

def area_vs_volume(data):
    """
        Features:
            Get a plot of the area of Lake George against its volume.
            To determine whether the area increases quickly with little volume added or vice-versa.
        Parameters:
            data: List. The whole dataset.
    """
    areas = []
    volumes = []

    # plt.plot(areas)
    # plt.plot(volumes)
    # plt.show()
    areas = [float(string) for string in get_column(data, "area")]
    volumes = [float(string) for string in get_column(data, "volume")]

    plt.scatter(areas, volumes, cmap="jet_r", linewidths=0.5, edgecolors="black", alpha=0.5)
    plt.title("Area VS Volume")
    plt.xlabel("Area (m^2)")
    plt.ylabel("Volume (litres)")
    plt.show()

def lake_george_simple_model(data, evaporation_rate):
    """
        Features:
            This is a simple model to show how Lake George fills and ebbs over time.
            This model is based on the assumption that the evaporation of the lake is constant.
        Parameters:
            data: List. The whole dataset.
            evaporation_rate: Float. THe given evaporation.
        Returns:
            List of float. The list of volumes which are calculated by the model.
    """
    volume_data = [float(string) for string in get_column(data, "volume")]
    rainfall_data = [float(string) for string in get_column(data, "rainfall")]

    result = [volume_data[0]]
    humidity_area = largest_area(data)
    for index in range(1, len(volume_data)):
        result.append(result[index - 1] + (rainfall_data[index] - evaporation_rate) * humidity_area)
        humidity_area = volume_to_area(result[index])
    return result

def lake_george_complex_model(data):
    """
        Features:
            This is a complex model to show how Lake George fills and ebbs over time.
            This model is based on the assumption that the evaporation is changed based on the environment.
            
        Parameters:
            data: List. The whole dataset.
        Returns:
            List of float. The list of volumes which are calculated by the model.
    """
    volume_data = [float(string) for string in get_column(data, "volume")]
    rainfall_data = [float(string) for string in get_column(data, "rainfall")]
    min_temper_data = [float(string) for string in get_column(data, "min_temperature")]
    max_temper_data = [float(string) for string in get_column(data, "max_temperature")]
    wind_speed_data = [float(string) for string in get_column(data, "wind_speed")]
    solar_expo_data = [float(string) for string in get_column(data, "solar_exposure")]
    humidity_data = [float(string) for string in get_column(data, "humidity")]

    result = [volume_data[0]]
    modelled_area = largest_area(data)
    for index in range(1, len(volume_data)):
        evaporation = -3 * min_temper_data[index] + 1.6 * max_temper_data[index] - 2.5 * wind_speed_data[index] \
                      + 4.5 * solar_expo_data[index] - 0.4 * humidity_data[index]
        result.append(result[index - 1] + rainfall_data[index] * largest_area(data) - evaporation * modelled_area)
        modelled_area = volume_to_area(result[index])

    return result

def evaluate_model(data, volumes):
    """
        Features:
            To check the veracity of a model. By compare the model to the actual data.
        Parameters:
            data: the actual data.
            volumes: List of floats. the result of the model. A list of volumes.
        Returns:
            The relative standard deviation.
    """
    differ_square_sum = 0  # The sum of the square of difference between modeled data and actual data
    actual_volume = [float(string) for string in get_column(data, "volume")]
    for index in range(len(volumes)):
        differ_square_sum = differ_square_sum + pow((volumes[index] - actual_volume[index]) / actual_volume[index], 2)
    return math.sqrt(differ_square_sum / len(volumes))
