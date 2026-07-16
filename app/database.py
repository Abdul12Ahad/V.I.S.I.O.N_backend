import sqlite3
import json

DATABASE_NAME = "vision.db"


def init_db():

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS analysis_history(

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            image_name TEXT,

            description TEXT,

            what_it_is TEXT,

            how_it_works TEXT,

            why_important TEXT,

            fun_fact TEXT,

            key_concepts TEXT,

            related_topics TEXT,

            learn_more TEXT,

            learning_level TEXT,

            image_path TEXT,

            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

        )
    """)

    conn.commit()
    conn.close()


def save_analysis(
    image_name,
    level,
    image_path,
    result
):

    conn = sqlite3.connect(DATABASE_NAME)

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO analysis_history(

            image_name,
            description,
            what_it_is,
            how_it_works,
            why_important,
            fun_fact,
            key_concepts,
            related_topics,
            learn_more,
            learning_level,
            image_path

        )

        VALUES(?,?,?,?,?,?,?,?,?,?,?)

        """,
        (

            image_name,

            result["description"],

            result["what_it_is"],

            result["how_it_works"],

            result["why_important"],

            result["fun_fact"],

            json.dumps(result["key_concepts"]),

            json.dumps(result["related_topics"]),

            json.dumps(result["learn_more"]),

            level,

            image_path

        )
    )

    conn.commit()

    conn.close()


def get_history():

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute("""

        SELECT *

        FROM analysis_history

        ORDER BY created_at DESC

    """)

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:

        item = dict(row)

        item["key_concepts"] = json.loads(item["key_concepts"] or "[]")

        item["related_topics"] = json.loads(item["related_topics"] or "[]")

        item["learn_more"] = json.loads(item["learn_more"] or "[]")

        history.append(item)

    return history

def search_history(query):

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT *

        FROM analysis_history

        WHERE

            image_name LIKE ?
            OR description LIKE ?
            OR what_it_is LIKE ?

        ORDER BY created_at DESC
        """,

        (
            f"%{query}%",
            f"%{query}%",
            f"%{query}%"
        )
    )

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:

        item = dict(row)

        item["key_concepts"] = json.loads(item["key_concepts"] or "[]")
        item["related_topics"] = json.loads(item["related_topics"] or "[]")
        item["learn_more"] = json.loads(item["learn_more"] or "[]")

        history.append(item)

    return history

def get_recent_learning(limit=3):

    conn = sqlite3.connect(DATABASE_NAME)

    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            description,
            key_concepts

        FROM analysis_history

        ORDER BY id DESC

        LIMIT ?
        """,
        (limit,)
    )

    rows = cursor.fetchall()

    conn.close()

    history = []

    for row in rows:

        history.append({

            "description": row["description"],

            "key_concepts": json.loads(
                row["key_concepts"] or "[]"
            )

        })

    return history