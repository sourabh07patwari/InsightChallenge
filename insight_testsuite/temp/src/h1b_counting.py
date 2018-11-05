import csv
import sys


# This method will return the total number of certified professionals in the csv file and also store the dictionary
# where dict_states stores number of certified professionals with respect to different states
# and where dic_occupation stores number of certified professionals with respect to different occupation
def parse_csv(filename, dict_states, dict_occupation):

    total_certified = 0
    # open method to open the csv and read the contents of it
    with open(filename, 'r') as csv_file:
        # Reading the csv file with delimiter using ';'
        dialect = csv.Sniffer().sniff(csv_file.read(), delimiters=';,')
        csv_file.seek(0)
        reader = csv.reader(csv_file, dialect)

        num_rows = 0
        case_status_index = 0
        occupation_index = 0
        state_index = 0

        # Checking the columns first and storing the indexes of states, SOC name and case status
        # Then storing the number of certified professionals w.r.t states in one dictionary and other w.r.t occupation
        for row in reader:
            if num_rows == 0:
                header_index = 0

                for header in row:

                    if header == "CASE_STATUS":
                        case_status_index = header_index

                    if header == "WORKSITE_STATE":
                        state_index = header_index

                    if header == "SOC_NAME":
                        occupation_index = header_index

                    header_index += 1

            else:

                if row[case_status_index] == "CERTIFIED":
                    total_certified += 1

                if row[state_index] in dict_states:
                    if row[case_status_index] == "CERTIFIED":
                        dict_states[row[state_index]] += 1
                else:
                    if row[case_status_index] == "CERTIFIED":
                        dict_states[row[state_index]] = 1

                # If the SOC name consists ' " ' in the name then to remove it these two lines of code
                string_occupation = row[occupation_index]
                string_occupation = string_occupation.replace('"','')
                if string_occupation in dict_occupation:
                    if row[case_status_index] == "CERTIFIED":
                        dict_occupation[string_occupation] += 1
                else:
                    if row[case_status_index] == "CERTIFIED":
                        dict_occupation[string_occupation] = 1

            num_rows += 1

    return total_certified


# This method calculates the percentage of number of certified professionals w.r.t total professionals applied for the
# H1B status. Also taken into consideration rounding of percentage to 1 decimal after point
def calculate_percentage(number_certified, total_certified):
    percentage = float(number_certified)/float(total_certified)
    percentage *= 100
    percentage = round(percentage, 1)
    return percentage


# Generating the top_10_states.txt files output according to Data stored from the parsing method in dictionary
# and the third column is the percentage which is calculated from total number of certified professionals and the
# value from the dictionary
def feed_result_states(state_info, filename, total_certified):
    with open(filename, 'w') as f:
        f.write("TOP_STATES;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
        row_num = 1
        for item in state_info:
            if row_num <= 10:
                percentage = calculate_percentage(item[1], total_certified)
                f.write("%s;" % item[0])
                f.write("%s;" % item[1])
                f.write("%s" % percentage)
                f.write("%")
                f.write("\n")
            row_num += 1


# Generating the top_10_occupation.txt files output according to Data stored from the parsing method in dictionary
# and the third column is the percentage which is calculated from total number of certified professionals and the
# value from the dictionary
def feed_result_occupation(occupation_info, filename, total_certified):
    with open(filename, 'w') as f:
        f.write("TOP_OCCUPATIONS;NUMBER_CERTIFIED_APPLICATIONS;PERCENTAGE\n")
        row_num = 1
        for item in occupation_info:
            if row_num <= 10:
                percentage = calculate_percentage(item[1], total_certified)
                f.write("%s;" % item[0])
                f.write("%s;" % item[1])
                f.write("%s" % percentage)
                f.write("%")
                f.write("\n")
            row_num += 1


# This is the method that returns the Array of Array which represents the dictionary passed to it but in a sorted order
# according to the given condition in the problem
def sort_condition(dict):
    sorted_dic = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_dic


# This is the method which is called in main which consists of all the methods required to execute the program
def h1b_report(input_filename,output_file_occupation,output_file_states):
    dict_states = {}
    dict_occupation = {}

    print("Parsing .csv file and calculating parameters for the output")
    total_certified = parse_csv(input_filename, dict_states, dict_occupation)

    print("Sorting the result according to the given requirements")
    sorted_dict_states = sort_condition(dict_states)
    sorted_dict_occupation = sort_condition(dict_occupation)

    print("Generating .txt file for top 10 states")
    feed_result_states(sorted_dict_states, output_file_states, total_certified)
    print("Generating .txt file for top 10 occupations")
    feed_result_occupation(sorted_dict_occupation, output_file_occupation, total_certified)


# In this main method all the system arguments are accepted for input file and output files and h1b_report method is
# called instead of all methods in the main
if __name__ == "__main__":

    input_filename = sys.argv[1]
    output_file_states = sys.argv[3]
    output_file_occupation = sys.argv[2]
    print("EXECUTING h1b_counting.py")

    h1b_report(input_filename,output_file_occupation,output_file_states)
    print("Finished the program. Now check the files in output folder")