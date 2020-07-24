from  more_itertools import unique_everseen

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Path of the file to read
file_path = 'used_car_data.csv'

read_data = pd.read_csv(file_path)

# See which columns are in the file
cols = read_data.columns

# dropna drops missing values (think of na as "not available")
#read_data = read_data.dropna(axis=0)

nameCol = read_data.Name
locCol = read_data.Location
yearCol = read_data.Year
kiloCol = read_data.Kilometers_Driven
ownerCol = read_data.Owner_Type
mileageCol = read_data.Mileage
fuelCol = read_data.Fuel_Type

# Question 1: Show all the makes of cars available in the dataset and how many cars there are for each make
def findMake(makeColumn):
    make = {}
    for car in makeColumn:
        makeTemp = car.split()[0].title()
        if makeTemp not in make:
            make[makeTemp] = 1
        else:
            make[makeTemp] += 1
    print("Car makes & number of cars:")
    print(len(make.keys()))
    for i in make:
        print(i, ":", make[i])
        
# Question 2: Which city has the most used cars?
def carsPerCity(locationCol):
    locations = {}
    for loc in locationCol:
        if loc not in locations:
            locations[loc] = 1
        else:
            locations[loc] += 1
    print("Location & number of cars:")
    for i in locations:
        print(i, ":", locations[i])
     
# Question 3: What is the distribution of the  model year of the used cars?
def yearDistr(yearCol):
    plt.hist(yearCol, color='blue', edgecolor='black',
             bins=int(180/5))
    
    sns.distplot(yearCol, hist=True, kde=False, 
             bins=int(180/5), color = 'blue',
             hist_kws={'edgecolor':'black'})
    plt.title("Distribution of Car Edition's Year of Make")
    plt.xlabel("Year")
    plt.ylabel("Number of Cars")
    plt.savefig('YearDistr.png')
 
# Question 4: How many cars have a total distance usage of under 100,000 kilometers?
def under100(kiloCol):
    count = 0
    for i in kiloCol:
        if i < 100000: 
            count+=1
    print("Number of cars with less than 100,000 km driven:", count)   
    
# Question 5: At what upper and lower limits can the total distance travelled be categorised as "low" or "high"? Include arguments for your answer.
def stats(col):
    print(round(col.describe()))
    
# Question 6: Are there any outliers in the Kilometers_Driven column? Include arguments for your answer.
def boxPlot(colName):
    read_data.boxplot(column=colName)
    plt.ylim(0, 800000)
    plt.savefig(colName+'.png')
    
# Question 7: Does the year of manufacture correspond to the total distance usage?
def linearReg(colXName, colYName):
    sns.lmplot(x=colXName, y=colYName, data=read_data)
    ax = plt.gca()
    ax.set_yscale('log')
    
# Question 8: How many cars have had three owners already?
def ownerType(ownerCol):
    count=0
    for i in ownerCol:
        if i != 'First' and i != 'Second':
            count += 1
    print("Number of cars that have had three owners already:", count )

# Question 9: Which type of fuel is the most efficient in terms of fuel consumption?
def mostEconomicalFuel(fuelCol, mileageCol):
    fuelDict = {}
    mileageDict = {}
    mileageAvg = {}
    for fuel in fuelCol:
        if fuel not in fuelDict:
            fuelDict[fuel] = 1
        else:
            fuelDict[fuel] += 1
    for fuel in fuelDict:
        tempData = read_data.loc[read_data.Fuel_Type == fuel, 'Mileage']
        for i in tempData:
            if i is not None:
                if fuel not in mileageDict:
                    mileageDict[fuel] = float(str(i).split()[0])
                else:
                    mileageDict[fuel] += float(str(i).split()[0])     
        mileageAvg[fuel] = mileageDict[fuel]/fuelDict[fuel]
        
    print(fuelDict)
    print(mileageDict, "\n")
    print('Average mileage for each fuel type:\n')
    for i in mileageAvg:
        print(i, ":", mileageAvg[i])

# Question 10: What are the different factors that affect the price of used cars in India? Include arguments for your answer.
# This is a function that converts each value in the 'Location' column to integers. The returned list is then used as a parameter
# for another function written using R (made by my teammate and therefore not in this repository).
def locationInt(locCol):
    locsFinal = list(locCol)
    locs = []
    for i in locCol:
        locs.append(i)
    locs = list(unique_everseen(locs))
#    print(locs)
    locsDict = {}
    count = 0
    for elem in locs:
        locsDict[elem] = count
        count += 1
    pos = 0
#    print(locsDict)
    for k in locsFinal:
        if k in locsDict:
            locsFinal[pos] = locsDict[k]
            pos += 1
    print(locsFinal)
    return locsFinal
    







