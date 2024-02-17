# python-docker
A simple Python app for [Docker's Python Language Guide](https://docs.docker.com/language/python).

# Instructions
- Use command `rm -rf .git` to remove the git and add yours.

# Docker
- Run your project and use command `docker-compose up -d --build` to build and run the docker project.
- Use command `docker-compose down` to shutdown the project
- You can use command `docker exec -it demo /bin/bash` to go inside container

# Local Development
- `python3 -m venv .venv` create virtual environment
- `source .venv/bin/activate` activate virtual environment on linux system
- `pip install -e .` setup python environment