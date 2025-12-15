1️] Find the largest number in a list
arr = [10, 45, 23, 89, 12]

largest = arr[0]
for i in arr:
    if i > largest:
        largest = i

print(largest)
________________________________________
2️] Find the second largest number in a list
arr = [10, 45, 23, 89, 12]

first = second = float('-inf')

for i in arr:
    if i > first:
        second = first
        first = i
    elif i > second and i != first:
        second = i

print(second)
________________________________________
3️] Reverse a string
s = "python"
rev = ""

for i in s:
    rev = i + rev

print(rev)
________________________________________
4️] Check if number is palindrome
n = 121
temp = n
rev = 0

while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n //= 10

print(temp == rev)
________________________________________
5️] Count vowels in a string
s = "interview"
count = 0

for ch in s:
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        count += 1

print(count)
________________________________________
6️] Check if number is prime
n = 29
is_prime = True

if n <= 1:
    is_prime = False
else:
    for i in range(2, n):
        if n % i == 0:
            is_prime = False
            break

print(is_prime)
________________________________________
7️] Remove duplicates from a list
arr = [1, 2, 2, 3, 4, 3]
unique = []

for i in arr:
    if i not in unique:
        unique.append(i)

print(unique)
________________________________________
8️] Find factorial of a number
n = 5
fact = 1

for i in range(1, n + 1):
    fact *= i

print(fact)
________________________________________
9️] Find missing number from 1 to n
arr = [1, 2, 4, 5]
n = 5
total = 0

for i in range(1, n + 1):
    total += i

sum_arr = 0
for i in arr:
    sum_arr += i

print(total - sum_arr)
________________________________________
10] Fibonacci series (n terms)
n = 6
a = 0
b = 1

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c


1️] Two Sum
LeetCode #1
def twoSum(nums, target):
    d = {}
    for i in range(len(nums)):
        if target - nums[i] in d:
            return [d[target - nums[i]], i]
        d[nums[i]] = i
________________________________________
2️] Longest Substring Without Repeating Characters
LeetCode #3
def lengthOfLongestSubstring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len
________________________________________
3️] Valid Anagram
LeetCode #242
def isAnagram(s, t):
    if len(s) != len(t):
        return False

    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in t:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True
________________________________________
4️] Product of Array Except Self
def productExceptSelf(nums):
    n = len(nums)
    res = [1] * n

    left = 1
    for i in range(n):
        res[i] = left
        left *= nums[i]

    right = 1
    for i in range(n - 1, -1, -1):
        res[i] *= right
        right *= nums[i]

    return res
________________________________________
5]Maximum Subarray (Kadane’s Algorithm)
def maxSubArray(nums):
    curr = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        curr = max(nums[i], curr + nums[i])
        best = max(best, curr)

    return best
________________________________________
6]Merge Intervals
def merge(intervals):
    intervals.sort()
    result = [intervals[0]]

    for i in range(1, len(intervals)):
        last = result[-1]
        curr = intervals[i]

        if curr[0] <= last[1]:
            last[1] = max(last[1], curr[1])
        else:
            result.append(curr)

    return result
________________________________________
7]Move Zeroes
def moveZeroes(nums):
    index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1

    for i in range(index, len(nums)):
        nums[i] = 0
________________________________________
8]Find the Duplicate Number
def findDuplicate(nums):
    slow = nums[0]
    fast = nums[0]

    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break

    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    return slow
________________________________________
9]Valid Parentheses
def isValid(s):
    stack = []
    mp = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in mp:
            if not stack or stack.pop() != mp[ch]:
                return False
        else:
            stack.append(ch)

    return not stack
    
10]Majority Element
def majorityElement(nums):
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        count += 1 if num == candidate else -1

    return candidate




SQL
2️] Find second highest salary
SELECT MAX(salary)
FROM employee
WHERE salary < (SELECT MAX(salary) FROM employee);

3️] Find employees earning more than average salary
SELECT *
FROM employee
WHERE salary > (SELECT AVG(salary) FROM employee);

4️] Find department-wise total salary
SELECT department_id, SUM(salary)
FROM employee
GROUP BY department_id;

5️] Find duplicate emails
SELECT email, COUNT(*)
FROM employee
GROUP BY email
HAVING COUNT(*) > 1;

6] Employees Earning More Than Their Managers
SELECT e.name AS Employee
FROM Employee e
JOIN Employee m
ON e.managerId = m.id
WHERE e.salary > m.salary;

7]Customers Who Never Order
SELECT name AS Customers
FROM Customers
WHERE id NOT IN (
    SELECT customerId FROM Orders
);

8] Rising Temperature
LeetCode 197
SELECT w1.id
FROM Weather w1
JOIN Weather w2
ON DATEDIFF(w1.recordDate, w2.recordDate) = 1
WHERE w1.temperature > w2.temperature;

9] Department Highest Salary
SELECT d.name AS Department, e.name AS Employee, e.salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);

10] Rank Scores
SELECT score,
       DENSE_RANK() OVER (ORDER BY score DESC) AS `rank`
FROM Scores;

11] Delete Duplicate Emails
DELETE p1
FROM Person p1
JOIN Person p2
ON p1.email = p2.email
AND p1.id > p2.id;

Q6. Replace Employee ID With The Unique Identifier
SELECT eu.unique_id, e.name
FROM Employees e
LEFT JOIN EmployeeUNI eu
ON e.id = eu.id;

Q8. Customer Who Visited but Did Not Make Any Transactions
SELECT customer_id, COUNT(*) AS count_no_trans
FROM Visits
WHERE visit_id NOT IN (SELECT visit_id FROM Transactions)
GROUP BY customer_id;


Q10. Average Time of Process per Machine
SELECT machine_id,
ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT machine_id,
    MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time,
    MAX(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time
    FROM Activity
    GROUP BY machine_id, process_id
) t
GROUP BY machine_id;

Q11. Employees with Missing Information
SELECT employee_id
FROM Employees
WHERE employee_id NOT IN (SELECT employee_id FROM Salaries)
UNION
SELECT employee_id
FROM Salaries
WHERE employee_id NOT IN (SELECT employee_id FROM Employees)
ORDER BY employee_id;

Q12. Employees Whose Manager Left the Company
SELECT employee_id
FROM Employees
WHERE manager_id NOT IN (SELECT employee_id FROM Employees)
AND manager_id IS NOT NULL;

Q15. Calculate Special Bonus
SELECT employee_id,
CASE
    WHEN employee_id % 2 = 1 AND name NOT LIKE 'M%' THEN salary
    ELSE 0
END AS bonus
FROM Employees;

Q16. The Latest Login in 2020
SELECT user_id, MAX(time_stamp) AS last_stamp
FROM Logins
WHERE YEAR(time_stamp) = 2020
GROUP BY user_id;

Q17. Group Sold Products By The Date
SELECT sell_date,
COUNT(DISTINCT product) AS num_sold,
GROUP_CONCAT(DISTINCT product ORDER BY product) AS products
FROM Activities
GROUP BY sell_date;

Q18. Fix Names in a Table
SELECT user_id,
CONCAT(UPPER(LEFT(name,1)), LOWER(SUBSTRING(name,2))) AS name
FROM Users;

Q19. Patients With a Condition
SELECT patient_id, patient_name, conditions
FROM Patients
WHERE conditions LIKE 'DIAB1%'
OR conditions LIKE '% DIAB1%';

Q21. Find Total Time Spent by Each Employee
SELECT emp_id, event_day AS day, SUM(out_time - in_time) AS total_time
FROM Employees
GROUP BY emp_id, event_day;

Q24. Consecutive Numbers
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1
JOIN Logs l3 ON l2.id = l3.id - 1
WHERE l1.num = l2.num AND l2.num = l3.num;

Q26. Customers Who Bought All Products
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);

Q28. Biggest Single Number
SELECT MAX(num) AS num
FROM MyNumbers
WHERE num IN (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
);

Q29. Exchange Seats
SELECT
CASE
    WHEN id % 2 = 1 AND id < (SELECT MAX(id) FROM Seat) THEN id + 1
    WHEN id % 2 = 0 THEN id - 1
    ELSE id
END AS id,
student
FROM Seat
ORDER BY id;

Q30. Product Price at a Given Date
SELECT p.product_id, IFNULL(t.new_price, 10) AS price
FROM Products p
LEFT JOIN (
    SELECT product_id, new_price
    FROM Products
    WHERE (product_id, change_date) IN (
        SELECT product_id, MAX(change_date)
        FROM Products
        WHERE change_date <= '2019-08-16'
        GROUP BY product_id
    )
) t
ON p.product_id = t.product_id;

Q31. Last Person to Fit in the Bus
SELECT person_name
FROM Queue
WHERE turn = (
    SELECT MAX(turn)
    FROM (
        SELECT turn, SUM(weight) OVER (ORDER BY turn) AS total_weight
        FROM Queue
    ) t
    WHERE total_weight <= 1000
);

Q32. Customers With Strictly Increasing Purchases
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING COUNT(order_date) = COUNT(DISTINCT order_date)
AND MIN(order_date) <> MAX(order_date);

Q33. Bank Account Summary II
SELECT u.name, SUM(t.amount) AS balance
FROM Users u
JOIN Transactions t
ON u.account = t.account
GROUP BY u.name
HAVING SUM(t.amount) > 10000;

Q34. Confirmation Rate
SELECT s.user_id,
ROUND(
    IFNULL(SUM(c.action = 'confirmed') / COUNT(c.action), 0), 2
) AS confirmation_rate
FROM Signups s
LEFT JOIN Confirmations c
ON s.user_id = c.user_id
GROUP BY s.user_id;

Q35. Employees With Bonuses Less Than 1000
SELECT e.name, b.bonus
FROM Employee e
LEFT JOIN Bonus b
ON e.empId = b.empId
WHERE b.bonus < 1000 OR b.bonus IS NULL;

Q36. Monthly Transactions I
SELECT
DATE_FORMAT(trans_date, '%Y-%m') AS month,
country,
COUNT(*) AS trans_count,
SUM(state = 'approved') AS approved_count,
SUM(amount) AS trans_total_amount,
SUM(CASE WHEN state = 'approved' THEN amount ELSE 0 END) AS approved_total_amount
FROM Transactions
GROUP BY month, country;

Q37. Tree Node
SELECT id,
CASE
    WHEN p_id IS NULL THEN 'Root'
    WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
    ELSE 'Leaf'
END AS type
FROM Tree;

Q38. Immediate Food Delivery II
SELECT ROUND(
    SUM(order_date = customer_pref_delivery_date) * 100 / COUNT(*),
    2
) AS immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN (
    SELECT customer_id, MIN(order_date)
    FROM Delivery
    GROUP BY customer_id
);

Q39. Game Play Analysis IV
SELECT ROUND(
    COUNT(DISTINCT a.player_id) / COUNT(DISTINCT b.player_id),
    2
) AS fraction
FROM Activity a
JOIN Activity b
ON a.player_id = b.player_id
AND DATEDIFF(a.event_date, b.event_date) = 1;

Q40. Department Top Three Salaries
SELECT d.name AS Department, e.name AS Employee, e.salary
FROM Employee e
JOIN Department d
ON e.departmentId = d.id
WHERE (
    SELECT COUNT(DISTINCT salary)
    FROM Employee
    WHERE departmentId = e.departmentId
    AND salary > e.salary
) < 3;

Q41. Customers Who Bought Products A and B but Not C
SELECT customer_id
FROM Orders
GROUP BY customer_id
HAVING SUM(product_name = 'A') > 0
AND SUM(product_name = 'B') > 0
AND SUM(product_name = 'C') = 0;

Q42. All People Report to the Given Manager
SELECT employee_id
FROM Employees
WHERE manager_id = 1
OR manager_id IN (
    SELECT employee_id
    FROM Employees
    WHERE manager_id = 1
);

Q43. Number of Calls Between Two Persons
SELECT from_id AS person1, to_id AS person2, COUNT(*) AS call_count, SUM(duration) AS total_duration
FROM Calls
GROUP BY person1, person2
UNION
SELECT to_id AS person1, from_id AS person2, COUNT(*) AS call_count, SUM(duration) AS total_duration
FROM Calls
GROUP BY person2, person1;

Q44. Product Sales Analysis III
SELECT product_id, year AS first_year, quantity, price
FROM Sales
WHERE (product_id, year) IN (
    SELECT product_id, MIN(year)
    FROM Sales
    GROUP BY product_id
);

Q45. Capital Gain/Loss
SELECT stock_name,
SUM(CASE WHEN operation = 'Sell' THEN price ELSE -price END) AS capital_gain_loss
FROM Stocks
GROUP BY stock_name;

Find the Quiet Students in All Exams
SELECT student_id, student_name
FROM Student
WHERE student_id NOT IN (
    SELECT DISTINCT student_id
    FROM Exam e
    JOIN (
        SELECT exam_id, MIN(score) AS mn, MAX(score) AS mx
        FROM Exam
        GROUP BY exam_id
    ) t
    ON e.exam_id = t.exam_id
    WHERE e.score = t.mn OR e.score = t.mx
);

47. Count Apples and Oranges
SELECT
SUM(CASE WHEN fruit = 'apples' THEN num ELSE 0 END) AS apples_count,
SUM(CASE WHEN fruit = 'oranges' THEN num ELSE 0 END) AS oranges_count
FROM Fruits;

49. Report Contiguous Dates
SELECT state,
MIN(date) AS start_date,
MAX(date) AS end_date
FROM (
    SELECT state, date,
    DATE_SUB(date, INTERVAL ROW_NUMBER() OVER (PARTITION BY state ORDER BY date) DAY) AS grp
    FROM Log
) t
GROUP BY state, grp;



