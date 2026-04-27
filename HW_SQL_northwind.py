from lecture_31_SQL import create_connection, execute_query, select_query

if __name__ == '__main__':
    connection = create_connection('northwind.db')

    # 1. Вибрати замовлення, що мають бути відвантажені в країну, що починається з N відсортувати по вазі
    # по зменшенню та вивести тільки перші 10 результатів
    # НЕ ЗРОЗУМІЛА, ДЕ ВЗЯТИ ВАГУ ЗАМОВЛЕННЯ

    query1 = """
    SELECT * FROM Orders
    WHERE ShipCountry LIKE 'N%'
    ORDER BY Freight DESC
    LIMIT 10;
    """

    print('1. Замовлення в країну N')
    result = select_query(connection, query1)
    for row in result:
        print(row)
        print('*' * 30)

# 2. Знайти замовників у яких ми не маємо телефонів

    query2 = """
    SELECT 
CustomerID
,CompanyName
,ContactName
,ContactTitle
,Country
,Region
,City
,Phone
FROM Customers
WHERE Phone IS NULL
    """

    print('2. Замовники без номеру телефона')
    result = select_query(connection, query2)
    for row in result:
        print(row)
        print('*' * 30)

# 3. Порахувати клієнтів, що мають телефон
    query3 = """
SELECT
COUNT (*)
FROM Customers
WHERE Phone IS NOT NULL
"""
    print('3. Порахувати клієнтів, що мають телефон')
    result = select_query(connection, query3)
    print(result)


#4. Порахувати постачальників з кожної країни, відсортувати по кількості по зменшенню
    query4 = """
SELECT
Country
, COUNT(COUNTRY) AS SuppliersQuantity
FROM Suppliers
GROUP BY Country
ORDER BY SuppliersQuantity DESC
"""
    print('4. Постачальники по країнах')
    result = select_query(connection, query4)
    for row in result:
        print(row)
        print('*' * 30)

#6. Вибрати унікальні країни замовників та постачальників та відсортувати по збільшенню
    query6 = """
SELECT
Country
, COUNT(COUNTRY) AS PartnerQuantity
FROM Suppliers
GROUP BY Country
UNION
SELECT
Country
, COUNT(COUNTRY) AS PartnerQuantity
FROM Customers
WHERE COUNTRY IS NOT NULL
GROUP BY Country
ORDER BY PartnerQuantity
"""
    print('6. Список країн замовників та постачальників')
    result = select_query(connection, query6)
    for row in result:
        print(row)
        print('*' * 30)

#7. Знайти замовників та співробітників, що обслуговують їх замовлення вони мають бути з Лондона і ті і ті,
# а доставка має йти компанією доставки Speedy Express вивести ім'я прізвище робітника та компанії замовника
    query7 = """
SELECT
    c.City AS CustomerCity,
    c.CompanyName AS CustomerCompany,
    e.City AS EmployeesCity,
    e.FirstName || ' ' || e.LastName AS EmployeeFullName,
    s.CompanyName AS ShipCompanyName
FROM Orders o
INNER JOIN Shippers s
    ON s.ShipperID = o.ShipVia
INNER JOIN Customers c
    ON c.CustomerID = o.CustomerID
INNER JOIN Employees e 
	ON e.EmployeeID = o.EmployeeID
WHERE s.CompanyName = 'Speedy Express'
AND CustomerCity = 'London'
AND EmployeesCity = 'London'
"""
    print('7. Замовники і співробітники з Лондона, доставка через Speedy Express')
    result = select_query(connection, query7)
    for row in result:
        print(row)
        print('*' * 30)

# 8. Знайти замовників, що не зробили жодного замовлення
    query8 = """
SELECT
Customers.CustomerID
,Customers.CompanyName
FROM Customers
LEFT JOIN Orders
ON Orders.CustomerID = Customers.CustomerID
WHERE Orders.CustomerID IS NULL
"""
    print('8. Замовники, які не зробили жодного замовлення')
    result = select_query(connection, query8)
    for row in result:
        print(row)
        print('*' * 30)


#9.Вивести усі унікальні товари яких замовлено рівно 10 одиниць
    query9 = """
WITH temp_table AS (
SELECT
    od.ProductID
    ,od.OrderID 
    ,SUM(od.Quantity) AS QuantitySum
FROM "Order Details" od
GROUP BY od.ProductID, od.OrderID
HAVING SUM(od.Quantity) = 10
)
SELECT DISTINCT ProductID FROM temp_table
ORDER BY ProductID

"""
    print('9. Список товарів, яких замовлено 10 од.')
    result = select_query(connection, query9)
    for row in result:
        print(row)
        print('*' * 30)
