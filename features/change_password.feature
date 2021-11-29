Feature: Change Password

	Scenario: Admin user does not provide a new password
		Given a user is on the Profile page and clicks on the Change Password button
		When he enters only a password confirmation
		Then the platform should show him a error message b1


	Scenario: Admin user does not provide a password confirmation
		Given a user is on the Profile page and clicks on the Change Password button b2
		When he enters only the new password
		Then the platform should show him a error message b2


	Scenario: Admin user provides a wrong password confirmation
		Given a user is on the Profile page and clicks on the Change Password button b3
		When he enters a wrong password confirmation
		Then the platform should show him a error message b3


	Scenario: Admin user provides a new password and a password confirmation
		Given a user is on the Profile page and clicks on the Change Password button b4
		When he enters a new password and a password confirmation
		Then the platform should show him a success message