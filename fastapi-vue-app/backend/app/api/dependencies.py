from database import database


async def get_db():
    """
    Get the database connection.
    This function can be used in FastAPI dependencies
    to provide a database session.
    """
    return database
