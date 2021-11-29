Feature: Create new company

  Scenario: User provides a Name, an Edition and a Educational institution to the new company d1
	Given a user is logged and is on the Create Company page d1
    When he enters a name and selects an edition with an educational institution both valid
    Then the platform should show him a success message d1


  Scenario: User does not provide a Name to the new company d2
    Given a user is logged and is on the Create Company page d2
    When he does not provide a name to the new company
    Then the Save button should remain disabled d2


  Scenario: User does not provide an Edition to the company d3
    Given a user is logged and is on the Create Company page d3
    When he does not provide an edition to the new company
    Then the Save button should remain disabled d3


  Scenario: User does not provide an Educational institution to the company d4
    Given a user is logged and is on the Create Company page d4
    When he does not provide an Educational institution to the new company
    Then the Save button should remain disabled d4


  Scenario: User does not provide any data to the new company d5
    Given a user is logged and is on the Create Company page d5
    When he does not provide any data to the new company
    Then the Save button should remain disabled d5