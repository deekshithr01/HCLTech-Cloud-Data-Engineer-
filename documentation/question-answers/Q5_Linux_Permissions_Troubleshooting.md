# Q5: Permissions and System Troubleshooting

## Problem Statement

A Linux server hosts an application that processes confidential financial reports. The tasks are to create a finance group and report file, configure file permissions, identify high-CPU processes, check memory and disk utilization, and locate files larger than 100 MB.

## (a) Create a group named finance and a report file

**Linux commands:**

```bash
sudo groupadd finance
touch financial_report.txt
```

**Explanation:**

- `sudo groupadd finance` creates a group named `finance`. Administrative privileges are required.
- `touch financial_report.txt` creates an empty report file if it does not already exist.

To assign the report file to the finance group, use:

```bash
sudo chgrp finance financial_report.txt
```

## (b) Set the required file permissions

**Command:**

```bash
chmod 640 financial_report.txt
```

**Explanation:**

The permission value `640` represents:

- Owner: `6` = read and write (`rw-`).
- Group: `4` = read-only (`r--`).
- Others: `0` = no permissions (`---`).

The resulting permission string is:

```text
-rw-r-----
```

This restricts access to the owner and members of the assigned group.

## (c) Identify processes consuming the most CPU

**Command:**

```bash
ps aux --sort=-%cpu | head -n 6
```

**Explanation:**

- `ps aux` lists running processes.
- `--sort=-%cpu` sorts processes by CPU usage in descending order.
- `head -n 6` displays the header and the five highest-CPU processes.

This helps identify processes that may be consuming excessive CPU resources.

## (d) Display memory usage and filesystem disk utilization

**Memory usage command:**

```bash
free -h
```

**Explanation:** Displays total, used, and available memory in human-readable units.

**Disk utilization command:**

```bash
df -h
```

**Explanation:** Displays filesystem size, used space, available space, and usage percentage.

## (e) Find files larger than 100 MB under an application directory

**Command:**

```bash
find /path/to/application -type f -size +100M -print
```

Replace `/path/to/application` with the actual application directory.

**Explanation:**

- `find` searches the specified directory.
- `-type f` selects regular files.
- `-size +100M` selects files larger than 100 MB.
- `-print` displays the paths of matching files.

## Result

Linux commands were identified for group creation, file permission management, CPU process monitoring, memory and disk utilization, and locating files larger than 100 MB.