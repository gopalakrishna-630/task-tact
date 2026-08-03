import sys
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from datetime import datetime

from ui.layout import create_layout
from ui.input import ask, ask_yes_no, pause
from ui.tables import build_task_table
from ui.dialogs import success, error, warning, info

from services.task_service import TaskService
from services.search_service import SearchService
from services.filter_service import FilterService
from services.report_service import ReportService
from services.settings_service import SettingsService

from core.utils import clear_screen
from core.constants import CATEGORIES, PRIORITIES, STATUS
from core.validator import validate_date

import menus

console = Console()

class App:
    def __init__(self):
        self.menu_title = "Main Menu"
        self.menu_items = menus.MAIN_MENU
        self.content = info("Welcome to TaskTact\n\nSelect an option from the menu.")
        
    def set_menu(self, title, items):
        self.menu_title = title
        self.menu_items = items
        self.content = info(f"{title} Options")
        
    def handle_main_menu(self, choice: str) -> None:
        if choice == "1":
            self.set_menu("Task Menu", menus.TASK_MENU)
        elif choice == "2":
            self.set_menu("Search Menu", menus.SEARCH_MENU)
        elif choice == "3":
            self.set_menu("Filter Menu", menus.FILTER_MENU)
        elif choice == "4":
            self.set_menu("Report Menu", menus.REPORT_MENU)
        elif choice == "5":
            self.set_menu("Settings Menu", menus.SETTINGS_MENU)
        elif choice == "0":
            console.print("\nGoodbye!\n")
            sys.exit(0)
        else:
            self.content = error("Invalid Choice")

    def handle_task_menu(self, choice: str) -> None:
        if choice == "1":
            title = ""
            while not title:
                title = ask("Title")
                if not title:
                    console.print("[red]Title cannot be empty. Please try again.[/red]")
            
            description = ask("Description")
            
            console.print(f"Categories: {', '.join(CATEGORIES)}")
            category = ""
            while category not in CATEGORIES:
                category = ask("Category")
                if category not in CATEGORIES:
                    console.print("[red]Invalid Category. Please try again.[/red]")
                
            console.print(f"Priorities: {', '.join(PRIORITIES)}")
            priority = ""
            while priority not in PRIORITIES:
                priority = ask("Priority (High/Medium/Low)")
                if priority not in PRIORITIES:
                    console.print("[red]Invalid Priority. Please try again.[/red]")
                
            deadline = ""
            while True:
                deadline = ask("Deadline (YYYY-MM-DD)")
                if not validate_date(deadline):
                    console.print("[red]Invalid date format. Must be YYYY-MM-DD. Please try again.[/red]")
                    continue
                dt = datetime.strptime(deadline, "%Y-%m-%d")
                if dt.date() < datetime.now().date():
                    console.print("[red]Date cannot be in the past. Please try again.[/red]")
                    continue
                break
            
            try:
                TaskService.create_task(title, description, category, priority, deadline)
                self.content = success("Task added successfully!")
            except Exception as e:
                self.content = error(str(e))
                
        elif choice == "2":
            tasks = TaskService.get_all_tasks()
            if not tasks:
                self.content = warning("No tasks found.")
            else:
                self.content = build_task_table(tasks)
                
        elif choice == "3":
            task_id = ask("Enter Task ID to update")
            task = SearchService.by_id(task_id)
            if not task:
                self.content = error("Task not found.")
                return
                
            console.print("Leave blank to keep current value.")
            title = ask(f"Title [{task.title}]") or task.title
            description = ask(f"Description [{task.description}]") or task.description
            
            while True:
                category = ask(f"Category [{task.category}]") or task.category
                if category in CATEGORIES:
                    break
                console.print("[red]Invalid Category. Please try again.[/red]")
                
            while True:
                priority = ask(f"Priority [{task.priority}]") or task.priority
                if priority in PRIORITIES:
                    break
                console.print("[red]Invalid Priority. Please try again.[/red]")
                
            while True:
                deadline = ask(f"Deadline [{task.deadline}]") or task.deadline
                if not validate_date(deadline):
                    console.print("[red]Invalid date format. Must be YYYY-MM-DD. Please try again.[/red]")
                    continue
                dt = datetime.strptime(deadline, "%Y-%m-%d")
                if dt.date() < datetime.now().date():
                    console.print("[red]Date cannot be in the past. Please try again.[/red]")
                    continue
                break
                
            updated = TaskService.update_task(task_id, title=title, description=description, category=category, priority=priority, deadline=deadline)
            if updated:
                self.content = success("Task updated successfully!")
            else:
                self.content = error("Failed to update task.")
                
        elif choice == "4":
            task_id = ask("Enter Task ID to complete")
            if TaskService.complete_task(task_id):
                self.content = success("Task marked as completed!")
            else:
                self.content = error("Task not found or update failed.")
                
        elif choice == "5":
            task_id = ask("Enter Task ID to delete")
            if TaskService.delete_task(task_id):
                self.content = success("Task deleted successfully!")
            else:
                self.content = error("Task not found.")
                
        elif choice == "0":
            self.set_menu("Main Menu", menus.MAIN_MENU)
        else:
            self.content = error("Invalid Choice")

    def handle_search_menu(self, choice: str) -> None:
        tasks = []
        if choice == "1":
            val = ask("Enter Task ID")
            task = SearchService.by_id(val)
            if task:
                tasks = [task]
        elif choice == "2":
            val = ask("Enter Title keyword")
            tasks = SearchService.by_title(val)
        elif choice == "3":
            val = ask("Enter Description keyword")
            tasks = SearchService.by_description(val)
        elif choice == "4":
            val = ask("Enter Category")
            tasks = SearchService.by_category(val)
        elif choice == "5":
            val = ask("Enter Priority")
            tasks = SearchService.by_priority(val)
        elif choice == "6":
            val = ask("Enter Status")
            tasks = SearchService.by_status(val)
        elif choice == "7":
            val = ask("Enter Tag")
            tasks = SearchService.by_tag(val)
        elif choice == "0":
            self.set_menu("Main Menu", menus.MAIN_MENU)
            return
        else:
            self.content = error("Invalid Choice")
            return
            
        if tasks:
            self.content = build_task_table(tasks)
        else:
            if choice in [str(i) for i in range(1, 8)]:
                self.content = warning("No tasks found.")

    def handle_filter_menu(self, choice: str) -> None:
        tasks = []
        if choice == "1":
            val = ask("Enter Category")
            tasks = FilterService.by_category(val)
        elif choice == "2":
            val = ask("Enter Priority")
            tasks = FilterService.by_priority(val)
        elif choice == "3":
            val = ask("Enter Status")
            tasks = FilterService.by_status(val)
        elif choice == "4":
            tasks = FilterService.completed()
        elif choice == "5":
            tasks = FilterService.pending()
        elif choice == "6":
            tasks = FilterService.overdue()
        elif choice == "7":
            tasks = FilterService.due_today()
        elif choice == "8":
            tasks = FilterService.due_this_week()
        elif choice == "0":
            self.set_menu("Main Menu", menus.MAIN_MENU)
            return
        else:
            self.content = error("Invalid Choice")
            return
            
        if tasks:
            self.content = build_task_table(tasks)
        else:
            if choice in [str(i) for i in range(1, 9)]:
                self.content = warning("No tasks found matching filter.")

    def handle_report_menu(self, choice: str) -> None:
        if choice == "1":
            data = ReportService.dashboard()
            lines = [f"{k.capitalize()}: {v}" for k, v in data.items()]
            self.content = info("\n".join(lines))
        elif choice == "2":
            rate = ReportService.completion_rate()
            self.content = info(f"Completion Rate: {rate}%")
        elif choice == "3":
            data = ReportService.category_report()
            lines = [f"{k}: {v}" for k, v in data.items()]
            self.content = info("\n".join(lines) if lines else "No data.")
        elif choice == "4":
            data = ReportService.priority_report()
            lines = [f"{k}: {v}" for k, v in data.items()]
            self.content = info("\n".join(lines) if lines else "No data.")
        elif choice == "5":
            data = ReportService.status_report()
            lines = [f"{k}: {v}" for k, v in data.items()]
            self.content = info("\n".join(lines) if lines else "No data.")
        elif choice == "6":
            tasks = ReportService.recent_tasks()
            if tasks:
                self.content = build_task_table(tasks)
            else:
                self.content = warning("No recent tasks.")
        elif choice == "0":
            self.set_menu("Main Menu", menus.MAIN_MENU)
        else:
            self.content = error("Invalid Choice")

    def handle_settings_menu(self, choice: str) -> None:
        if choice == "1":
            if SettingsService.backup_data():
                self.content = success("Backup created successfully!")
            else:
                self.content = error("Failed to create backup.")
        elif choice == "2":
            if SettingsService.restore_data():
                self.content = success("Data restored successfully!")
            else:
                self.content = error("Failed to restore data.")
        elif choice == "3":
            if ask_yes_no("Are you sure you want to reset all data?"):
                if SettingsService.reset_application():
                    self.content = success("Application reset successfully!")
                else:
                    self.content = error("Failed to reset application.")
            else:
                self.content = info("Reset cancelled.")
        elif choice == "4":
            info_dict = SettingsService.application_info()
            lines = [f"{k.replace('_', ' ').capitalize()}: {v}" for k, v in info_dict.items()]
            self.content = info("\n".join(lines))
        elif choice == "0":
            self.set_menu("Main Menu", menus.MAIN_MENU)
        else:
            self.content = error("Invalid Choice")

    def run(self):
        while True:
            try:
                clear_screen()
                TaskService.update_overdue_tasks()
                dashboard_data = ReportService.dashboard()
                
                layout = create_layout(
                    menu_title=self.menu_title,
                    menu_items=self.menu_items,
                    dashboard_data=dashboard_data,
                )
                
                layout["content"].update(self.content)
                
                console.print(layout)
                
                while True:
                    choice = ask("\nSelect Option")
                    valid_keys = [item["key"] for item in self.menu_items]
                    if choice in valid_keys:
                        break
                    console.print("[red]Invalid Choice. Please try again.[/red]")
                
                if self.menu_title == "Main Menu":
                    self.handle_main_menu(choice)
                elif self.menu_title == "Task Menu":
                    self.handle_task_menu(choice)
                elif self.menu_title == "Search Menu":
                    self.handle_search_menu(choice)
                elif self.menu_title == "Filter Menu":
                    self.handle_filter_menu(choice)
                elif self.menu_title == "Report Menu":
                    self.handle_report_menu(choice)
                elif self.menu_title == "Settings Menu":
                    self.handle_settings_menu(choice)
                    
            except KeyboardInterrupt:
                console.print("\nInterrupted. Exiting...\n")
                sys.exit(0)
            except Exception as e:
                self.content = error(f"An unexpected error occurred: {str(e)}")

def main():
    app = App()
    app.run()

if __name__ == "__main__":
    main()
