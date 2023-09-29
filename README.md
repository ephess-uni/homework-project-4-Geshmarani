# Homework Project 4
This project consists of multiple intermediate exercises with using `datetime` objects. There are 4 sub-parts
to this project.  In each sub-part, you will implement a function.  Each of the required functions must be present
in your `hp_4.py` file.  Note: you can include more functions in your module if 
necessary; software tests will only test the required functions.

## reformat_dates()
Write a function `reformat_dates(dates)` that accepts a list of date strings with 
format `yyyy-mm-dd` and returns a list of date strings with format `dd mmm yyyy` 
(example: 01 Jan 2001). 

Here is an example run:

```pycon
>>> old_dates = ['2000-01-01', '2000-01-02', '2000-01-03']
>>> reformat_dates(old_dates)
['01 Jan 2000', '02 Jan 2000', '03 Jan 2000']
```

[Reference for `strptime` and `strftime` format strings. ](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)

## date_range()
Implement the function `date_range(start, n)` generates and
returns a daily sequence `n` of `datetime` objects.

- `start`: a string in the format `yyyy-mm-dd` representing the start date.

Your function should meet the following requirements:

- raise a `TypeError` if `start` not  a `str` type.
  - hint: use `isinstance(start, str)` as it returns `True` if `start` is a `str` type. Use the same test for `start`.
- raise a `TypeError` if `n` is not an `int` type.
- return a `list` of `n` `datetime` objects from `start` to `start` plus days--inclusive.  Note: `start` should be in the list and the list should have `n` elements.

Use the [strptime reference](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-format-codes) documentation for assistance in parsing the dates appropriately.


Here's an example run:

```pycon
>>> date_range('2000-01-01', 3)
[datetime.datetime(2000, 1, 1, 0, 0),
 datetime.datetime(2000, 1, 2, 0, 0),
 datetime.datetime(2000, 1, 3, 0, 0)]
```

## add_date_range()
In this exercise, you will write a function that adds a date field to a sequence of values. Define your function
with the signature `add_date_range(values, start_date)`.

Here:
- `values` is a daily sequence (type list) of numerical values (ex: average daily temperature)
- `start_date` is a date string with format `yyyy-mm-dd` representing the date that the daily sequence started on.

Your function should return a `list` type containing `tuple` elements where each element contains `(date, value)` and `date` is a datetime object. The datetime object for
element 0 should store `start_date`.  Element 1's datetime object should be store a date 1 day after `start_date`, and so on.

Hint: use your `date_range()` function. As another hint, `zip()` should be particularly useful here.

Here is an exmaple run:

```pycon
>>> values = [100, 101, 102,]
>>> add_date_range(values, '2000-01-01')
[(datetime.datetime(2000, 1, 1, 0, 0), 100),
 (datetime.datetime(2000, 1, 2, 0, 0), 101),
 (datetime.datetime(2000, 1, 3, 0, 0), 102)]
```

## fees_report()
Libraries are a wonderful place to source books. When books are checked out, they are assigned a due date. If a book is returned late, a late fee of $0.25/day is charged to the library patron's library account.

In this exercise, you will write a function called `fees_report(infile, outfile)` that reads a CSV data file `infile` containing information about book returns.  Your code should calculate late fees for each account listed in the input data source and write out a summary report in CSV form `outfile`.  Details follow.

    
Your program should:

1. Read in the `infile` CSV file (a [DictReader](https://docs.python.org/3.10/library/csv.html#csv.DictReader) is highly recommended.)
2. Calculate late fees on a `patron_id` basis.
3. Write a summary report to the filename given in `outfile` for **accounts with late fees** only.


### Input File Format

The input data file name is passed to `fee_report()` via the `infile` argument. 
Example files `book_returns.csv` and a shorter `book_returns_short.csv` are provided. 
Use the `get_data_file_path` function defined in `src/util` to get the correct path 
for one of these input files during your manual tests.

Any return report has the following structure:

```
book_uid, isbn_13, patron_id, date_checkout, date_due, date_returned
```

Here is a description of each field:

- `patron_id`: A unique ID string associated with a library patron account.  Note that there may be duplicates for this field as many patrons check out multiple books.
- `isbn_13`: This is the ISBN-13, a 13 digit number of the book. This can be interpreted as a string.
- `book_uid`: This string ID is a unique identifier that the library assigns to each book.  No two books have the same `book_uid`.
- `date_checkout`: A date string representing the day that the book was checked out.  
  The date format is `mm/dd/yyyy`.
- `date_due`: A date string representing the date that the book was due.  The date 
  format is `mm/dd/yyyy`.
- `date_returned`: The date that the book was returned. The date format is `mm/dd/yy`.

### Output File Format
The output filename is passed to the `fee_report()` function via the `outfile` argument.

The output format is CSV with the following fields:

```
patron_id, late_fees
```

Field descriptions:
- `patron_id`: Library patron account ID string.
- `late_fees`: the total USD amount fee for the patron_id formatted as a floating point 
  value with 2 decimal places of precision. Note: No "$" should be included in the values. Example: 1.25.

### Tests
Your `fees_report()` implementation should:
- write CSV formatted output
- use the correct fieldnames (header column names in the output file)
- use the correct currency format
- include a fee for all patrons represented in the input data (even if the fee is 0.00)
- accumulate fees for patrons--only one row per patron_id in the output file

