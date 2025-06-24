# Test Planning

This projects is to test the website 
https://www.saucedemo.com/v1/index.html.

## Overview
## Overview

The purpose of this test plan is to ensure comprehensive testing coverage for the website using Playwright. 
The test suite aims to validate the functionality of the application across different scenarios.

## Objectives

- Validate the login functionality with correct and incorrect credentials.
- Verify the shopping cart
- Verify navigation links
- Verify the "About section"
- Verify products list
- Verify the order 
- Verify the sum of the cart list

## Test Scope

The test scope includes:

- Login functionality
- Account sections and balances
- Navigation links

## Test Strategy

### Automated Testing

- Utilize Playwright for automated end-to-end testing.
- Create test scripts to cover various scenarios based on user interactions.
- Implement page object model (POM) for better maintainability and readability.

### Manual Testing
- Perform exploratory testing to uncover potential issues not covered by automated tests.
- Test on different browsers and devices to ensure cross-browser compatibility.
- Verify accessibility features and compliance with accessibility standards.

## Test Cases

1. **Login Functionality**
   - Test with valid credentials.
   - Test with invalid username/password.
   - Test with missing username/password.
   - Verify error messages for invalid credentials.

2. **Shopping Cart**
   - Verify the display of balances for each account section.

3. **Navigation Links**
   - Test links on each product

4. **About section**
   - Verify page redirect and "back"-"forward" functionalities.

5. **Products List**
   - Verify the number of products from the first page

6. **Order**
   - Verify the order details: name, city, zip code

7**Order**
   - Vhe sum of the products added in the cart


## Test Execution

- Execute automated tests in CI/CD pipelines after each code change.
- Run manual tests on staging and production environments before deployment.
- Perform regression testing after bug fixes or new feature implementations.
- Continuously update test cases and scripts to adapt to application changes.

## Reporting

- Generate test reports using Playwright's built-in reporting capabilities.
- Include detailed information about test results, including passed, failed, and skipped tests.
- Attach screenshots or videos for visual validation of test execution.