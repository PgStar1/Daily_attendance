# Daily_attendance
# Daily Attendance Analysis Script
## Overview

The script processes a CSV file containing attendance data, calculates the attendance percentages for "Present" and "Absent" students, and generates bar charts for visual representation. It specifically visualizes the attendance percentages for the first 7 dates in the dataset.

## Dependencies

Before running the script, make sure you have the following Python libraries installed:

- `pandas`: For data manipulation and analysis.
- `matplotlib`: For creating bar charts.
- `plotly`: For interactive visualizations (though not fully utilized in this version of the script).
- `Pillow`: For image processing (not fully utilized in this version).
- `numpy`: For numerical operations.

To install the dependencies, run the following:

pip install pandas matplotlib plotly Pillow numpy
# Attendance Data Processing

## 1. Prepare the Dataset

Place your dataset (CSV file) in the appropriate directory. Ensure it contains the following columns:

| Column Name | Description |
|-------------|-------------|
| `Date`      | Date of the attendance record (in YYYYMMDD format). |
| `Absent`    | Number of students absent on that day. |
| `Present`   | Number of students present on that day. |
| `Enrolled`  | Total number of enrolled students. |

## 2. Run the Script

Execute the Python script. It will:

1. Read the CSV file.
2. Process the data to calculate attendance percentages for "Absent" and "Present" students.
3. Print basic information about the dataset (such as the number of rows, columns, and data types).
4. Generate a bar chart comparing the attendance percentages for the first 7 dates.

## 3. Output

The script will output the following:

### DataFrame Information:

- The number of rows and columns.
- The first 7 rows of the data.
- The last 6 rows of the data.
- Column labels and data types.
- General statistics of the data, including any missing values.

### Visualizations:

- A bar chart showing the percentage of "Present" and "Absent" students for the first 7 dates in the dataset.

## Functions

### `create_dataframe(csv_file)`
**Purpose**: Reads the CSV file and processes the Date column to a datetime format. Also sets pandas display options to show all rows and columns.

### `print_dataframe_info(df)`
**Purpose**: Prints basic information about the DataFrame, including:
- Number of rows and columns.
- The first 7 rows of data.
- The last 6 rows of data.
- Data types and column information.
- General statistics (e.g., mean, min, max) for numeric columns.

### `processing(df)`
**Purpose**: Processes the data to calculate attendance percentages (`Absent_Percentage` and `Present_Percentage`). Then, it generates a bar chart comparing the attendance percentages for the first 7 dates.

### Visualization:
Displays a bar chart using `matplotlib` comparing the attendance for the first 7 dates.

## Input Data Format

The input should be a CSV file with the following columns:

| Date       | Absent | Present | Enrolled |
|------------|--------|---------|----------|
| 20230401   | 5      | 95      | 100      |
| 20230402   | 4      | 96      | 100      |
| ...        | ...    | ...     | ...      |

The `Date` column should be in the format `YYYYMMDD`.

## Output

### Console Output:

The script prints the following information:
- Number of rows and columns.
- First 7 rows of data.
- Last 6 rows of data.
- Column labels and data types.
- Summary statistics of the data (mean, min, max).

### Visual Output:
The script generates a bar chart comparing the "Absent" and "Present" percentages for the first 7 dates.
