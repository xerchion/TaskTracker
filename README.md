# Task Tracker CLI

## Description
Task Tracker CLI is a simple command-line application that allows you to add, update, mark, and delete tasks in a JSON file. The application also lets you view a list of tasks based on their status.


This project is part of the [roadmap.sh](https://roadmap.sh/) backend learning path. It serves as a hands-on exercise to reinforce concepts and skills in backend development.


## Usage
To execute the commands, the `python TaskTracker.py` command should be followed by the appropriate subcommands and arguments based on the operation you wish to perform. The specific commands for each operation are listed below.
### Add Task

To add a new task, use the `add`command followed by the task description.

```bash
python TaskTracker.py add "somthing to do"
```

### List Tasks

To list tasks based on their status, use the `list` command with an argument specifying "todo", "in-progress", or "done". All tasks can be displayed by omitting the status argument.

```bash
python TaskTracker.py list "todo"
python TaskTracker.py list
```

### Update Task Description

To update a task's description, use the `update` command followed by the task ID and the new description.

```bash
python TaskTracker.py 2 "I need to do this other thing"
```

### Mark Task Status

To mark a task as "in-progress" or "done," use the `mark` command along with the task ID and the desired status.

```bash
python TaskTracker.py mark-in-progress 1
python TaskTracker.py mark-done 2
```

### Delete Task

To delete a task, use the `delete` command followed by the task ID you wish to remove.

```bash
python TaskTracker.py delete 2
```
### Technical Notes


- **Programming Paradigm**:
This project is designed using object-oriented programming principles, ensuring modularity and reusability of code.
- **Testing**:
Unit tests are written using pytest and unittest to ensure functionality and catch issues early. Test coverage is monitored using coverage to ensure that all parts of the codebase are adequately tested.
- **Code Quality**:
The project adheres to best practices in programming, including consistent code style and design patterns. Type hinting is employed for code clarity and to assist in maintaining a clear and understandable codebase.
- **Linting**: Code linting tools are used to enforce coding standards and improve code quality. Type checking is utilized to catch potential type errors and enhance code readability.
## Contact


If you have any questions, feel free to reach out:

Email: xerchion@gmail.com

GitHub: [Sergio U.B.](https://github.com/xerchion)

## Project Link

For more details about this project, visit the [Task Tracker Project Roadmap](https://roadmap.sh/projects/task-tracker).