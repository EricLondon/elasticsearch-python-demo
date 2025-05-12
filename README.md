# Elasticsearch Python Demo

## Prerequisites

- [Docker](https://docs.docker.com/desktop/setup/install/mac-install/)

- [homebrew](https://brew.sh/)

- [pyenv](https://github.com/pyenv/pyenv)

## Local setup

```bash
# install homebrew, example:
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# install pyenv
brew install pyenv

# install python 3.12.x
pyenv install 3.12

# check python version
python --version
Python 3.12.9

# check python binary path
which python
/Users/ericlondon/.pyenv/shims/python

# update pip
pip install --upgrade pip

# install poetry
pip install poetry

# check poetry path
which poetry
/Users/ericlondon/.pyenv/shims/poetry

# git clone this repo

# install poetry/pip dependencies
poetry install
```

## Docker Setup

```bash
# start elasticsearch via docker compose
docker compose up

# check elasticsearch is running
curl http://localhost:9200/ admin:e46yYv8rTVy3EgbTTs

# response:
{
  "name" : "es01",
  "cluster_name" : "elasticsearch-demo",
  "cluster_uuid" : "ME_mS6E2RuiJcutCH8JrKw",
  "version" : {
    "number" : "8.7.1",
    "build_flavor" : "default",
    "build_type" : "docker",
    "build_hash" : "f229ed3f893a515d590d0f39b05f68913e2d9b53",
    "build_date" : "2023-04-27T04:33:42.127815583Z",
    "build_snapshot" : false,
    "lucene_version" : "9.5.0",
    "minimum_wire_compatibility_version" : "7.17.0",
    "minimum_index_compatibility_version" : "7.0.0"
  },
  "tagline" : "You Know, for Search"
}
```

## Usage

```bash
# populate people
poetry run populate_people

# get person
poetry run get_person Eric
```



