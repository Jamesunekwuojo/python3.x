# name = input('what is ur name?')
# print(name)


# Import synthax
import statistics

list = [1,2,3,4,5,6,4,5,5,6,]

x= statistics.mean(list)
print(x)

mode = statistics.mode(list)
print(mode)

stdDev = statistics.stdev(list)
print(stdDev)

variance = statistics.variance(list)
print(variance)

# DIFFERENT APPROACHES TO IMPORTS DEPENDING ON USECASES
# import statistics as stats
# from statistics import mean, mode, stdev, variance
# from statistics import *