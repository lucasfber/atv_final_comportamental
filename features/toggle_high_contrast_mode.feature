Feature: Toggle High Contrast

  Scenario: High contrast is not enabled, user enables it c1
	Given a user is logged and the high contrast is not enabled c1
    When the user clicks on Enable/Disable High Contrast c1
    Then the platform should enable the high contrast c1


  Scenario: High contrast is enabled, user disable it c2
	Given a user is logged and the high contrast is enabled c2
    When the user clicks on Enable/Disable High Contrast c2
    Then the platform should disable the high contrast c2

  Scenario: High contrast is still enabled after user logout c3
	Given a user is logged and the high contrast is disabled c3
    When the user clicks to enable it and logs out c3
    Then High Contrast should be enabled when the user logs in again c3

  Scenario: High contrast is still disabled after user logout c4
    Given a user is logged and the high contrast is enabled c4
    When the user clicks on disable it and logs out c4
    Then High Contrast should be disabled when the user logs in again c4

