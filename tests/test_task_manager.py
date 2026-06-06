import unittest
from datetime import datetime, timedelta

import task_utils
import validation


class TaskManagerTests(unittest.TestCase):
    def setUp(self):
        task_utils.tasks.clear()

    def test_add_task_success(self):
        task = task_utils.add_task(
            "Test Task",
            "This is a test task.",
            (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )

        self.assertEqual(task["title"], "Test Task")
        self.assertEqual(task["description"], "This is a test task.")
        self.assertFalse(task["completed"])
        self.assertEqual(len(task_utils.tasks), 1)

    def test_mark_task_as_complete(self):
        task_utils.add_task(
            "Complete Task",
            "Complete this task.",
            (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )
        completed_task = task_utils.mark_task_as_complete(0)

        self.assertTrue(completed_task["completed"])
        self.assertTrue(task_utils.tasks[0]["completed"])

    def test_view_pending_tasks_no_error(self):
        pending = task_utils.view_pending_tasks()
        self.assertEqual(pending, [])

        task_utils.add_task(
            "Pending Task",
            "This task is pending.",
            (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )
        self.assertEqual(len(task_utils.view_pending_tasks()), 1)

        task_utils.mark_task_as_complete(0)
        self.assertEqual(task_utils.view_pending_tasks(), [])

    def test_calculate_progress(self):
        self.assertEqual(task_utils.calculate_progress(), 0)

        task_utils.add_task(
            "Task 1",
            "First task.",
            (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )
        self.assertEqual(task_utils.calculate_progress(), 0)

        task_utils.mark_task_as_complete(0)
        self.assertEqual(task_utils.calculate_progress(), 100)

        task_utils.add_task(
            "Task 2",
            "Second task.",
            (datetime.today() + timedelta(days=2)).strftime("%Y-%m-%d"),
        )
        self.assertEqual(task_utils.calculate_progress(), 50)

    def test_validate_task_title_and_description(self):
        self.assertTrue(validation.validate_task_title("Valid title"))
        self.assertFalse(validation.validate_task_title("   "))
        self.assertFalse(validation.validate_task_title(123))

        self.assertTrue(validation.validate_task_description("Valid description"))
        self.assertFalse(validation.validate_task_description(""))
        self.assertFalse(validation.validate_task_description(None))

    def test_validate_due_date(self):
        valid_date = (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d")
        self.assertTrue(validation.validate_due_date(valid_date))
        self.assertFalse(validation.validate_due_date("2020-01-01"))
        self.assertFalse(validation.validate_due_date("not-a-date"))

    def test_add_task_invalid_values_raise(self):
        with self.assertRaises(ValueError):
            task_utils.add_task("", "Description", "2099-01-01")

        with self.assertRaises(ValueError):
            task_utils.add_task("Title", "", "2099-01-01")

        with self.assertRaises(ValueError):
            task_utils.add_task("Title", "Description", "invalid-date")

    def test_mark_task_as_complete_invalid_index(self):
        with self.assertRaises(IndexError):
            task_utils.mark_task_as_complete(0)

        task_utils.add_task(
            "Task",
            "Description",
            (datetime.today() + timedelta(days=1)).strftime("%Y-%m-%d"),
        )
        with self.assertRaises(IndexError):
            task_utils.mark_task_as_complete(1)

        with self.assertRaises(TypeError):
            task_utils.mark_task_as_complete("0")


if __name__ == "__main__":
    unittest.main()
