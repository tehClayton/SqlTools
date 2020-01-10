import pytest

from sql_helpers.iter_commands import iter_commands


@pytest.mark.parametrize(
    "input,expected",
    [
        # Single SQL statement
        (
            "SELECT * FROM users;",
            [(1, 1, 1, "SELECT * FROM users;")]
        ),
        # Single SQL statement preceded by comment
        (
            """
                # Get all users
                SELECT * FROM users;
            """,
            [(3, 1, 1, "\n# Get all users\nSELECT * FROM users;")]
        ),
        # Single SQL statement with comment in middle of statement
        (
            """
                # Get all users
                SELECT
                    # User ids only!
                    id
                FROM users;
            """,
            [(6, 1, 1, "\n# Get all users\nSELECT\n# User ids only!\nid\nFROM users;")]
        ),
        # Single SQL statement followed by comment
        (
            """
                SELECT * FROM users;

                # Get all users with similar interests
            """,
            [(2, 1, 1, "\nSELECT * FROM users;")]
        ),
        # Two SQL statements each with comments
        (
            """
                # Get all users
                SELECT * FROM users;

                # Get all users with similar interests
                SELECT * FROM
                    users
                WHERE interest IN ('audiobooks', 'drums');
            """,
            [
                (3, 1, 1, "\n# Get all users\nSELECT * FROM users;"),
                (8, 4, 2, "\n# Get all users with similar interests\n"
                          "SELECT * FROM\nusers\nWHERE interest IN ('audiobooks', 'drums');")
            ]
        ),
        # Three SQL statements each with comments
        (
            """
                # Get all users
                SELECT * FROM users;

                # Get all users with similar interests
                SELECT * FROM
                    users
                WHERE interest IN ('audiobooks', 'drums');

                # Get all users with dissimilar interests
                SELECT * FROM
                    users
                WHERE interest NOT IN ('audiobooks', 'drums');
            """,
            [
                (3, 1, 1, "\n# Get all users\nSELECT * FROM users;"),
                (8, 4, 2, "\n# Get all users with similar interests\n"
                          "SELECT * FROM\nusers\nWHERE interest IN ('audiobooks', 'drums');"),
                (13, 9, 3, "\n# Get all users with dissimilar interests\n"
                           "SELECT * FROM\nusers\nWHERE interest NOT IN ('audiobooks', 'drums');")
            ]
        ),
        # Single SQL statement with semi-colon on newline
        (
            """
                # Get all users
                SELECT * FROM users
                ;
            """,
            [(4, 1, 1, "\n# Get all users\nSELECT * FROM users\n;")]
        ),
        # Single SQL statement with semi-colon at end of comment
        (
            """
                # Get all users;
                SELECT * FROM users;
            """,
            [(3, 1, 1, "\n# Get all users;\nSELECT * FROM users;")]
        ),
        # Single SQL statement with semi-colon in middle of comment
        (
            """
                # Get all; users
                SELECT * FROM users;
            """,
            [(3, 1, 1, "\n# Get all; users\nSELECT * FROM users;")]
        ),
    ]
)
def test_iter_commands(input, expected):
    result = list(iter_commands(input))

    assert result == expected
