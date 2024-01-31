
![2021-22_UN_Human_Development_Report svg](https://github.com/anubhavsingh1729/MADE/assets/43649870/af4fddf0-5350-4e9c-8c5b-f5ac26983007)

## Title
Correlation between R&D Investment and Human development Index.

## Main Question
Does the government spending on research and development affects the trend in Human Development Index?

## Description
The aim of this project is to analyze how government spending on research and development activity affects the trend in human development index. The Human Development Index (HDI) is a summary measure of average achievement in key dimensions of human development: a long and healthy life, being knowledgeable and having a decent standard of living.
By comprehensively examining the patterns, trends and correlations, it could be possible to verify a potential relationship. This analysis could provide key insights to further help with evidence based decision making process.

## Data Sources
### Data Source 1: hdr.undp.org
* Data Url : <https://hdr.undp.org/sites/default/files/2021-22_HDR/HDR21-22_Statistical_Annex_HDI_Trends_Table.xlsx>
* type : excel

### Data Source 2: worldbank.org
* Data Url : <https://api.worldbank.org/v2/en/indicator/GB.XPD.RSDV.GD.ZS?downloadformat=excel>
* type : excel

## Project Setup
1. Clone the repository:

```
git clone git@github.com:anubhavsingh1729/MADE.git
```

2. Install requirements:

```
pip install -r requirements.txt
```

3. Run the ETL pipeline
* Go to /project and run the pipeline.sh script.

```
chmod +x pipeline.sh
sh pipeline.sh
```

## Final Report

[report.ipynb](https://github.com/anubhavsingh1729/MADE/blob/main/project/report.ipynb)
