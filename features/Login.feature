Feature: Login functionality
  Background:
    Given I navigate to homepage

  @Login @Regression
  Scenario Outline: Validate successful login
    When I validate the page title
    When I enter username as "<userName>"
    And I enter password as "<password>"
    And I click on Continue button
    Then I verify the user has logged in successfully

    Examples:
      | userName | password |
      | testUser | Test1234 |

  @Login @Regression
  Scenario Outline: Validate login failure with valid username and invalid password
    When I validate the page title
    When I enter username as "<userName2>"
    And I enter password as "<password2>"
    And I click on Continue button
    Then I verify invalid login error message is displayed

    Examples:
      | userName2 | password2 |
      | testUser | User12345 |
      | testUser ||

  @Login
  Scenario Outline: Validate login failure with invalid username and invalid password
    When I validate the page title
    When I enter username as "<userName3>"
    And I enter password as "<password3>"
    And I click on Continue button
    Then I verify invalid login attempt message is displayed

    Examples:
      | userName3 | password3 |
      | testUser1 | User12345 |