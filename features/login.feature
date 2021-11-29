Feature: Login

	Scenario: Admin user with valid credentials a1
		Given a user with valid credentials
		When he enters his credentials and click Sign In button
		Then the user should be redirect to platform’s main page


	Scenario: Admin user with invalid email a2
		Given a user with an invalid email
		When he enters his credentials and click Sign In button a2
		Then the platform should show him a error message a2


	Scenario: Admin user with invalid password a3
		Given a user with an invalid password
		When he enters his credentials and click Sign In button a3
		Then the platform should show him a error message a3


	Scenario: Admin user with invalid credentials a4
		Given a user with both invalid credentials
		When he enters his invalid credentials and click Sign In button a4
		Then the platform should show him a error message a4


	Scenario: Admin user enters only his username a5
		Given a user with a valid username
		When he enters only his username
		Then the Sign In button should remain disabled


	Scenario: Admin user enters only his password
		Given a user with a valid password
		When he enters only his password
		Then the Sign In button should remain disabled a6