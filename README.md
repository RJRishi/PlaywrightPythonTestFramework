# PlaywrightPythonTestFramework
A robust, scalable test automation framework built using Python, Playwright, and Cucumber BDD, powered by the pytest execution engine. This project showcases industry-standard QA automation practices, combining Behavior-Driven Development (BDD) with a highly scalable test runner for parallel execution and robust assertions.
---------------------------------------------------------------------------------------------

Key Features:
Behavior-Driven Development: 
Uses Cucumber (Behave) syntax for human-readable test scenarios.

Page Object Model (POM): 
Separates page UI elements and actions from test scripts to reduce code duplication.

Playwright Engine: 
Leverages fast, reliable, and modern browser automation.

Pytest Test Runner: Powered by pytest for advanced test execution, structured test fixtures, and smart assertions.

Parallel Execution: Supports concurrent test runs via pytest plugins to drastically reduce overall execution time.

Cross-Browser Testing: 
Configured to run tests across Chromium, Firefox, and WebKit.

Automated Reporting: 
Generates detailed execution reports for easy debugging.

---------------------------------------------------------------------------------------------

Project Structure:

├── Features/          # Gherkin .feature files (User scenarios)
├── StepDefinitions/   # Python code mapping to feature steps
├── POMfiles/          # Page Object classes (UI locators and actions)
├── .vs/               # IDE configuration files
└── README.md          # Project documentation

---------------------------------------------------------------------------------------------

Prerequisites:

Before running the tests, ensure you have the following installed:

Python installation - 3.8 or higher
Pytest Installation - pip install pytest
Playwright Installation - pip install pytest-playwright
