Feature: Guess the word
  Background:
    Given I am logged in with name '1234' and password '1234'

  Scenario: 1 GET request
    When I search for users
    Then I can see total 12 users
    Then I get status code 200

  Scenario: 2 POST request
    When I create user with name "John" and job "Tester"
    Then I get status code 201

  Scenario: 3 PUT request
    When I update user with name "John1" and job "Tester1"
    Then I get status code 200

  Scenario: 4 DELETE request
    When I delete a user
    Then I get status code 204