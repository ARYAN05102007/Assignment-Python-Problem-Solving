# [Assignment] Python Problem Solving

A set of six beginner-friendly Python problems solved using only basic constructs: loops, conditionals, lists, strings, and dictionaries. All six are adapted from popular LeetCode problems.

> **Rule:** No user-defined functions. Each program runs top to bottom and prints the result for every item in its `tests` list.

## Problems

| # | Problem | LeetCode | Difficulty | Concept Practiced |
|---|---------|----------|------------|-------------------|
| 1 | Fizz Buzz | [#412](https://leetcode.com/problems/fizz-buzz/) | Easy | Loops, `%` operator, if/elif order |
| 2 | Palindrome Number | [#9](https://leetcode.com/problems/palindrome-number/) | Easy | `%` and `//` for digit handling, negative numbers |
| 3 | Contains Duplicate | [#217](https://leetcode.com/problems/contains-duplicate/) | Easy | Lists, sets or nested loops |
| 4 | Two Sum | [#1](https://leetcode.com/problems/two-sum/) | Easy | Nested loops or dictionary lookup |
| 5 | Best Time to Buy and Sell Stock | [#121](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/) | Easy | Tracking a running minimum |
| 6 | Roman to Integer | [#13](https://leetcode.com/problems/roman-to-integer/) | Easy | Dictionary mapping, subtractive rule |

## Problem Summaries

**1. Fizz Buzz (LeetCode #412)**
For each `n` in `tests`, build a list of strings from 1 to `n`: `"FizzBuzz"` if divisible by 3 and 5, `"Fizz"` if divisible by 3, `"Buzz"` if divisible by 5, otherwise the number as a string. Check the "both" case first.

**2. Palindrome Number (LeetCode #9)**
Decide whether an integer reads the same forwards and backwards. Negative numbers are never palindromes. Use `x % 10` and `x // 10` to reverse the digits.

**3. Contains Duplicate (LeetCode #217)**
Print `True` if any value appears at least twice in the list, otherwise `False`.

**4. Two Sum (LeetCode #1)**
Find the two positions in `nums` whose values add up to `target`. Each test has exactly one valid pair, and the smaller index is printed first.

**5. Best Time to Buy and Sell Stock (LeetCode #121)**
Given daily prices, find the maximum profit from buying on one day and selling on a later day. Print `0` if no profit is possible.

**6. Roman to Integer (LeetCode #13)**
Convert a valid Roman numeral (1 to 3999) to an integer. If a symbol is smaller than the one after it, subtract it; otherwise add it.

## Constraints

- No functions: use plain loops and conditionals only.
- Every program must loop over its given `tests` and print one result per line.
- Output must match the expected output exactly (spacing, quotes, and `True`/`False` capitalization).

## Expected Outputs

<details>
<summary>Click to expand</summary>

**Q1 – Fizz Buzz**
```
['1', '2', 'Fizz', '4']
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz']
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz']
['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']
```

**Q2 – Palindrome Number**
```
True
False
False
True
True
True
```

**Q3 – Contains Duplicate**
```
False
True
True
False
True
```

**Q4 – Two Sum**
```
2 3
1 2
0 3
0 2
```

**Q5 – Best Time to Buy and Sell Stock**
```
2
4
4
0
4
```

**Q6 – Roman to Integer**
```
9
40
2024
444
14
```
</details>

## Project Structure

```
python-problem-solving/
├── q1_fizzbuzz.py
├── q2_palindrome_number.py
├── q3_contains_duplicate.py
├── q4_two_sum.py
├── q5_best_time_to_buy_sell_stock.py
├── q6_roman_to_integer.py
└── README.md
```

## How to Run

Make sure Python 3 is installed, then run any file from the project folder:

```bash
python q1_fizzbuzz.py
python q2_palindrome_number.py
# ...and so on
```

Compare the printed output with the expected output above.

## Author

Aryan – Roll No. 45
