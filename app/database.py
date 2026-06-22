import sqlite3

DATABASE_NAME = "vision.db"


def init_db():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS analysis_history (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            image_name TEXT,

            description TEXT,

            what_it_is TEXT,

            how_it_works TEXT,

            why_important TEXT,

            fun_fact TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
        """
    )

    conn.commit()

    conn.close()


def save_analysis(
    image_name,
    result
):

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis_history (

            image_name,
            description,
            what_it_is,
            how_it_works,
            why_important,
            fun_fact

        )

        VALUES (?, ?, ?, ?, ?, ?)
        """,
        (
            image_name,
            result["description"],
            result["what_it_is"],
            result["how_it_works"],
            result["why_important"],
            result["fun_fact"]
        )
    )

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(
        DATABASE_NAME
    )

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *
        FROM analysis_history
        ORDER BY created_at DESC
        """
    )

    rows = cursor.fetchall()

    conn.close()

    return [
        dict(row)
        for row in rows
    ]