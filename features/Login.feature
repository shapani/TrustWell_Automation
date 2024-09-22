Feature: 01_Login functionality
  Background:
    Given I navigate to homepage

  @Login @Regression @TC_LOGIN_01
  Scenario Outline: 01_Validate successful login
    When I validate the page title
    When I enter username as "<userName>"
    And I enter password as "<password>"
    And I click on Continue button
    Then I verify the user has logged in successfully

    Examples:
      | userName | password |
      | testUser | Test1234 |

  @Login @Regression @TC_LOGIN_02
  Scenario Outline: 02_Validate login failure with valid username and invalid password
    When I validate the page title
    When I enter username as "<userName2>"
    And I enter password as "<password2>"
    And I click on Continue button
    Then I verify invalid login error message is displayed

    Examples:
      | userName2 | password2 |
      | testUser | User12345 |
      | testUser ||

  @Login @Regression @TC_LOGIN_03
  Scenario Outline: 03_Validate login failure with invalid username and invalid password
    When I validate the page title
    When I enter username as "<userName3>"
    And I enter password as "<password3>"
    And I click on Continue button
    Then I verify invalid login attempt message is displayed

    Examples:
      | userName3 | password3 |
      | testUser1 | User12345 |