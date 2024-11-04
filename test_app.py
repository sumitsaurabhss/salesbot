import unittest
import time
from graph import build_graph

thread = {"configurable": {"thread_id": "1"}}

class TestSQLAgent(unittest.TestCase):

    def setUp(self):
        self.graph = build_graph()

    def test_sales(self):
        time.sleep(1)
        result = self.graph.invoke({"question": "Give all sales"}, thread)
        expected_sql =  "SELECT * FROM sales"
        self.assertEqual(result['sql_query'], expected_sql)

    def test_total_sales_product(self):
        time.sleep(1)
        result = self.graph.invoke({"question": "What are the products available"}, thread)
        expected_sql = "SELECT name FROM products"
        self.assertEqual(result['sql_query'], expected_sql)

    def test_highest_revenue(self):
        time.sleep(1)
        result = self.graph.invoke({"question": "Which product generated highest revenue?"}, thread)
        expected_sql = "SELECT p.name FROM sales s JOIN products p ON s.product_id = p.id GROUP BY p.name ORDER BY SUM(s.revenue) DESC LIMIT 1"
        self.assertEqual("".join(result['sql_query']), expected_sql)

    def test_most_spent_customer(self):
        time.sleep(1)
        result = self.graph.invoke({"question": "Which customer spent the most?"}, thread)
        expected_sql = "SELECT c.name, SUM(s.revenue) AS total_revenue FROM customers c JOIN sales s ON c.id = s.customer_id GROUP BY c.name ORDER BY total_revenue DESC LIMIT 1"
        self.assertEqual("".join(result['sql_query']), expected_sql)

    def test_common_payment_method(self):
        time.sleep(1)
        result = self.graph.invoke({"question": "what is the most preferred method for payment?"}, thread)
        expected_sql =  "SELECT PaymentMethod, COUNT(*) AS Frequency FROM transactions GROUP BY PaymentMethod ORDER BY Frequency DESC LIMIT 1"
        self.assertEqual("".join(result['sql_query']), expected_sql)


if __name__ == '__main__':
    unittest.main()
