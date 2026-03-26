from setuptools import setup, find_packages

import os


def read_dependencies(file_name: str) -> list[str]:
    """Считывает зависимости из requirements.txt."""
    filepath = os.path.join(os.path.dirname(__file__), file_name)
    with open(filepath, "r", encoding="utf-8") as f:
        dependencies = [
            line.strip() for line in f if line.strip() and not line.startswith("#")
        ]
    return dependencies


def read_long_description(file_name) -> str:
    """Считывает описание из переданного файла."""
    filepath = os.path.join(os.path.dirname(__file__), file_name)
    with open(filepath, "r", encoding="utf-8") as f:
        description = f.read()
    return description


if __name__ == "__main__":
    setup(
        name="theater",
        version="0.1.0",
        package_dir={"": "src"},
        packages=find_packages("src", include=["theater*"]),
        install_requires=[*read_dependencies("requirements.txt")],
        python_requires=">=3.8",
        author="Julya Shapaeva",
        author_email="shapaeva_julya@mail.ru",
        description="Library with theater models and services.",
        long_description=read_long_description("README.md"),
        long_description_content_type="text/markdown",
        url="https://github.com/julyashap/theater_models",
    )
