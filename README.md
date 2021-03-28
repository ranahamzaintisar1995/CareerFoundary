# CareerFoundary
Coding challange at Career Foundary

## How to run
The project consists of one python file which is straight executable.
The code has been developed through python 3.7 so just save the file and run it simply.


## Deliverable 1
Looking at the dataset, we had multiple rows per day and sort of a timeseries based data. The main goal was to get metrics per day from multiple rows per day. After the data had been read into a pandas dataframe, days and months were extracted to be used for further tranformations.

Nested for loops were used to get each day in every month and metrics were generated for the following columns per day:
- date
- volatility
- maximum price
- minimum price
- maximum volume traded
- maximum trades

The attached python file gives a better understanding of how the objective was achieved.
Unfortunately due to lack of time, the data was prepared but not inserted inside a database.

The data after the transformation looks like this:
| date | volatility | maxPrice | minPrice | maxVolumeTraded | maxtrades |
| :---: | :---: | :---: | :---: | :---: | :---: |
| 2020-01-01 | 17.739562 | 7231.81 | 7150.00 | 32.994884 | 88 |
| 2020-01-02 | 82.482764 | 7184.86 | 6922.98  | 327.606155 | 649 |
| 2020-01-03 | 149.543404 | 7389.02 | 6871.93 | 353.685560 | 544 |
