**OneBanc MPIN Strength Checker**

As part of my assignment round, this project evaluates the strength of a user's MPIN (Mobile Personal Identification Number) based on predefined rules and demographic data. It identifies weak PINs and provides reasons for their classification.

---

📄***About Repository***

*  TestQues is a folder that contains the code snippets of the questions given.
*  main.py file is the complete version of the problem statement given.
*  To run the test cases I used a JSON file of 50 sample test cases and called it in test.py file.

---

✅ ***Features***

*  Detects commonly used PINs (e.g, 1234, 0000, 1111, etc..).
*  Checks for personal demographic patterns like:
    * User's Date of Birth.
    * Spouse's DoB.
    * Wedding Anneversary.
*  Supports 4-digit and 6-digit PIN formats.
*  Supports reason codes for weak PINs.
*  Includes unit tests to validate logic.

---

🧪 ***Reason Codes***

* COMMONLY_USED -> PIN is found in the list of commonly used patterns
* DEMOGRAPHIC_DOB_SELF -> Matches a pattern derived from user's date of birth
* DEMOGRAPHIC_DOB_SPOUSE -> Matches a pattern derived from spouse's date of birth
* DEMOGRAPHIC_ANNIVERSARY -> Matches a pattern derived from anniversary date
* INVALID_PIN_FORMAT -> PIN is not numeric or not 4/6 digits long

---

🧑‍💻 ***How to Run***

1. Clone the Repository or download the files to your local machine.
2. Make sure python is installed.
3. Run commands:
    * for TestQues:
                    cd TestQues
                    python file_name.py
    * for main file:
                    python main.py
    * for test cases:
            ! Please run :  chcp 65001 in your command prompt to get the test case Colors.
            Then run:
                    python test.py