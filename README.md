# Insight Data Science Challenge/h1bstatistics

Used python language to solve the challenge.
Here are the following approaches I used in the challenge.

1. Read the records from the h1b_input csv file and stored the necessary field based on their header names
2. Stored the information by implementing a data dictionary for the key value pairs for state - no. of 
certified professionals for that state and occupation - no. of certified professionals for that occupation.
3. Also calculated total number of certified professionals in the entire csv file to calculate the percentage 
field in the output.txt file 
4. Used a sort operation to sort the calculated fields according to the given requirements i.e first sort according to 
number fo certified professionals (descending) and if number are tied then second sort according to the name of the 
occupation.
5. All of these data are collected, calculated and stored in two .txt files as given in the system arguments 
during run.sh file.

To run the code by using .sh files follow the given procedure:
1. Download the entire Insight challenge folder
2. Run the terminal and check if python is installed (If not then install)
3. Change the directory of the terminal to h1b_statistics folder
 (You can change the input file if you want)
4. Now use command: chmod 777 ./run.sh
5. Now run the .sh file by using command: ./run.sh
6. It will generate output files of top_10_states.txt and top_10_occupation.txt in the output folder
7. Now to run the tests from insight_testsuite/run_tests.sh file change the directory of terminal to insight_testsuite
8. Now use command: chmod 777 ./run_tests.sh
9. Now run the .sh file by using command: ./run_tests.sh
10. This command will show how many of the given test cases passed by the program.
