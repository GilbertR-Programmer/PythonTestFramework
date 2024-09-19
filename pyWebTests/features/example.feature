Feature: Google Search

  Scenario: Searching on Google
    Given I open the Google homepage
    When I search for "Selenium WebDriver"
    Then the results page should display results for "Selenium WebDriver"
