This test automation framework has been designed using below technologies:
1. Python 3.12 
2. Behave framework (BDD)
3. Gherkin
3. Allure Report
4. Code Repository: Git
5. CICD Pipeline: Jenkins
6. Selenium Webdriver

**Pre-requisites:**
1. Python 3.12 and above
2. Allure
3. Allure-Behave
4. Virtual environment should be setup
5. Selenium
6. Webdriver Manager
7. Editor - Pycharm or any other compatible editors

**How to run the testcases:**
Open the terminal and run the below command from the project root directory:

1. To run all the feature files (testcases) from feature directory: 
   behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features 
2. To run the specific tag (example: @login, @Calories):
   behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features --tags=<Login>        


**How to view the test automation execution report:**
After executing the above steps to run the testcases, the *.json file should be created in "allure-report" directory.
Run the below command in same terminal: 
   allure serve allure-results

