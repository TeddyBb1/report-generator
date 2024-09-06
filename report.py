import sys
import pandas as pd
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QPushButton, QFileDialog, QWidget, QLabel
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Spacer, Image
from reportlab.lib import colors

class ReportGenerator(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CSV to PDF Report Generator")
        self.setGeometry(300, 300, 400, 200)

        layout = QVBoxLayout()

        # Label for loading the CSV file
        self.label = QLabel("Select a CSV file to generate the PDF report")
        layout.addWidget(self.label)

        # Button for loading the CSV file
        self.load_button = QPushButton("Load CSV")
        self.load_button.clicked.connect(self.load_csv)
        layout.addWidget(self.load_button)

        # Button for generating the PDF report
        self.generate_button = QPushButton("Generate PDF")
        self.generate_button.setEnabled(False)
        self.generate_button.clicked.connect(self.generate_pdf)
        layout.addWidget(self.generate_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        # Variables to store CSV data
        self.data = None
        self.csv_path = None

    def load_csv(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select CSV File", "", "CSV Files (*.csv)", options=options)
        if file_name:
            self.csv_path = file_name
            self.data = pd.read_csv(file_name)
            self.label.setText(f"File loaded: {file_name}")
            self.generate_button.setEnabled(True)

    def generate_graph(self):
        # Generate a graph based on the first two columns of the CSV file
        plt.figure(figsize=(6, 4))
        self.data.plot(kind='bar', x=self.data.columns[0], y=self.data.columns[1], color='blue')
        plt.title("Graph Generated from CSV")
        plt.savefig("bar_graph.png")
        plt.close()

    def generate_pdf(self):
        if self.data is None:
            self.label.setText("No data loaded.")
            return

        # Generate the graph before creating the PDF
        self.generate_graph()

        # Generate the PDF using ReportLab
        pdf_filename = "report.pdf"
        doc = SimpleDocTemplate(pdf_filename, pagesize=A4)

        # Create a table from CSV data
        table_data = [self.data.columns.tolist()] + self.data.values.tolist()
        table = Table(table_data)
        table.setStyle(TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, 0), 12),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ]))

        # Add table and graph to the PDF
        elements = [table, Spacer(1, 12)]

        # Add the graph image using the Image class from platypus
        img = Image("bar_graph.png", width=400, height=300)
        elements.append(img)

        doc.build(elements)

        self.label.setText(f"PDF generated: {pdf_filename}")

# Application startup
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ReportGenerator()
    window.show()
    sys.exit(app.exec())
