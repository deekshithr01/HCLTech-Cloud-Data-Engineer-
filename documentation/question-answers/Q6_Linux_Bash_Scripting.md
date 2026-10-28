# Q6: Bash Scripting — Backup Check

## Problem Statement

Write a Bash script named `backup_check.sh` that accepts source and destination directories, validates the arguments, checks the source directory, creates the destination directory if necessary, creates a timestamped compressed archive, and displays success or failure messages.

## 1. Complete Bash Script

**File:** `Linux/scripts/backup_check.sh`

```bash
#!/bin/bash

# Validate the number of arguments
if [ "$#" -ne 2 ]; then
    echo "Error: Please provide source and destination directories."
    echo "Usage: $0 <source_directory> <destination_directory>"
    exit 1
fi

SOURCE_DIR="$1"
DEST_DIR="$2"

# Check whether the source directory exists
if [ ! -d "$SOURCE_DIR" ]; then
    echo "Error: Source directory '$SOURCE_DIR' does not exist."
    exit 1
fi

# Create the destination directory if required
if ! mkdir -p "$DEST_DIR"; then
    echo "Error: Could not create destination directory '$DEST_DIR'."
    exit 1
fi

# Generate a timestamped compressed archive
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
ARCHIVE_NAME="backup_${TIMESTAMP}.tar.gz"
ARCHIVE_PATH="${DEST_DIR}/${ARCHIVE_NAME}"

if tar -czf "$ARCHIVE_PATH" -C "$(dirname "$SOURCE_DIR")" "$(basename "$SOURCE_DIR")"; then
    echo "Backup successful!"
    echo "Archive created: $ARCHIVE_PATH"
    exit 0
else
    echo "Error: Backup failed."
    rm -f "$ARCHIVE_PATH"
    exit 1
fi
```

## 2. Make the Script Executable

**Command:**

```bash
chmod +x Linux/scripts/backup_check.sh
```

This adds execute permission to the script.

## 3. Test with Valid Arguments

Create a sample source directory and file:

```bash
mkdir -p Linux/backup_test/source
echo "HCLTech Bash backup practical test" > Linux/backup_test/source/sample.txt
```

Execute the script:

```bash
./Linux/scripts/backup_check.sh Linux/backup_test/source Linux/backup_test/backups
```

**Expected output:**

```text
Backup successful!
Archive created: Linux/backup_test/backups/backup_TIMESTAMP.tar.gz
```

The timestamp in the actual filename varies with the execution time.

## 4. Test with Missing Arguments

**Command:**

```bash
./Linux/scripts/backup_check.sh
```

**Expected output:**

```text
Error: Please provide source and destination directories.
Usage: ./Linux/scripts/backup_check.sh <source_directory> <destination_directory>
```

The script exits with a nonzero status because the required arguments are missing.

## 5. Test with a Nonexistent Source Directory

**Command:**

```bash
./Linux/scripts/backup_check.sh Linux/backup_test/missing Linux/backup_test/backups
```

**Expected output:**

```text
Error: Source directory 'Linux/backup_test/missing' does not exist.
```

The script stops without creating a backup archive.

## 6. Verify the Backup Archive

List the generated archives:

```bash
ls -lh Linux/backup_test/backups
```

Inspect the archive contents:

```bash
tar -tzf Linux/backup_test/backups/*.tar.gz
```

The listing should include the source directory and its sample file.

## Result

The Bash backup script validates its arguments, checks the source directory, creates the destination directory when needed, generates a timestamped compressed archive, and reports success or failure. Valid arguments, missing arguments, and a nonexistent source directory were tested.