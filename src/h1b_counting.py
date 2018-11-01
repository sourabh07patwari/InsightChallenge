import os.path as pth
import csv


def h1b_report_csv(filename):

    total_certified = 0
    dict_states = {}
    dict_occupation = {}
    SAMPLES = list()

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

                    if header == "EMPLOYER_STATE":
                        state_index = header_index

                    if header == "SOC_NAME":
                        occupation_index = header_index
                    header_index += 1

            else:
                example = list()
                example.append((row[case_status_index]))
                example.append((row[occupation_index]))
                example.append((row[state_index]))
                SAMPLES.append(example)

                if row[case_status_index] == "CERTIFIED":
                    total_certified += 1

                if row[state_index] in dict_states:
                    if row[case_status_index] == "CERTIFIED":
                        dict_states[row[state_index]] += 1
                else:
                    dict_states[row[state_index]] = 1

                if row[occupation_index] in dict_occupation:
                    if row[case_status_index] == "CERTIFIED":
                        dict_occupation[row[occupation_index]] += 1
                else:
                    dict_occupation[row[occupation_index]] = 1

            num_rows += 1
    print(SAMPLES)
    print("Total Certified Professionals: " + str(total_certified))
    print(dict_occupation)
    print(dict_states)

    return SAMPLES


def feed_result(SAMPLES, filename):
    with open(filename, 'w') as f:
        f.write("NO., CASE STATUS, OCCUPATION, STATE\n")
        row_num = 1
        for item in SAMPLES:
            f.write("%s;" % row_num)
            col_num = 0
            for i in item:
                if col_num != len(item)-1:
                    f.write("%s;" % i)
                else:
                    f.write("%s" % i)
                col_num += 1
            f.write("\n")
            row_num += 1


if __name__ == "__main__":
    filename = '../insight_testsuite/tests/test_1/input/h1b_input.csv'
    output_file = '../insight_testsuite/tests/test_1/output/result.txt'
    SAMPLES = h1b_report_csv(filename)
    feed_result(SAMPLES, output_file)

