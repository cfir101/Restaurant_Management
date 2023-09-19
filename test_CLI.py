import unittest
from unittest import TestCase
from menu_items import *
from customer_system import *
from employee_system import *
from CLI import *
from unittest.mock import patch 

class TestMainMenu(TestCase):
    def setUp(self):
        self.main_menu = MainMenu()

    @mock.patch('click.echo')
    @mock.patch('click.prompt')
    def test_display_valid_choice(self, mock_prompt, mock_echo):
        mock_prompt.side_effect = [1, 2]
        with mock.patch.object(MenuItem, 'load_from_csv', return_value=None):
            self.main_menu.display()
            mock_echo.assert_called_with("\nCustomer Menu")

    @mock.patch('click.echo')
    @mock.patch('click.prompt')
    def test_display_invalid_choice(self, mock_prompt, mock_echo):
        mock_prompt.side_effect = [3, 0]
        with self.assertRaises(SystemExit):
            self.main_menu.display()
        error_message = "Invalid choice. Please try again."
        mock_echo.assert_called_with(error_message)

    @mock.patch('click.echo')
    @mock.patch('click.prompt')
    def test_customer_menu_place_order(self, mock_prompt, mock_echo):
        mock_prompt.side_effect = [1, 2]
        with mock.patch.object(OrderSystem, 'place_order', return_value=None):
            self.main_menu.customer_menu()
            mock_echo.assert_called_with("\nGoodbye maybe next time.\n")

    @mock.patch('click.echo')
    @mock.patch('click.prompt')
    def test_customer_menu_exit(self, mock_prompt, mock_echo):
        mock_prompt.side_effect = [2]
        self.main_menu.customer_menu()
        mock_echo.assert_not_called()

    @mock.patch('click.echo')
    @mock.patch('click.prompt')
    def test_customer_menu_invalid_choice(self, mock_prompt, mock_echo):
        mock_prompt.side_effect = [3, 2]
        self.main_menu.customer_menu()
        error_message = "Invalid choice. Please try again."
        mock_echo.assert_called_with(error_message)

    @mock.patch('click.echo')
    def test_employee_menu(self, mock_echo):
        with mock.patch.object(EmployeeSystem, 'Employee_menu', return_value=None):
            self.main_menu.employee_menu()
            mock_echo.assert_called_with("\nGoodbye maybe next time.\n")

    @mock.patch('click.echo')
    def test_exit(self, mock_echo):
        with self.assertRaises(SystemExit):
            self.main_menu.exit()
        mock_echo.assert_called_with("\nGoodbye maybe next time.\n")


if __name__ == '__main__':
    unittest.main()
