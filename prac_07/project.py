import datetime


class Project:
    """Represent a project."""

    def __init__(self, name, start_date, priority, estimate, completion=0):
        """Construct a Project object."""
        self.name = name
        self.start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y").date()
        self.priority = priority
        self.estimate = estimate
        self.completion = completion

    def __str__(self):
        """Return string representation of a Project."""
        return f"{self.name}, start: {self.start_date.strftime('%d/%m/%Y')}, " \
               f"priority {self.priority}, estimate: ${self.estimate:.2f}, " \
               f"completion: {self.completion}%"