#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


if __name__ == '__main__':
    with open("./Input/Names/invited_names.txt", "r+") as  file_names:
        names_list = file_names.readlines()

    for i in range(0, len(names_list) - 1):
        names_list[i] = names_list[i].strip('\n') 

    with open("./Input/Letters/starting_letter.txt") as letter:
        mail_template = letter.readlines()
    
    for i in names_list: 
        with open(f"./Output/ReadyToSend/letter_for_{i}.txt", "w") as letter:
            for t in mail_template:
                x = t.replace("[name]", i)
                letter.write(x) 

#   for i in names_list:
#       with open(f"./Output/ReadyToSend/{i}.txt", "w+") as output_letter:
#           read_list = output_letter.readlines()
#            read_list[0].replace("[name]", i)
#            for item in read_list: 
#                output_letter.write(item)

"""
    for i in names_list:
        output_letter = []
        with open(f"./Output/ReadyToSend/{i}.txt", "w+") as mail_merge:
            for k in range(0, len(mail_template) - 1):
                print(f"k ==== {k}")
                if k == 0:
                    output_letter[k] = mail_template[0].replace("[name]", i)
                    print(output_letter[k])
                else:
                    output_letter.append(mail_template[k])
                #print(j)
                print(output_letter[k]) 
#                mail_template[0] = mail_template[0].replace("[name]", i)
                mail_merge.write(output_letter[k])
"""
#    print(names_list)
#    print(mail_template)