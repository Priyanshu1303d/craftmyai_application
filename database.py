import sqlite3

DB_FILE = "data/projects.db"


def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    # Create projects table if not exists
    cursor.execute(
        """
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT NOT NULL,
                assigned_admin TEXT DEFAULT NULL,
                assignment_status TEXT DEFAULT NULL,
                assigned_by TEXT DEFAULT NULL
            )
    """
    )

    # Create availability table if not exists
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS availability (
            id INTEGER PRIMARY KEY CHECK (id = 1),
            accepting_projects BOOLEAN NOT NULL,
            reopen_date TEXT NOT NULL
        )
    """
    )

    # Insert default availability if not exists
    cursor.execute("SELECT COUNT(*) FROM availability")
    if cursor.fetchone()[0] == 0:
        cursor.execute(
            "INSERT INTO availability (id, accepting_projects, reopen_date) VALUES (1, 1, 'TBA')"
        )

    conn.commit()
    conn.close()


def add_project(name, description):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO projects (name, description) VALUES (?, ?)", (name, description)
    )
    conn.commit()
    conn.close()


def get_projects(assigned=None):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    if assigned is None:
        cursor.execute("SELECT * FROM projects")
    elif assigned:
        cursor.execute(
            "SELECT * FROM projects WHERE assigned_admin IS NOT NULL AND assignment_status = 'accepted'"
        )
    else:
        cursor.execute("SELECT * FROM projects WHERE assigned_admin IS NULL")

    projects = cursor.fetchall()
    conn.close()
    return projects


def delete_project(project_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM projects WHERE id = ?", (project_id,))
    conn.commit()
    conn.close()


def get_availability():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT accepting_projects, reopen_date FROM availability WHERE id = 1"
    )
    result = cursor.fetchone()
    conn.close()

    return {"accepting": bool(result[0]), "reopen_date": result[1]}


def update_availability(status, reopen_date):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE availability SET accepting_projects = ?, reopen_date = ? WHERE id = 1",
        (status, reopen_date),
    )
    conn.commit()
    conn.close()


def assign_project(project_id, admin, assigned_by):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    if admin:
        cursor.execute(
            "UPDATE projects SET assigned_admin = ?, assignment_status = 'pending', assigned_by = ? WHERE id = ?",
            (admin, assigned_by, project_id),
        )
    else:
        cursor.execute(
            "UPDATE projects SET assigned_admin = NULL, assignment_status = NULL, assigned_by = NULL WHERE id = ?",
            (project_id,),
        )
    conn.commit()
    conn.close()


def get_assigned_projects(admin):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM projects WHERE assigned_admin = ? AND assignment_status = 'accepted'",
        (admin,),
    )
    assigned_projects = cursor.fetchall()
    conn.close()
    return assigned_projects


def get_pending_assignments(admin):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM projects WHERE assigned_admin = ? AND assignment_status = 'pending'",
        (admin,),
    )
    pending_assignments = cursor.fetchall()
    conn.close()
    return pending_assignments


def accept_assignment(project_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE projects SET assignment_status = 'accepted' WHERE id = ?", (project_id,)
    )
    conn.commit()
    conn.close()


def reject_assignment(project_id):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE projects SET assigned_admin = NULL, assignment_status = NULL, assigned_by = NULL WHERE id = ?",
        (project_id,),
    )
    conn.commit()
    conn.close()
