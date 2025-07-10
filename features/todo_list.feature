Feature: To-Do List Manager Functionality

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries"
    Then the to-do list should contain "Buy groceries"

  Scenario: List all tasks in the to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Buy milk    |
      | Pay bills   |
    When the user lists all tasks
    Then the output should include:
      | Task        |
      | Buy milk    |
      | Pay bills   |

  Scenario: Mark a task as completed
    Given the to-do list contains a task "Study" with status "Pending"
    When the user marks task "Study" as completed
    Then the task "Study" should be marked as completed

  Scenario: Clear the entire to-do list
    Given the to-do list contains tasks:
      | Task        |
      | Exercise    |
      | Sleep early |
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Remove a task from the to-do list
    Given the to-do list contains tasks:
      | Task     |
      | Laundry  |
      | Cooking  |
    When the user removes task "Laundry"
    Then the to-do list should contain only:
      | Task    |
      | Cooking |

  Scenario: Attempt to complete a non-existent task
    Given the to-do list is empty
    When the user marks task "Walk dog" as completed
    Then an error should be shown
 