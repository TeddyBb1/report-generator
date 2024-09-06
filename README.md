# 📊 CSV to PDF Report Generator

Welcome to the **Report Generator** project! This Python-based tool allows you to convert CSV files into professional PDF reports that include both **graphs** and **tables**. With this tool, you can easily visualize and document your data.

## 🚀 Features

- **CSV File Upload**: Load any CSV file with at least two columns for processing.
- **Graph Generation**: Automatically create bar graphs based on the data in the first two columns of your CSV file.
- **PDF Creation**: Generate a PDF report that includes a data table and a graph, perfect for sharing or documenting your results.

## 🛠️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/TeddyBb1/report-generator.git
   ```
   
2. Navigate to the project folder:
   ```bash
   cd report-generator
   ```

3. Install the required dependencies:
   ```bash
   pip install pandas matplotlib reportlab PySide6
   ```

## 🖥️ Usage

To run the application, use the following command:

```bash
python report.py
```

After starting the app:
1. **Step 1**: Click the "Load CSV" button to select a CSV file from your computer.
2. **Step 2**: After loading the CSV, click the "Generate PDF" button to create a PDF report.

## 📄 Example

Example CSV file format:

```csv
Category,Value
A,10
B,15
C,7
D,22
E,5
```

Once loaded, the application will generate a **PDF report** that includes:
- A **table** with your CSV data.
- A **bar graph** visualizing the data.

## 👤 Author

Developed by **TeddyBb1**.  
Feel free to fork the repository, open issues, and contribute to make it even better! 😊
