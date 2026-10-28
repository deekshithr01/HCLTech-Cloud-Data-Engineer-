# Q4: Linux Log Analysis

## Problem Statement

Assume `/var/log/application.log` contains millions of log entries in the following format:

`2026-10-28 10:15:23 ERROR payment-service Transaction failed`

Write Linux commands to find errors, display recent errors, count errors, extract errors for a specified date, and calculate hourly error counts.

## (a) Find all lines containing ERROR

**Command:**

```bash
grep 'ERROR' /var/log/application.log
```

**Explanation:** The `grep` command searches the log file and displays all lines containing the word `ERROR`.

## (b) Display the 20 most recent error entries

**Command:**

```bash
grep 'ERROR' /var/log/application.log | tail -n 20
```

**Explanation:** The `grep` command filters error entries, and `tail -n 20` displays the last 20 matching entries.

## (c) Count the total number of error entries

**Command:**

```bash
grep -c 'ERROR' /var/log/application.log
```

**Explanation:** The `-c` option counts the lines containing `ERROR` and displays the total number of matching lines.

## (d) Extract error entries for a specified date into a separate file

**Command:**

```bash
grep '^2026-10-28 .*ERROR' /var/log/application.log > errors_2026-10-28.log
```

**Explanation:** The command filters error entries dated 28 October 2026 and redirects the matching lines into `errors_2026-10-28.log`.

## (e) Calculate the number of errors occurring in each hour

**Command:**

```bash
grep 'ERROR' /var/log/application.log | awk '{print substr($2,1,2)}' | sort | uniq -c
```

**Explanation:**

- `grep 'ERROR'` filters error entries.
- `awk '{print substr($2,1,2)}'` extracts the hour from the timestamp.
- `sort` groups identical hour values together.
- `uniq -c` counts the occurrences of each hour.

The output shows the number of errors occurring during each hour.

## Result

Linux commands were used to filter error entries, display the most recent errors, count errors, extract errors for a specified date, and calculate hourly error counts.