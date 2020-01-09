# Welcome to sql-parser!
This is the slickest tool for manipulating SQL statements. This library
contains the infamous iter_commands function which, when passed a string of
SQL commands creates a generator that yields each individual SQL statement,
while ignoring any comments.


## Initial setup

### Create environment
`conda env create -f environment.yml`

### Activate environment
`conda activate sql-helper`

### Install sql_helpers library
`pip install -e .`

### Run unit tests (coming soon in a PR):
`pytest sql_helpers/`


## Implementation notes
Unit tests were written under the assumption that we want to keep comments
associated with each SQL statement with the SQL statement.

I decided to append the stripped line to each command, rather than the
original. This essentially operates under the assumption that the original
indentation in each SQL statement is not important to the consumer of this
generator. It has the benefit of cleaner looking unit tests.

