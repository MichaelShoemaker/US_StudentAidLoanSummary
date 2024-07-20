# US_StudentAidLoanSummary
Parser for MyStudentAid.txt File from studentaid.gov

## Why?
Looking through my student loan data it was a pain to try to figure out how much I've actually paid in interest.<br><br>
The MyStudentData.txt File does not appear to have a summary and was a bit cryptic to figure out how to read.<br><br>
Using a naive approach I put together this parser and tested it on my loan data and it seems to work correctly.<br><br>


## Usage:
Log into your account at studentaid.gov
![alt text](./images/studentaid-login.png "Student Aid Login")
<br>

Once logged in click on the View Details button
![alt text](./images/view_details.png "View Details")
<br>

Click on Download My Aid Data
![alt text](./images/download_my_aid_data.png "Download Data")
<br>

You should see the file download as "MyStudentData.txt"<br>
Below example has (1) because I downloaded it twice.<br>
![alt text](./images/MyStudentAidFile.png "My Aid Data")
<br>

Then just place this file in the same directory as parse_aid.py and run parse_aid.py<br>
![alt text](./images/example_run.png "Example Run")