Feature: calculate the area of a triangle
As an aspiring mathematician
I should be able to calculate the area of a triangle
So that I can chat with my math friends like a pro


Scenario: I confirm the webpage opened correctly
    Given I open the url "https://byjus.com/herons-calculator/"
    When I pause for 1000ms
    Then I expect that element "h1" contains the text "Heron's Calculator"

Scenario: I can calculate the area of a triangle
    Given I open the url "https://byjus.com/herons-calculator/"
    When I add "25" to the inputfield "#a"
    And I add "20" to the inputfield "#b"
    And I add "15" to the inputfield "#c"
    And I click on the element ".clcbtn"
    Then I expect that element "#_d" contains the text "150"


