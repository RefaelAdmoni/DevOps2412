def add_names(name1, name2, name3):
    open_file = open("names.txt", "r+")
    open_file.writelines(name1 + "\n")
    open_file.writelines(name2 + "\n")
    open_file.writelines(name3 + "\n")
    open_file.close()

def read_file():
    open_file = open("names.txt", "r")
    for name in open_file.readlines():
        print("hello " + name)
    open_file.close()

add_names("Refael","Omer", "Aviel")
read_file()




