# Interview Assignment: Analyzing Anonymized Website Traffic Logs for Suspicious Activities

## Assignment Summary:
This assignment requires you to analyze anonymized website traffic logs with high efficiency and minimal resource usage. The main focus of this assignment is to write an efficient script capable of processing large datasets.

## Test Duration and Submission Instructions:
- **Test Duration:** You will have a total of three (3) hours to complete the programming test from the moment you start. Please note that the time needed to consult the assignment, including phone calls or email responses, will be excluded from the total test time. This means that any time spent communicating with us will not count towards your three-hour limit.

- **Submission Deadline:** Once the three-hour time limit has elapsed, you must submit your results via email to [potfaj.michal@pantarhei.sk]. Please ensure that your submission includes all necessary files and documentation.

- **Extension for Improvement:** If you feel that you could produce a better solution after the initial three-hour period, you are welcome to submit an updated version of your program.

- **Communication During the Test:** Throughout the test, you may ask questions or seek clarification via email at [potfaj.michal@pantarhei.sk] or by calling [+421 907 824 800]. 

## Key Requirement:
- **Memory Consumption:** Your application's memory usage must not exceed 300 MB.
- Your solution must be able to handle new log files with the same format as the file provided with the test.

## Dataset:
The dataset (`firewall-logs.csv`) includes anonymized website traffic logs, featuring data such as timestamps, anonymized client IP addresses, request paths, HTTP methods, protocols, and user agents.

## Tasks:
1. **Fix User-Agent column:**
   - The User-Agent column is not always correctly formatted, with some values not enclosed in quotes. Write a script to fix this issue. **(You can write this as separate script to pre-process your data)**

2. **Time series chart:**
   - Produce a time series chart illustrating the number of requests every 10 seconds. ***(Must be part of main script)**

3. **Most requested endpoints:**
   - Identify the top 5 most requested endpoints and the source IP address that requested each the most. ***(Must be part of main script)**

4. **Most requesting IPs:**
   - List the top 5 source IP addresses making the most requests. (Must be part of main script)
   - Produce a time series chart displaying the number of requests for each of the top 5 requesting IPs. ***(Must be part of main script)**

5. **Documentation:**
   - Provide clear documentation on how to run your program and any requirements or dependencies.

## Deliverables:
1. A functioning program (source code).
2. A sample analysis report generated by your program.
3. Documentation of how to run your program.

## Evaluation Criteria:
- **Output:** The program's output should meet the expected results.
- **Efficiency:** The program should be written efficiently and use resources sparingly.
- **Code Quality:** Emphasis on code readability and maintainability.

## Notes:
- This assignment is designed to evaluate your skills in data processing, analysis, and problem-solving through programming. Focus on demonstrating your ability to efficiently handle and analyze large datasets.
