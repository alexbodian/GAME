# Gun Activity Map Explorer
# Documentation:
* Developer facing documention is in "DevDoc.txt.docx" and can be accessed at "https://docs.google.com/document/d/1v4i81QPrPG90T3APa-RGXu0q59BGI6yrpGUT7YrygVU/edit?usp=sharing"
* User facing documention is in "UserDoc.txt.docx" and can be accessed at "https://docs.google.com/document/d/1z3idVZF4jsTaSJ3Kj0FtgHHZjjzrNilGvDH3Y7ixMvk/edit?usp=sharing"
## Scripts:
* The only Main Scripts ran in this program are in "app.py"
## Databases provided files:
* The database of Kaggle provided Mass Shootings is in "Mass Shootings Dataset Ver 2.csv", provided at "https://www.kaggle.com/zusmani/us-mass-shootings-last-50-years"
* The database of Kaggle provided State Provisions is in "laws.csv", and "codebook.xlsx", provided at "https://www.kaggle.com/jboysen/state-firearms"
* The database of Mother Jones provided Mass Shootings is pulled directly from their google docs at "https://docs.google.com/spreadsheets/d/1b9o6uDO18sLxBqPwl_Gh9bnhW-ev_dABH83M5Vb5L8o/export?format=csv&gid=0",
* The database of FBI provided Background Checks by State in "nics-firearm-background-checks.csv", provided at "https://www.fbi.gov/services/cjis/nics"
## Website Host:
* This Program is hosted by Heroku at "http://gunactivitymapexploreronline.herokuapp.com/"
## Config:
* The required libraries and versions are listed in the "requirements.txt"
## Extra Info:
* The follow items were used for testing during development, but are no longer used: "background-checks", "shootings", "state-firearms", and "NICS_Firearm_Checks_Month_Year_by_State"
* Background checks from FIB formatted by BuzzFeed at :"https://github.com/BuzzFeedNews/nics-firearm-background-checks"
* US states in JSON form provided at "https://gist.github.com/mshafrir/2646763"
* Python Dictionary to translate US States to Two letter codes: "https://gist.github.com/rogerallen/1583593"
* Examples of Dash provided from Dash's documentation: "https://dash.plot.ly/"
* Used Udemy to understand Dash better, guide provided at "https://www.udemy.com/interactive-python-dashboards-with-plotly-and-dash/learn/v4/overview"
