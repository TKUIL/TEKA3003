from urllib import request
import tomli
from project import Project

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # Tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # Deserialisoi TOML-formaatissa oleva merkkijono
        toml_data = tomli.loads(content)

        # Haetaan tiedot deserialisoidusta TOML-datasta
        name = toml_data.get("tool", {}).get("poetry", {}).get("name", "N/A")
        description = toml_data.get("tool", {}).get("poetry", {}).get("description", "N/A")
        license = toml_data.get("tool", {}).get("poetry", {}).get("license", "N/A")
        authors = toml_data.get("tool", {}).get("poetry", {}).get("authors", [])

        # Riippuvuudet ja kehityksen aikaiset riippuvuudet
        dependencies = list(toml_data.get("tool", {}).get("poetry", {}).get("dependencies", {}).keys())
        dev_dependencies = list(toml_data.get("tool", {}).get("poetry", {}).get("group", {}).get("dev", {}).get("dependencies", {}).keys())

        # Palauta Project-olio tiedoilla
        return Project(name, description, license, authors, dependencies, dev_dependencies)
