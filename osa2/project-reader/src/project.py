class Project:
    def __init__(self, name, description, license, authors, dependencies, dev_dependencies):
        self.name = name
        self.description = description
        self.license = license
        self.authors = authors
        self.dependencies = dependencies
        self.dev_dependencies = dev_dependencies

    def __str__(self):
        authors_formatted = "\n- ".join(self.authors) if self.authors else "N/A"
        dependencies_formatted = "\n- ".join(self.dependencies) if self.dependencies else "N/A"
        dev_dependencies_formatted = "\n- ".join(self.dev_dependencies) if self.dev_dependencies else "N/A"

        return (
            f"Name: {self.name}\n"
            f"Description: {self.description}\n"
            f"License: {self.license}\n\n"
            f"Authors:\n- {authors_formatted}\n\n"
            f"Dependencies:\n- {dependencies_formatted}\n\n"
            f"Development dependencies:\n- {dev_dependencies_formatted}"
        )
