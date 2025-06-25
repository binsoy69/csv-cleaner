# 🧹 CSV Data Cleaner CLI Tool

A command-line utility for cleaning messy CSV files using Python and pandas.  
Built to demonstrate practical data wrangling, CLI design, and code reusability.

---

## 🚀 Features

- 📂 Load any CSV file
- ✅ Remove duplicate rows (`--dedup`)
- 🕳️ Drop or fill missing values (`--dropna`, `--fillna`)
- ✏️ Rename columns via command-line (`--rename`)
- 📊 Before/after data stats (rows, columns, missing data)
- 💾 Save cleaned CSV to a new file

---

## 📦 Requirements

- Python 3.7+
- pandas

Install with:
```bash
pip install pandas
```

## 💡 Usage
#### Remove duplicates and drop rows with missing values
```bash
python cleaner.py --file sample.csv --dedup --dropna --out clean.csv
```

#### Fill missing cells with "N/A"
```bash
python cleaner.py --file sample.csv --fillna "N/A"
```

#### Rename columns
```bash
python cleaner.py --file sample.csv --rename Name=FullName,Email=Contact --out renamed.csv
```
## 🧪 Sample Data
Comes with sample.csv that includes:
- Duplicates
- Missing values
- Blank rows
- Useful edge cases for testing

## 📁 Project Structure
```
csv-cleaner/
├── cleaner.py            # Main CLI script
├── sample.csv            # Messy test data
├── cleaned_output.csv    # Output example
└── README.md
```
