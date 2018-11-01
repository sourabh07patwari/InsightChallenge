import os.path as pth
import csv


def parsecsv(filename, dict_states, dict_occupation):

    total_certified = 0
    with open(filename, 'r') as csvfile:
        dialect = csv.Sniffer().sniff(csvfile.read(), delimiters=';,')
        csvfile.seek(0)
        reader = csv.reader(csvfile, dialect)

        num_rows = 0
        case_status_index = 0
        occupation_index = 0
        state_index = 0

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


def calculate_percentage(number_certified, total_certified):
    percentage = float(number_certified)/float(total_certified)
    percentage *= 100
    percentage = round(percentage, 1)
    return percentage


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


def sort_condition(dict):
    sorted_dic = sorted(dict.items(), key=lambda x: (-x[1], x[0]))
    return sorted_dic


def h1b_report(input_filename,output_file_occupation,output_file_states):
    dict_states = {}
    dict_occupation = {}

    total_certified = parsecsv(input_filename, dict_states, dict_occupation)

    sorted_dict_states = sort_condition(dict_states)
    sorted_dict_occupation = sort_condition(dict_occupation)

    feed_result_states(sorted_dict_states, output_file_states, total_certified)
    feed_result_occupation(sorted_dict_occupation, output_file_occupation, total_certified)

    print(sorted_dict_states)
    print(sorted_dict_occupation)
    print(total_certified)


if __name__ == "__main__":
    input_filename = '../insight_testsuite/tests/test_1/input/h1b_input.csv'
    output_file_states = '../insight_testsuite/tests/test_1/output/top_states.txt'
    output_file_occupation = '../insight_testsuite/tests/test_1/output/top_occupation.txt'

    h1b_report(input_filename,output_file_occupation,output_file_states)
