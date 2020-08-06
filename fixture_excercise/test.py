import sqlite3

class ParameterDatabase:
    def __init__(self, owner="app"):
        self.db = sqlite3.connect("test.db")
        self.dbc = self.db.cursor()
        self.owner = owner
        self.dbc.execute("CREATE TABLE IF NOT EXISTS params(owner TEXT, name TEXT, value TEXT)")
        self.dbc.execute("CREATE UNIQUE INDEX IF NOT EXISTS params_pk ON params(owner, name)")

    def get(self, name):
        """Get the parameter value from database. Returns None if no such parameter exists."""
        self.dbc.execute("SELECT value FROM params WHERE owner=? AND name=?", [self.owner, name])
        row = self.dbc.fetchone()
        return row[0] if row else None
    
    def put(self, name, value):
        """Set the parameter value in database."""
        self.dbc.execute("REPLACE INTO params(owner, name, value) VALUES(?, ?, ?)", [self.owner, name, value])

    def clear(self):
        """Clear all parameters."""
        self.dbc.execute("DELETE FROM params WHERE owner=?", [self.owner])

    def close(self):
        self.db.commit()
        self.db.close()

# Fix following issues in test cases
# - remove code repetition
# - test data remains in database after tests are complete

def test_can_put_and_get():
    params = ParameterDatabase("automated-test")
    params.put("somename", "somevalue")
    assert params.get("somename") == "somevalue"
    params.close()

def test_cannot_get_non_existing():
    params = ParameterDatabase("automated-test")
    assert params.get("nosuchname") == None
    params.close()

def test_can_update():
    params = ParameterDatabase("automated-test")
    params.put("anothername", "somevalue")
    params.put("anothername", "anothervalue")
    assert params.get("anothername") == "anothervalue"
    params.close()
