# Detailed Instructions

## 1. Run `sql_to_csv.py`

This script extracts data from a SQL database and exports it to CSV format. Make sure to configure your database connection in the script before running it.

To run the script:

```bash
python sql_to_csv.py
```

This will generate the necessary CSV files for further data processing.

## 2. Execute `data.ipynb`

Once the CSV files have been created, open and execute the `data.ipynb` notebook. This notebook performs the following tasks:

- Data loading
- Data cleaning
- Feature engineering

To run the notebook:

```bash
jupyter notebook data.ipynb
```

Make sure all cells run successfully before proceeding to the next steps.

## 3. Execute `charts.ipynb` and `charts2.ipynb`

These notebooks generate visualizations and charts based on the processed data. Execute them in the following order:

1. Open and run `charts.ipynb`
2. Open and run `charts2.ipynb`

To open and run the notebooks:

```bash
jupyter notebook charts.ipynb
jupyter notebook charts2.ipynb
```

## 4. Execute `ml.ipynb`

Finally, open and run the `ml.ipynb` notebook, which contains the machine learning model training and evaluation. This notebook depends on the cleaned and processed data, so ensure the previous steps are completed.

```bash
jupyter notebook ml.ipynb
```

This will train the model and generate results, which can be used for further analysis.

## Conclusion

By following the steps above, you will successfully extract data, process it, generate charts, and train a machine learning model. Make sure to check for any additional configuration required within each script or notebook, such as file paths or parameters.
