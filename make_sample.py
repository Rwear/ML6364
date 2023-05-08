# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pandas as pd


def print_csv10(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
    chi = pd.read_csv('output.csv', nrows=500)
    print(chi)
    chi.to_csv('NY_sample_old.csv', index=False)

    # DC = pd.read_csv('output.csv')
    # DC.to_csv('output_sample.csv', index=False)
    # print(DC)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_csv10('PyCharm')
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
