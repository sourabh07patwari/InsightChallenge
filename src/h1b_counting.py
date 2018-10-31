import os.path as pth


def parsecsv(filename):
    with open(filename) as file:
        SAMPLES = list()
        num_rows = 0
        case_status_index = 0
        occupation_index = 0
        state_index = 0

        for row in file:
            if num_rows == 0:
                header_index = 0
                first_row = row.split(';')
                for header in first_row:
                    if header == "CASE_STATUS":
                        case_status_index = header_index
                    if header == "EMPLOYER_STATE":
                        state_index = header_index
                    if header == "SOC_NAME":
                        occupation_index = header_index
                    header_index += 1
            else:
                all_rows = row.split(';')

                example = list()
                example.append((all_rows[case_status_index]))
                example.append((all_rows[occupation_index]))
                example.append((all_rows[state_index]))
                SAMPLES.append(example)
            num_rows += 1
    print(SAMPLES)
    return SAMPLES


def feed_result(SAMPLES, filename):
    with open(filename, 'w') as f:
        f.write("NO., CASE STATUS, OCCUPATION, STATE\n")
        row_num = 1
        for item in SAMPLES:
            f.write("%s;" % row_num)
            col_num = 0
            for i in item:
                if col_num != len(item):
                    f.write("%s;" % i)
                else:
                    f.write("%s" % i)
                col_num += 1
            f.write("\n")
            row_num += 1


if __name__ == "__main__":
    filename = '../insight_testsuite/tests/test_1/input/h1b_input.csv'
    output_file = '../insight_testsuite/tests/test_1/output/result.txt'
    SAMPLES = parsecsv(filename)
    feed_result(SAMPLES, output_file)

