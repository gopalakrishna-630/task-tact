# TaskTact

TaskTact is a modern, terminal-based task management application built in Python. It features a beautiful command-line interface powered by the `rich` library, providing a clean, organized, and interactive way to manage your day-to-day to-do list directly from your terminal.

## Features

- **Task Management**: Seamlessly add, view, update, complete, and delete tasks.
- **Rich Terminal UI**: Enjoy a visually pleasing interface with colorful tables, panels, and input prompts.
- **Advanced Search & Filter**: 
  - Perform a **Global Search** across all task fields (ID, title, description, tags).
  - Filter tasks dynamically by Category, Priority, and Status.
  - View tasks categorized by timeline (Due Today, Due This Week, Overdue).
- **Interactive Numeric Selection**: Select categories, priorities, and statuses quickly via numbered lists—no need to type out full strings!
- **Detailed Reports**: Generate dashboards, completion rates, and breakdowns by category or priority.
- **Data Persistence**: Tasks are securely saved to a local JSON file (`data/tasks.json`).
- **Backup & Restore**: Easily backup your task data or completely reset the application from the Settings menu.

## Requirements

- Python 3.8+
- [Rich](https://github.com/Textualize/rich) (Terminal formatting library)

## Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd TaskTact
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

TaskTact is structured as a standard Python module. To launch the interactive application, run the following command from the root of the project:

```bash
python3 -m tasktact
```

Follow the on-screen numbered prompts to navigate the menus and manage your tasks.

## Project Structure

The project strictly follows modern Python application standards to keep the source code clean and separated from data artifacts:

```text
TaskTact/
├── tasktact/               # Core application package
│   ├── __init__.py         
│   ├── __main__.py         # Entry point (run via python3 -m tasktact)
│   ├── menus.py            # Menu configurations
│   ├── core/               # Validation, themes, constants
│   ├── models/             # Data models (Task)
│   ├── services/           # Business logic (Filtering, Searching, Reporting)
│   ├── storage/            # JSON reading, writing, and backup handling
│   └── ui/                 # Rich UI components, tables, and input prompts
├── data/                   # Dedicated folder for data persistence
│   └── tasks.json          # Your local database
├── tests/                  # Unit and integration tests
├── requirements.txt        # Project dependencies
└── README.md               # Documentation
```

## Contributing

Feel free to open an issue or submit a pull request if you'd like to improve the search algorithms, add new reporting metrics, or suggest UI enhancements.

## License

This project is licensed under the MIT License.
