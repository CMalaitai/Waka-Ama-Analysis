import os

def year_finals(year):
    # / is root directory
    # ./ is current directory
    # ../ is parent directory

    path = "./"

    finals_2017 = []
    finals_2018 = []

    for r, d, f in os.walk(path):
        for file in f:
            if 'Final' in file:
                if "2017" in r:
                    finals_2017.append(os.path.join(r, file))
                elif "2018" in r:
                    finals_2018.append(os.path.join(r, file))

    if(year == "2017" or year.lower() == "a"):
        print("2017 Finals:")
        for i in finals_2017:
            print(i)
    elif(year == "2018" or year.lower() == "b"):
        print("2018 Finals:")
        for i in finals_2018:
            print(i)

year = input("Choose a year:\n[a] 2017\n[b] 2018\n>>")

year_finals(year)