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
1. Open the terminal and run the below command from the project root directory:
   a. behave -f allure_behave.formatter:AllureFormatter -o allure-results/ features --tags=Login



**How to view the test automation execution report:**
1. After executing the above steps to run the testcases, the *.json file should be created in "allure-report" directory.
2. Run the below command in same terminal: 
   3. allure serve allure-results

