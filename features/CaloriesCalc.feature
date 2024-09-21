Feature: Calories Calculation functionality
  Background:
    Given I navigate to homepage

  @Calories @NewCalories @TC_CALC_01 @Regression
  Scenario Outline: verify calories calories calculation with positive values
    When I enter username as "<userName>"
    And I enter password as "<password>"
    And I click on Continue button
    When I click on Add Nutrient button on Home page
    And I enter "Carbs" value as "20.0"
    And I click on Add Nutrient button on Home page
    And I enter "Fat" value as "2.1"
    And I click on Add Nutrient button on Home page
    When I enter "Alcohol" value as "1.75"
    And I click on Add Nutrient button on Home page
    When I enter "Sugar Alcohol" value as "3"
    Then I verify the Total Calories Values based on the formula

   Examples:
      | userName | password |
      | testUser | Test1234 |

   @Calories @UpdateCalories @TC_CALC_02 @Regression
   Scenario Outline: Verify the calories values after modifying nutrient value
    When I enter username as "<userName>"
    And I enter password as "<password>"
    And I click on Continue button
    And I click on Add Nutrient button on Home page
    And I enter "Carbs" value as "0.0"
    And I click on Add Nutrient button on Home page
    And I enter "Fat" value as "20"
    And I click on Add Nutrient button on Home page
    And I enter "Alcohol" value as "3"
    And I click on Add Nutrient button on Home page
    And I enter "Sugar Alcohol" value as "-4"
    And I update the "Sugar Alcohol" value as "4"
    And I enter "Fat" value as "0"
    Then I verify the Total Calories Values based on the formula

   Examples:
      | userName | password |
      | testUser | Test1234 |

#
#  @Calories
#  Scenario: Edit the existing Nutrients to update the calories value
