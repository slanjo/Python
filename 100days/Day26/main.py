import pandas
import random
if __name__ == '__main__':
    numbers = [1, 2, 3]
    #LIST COMPREHENSION
    new_numbers = [item + 1 for item in numbers]
    print(f"numbers>>> {numbers}")
    print(f"new_numbers>>> {new_numbers}")

    name = "Angela"
    new_list = [letter for letter in name]
    print(new_list)

    #Python sequecnes: list, string, tuple, range
    new_range = [letter * 2 for letter in range(1,5)] 
    print(new_range)

    #CONDITIONAL LIST COMPREHENSION
    #new_list = [new_item for item in list if test]
    names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
    names_caps = [nme.upper() for nme in names if len(nme) > 5]
    print(names_caps)

    numbers2 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    #filter out odd numbers
    even_list = [num for num in numbers2 if num % 2 == 0]
    print(even_list) 
    print("#"*30)#DATA OVERLAP SOLUTION    
    with open("file1.txt") as file1:
        f1 = file1.readlines()

    with open("file2.txt") as file2:
        f2 = file2.readlines()

    f3 = []
    for i in range(0, len(f1)):
        f1[i] = f1[i].strip('\n')

    for i in range(0, len(f2)):
        f2[i] = f2[i].strip('\n')
    print(f1)
    print(f2)
    print(f3)

    f1.pop()
    f2.pop()
    f3 = [int(item1) for item1 in f1 if item1 in f2]
    #US states COMPREHENSION solution
    #missing_states = [state for state in all_states if state not in guessed_states]
    print(f1)
    print(f2)
    print(f3)

    new_dict = {student:random.randint(1,100) for student in names}
    print(new_dict)
    passed_dict = { key:value for (key,value) in new_dict.items() if value >= 60}
    print(passed_dict)

    sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
    word_list = sentence.split()
    print(word_list)
    result2 = { item:len(item) for item in word_list}
    print(result2)
    print("*" * 50, "dictionary comprehension")
    weather_c = {
        "Monday": 12,
        "Tuesday": 14,
        "Wednesday": 15,
        "Thursday": 14,
        "Friday": 21,
        "Saturday": 22,
        "Sunday": 24,
    }

    weather_f = { day:(temp_c * 9/5 ) + 32 for (day,temp_c) in weather_c.items()}

    print(weather_f)
    #Loop through a dictionary:

    for (key, value) in weather_c.items():
        print(value)

    #Loop through pandas DataFrame

    print("*" * 50, "Loop Through Pandas DataFrame")
    student_dict = {
            "student": ["Angela", "James", "Lily"], 
            "grade": [56, 76, 98]
            }
    for (key, value) in student_dict.items():
        print(key)
 
    print(student_dict)
    student_data_frame = pandas.DataFrame(student_dict)
    print(student_data_frame)
    for (key, value) in student_data_frame.items():
        print(value)

    for (key, value) in student_data_frame.items():
        print(key)

    #Loop through rows of a DataFrame
    for (index, row) in student_data_frame.iterrows():
        print(row)

