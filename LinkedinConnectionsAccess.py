import pandas as pd
# from googlesearch import search
import webbrowser
from linkedin import linkedin

CID = "86pcc339a126pg"
CSEC = "AnCUuisR8L35yMIW"
RETURN_URL = 'https://localhost:8000'

#authenticate the profile access
auth = linkedin.LinkedInAuthentication(CID,CSEC,RETURN_URL)
app = linkedin.LinkedInApplication(auth)

webbrowser.register('chrome',None,
    webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))

# webbrowser.get('chrome').open(url)
# app.make_request("POST",url)
df = pd.dataframe()

conn = app.get_connections(selectors=['headline', 'first-name', 'last-name'], params={'start':10, 'count':5})

for each_conn in range(len(conn)):
  df.append(app.get_profile(selectors=['id', 'first-name', 'last-name', 'email', 'phone-number', 'location', 'Current-company','Current-jobtitle','Prev-company',\
                                    'prev-JobTitles','institute','degree']))

df.to_excel(r'LeadsData.xlsx', index = True)
