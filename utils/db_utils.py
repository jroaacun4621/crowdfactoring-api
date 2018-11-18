
def create_autocommit_session(database):
    """
    Begin transaction from a database autocommit session, used for "select" SQL sentences
    :param database: fask.ext.sqlalchemy, database to create the session and start the transaction
    :return: sqlalchemy.orm.session.SessionTransaction, Transactional token which is compatible with the with statement
    """
    return database.create_scoped_session({"autocommit": True})