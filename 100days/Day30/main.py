
if __name__ == '__main__':

#FileNotFoundError:
#    with open("a_file.txt") as file:
#        file.read()
    
#KeyError
#    a_dict = {"key1":"value1", "key2":"value2"}
#    print(a_dict["key1"])
#    print(a_dict["key3"])

#IndexError
#    a_list = ["Apple", "Banana", "Pear"]
#    print(a_list[3])

#TypeError
#    string = "abc"
#    a = 2
#    print(string + a)
    
    try:
        with open("a_file.txt") as file:
            file.read()
        a_dict = {"key1":"value1", "key2":"value2"}
        #when we're executing something that might cause an exception
        print(a_dict["asdf"])
    
    except FileNotFoundError:
        #execute if there was an exception
        file = open("a_file.txt", "w")
        file.write("Something") 
    except KeyError as greska:
        print(f"Key {greska} does not exist!")
    else:
        #execute code if there were not exceptions
        pass

    finally:
        #execute always, regardless if we had an exception or not. 
        pass

