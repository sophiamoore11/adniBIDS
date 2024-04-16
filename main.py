# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
import pandas as pd
idaSearch21324 = pd.read_csv("/Users/sophiamoore/Downloads/idaSearch_2_13_2024.csv")

SID_unique = pd.unique(idaSearch21324["Subject ID"])
SID_MRIPET = []
# Loop for each SID
for currID in SID_unique:
    #subset DF w/ all of currID's rows
    idDF = idaSearch21324[idaSearch21324["Subject ID"]==currID]
    #group by SID. if both MRI and PET exists, len = 2
    both = len(idDF.groupby("Modality").count())==2
    if both:
        SID_MRIPET.append(currID)
print(SID_MRIPET)
















