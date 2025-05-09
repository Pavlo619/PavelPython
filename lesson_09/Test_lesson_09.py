from sqlalchemy import create_engine


db = "postgresql://postgres:123@localhost:5432/postgres"


db_connect = create_engine(db)


def test_add_subject():
    connect = db_connect.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (16, 'Chinese')")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 16")
    assert result.rowcount == 1
    connect.execute("delete from subject where subject_id = 16")


def test_update_subject():
    connect = db_connect.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (16, 'Chinese')")
    connect.execute("UPDATE subject SET subject_title = 'Portuguese' WHERE subject_id = 16")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 16").fetchall()
    assert result[0][1] == 'Portuguese'
    connect.execute("delete from subject where subject_id = 16")


def test_delete_subject():
    connect = db_connect.connect()
    connect.execute("INSERT INTO subject (subject_id, subject_title) values (16, 'Chinese')")
    connect.execute("DELETE FROM subject WHERE subject_id = 16")
    result = connect.execute("SELECT * FROM subject WHERE subject_id = 16")
    assert result.rowcount == 0
