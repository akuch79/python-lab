# Python Lab Project — Work Description

In this project, I set up a Python project using Git and GitHub. I created some Python utility functions, wrote tests for them, and set up GitHub Actions so that the tests can run automatically when I push changes to GitHub.

## 1. Python Project Structure

I created a basic project structure with:

* `src/` — contains my Python source code
* `tests/` — contains my automated tests
* `docs/` — contains my project documentation
* `.gitignore` — prevents unnecessary files like `__pycache__` from being added to Git

## 2. Python Utility Functions

In `src/utils.py`, I created three functions:

* `square(n)` — finds the square of a number
* `is_even(n)` — checks if a number is even
* `celsius_to_fahrenheit(c)` — converts Celsius to Fahrenheit

## 3. Automated Testing

I created `tests/test_main.py` and used **pytest** to test my functions.

The tests checked that all three functions were working correctly. When I ran the tests, I got:

```text
3 passed in 0.12s
```

This confirmed that my functions were working as expected.

## 4. Git and GitHub

I used Git to track the changes I made to my project and connected my local project to my GitHub repository.

My project is available on GitHub as **akuch79/python-lab**.

I also made several commits to keep track of my progress, including:

* `Initialize Python lab project`
* `Add test file`
* `Add unit tests for utility functions`
* `Ignore Python cache files`
* `Add GitHub Actions test workflow`

## 5. GitHub Actions

I created a GitHub Actions workflow at:

```text
.github/workflows/tests.yml
```

The workflow automatically:

1. Checks out my repository
2. Sets up Python 3.14
3. Installs pytest
4. Runs my tests

This means that when I push changes to the `main` branch, GitHub can automatically run my tests and check that my code is still working.

## Overall

Through this project, I learned how to combine Python programming, testing, Git, GitHub, and GitHub Actions into one workflow.

My workflow is:

```text
Write Python code
       ↓
Write and run tests
       ↓
Use Git to track changes
       ↓
Push changes to GitHub
       ↓
GitHub Actions runs the tests
       ↓
Check that everything passes
```

This project gave me a good foundation for learning more about Python testing, version control, and CI/CD.
