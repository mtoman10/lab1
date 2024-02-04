import parser_data
from plot_data import plot_data



def clean_data(data):
    print ("Write code to remove garbage data")


    print ("Create new file without garbage data and save it in data folder")
    file_name_clean = "walking_steps_clean.csv"





def main():
    # Get data
    file_name = "test.csv"  # Change to your file name
    data = parser_data.get_data(file_name) #data -- time,X,Y,Z
    clean_data(data)


if __name__== "__main__":
  main()

