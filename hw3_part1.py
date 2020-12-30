import pandas as pd
import math
import argparse
import time

parser = argparse.ArgumentParser()
parser.add_argument('--x', help='Latitude and longitude for point of form [lat,long] ex: [-111.931, 37.58523] ', type=str)
parser.add_argument('--dataset', help='Dataset location, ex : millerkeith2018data1.csv', type=str)
parser.add_argument('--k', help='Number of points to find nearest to above point, ex : 20', type=int)
args = parser.parse_args()
start_time = time.time()

input_x = eval(args.x)

df = pd.read_csv(args.dataset)
input_points = []
for i in input_x:
    input_points.append(float(i))
input_k = args.k

points = []
for index,row in df.iterrows():
  lst = []
  lst.append(row['Latitude'])
  lst.append(row['Longitude'])
  points.append(lst)
k_closestPoints = []
index = 0

for p in points:
  d = math.sqrt(((float(p[0])-input_points[0])**2) + ((float(p[1])-input_points[1])**2))
  tup = (d, index)
  k_closestPoints.append(tup)
  index+=1

k_closestPoints.sort()

print("{} closest points to {} are: ".format(input_k, input_points))
for i in range(input_k):
  index = k_closestPoints[i][1]
  print(points[index])

print("Time of execution = %s seconds" % (time.time() - start_time))