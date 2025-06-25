import argparse
import pandas as pd

def display_stats(df, label=""):
    print(f"\n📊 Dataset Stats {label}")
    print("-" * 30)
    print(f"🧾 Rows: {df.shape[0]}")
    print(f"📐 Columns: {df.shape[1]}")
    print(f"🧱 Columns: {list(df.columns)}")
    print("🕳️ Missing values per column:")
    print(df.isnull().sum())
    print()


def main():
    parser = argparse.ArgumentParser(description="🧹 CSV Data Cleaner Tool")
    parser.add_argument('--file', required=True, help='Path to the CSV file')
    parser.add_argument('--dedup', action='store_true', help='Remove duplicate rows')
    parser.add_argument('--dropna', action='store_true', help='Drop rows with missing values')
    parser.add_argument('--fillna', type=str, help='Fill missing values with a specific value')
    parser.add_argument('--out', type=str, default='cleaned_output.csv', help='Output file name')
    parser.add_argument('--rename', type=str, help='Rename columns (e.g., Name=FullName,Email=EmailAddress)')


    args = parser.parse_args()

    print(f"📂 Loading file: {args.file}")
    df = pd.read_csv(args.file)
    display_stats(df, "(before cleaning)")

    print("🧾 Initial rows:", len(df))

    if args.dedup:
        df = df.drop_duplicates()
        print("✅ Removed duplicates.")

    if args.dropna:
        df = df.dropna()
        print("🗑️ Dropped rows with missing values.")

    if args.fillna is not None:
        df = df.fillna(args.fillna)
        print(f"🩹 Filled missing values with: {args.fillna}")

    display_stats(df, "(after cleaning)")

    df.to_csv(args.out, index=False)
    print(f"📁 Cleaned file saved as: {args.out}")

if __name__ == "__main__":
    main()
