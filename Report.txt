In Part 1 I have executed the code locally, on dataset from website link https://openei.org/datasets/dataset/miller-keith-2018-windplantdata , dataset name 'millerkeith2018data2.csv', found my code executes in time 1.92 seconds. Next I created the code using PySpark for execution on EMR cluster in Amazon, screenshot of EMR specs is enclosed with the submission. The code executed in 0.36 seconds due to parallelization. There was a 81% reduction in execution time. Hence, I was able to demonstrate that using more than 1 server speeds up our computation and arrives at results faster. Screenshots for both executions on local as well as EMR cluster are enclosed with the python files for each.

############# Running part 1 #############

hw3_part1.py [-h] [--x X] [--dataset DATASET] [--k K]

optional arguments:
  -h, --help         show this help message and exit
  --x X              Latitude and longitude for point of form [lat,long] ex:
                     [-111.931, 37.58523]
  --dataset DATASET  Dataset location, ex : millerkeith2018data1.csv
  --k K              Number of points to find nearest to above point, ex : 20


Sample cmd: python hw3_part1.py --x "[-111.931, 37.58523]" --dataset "millerkeith2018data1.csv" --k 20

############# Running part 2 #############

python hw3_part2.py --h
usage: hw3_part2.py [-h] [--x X] [--dataset DATASET] [--k K]

optional arguments:
  -h, --help         show this help message and exit
  --x X              Latitude and longitude for point of form [lat,long] ex:
                     [-111.931, 37.58523]
  --dataset DATASET  Dataset location, ex : millerkeith2018data1.csv
  --k K              Number of points to find nearest to above point, ex : 20
  
Sample cmd: python hw3_part2.py --x "[-111.931, 37.58523]" --dataset "millerkeith2018data1.csv" --k 20


Python packages required:
PySpark, pandas, numpy