#Day 25 lecture notes
import csv
import pandas


if __name__ == '__main__':

#    with open("weather_data.csv", "r") as weather_data:
#        data = weather_data.readlines()
#
#    for i in data:
#        i = i.strip('\n') 
#        print(i)

#    for i in range(0, len(data) - 1):
#        data[i] = data[i].strip('\n')

#    with open("weather_data.csv") as data_file:
#        data = csv.reader(data_file)
#        temperatures = []
#        
#        for row in data:
#            if row[1] == "temp":
#                pass
#            else:
#                temperatures.append(int(row[1]))
#    print(temperatures)
#    print("===== READ DATA WITH PANDAS BELOW ===== ")
#    data = pandas.read_csv("weather_data.csv")
#    print(data["temp"])
#    print(type(data))
#    print(type(data["temp"]))
#    data_dict = data.to_dict()
#    temp_list = data["temp"].to_list()
#    print(f"TEMP LISTA {temp_list}")
#    print(data["temp"].mean())
#    print(f'MAX TEMP ==== {data["temp"].max()}')
#    print("PRINT ROW")
#    print(f'{data[data.day == "Monday"]}')
#
#    print(f'MAX TEMP WITH  ====') 
#    print(data[data.temp == data["temp"].max()])
#    monday = data[data.day == "Monday"]
#    print(f'------Monday in Celsius \n{(monday.temp * 1.8) + 32}')
#    CONVERT DICTIONARY TO DATAFRAME, SAVE AS CSV    
#    grade_data = {
#        "student": ["Djuka", "Suki", "Sule"],
#        "grade": [81, 65, 44]
#    }
#    grade_data_frame = pandas.DataFrame(grade_data)
#    print("*"*10)
#    print(grade_data_frame)
#    grade_data_frame.to_csv("ocjene.csv")
#    
#    END OF CONVERT DICTIONARY TO DATAFRAME, SAVE AS CSV    

    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    print(data["Primary Fur Color"])
    boja = data["Primary Fur Color"]
#    print(data["Primary Fur Color"].count())
    print(boja.count())
    print(boja.value_counts())
    output = boja.value_counts()
    output.to_csv("squirrel_by_collor.csv")