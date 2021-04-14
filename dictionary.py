import json
import os
from difflib import get_close_matches

if os.path.exists("data.json"):
    mydata = json.load(open("data.json"))
    while True:
        word = input("Enter a word: ").lower()

        if word!="\\end":
            if word not in mydata.keys():
                suggestions = get_close_matches(word,mydata.keys(),3)
                if suggestions != []:
                    print("Did you mean ?")
                    i = 1
                    for sugg in suggestions:
                        print(f"({i}) {sugg}")
                        i += 1
                    try:
                        selected_number = int(input("selection: "))
                        if selected_number in [1,2,3]:
                            word = suggestions[selected_number-1]
                        else:
                            print("invalid selection")    
                    except:
                        print("invalid selection")    
                else:
                    print("invalid entry! try again.")

            if  word in mydata.keys():
                number_lines = len(mydata.get(word))
                mydata_list = mydata.get(word)
                line_number = 1
                if number_lines > 1:
                    print("\n")
                    for line in mydata_list:
                        print(f"({line_number}) {line}")
                        line_number = line_number + 1
                    print("\n")
                else:
                    print(f"\n(def:) {mydata_list[0]}\n")
        else:
            print("Thank you for using Mouaad Dictionary.")
            break
else:
    print("Data is corrupted!")

