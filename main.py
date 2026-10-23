"""R8: command-line interface for the gym membership quote."""

from gym.membership import quote_membership


def ask_plan():
    """Read the plan from the user."""
    return input("Plan (BASIC, STANDARD, PREMIUM): ").strip().upper()


def ask_extras():
    """Read zero or more extras, separated by commas."""
    raw = input("Extras (comma separated, blank for none): ").strip()
    if not raw:
        return []
    return [extra.strip().upper() for extra in raw.split(",") if extra.strip()]


def ask_members():
    """Read the number of members. A non-numeric answer is invalid."""
    raw = input("Number of members: ").strip()
    try:
        return int(raw)
    except ValueError:
        return -1


def ask_confirmation():
    """Ask the user to confirm the quote."""
    return input("Confirm? (y/n): ").strip().lower() == "y"


def run():
    """Ask for the selection, show the quote and return the final result."""
    plan = ask_plan()
    extras = ask_extras()
    members = ask_members()

    quote = quote_membership(plan, extras, members)

    if quote["total"] == -1:
        print("Invalid selection.")
        print("Total: -1")
        return -1

    print(f"Subtotal: {quote['subtotal']}")
    print(f"After group discount (R4): {quote['after_group_discount']}")
    print(f"After special offer (R5): {quote['after_special_offer']}")
    print(f"After premium surcharge (R6): {quote['after_premium_surcharge']}")
    print(f"Total: {quote['total']}")

    if not ask_confirmation():
        print("Total: -1")
        return -1

    return quote["total"]


if __name__ == "__main__":
    run()
