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
