Feature: 02_Calories Calculation functionality
  Background:
    Given I navigate to homepage

  @Calories @NewCalories @TC_CALC_01 @Regression
  Scenario Outline: 01_Calories: Verify calories calories calculation with positive values.
    When I enter username as "<userName>"
    And I enter password as "<passWord>"
    And I click on Continue button
    And I click on Add Nutrient button on Home page
    And I enter "Carbs" value as "<carbsValue>"
    And I verify "Carbs" got added with value "<carbsValue>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Fat" value as "<fatValue>"
    And I verify "Fat" got added with value "<fatValue>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Alcohol" value as "<alcoholValue>"
    And I verify "Alcohol" got added with value "<alcoholValue>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Sugar Alcohol" value as "<sugarAlcoholVal>"
    And I verify "Sugar Alcohol" got added with value "<sugarAlcoholVal>" on Nutrients Dashboard
    Then I verify the Total Calories Values based on the formula

   Examples:
      | userName | passWord | carbsValue | fatValue | alcoholValue | sugarAlcoholVal |
      | testUser | Test1234 | 20.0       | 4        | 1            | 12              |

   @Calories @UpdateCalories @TC_CALC_02 @Regression
   Scenario Outline: 02_Calories: Verify the calories values after modifying the nutrient value.
    When I enter username as "<userName>"
    And I enter password as "<passWord>"
    And I click on Continue button
    And I click on Add Nutrient button on Home page
    And I enter "Carbs" value as "<orgCarbsValue>"
    And I verify "Carbs" got added with value "<orgCarbsValue>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Fat" value as "<orgFatValue>"
    And I verify "Fat" got added with value "<orgFatValue>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Alcohol" value as "<orgAlcoholValue>"
    And I verify "Alcohol" got added with value "<orgAlcoholValue>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Sugar Alcohol" value as "<OrgSugarAlcoholVal>"
    And I verify "Sugar Alcohol" got added with value "<OrgSugarAlcoholVal>" on Nutrients Dashboard
    And I update the "Carbs" value as "<newCarbsValue>"
    And I click on Submit button to add the Nutrient value
    And I verify "Carbs" got added with value "<newCarbsValue>" on Nutrients Dashboard
    And I update the "Fat" value as "<newFatValue>"
    And I click on Submit button to add the Nutrient value
    And I verify "Fat" got added with value "<newFatValue>" on Nutrients Dashboard
    And I update the "Protein" value as "<newProteinValue>"
    And I click on Submit button to add the Nutrient value
    And I verify "Protein" got added with value "<newProteinValue>" on Nutrients Dashboard
    Then I verify the Total Calories Values based on the formula

   Examples:
      | userName | passWord | orgCarbsValue | orgFatValue | orgAlcoholValue | OrgSugarAlcoholVal | newCarbsValue | newFatValue | newProteinValue |
      | testUser | Test1234 | 20.0          | 4.5         | 1.07             | 12.5               |  -4           |   3        | 0.25            |
      | testUser | Test1234 | 0.0           | -2.2        | 1.07             | Random             |  12           |   5.70     | 0.13            |

@Calories @deleteCalories @TC_CALC_03 @Regression
   Scenario Outline: 03_Calories: Verify the calories values after deleting the nutrient value.
    When I enter username as "<userName>"
    And I enter password as "<passWord>"
    And I click on Continue button
    And I click on Add Nutrient button on Home page
    And I enter "Carbs" value as "<Carbs>"
    And I verify "Carbs" got added with value "<Carbs>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I enter "Fat" value as "<Fat>"
    And I verify "Fat" got added with value "<Fat>" on Nutrients Dashboard
    And I delete "Carbs" Nutrient from the dashboard
    Then I verify the "Carbs" Nutrient got deleted successfully from the dashboard
    Then I verify the Total Calories Values based on the formula

   Examples:
      | userName | passWord | Carbs | Fat   |
      | testUser | Test1234 | 2.5   |0.00030000000000000000777777777777777 |

  @Calories @noUpdates @TC_CALC_04 @Regression
   Scenario Outline: 04_Calories: Verify user is able to close the Nutrient add dialog with Close button..
    When I enter username as "<userName>"
    And I enter password as "<passWord>"
    And I click on Continue button
    And I click on Add Nutrient button on Home page
    And I enter "Carbs" value as "<orgCarbs>"
    And I verify "Carbs" got added with value "<orgCarbs>" on Nutrients Dashboard
    And I click on Add Nutrient button on Home page
    And I update the "Carbs" value as "<newCarbs>"
    And I click on Close button to cancel the Nutrient value updates
    And I verify "Carbs" got added with value "<orgCarbs>" on Nutrients Dashboard
    And I update the "Carbs" value as "<newCarbs>"
    And I click on Cancel button to cancel the Nutrient value updates
    And I verify "Carbs" got added with value "<orgCarbs>" on Nutrients Dashboard
    Then I verify the Total Calories Values based on the formula

   Examples:
      | userName | passWord | orgCarbs | newCarbs |
      | testUser | Test1234 | 2.5      | 2.2      |