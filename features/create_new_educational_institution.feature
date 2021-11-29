Feature: Create New Educational Institution


  Scenario: User provides all required information to the new Education Institution e1
	Given a user is logged and is on the Create Education Institution page e1
    When he enters all required information and clicks on the Save button
    Then the platform should show him a success message e1


  Scenario: User does not provide a Name to the new Education Institution e2
	Given a user is logged and is on the Create Education Institution page e2
    When he does not provide the Education Institution name and clicks on the Save button
    Then the platform should show him an error message e2


  Scenario: User does not provide a Country to the new Education Institution e3
	Given a user is logged and is on the Create Education Institution page e3
    When he does not provide a Education Institution country and clicks on the Save button
    Then the platform should show him an error message e3


  Scenario: User does not provide a City to the new Education Institution e4
	Given a user is logged and is on the Create Education Institution page e4
    When he does not provide a Education Institution state and clicks on the Save button
    Then the platform should show him an error message e4


  Scenario: User does not provide a City to the new Education Institution e5
	Given a user is logged and is on the Create Education Institution page e5
    When he does not provide a Education Institution city and clicks on the Save button
    Then the platform should show him an error message e5


  Scenario: User does not provide a CEP to the new Education Institution e6
	Given a user is logged and is on the Create Education Institution page e6
    When he does not provide a Education Institution CEP and clicks on the Save button
    Then the platform should show him an error message e6


  Scenario: User does not provide an Address to the new Education Institution e7
    Given a user is logged and is on the Create Education Institution page e7
    When he does not provide a Education Institution address and clicks on the Save button
    Then the platform should show him an error message e7


  Scenario: User does not provide a Number to the new Education Institution e8
	Given a user is logged and is on the Create Education Institution page e8
    When he does not provide a Education Institution number and clicks on the Save button
    Then the platform should show him an error message e8


  Scenario: User does not provide any data to the new Education Institution e9
	Given a user is logged and is on the Create Education Institution page e9
    When he does not provide any data for the new Education Institution clicks on the Save button
    Then the platform should show him multiple error messages e9

