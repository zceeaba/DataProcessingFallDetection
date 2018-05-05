import json
from datetime import datetime
import datetime
import dateutil.parser
import numpy as np
from matplotlib import pyplot as plt
import dataparser
import matplotlib
import math

ground_truth_fall_time = []
ground_truth_fall_timeb = []
ground_truth_lay_time = []
ground_truth_lay_timeb = []
ground_truth_get_up_time = []
ground_truth_get_up_timeb = []
ground_truth_stand_time = []
ground_truth_stand_timeb = []
start_time_a = datetime.datetime(2018, 3, 22, 17, 27, 56)
start_time_b = datetime.datetime(2018, 3, 22, 17, 15, 56)
times_a = [[8, 10, 21, 23], [41, 45, 57, 61], [75, 80, 93, 97], [110, 114, 126, 129], [142, 146, 159, 164],
           [178, 183, 195, 198], [219, 222, 234, 237], [258, 262, 274, 278], [299, 303, 313, 317], [332, 335, 349, 353],
           [378, 382, 392, 396], [420, 424, 435, 440], [452, 456, 466, 470], [486, 491, 501, 507]]
times_b = [[8, 10, 21, 25], [36, 39, 53, 56], [68, 72, 86, 91], [99, 102, 118, 122], [134, 138, 151, 155],
           [168, 173, 190, 192], [210, 212, 230, 235], [249, 252, 269, 272], [281, 283, 302, 306], [317, 320, 339, 342],
           [357, 360, 373, 377], [391, 394, 410, 413], [426, 429, 443, 446], [456, 459, 471, 474]]


def convolution_filter(values, weight=[1, 1, 1, 1, 1]):
    weight_size = len(weight)
    value_size = len(values)
    window_length = int((weight_size - 1) / 2)
    result = np.zeros((value_size))
    weight = np.array(weight)
    weight_sum = np.sum(weight)
    for i in range(value_size):
        pre_list = np.zeros((window_length))
        post_list = np.zeros((window_length))
        for j in range(window_length, 0, -1):
            if not (i - j < 0):
                pre_list[window_length - j] = values[i - j]
            if not (i + j > value_size - 1):
                post_list[j - 1] = values[i + j]
        window = np.append(np.append(pre_list, values[i]), post_list)
        result[i] = window.dot(weight) / weight_sum
    return result


for times in times_a:
    ground_truth_fall_time.append(start_time_a + datetime.timedelta(0, times[0]))
    ground_truth_lay_time.append(start_time_a + datetime.timedelta(0, times[1]))
    ground_truth_get_up_time.append(start_time_a + datetime.timedelta(0, times[2]))
    ground_truth_stand_time.append(start_time_a + datetime.timedelta(0, times[3]))
for times in times_b:
    ground_truth_fall_timeb.append(start_time_b + datetime.timedelta(0, times[0]))
    ground_truth_lay_timeb.append(start_time_b + datetime.timedelta(0, times[1]))
    ground_truth_get_up_timeb.append(start_time_b + datetime.timedelta(0, times[2]))
    ground_truth_stand_timeb.append(start_time_b + datetime.timedelta(0, times[3]))

my_weight = [1, 1.2, 1.2, 1.5, 1.2, 1.2, 1]

wearable_data = dataparser.wearable()
wearable_data.sort(key=lambda x: x['result'])
t_value = []
x_acc_value = []
y_acc_value = []
z_acc_value = []
for index in range(len(wearable_data)):
    data = wearable_data[index]
    naive = data['result'].replace(tzinfo=None)
    if data['uid'] == 'c0' and datetime.datetime(2018, 3, 22, 17, 36, 46, 0) > naive > datetime.datetime(2018,
                                                                                                         3, 22,
                                                                                                         17,
                                                                                                         27,
                                                                                                         56,
                                                                                                         0):
        t_value.append(data['result'])
        x_acc_value.append(data["acceleration"][0])
        y_acc_value.append(data["acceleration"][1])
        z_acc_value.append(data["acceleration"][2])
# for fall_time in ground_truth_fall_time:
#      plt.axvline(fall_time, c='black', ls='--')

# for stand_time in ground_truth_stand_time:
#      plt.axvline(stand_time, c='blue', ls='--')
# for get_up_time in ground_truth_get_up_time:
#     plt.axvline(get_up_time, c='red', ls='--')
# for stand_time in ground_truth_stand_time:
#     plt.axvline(stand_time, c='blue', ls='--')
x_acc_value = np.array(x_acc_value)
y_acc_value = np.array(y_acc_value)
z_acc_value = np.array(z_acc_value)
magnitude = np.sqrt(np.power(x_acc_value, 2) + np.power(y_acc_value, 2) + np.power(z_acc_value, 2))

def normalize(data):
    zero_mean = (data - np.mean(data))
    return zero_mean/np.max(np.abs(zero_mean))

mode = 2
if mode == 1:
    x_data = convolution_filter(x_acc_value, my_weight)
    y_data = convolution_filter(y_acc_value, my_weight)
    z_data = convolution_filter(z_acc_value, my_weight)
    m_data = np.sqrt(np.power(x_data, 2) + np.power(y_data, 2) + np.power(z_data, 2))

elif mode == 0:
    x_data = x_acc_value
    y_data = y_acc_value
    z_data = z_acc_value
    m_data = magnitude

elif mode == 2:
    x_data = normalize(convolution_filter(x_acc_value, my_weight))
    y_data = normalize(convolution_filter(y_acc_value, my_weight))
    z_data = normalize(convolution_filter(z_acc_value, my_weight))
    m_data = normalize(np.sqrt(np.power(convolution_filter(x_acc_value, my_weight), 2) + np.power(convolution_filter(y_acc_value, my_weight), 2) + np.power(convolution_filter(z_acc_value, my_weight), 2)))

x_line = plt.plot(t_value, x_data, lw='2', label='x acceleration')
y_line = plt.plot(t_value, y_data, lw='2', label='y acceleration')
z_line = plt.plot(t_value, z_data, lw='2', label='z acceleration')
m_line = plt.plot(t_value, m_data, lw='2', c='black', label='magnitude')

t = 1
for lay_time in ground_truth_lay_time:
    if t:
        plt.axvline(lay_time, c='black', ls='dotted', lw=3, label='Fallen')
    else:
        plt.axvline(lay_time, c='black', ls='dotted', lw=3)
    t = 0
t = 1
for get_up_time in ground_truth_get_up_time:
    if t:
        plt.axvline(get_up_time, c='m', ls='dotted', lw=3, label='Get up')
    else:
        plt.axvline(get_up_time, c='m', ls='dotted', lw=3)
    t = 0
plt.xlabel('Timestamp(s)')
plt.ylabel('Acceleration Value(m/s^2)')
plt.xlim((datetime.datetime(2018, 3, 22, 17, 28, 32), datetime.datetime(2018, 3, 22, 17, 29, 44)))
plt.ylim((-1, 1))

plt.gcf().autofmt_xdate()
myFmt = matplotlib.dates.DateFormatter('%H:%M:%S')
plt.gca().xaxis.set_major_formatter(myFmt)
plt.legend()
plt.show()
