"""
This is a CLI expense tracking app.
"""

from datetime import datetime

expenses: list[dict] = (
    []
)  # [{"categoy": "Grocery", "amount": 3000, "date": 12-09-2025}]

category_dict: dict = {
    1: "Grocery",
    2: "Laundry",
    3: "Travelling",
    4: "Wifi & Mobile bills",
    5: "Electricity bill",
    6: "Water Bill",
    7: "Food",
    8: "Gas Bill",
    9: "School Fee",
    10: "Medicines",
    11: "Vehicle Fuel",
    12: "Kids Tuition Fee",
    13: "House Rent",
    14: "Servant Pay",
    15: "Stationary",
    16: "Miscellaneous",
    17: "Restaurant",
}


def is_yes_or_no(get_permission: str) -> str:
    """
    Utility function to get "yes" or "no"
    """
    while get_permission != "y" and get_permission != "n":
        print("Please enter either 'y' or 'n'")
        get_permission = input("Do you wanna add more? Y/N: ").lower()
    return get_permission


def check_category_key(cat_key) -> int:
    """Check if the entered category key exists in the given category dictionary"""
    while cat_key not in category_dict.keys():
        print("Please enter a number present in the above list of expenses categories")
        cat_key = int(input("Pick one number from the given list of expenses please: "))
    return cat_key


def show_expense_categories() -> None:
    """
    List all the category names with serial numbers
    so that users can easily pick them.
    """
    print("Welcome to your expense tracking app.")
    print("Following are the expense categories with their serial numbers.")
    for category_num, category_name in category_dict.items():
        print(f"{category_num}: {category_name}")


def get_expense_numbers():
    """
    Allow users to enter a category number to select an expense category.
    """
    let_add: bool = True
    expense: float = 0
    valid_category_num: int = 0
    while let_add:
        try:
            category_num: int = int(
                input("Pick one number from the given list of expenses please: ")
            )
            valid_category_num: int = check_category_key(category_num)
        except ValueError as e:
            print(f"{e}, please enter a valid category number")
            continue

        while True:
            try:
                expense = float(
                    input(
                        f"Please enter the expense for: {category_dict.get(valid_category_num)}: "
                    )
                )
                break
            except ValueError as e:
                print(f"{e}, please enter a valid amount")

        expenses.append(
            {
                "category": category_dict.get(valid_category_num),
                "amount": expense,
                "date": datetime.now().date(),
            }
        )
        get_permission: str = input("Do you wanna add more? Y/N: ").lower()
        to_coninue = is_yes_or_no(get_permission)
        if to_coninue == "y":
            let_add = True
        else:
            let_add = False


def calculate_expenses() -> str:
    """
    Add all the expenses
    """
    total_expense: float = 0
    for i in expenses:
        total_expense += i["amount"]

    return f"Total Expense: {total_expense}"


def show_result() -> None:
    """
    Show category name with its expense, and total expenses
    """
    for i in expenses:
        print(f"{i["category"]}: {i["amount"]}: {i["date"]}")
    print(calculate_expenses())


def main_func():
    """
    entry point
    """
    show_expense_categories()
    get_expense_numbers()
    print("\n")
    show_result()


main_func()
