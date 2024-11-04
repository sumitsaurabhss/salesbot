from langchain_core.tools import tool
from langchain_community.utilities import SQLDatabase
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from model import model

mysql_uri = "mysql+mysqlconnector://root:root@localhost/multiagent_sales_db"

db = SQLDatabase.from_uri(mysql_uri)

toolkit = SQLDatabaseToolkit(db=db, llm=model)

tools = toolkit.get_tools()

#sql_agent_tools = [tool for tool in tools if tool.name in ["sql_db_schema", "sql_db_query_checker"]]
#visual_agent_tools = [tool for tool in tools if tool.name in ["sql_db_query_checker", "sql_db_query"]]

@tool
def get_context() -> dict:
    """returns the context for the query"""
    return toolkit.get_context()


def clean_query(query: str) -> str:
    """Cleans a query string by removing `, ```sqlite and ``` and trailing whitespace.
    Args:
        query: The query string to clean.
    Returns:
        The cleaned query string.
    """

    if query.startswith("```sql"):
        query = query.replace("`", "").strip()
        query = query.replace("sql", "").strip()

    return query

def clean_code(code: str) -> str:
    """Cleans a code string by removing the first line and trailing whitespace.
    Args:
        code: The code string to clean.
    Returns:
        The cleaned code string.
    """

    if code.startswith("```"):
        code = code.replace("```", "").strip()
        code = code.replace("python", "").strip()

    return code