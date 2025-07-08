
# Understanding Data with Pandas

Use the following Python commands to quickly explore and understand your dataset using the Pandas library.

---

## 1. Check the Size of the Data
Shows the number of rows and columns.
```python
df.shape
```

---

## 2. View the First Few Rows
Displays the top 5 rows by default.
```python
df.head()
```

---

## 3. Take a Random Sample
Helps you inspect a few random rows.
```python
df.sample(5)  # Randomly selects 5 rows
```

---

## 4. Data Types and Structure
Gives a summary of column names, types, and non-null counts.
```python
df.info()
```

---

## 5. Check for Missing Values
Tells how many missing (NaN) values exist in each column.
```python
df.isnull().sum()
```

---

## 6. 📊 Statistical Summary
Provides mean, min, max, standard deviation, etc.
```python
df.describe()
```

---

## 7. Find and Remove Duplicate Rows
Shows number of duplicate rows and removes them.
```python
df.duplicated().sum()        # Count duplicates
df.drop_duplicates()         # Remove duplicates
```

---

## 8. Correlation Between Columns
Finds relationships between numeric columns.
```python
df.corr()                             # Full correlation matrix
df.corr()['column_name']             # Correlation with one specific column
```

---

### Note:
These are essential steps in **EDA (Exploratory Data Analysis)**. Always start with these before moving to data cleaning, visualization, or modeling.
