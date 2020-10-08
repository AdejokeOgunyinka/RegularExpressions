# Working With Regular Expressions

In this task, you will encounter and use the following
- Regular Expressions
- Test Driven Development

## Convections / Coding Styles

- Notice that names of modules, methods, functions and variables are `snake_cased`, while names of classes are `PascalCased`
- Ensure to have two spaces exactly between import and actual codes in modules
- Ensure to be consistent with usage of string quotes. Always use the single quote except in situations where you need to use double quotes

## About

This task deals with implementing functionalities for parsing email addresses. Parsing in this context simply means looking through email address strings to pick out important and useful information.

## Exercises

1. Create branch named `implement-email-parser` and only work within this branch
2. Complete implementation and testing of the email parser
3. When done, push your changes and raise a pull request on Github using the pull request template already added to the project (`.github` folder)

## Approach

- Try to not attempt to conceptualize the whole documentation and codebase at once, instead move step by step through the task
- Ensure to understand the problem before attempting to write any code
- Ensure to write the expected unit tests first before actual implemention, as that confirms that you are conforming to the `TDD Methodology`.
- Ensure to manually experiment within the modules to confirm the results of your implementations

## Running Your Tests

```bash

Machine> cd <this-project-folder>

Machine> python -m unittest tests/test_email_parser.py

```

## Parsing Email Addresses

Email addresses are usually in the format : `username@domain`. Ex. `johndoe@gmail.com`, `jane+doe@yahoo.com`, etc. This means that there are two(2) useful information we will need out of email addresses, namely `username` and `domain`

Given the email address (`johndoe@gmail.com`), we will have the dictionary below as the output of parsing
```python

{
  'username': 'johndoe',
  'domain': 'gmail.com'
}

```

Also, given the email address (`jane+doe@yahoo.com`), we will have the dictionary below as the output of parsing
```python

{
  'username': 'jane+doe',
  'domain': 'yahoo.com'
}

```

When writing the logic for parsing email addresses, below are CONSTRAINTS you need to put into consideration
- Usernames will be made up of alphabets or alphanumerics. Ex. `john`, `johndoe`, `john123`. Note that usernames cannot start with a number
- Usernames should also support only the `+` character in between as in example 2 above
- Domains will always end in `.com`, Ex. `gmail.com`, `yahoo.com`, `bz2.com`, etc.
- The part before `.com` in domains will be made up of alphabets or alphanumerics, Ex. `gmail`, `bz2`, `dom555`, etc. Note that domains cannot start with a number

To complete the implementation of the `EmailParser` class defined in the `email_parser.py` module, you will need to
1. Provide a regex pattern as a class attribute on the class EmailParser
2. Complete the implementation for the `parse` method to do the expected parsing
3. Return `None` for emails that do not match the regex pattern
