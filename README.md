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

### Run tests:
`pytest sql_helpers/`


## Implementation notes
Unit tests were written under the assumption that we want to keep comments
associated with each SQL statement with the SQL statement.

It is also assumed that each SQL statement in the script is valid and
is terminated with a semi-colon.

I decided to append the stripped line to each command, rather than the
original. This essentially operates under the assumption that the original
indentation in each SQL statement is not important to the consumer of this
generator. It has the benefit of cleaner looking unit tests.

Limitations of this function:
- Unable to parse multiple SQL statements that might appear on one
line.
- With my swapping of `_line` and `line` - each SQL statement's original indentation
is lost.

Notes on this function:
- For clarity I'd recommend changing variable `line_num` to `cmd_end_line`.
- I'd also suggest re-ordering the variables so they're set & yielded in a consistent
order.