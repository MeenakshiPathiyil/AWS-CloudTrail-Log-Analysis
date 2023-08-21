# AWS CloudTrail Log Analysis
## Overview 
The AWS CloudTrail Log Analysis program is designed to take a JSON file containing AWS CloudTrail logs as input and convert it into a pandas DataFrame. This allows users to perform further analysis on the CloudTrail logs using the powerful data manipulation and analysis capabilities provided by pandas.

## Requirements
* Python 3.7
* Pandas library
* (Optional) Jupyter Notebook or any Python IDE of your choice for further analysis.

## Installation
1. Clone this repository to your local machine.

   `git clone https://github.com/MeenakshiPathiyil/CloudTrail-Log-Analysis.git`

2. Install the required library by running the following command:

   `pip install pandas`

## Usage
1. Save your AWS CloudTrail log file in JSON format, named 'ctrail.json', and place it in the same directory as the 'cloud_trail.py' file.
2. Open the terminal or command prompt and navigate to the directory containing the 'cloud_trail.py' file and the 'ctrail.json' file.
3. Execute the 'cloud_trail.py' script using the following command:

   `python3 cloud_trail.py`

4. The program will read the JSON file, process the data, and convert it into a pandas DataFrame. The DataFrame will be displayed in the terminal.
5. If you want to perform further analysis on the DataFrame using Jupyter Notebook or any Python IDE, you can use the following code snippet:
   
   `import pandas as pd`
   
   `df = pd.read_csv('CloudTrail_Logs.csv')`

## Contribution
Contributions to this project are welcome! If you have any suggestions, bug reports, or improvements, please open an issue on the GitHub repository.
   
