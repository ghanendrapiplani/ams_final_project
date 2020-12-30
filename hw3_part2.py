import pyspark
import json
from pyspark.sql import SparkSession
import numpy as np 
import math
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--x', help='Latitude and longitude for point of form [lat,long] ex: [-111.931, 37.58523] ', type=str)
parser.add_argument('--dataset', help='Dataset location, ex : millerkeith2018data1.csv', type=str)
parser.add_argument('--k', help='Number of points to find nearest to above point, ex : 20', type=int)
args = parser.parse_args()
input_x = eval(args.x)


start_time = time.time()

input_points = []
for i in input_x:
    input_points.append(float(i))

input_dataset = args.dataset
input_k = args.k

print("Input point = ",input_x)
print("Number of points to find nearest to input points = ",input_k)
print("Input dataset = ", input_dataset)

spark = SparkSession \
    .builder \
    .appName("Python Spark SQL basic example") \
    .config("spark.some.config.option", "some-value") \
    .getOrCreate()

df = spark.read.option("header", "true").csv(input_dataset)



RDD = df.rdd.map(lambda x: (x.Longitude, x.Latitude))
k = input_k

points = RDD.collect()
start_time = time.time()
RDD = RDD.map(lambda x: ((x[0], x[1]), math.sqrt(((float(x[0])-input_points[0])**2) + ((float(x[1])-input_points[1])**2) ))).map(lambda x: (x[1], x[0]))

RDD = RDD.sortByKey()

RDD = RDD.map(lambda x: x[1])
k_closestPoints = RDD.take(k)

print("{} closest points to {} are: ".format(input_k, input_points))
for p in k_closestPoints:
    print(p)

print("Time of execution = %s seconds" % (time.time() - start_time))