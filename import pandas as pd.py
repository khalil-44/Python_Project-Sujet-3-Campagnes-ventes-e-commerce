import pandas as pd

# 1. Load Excel file
df = pd.read_excel("data.xlsx")

# 2. Convert InvoiceDate to datetime
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

# 3. Remove rows without CustomerID
df = df.dropna(subset=["CustomerID"])

# 4. Create a Revenue column
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
# Example segmentation: orders from a given country with Revenue > 100
country_filter = "France"
segmented = df[(df["Country"] == country_filter) & (df["Revenue"] > 100)]

# 5. Group by Country → total revenue
country_revenue = df.groupby("Country")["Revenue"].sum().reset_index()

# 6. Pivot table: Country × Month
df["Month"] = df["InvoiceDate"].dt.to_period("M")
pivot = pd.pivot_table(df, values="Revenue", index="Country", columns="Month", aggfunc="sum", fill_value=0)

# 7. Export top 10 countries by revenue
top10 = country_revenue.sort_values("Revenue", ascending=False).head(10)
top10.to_excel("top10_countries.xlsx", index=False)

# Optional: check results
print(top10)
print(pivot.head())
