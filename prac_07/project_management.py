import datetime


def load_projects_from_file(filename):
    projects = []
    with open(filename, "r") as file:
        header = file.readline().strip().split("\t")
        for line in file:
            data = line.strip().split("\t")
            name, start_date, priority, estimate, completion = data
            project = Project(name, start_date, int(priority), float(estimate), int(completion))
            projects.append(project)
    return projects


def save_projects_to_file(filename, projects):
    with open(filename, "w") as file:
        file.write("Name\tStart Date\tPriority\tEstimate\tCompletion\n")
        for project in projects:
            file.write(f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t"
                       f"{project.priority}\t{project.estimate:.2f}\t{project.completion}\n")


def display_projects(projects):
    incomplete_projects = [project for project in projects if project.completion < 100]
    completed_projects = [project for project in projects if project.completion == 100]

    print("Incomplete projects:")
    for project in sorted(incomplete_projects, key=lambda p: p.priority):
        print(f"  {project}")

    print("Completed projects:")
    for project in sorted(completed_projects, key=lambda p: p.priority):
        print(f"  {project}")


def filter_projects_by_date(projects):
    date_string = input("Show projects that start after date (dd/mm/yyyy): ")
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()

    filtered_projects = [project for project in projects if project.start_date > date]
    for project in sorted(filtered_projects, key=lambda p: p.start_date):
        print(f"  {project}")