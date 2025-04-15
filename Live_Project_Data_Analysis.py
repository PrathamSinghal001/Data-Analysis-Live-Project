# Live Project : Data Analysis
# Cloud Counselage

# Import libraries :-
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns


# Import dataset
df = pd.read_excel("D:/INTERNSHIP PROJECTS/Data analyst Data.xlsx")
# print(df)


# Data Cleaning :- 

# Handling null values 
# count null values 
print(df.isnull().sum())
"""
ANSWER : College Name                                                         15
         How did you come to know about this event?                         2216
         Specify in "Others" (how did you come to know about this event)    4805
"""

# Filling null values
df['College Name'].fillna(df['College Name'].mode()[0], inplace=True)
df['How did you come to know about this event?'].fillna(df['How did you come to know about this event?'].mode()[0], inplace=True)
df['Specify in "Others" (how did you come to know about this event)'].fillna(df['Specify in "Others" (how did you come to know about this event)'].mode()[0], inplace=True)

# Re-check null values 
print(df.isnull().sum())


# Handling duplicate values
print(df.duplicated().sum())
""" 
ANSWER : 0
"""


# Summarize information data 
print(df.describe())
"""
ANSWER :        
        Quantity  Year of Graduation         CGPA  Experience with python (Months)  Expected salary (Lac)
count    4894.0         4894.000000  4894.000000                      4894.000000            4894.000000
mean        1.0         2024.176951     8.038476                         5.395586              13.935635
std         0.0            1.000180     1.005184                         1.705364               6.451959
min         1.0         2023.000000     6.200000                         3.000000               5.000000
25%         1.0         2023.000000     7.200000                         4.000000               8.000000
50%         1.0         2024.000000     7.900000                         5.000000              13.000000
75%         1.0         2025.000000     8.900000                         7.000000              19.000000
max         1.0         2026.000000     9.900000                         8.000000              35.000000
"""


# Datatype information 
print(df.info())
""" 
ANSWER :
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 4894 entries, 0 to 4893
Data columns (total 16 columns):
 #   Column                                                           Non-Null Count  Dtype
---  ------                                                           --------------  -----
 0   First Name                                                       4894 non-null   object
 1   Email ID                                                         4894 non-null   object
 2   Quantity                                                         4894 non-null   int64
 3   Events                                                           4894 non-null   object
 4   Attendee Status                                                  4894 non-null   object
 5   College Name                                                     4894 non-null   object
 6   How did you come to know about this event?                       4894 non-null   object
 7   Specify in "Others" (how did you come to know about this event)  4894 non-null   object
 8   Designation                                                      4894 non-null   object
 9   Year of Graduation                                               4894 non-null   int64
 10  City                                                             4894 non-null   object
 11  CGPA                                                             4894 non-null   float64
 12  Experience with python (Months)                                  4894 non-null   int64
 13  Family Income                                                    4894 non-null   object
 14  Expected salary (Lac)                                            4894 non-null   int64
 15  Leadership- skills                                               4894 non-null   object
dtypes: float64(1), int64(4), object(11)
memory usage: 611.9+ KB
None
"""



# Analysis Questions
# Basic Questions


# 1. How many unique students are included in the dataset?
print(f"Number of Unique Students : {df["Email ID"].nunique()}")
"""
ANSWER : Number of unique students: 2157
"""


# 2. What is the average GPA of the students?
print(f"Average of GPA (Grade Point Average) :  {df['CGPA'].mean():.2f}")
""" 
ANSWER : Average of GPA (Grade Point Average) :  8.04
"""


# 3. What is the distribution of students across different graduation years?
grad_year_dist = df["Year of Graduation"].value_counts()
print(f"Graduation Year Distribution : {grad_year_dist}")
""" 
ANSWER : Graduation Year Distribution : 
Year of Graduation
2023    1536
2024    1511
2025    1292
2026     555
Name: count, dtype: int64
"""


# 4. What is the distribution of students' experience with Python programming?
python_exp_dist = df["Experience with python (Months)"].value_counts()
print(f"Python Experience Distribution : {python_exp_dist}")
""" 
ANSWER : Python Experience Distribution :
Experience with python (Months)
5    1242
3    1008
8     800
6     738
7     640
4     466
Name: count, dtype: int64
"""


# 5. What is the average family income of the students?
filter_family_inc = {"0-2 Lakh": 1, "2-5 Lakh": 3.5, "5-7 Lakh": 6, "7 Lakh+": 7.5}
df["Filtered Family Income"] = df["Family Income"].map(filter_family_inc)
avg_family_inc = df['Filtered Family Income'].mean()
print(f"Average Family Income : {avg_family_inc:.2f}")
""" 
ANSWER : Average Family Income : 1.30
"""


# 6. How does the GPA vary among different colleges? (Show top 5 results only)
top_5_gpa = df.groupby("College Name")["CGPA"].mean().sort_values(ascending=False).head(5)
print(f"The GPA vary among 5 different colleges : {top_5_gpa}")
""" 
ANSWER :
The GPA vary among 5 different colleges :                                            College Name
THAKUR INSTITUTE OF MANAGEMENT STUDIES, CAREER DEVELOPMENT & RESEARCH - [TIMSCDR]    8.585714
St Xavier's College                                                                  8.578571
B. K. Birla College of Arts, Science & Commerce (Autonomous), Kalyan                 8.456410
Symbiosis Institute of Technology, Pune                                              8.303448
AP SHAH INSTITUTE OF TECHNOLOGY                                                      8.283333
Name: CGPA, dtype: float64
"""


# 7. Are there any outliers in the quantity (number of courses completed) attribute?
# Quantiles
Q1 = df['Quantity'].quantile(0.25)
Q3 = df['Quantity'].quantile(0.75)
IQR = Q3 - Q1

# Boundaries
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Quantity'] < lower_bound) | (df['Quantity'] > upper_bound)]
print(f"Outliers in the Quantity (Number of Courses Completed) : {outliers.shape[0]}")
"""
ANSWER : Outliers in the Quantity (Number of Courses Completed) : 0
"""


# 8. What is the average GPA for students from each city?
avg_gpa_city = df.groupby("City")['CGPA'].mean().sort_values(ascending=True)
print(f"Average GPA for Students from each City : {avg_gpa_city}")
""" 
ANSWER : Average GPA for Students from each City : 
City
New Delhi    7.307143
Rewari       7.392308
Daman        7.421429
Nashik       7.592857
Panipat      7.615385
               ...
Puri         8.450000
Gurugram     8.459259
Sonipat      8.464286
Raipur       8.507143
Kolhapur     8.557143
Name: CGPA, Length: 177, dtype: float64
"""


# 9. Can we identify any relationship between family income and GPA?
sns.scatterplot(data=df, y="CGPA", x="Family Income")
plt.title("Relationship Between Family Income and GPA")
plt.xlabel("Family Income (in Lakhs)")
plt.ylabel("GPA (Grade Point Average)")
plt.show()
""" 
ANSWER : The graph shows that GPA is fairly consistent across all income groups, indicating no strong correlation between family income and GPA.
"""



# Moderate Questions


# 10. How many 10. How many students from various cities? (Solve using a data visualization tool).? (Solve using a data visualization tool).
sns.countplot(data=df, x="City", palette="cividis")
plt.xlabel("Cities")
plt.title("Students from Various Cities")
plt.xticks(rotation=90)
plt.show()
"""
ANSWER : The graph shows a wide distribution of students across many cities, with some cities contributing significantly more students than others.
"""


# 11. How does the expected salary vary based on factors like 'GPA', 'Family income', 'Experience with Python (Months)'?
# Calculate correlations between expected salary and other factors

#  Heatmap Representation 
correlations = df[['Expected salary (Lac)', 'CGPA', "Filtered Family Income", 'Experience with python (Months)']].corr()
print(correlations)

# Visualize correlations using a heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data=correlations, annot=True, cmap='gist_heat_r')
plt.title('Correlation Between Expected Salary and Other Factors')
plt.show()
""" 
ANSWER : Expected salary shows weak positive correlation with CGPA and Python experience, and minimal correlation with family income.
"""

# pairplot representation 
variables = ['Expected salary (Lac)', 'CGPA', 'Filtered Family Income', 'Experience with python (Months)']
sns.pairplot(data=df, vars=variables, diag_kind=True, kind="scatter")
plt.show()
""" 
ANSWER : The scatter plots show no strong linear relationships between expected salary and other factors like CGPA, income, or Python experience.
"""


# 12. Which event tends to attract more students from specific fields of study?
events = sns.countplot(data=df, x='Events', palette='muted')
plt.xticks(rotation=85)
plt.title("Event Participation Count by More Students")
for i in range(0, 16):
    events.bar_label(events.containers[i])
plt.show()
""" 
ANSWER : "Product Design & Full Stack" had the highest participation, followed by "Internship Program(IP) Success Conclave"
"""


# 13. Do students in leadership positions during their college years tend to have higher GPAs or better expected salaries?
leadership_exp = df[df['Leadership- skills']=='yes']['Expected salary (Lac)'].mean()
non_leadership_exp = df[df['Leadership- skills']=='no']['Expected salary (Lac)'].mean()

print(f"Mean Expected salary (Lac) with Leadership Expereinces : {leadership_exp:.2f}")
print(f"Mean Expected salary (Lac) with Non Leadership Expereinces : {non_leadership_exp:.2f}")

leadership_gpa = df[df['Leadership- skills']=='yes']['CGPA'].mean()
non_leadership_gpa = df[df['Leadership- skills']=='no']['CGPA'].mean()

print(f"Mean GPA with Leadership Expereinces : {leadership_gpa:.2f}")
print(f"Mean GPA with Non Leadership Expereinces : {non_leadership_gpa:.2f}")
""" 
ANSWER : 
Mean Expected salary (Lac) with Leadership Expereinces : 13.97
Mean Expected salary (Lac) with Non Leadership Expereinces : 13.80
Mean GPA with Leadership Expereinces : 8.04
Mean GPA with Non Leadership Expereinces : 8.04
"""


# 14. How many students are graduating by the end of 2024?
graduating_students = df[df['Year of Graduation'] <= 2024]
grad_student_2024 = graduating_students.shape[0]
print(f"Number of students graduating by the end of 2024: {grad_student_2024}")
""" 
ANSWER : students are graduating by the end of 2024 : 3047
"""


# 15. Which promotion channel brings in more student participation for the event?
promotion_channels = df['How did you come to know about this event?'].value_counts()
print(f"promotion channel brings in more student participation for the event : {promotion_channels}")
""" 
ANSWER : 
How did you come to know about this event?
Whatsapp                                          3283
Email                                              438
SPOC/ College Professor                            326
Others                                             153
Cloud Counselage Website                           129
"""


# 16. Find the total number of students who attended the events related to Data Science.
event_attend = df[(df['Events']=='IS DATA SCIENCE FOR YOU?') | (df['Attendee Status']=='Attending')].count()
event_attend_count = event_attend.shape[0]
print(f"Total Number of students who attended the events related to Data Science : {event_attend_count}")
""" 
ANSWER : total number of students who attended the events related to Data Science : 17
"""


# 17. Those who have high CGPA & more experience in language tend to have high expectations for salary (Avg)?
high_cgpa_exp = df[(df['CGPA']>=8) & (df['Experience with python (Months)']>=6)]
salary_expect_avg = df['Expected salary (Lac)'].mean()
print(f"High CGPA & more experience in language trend to have high expectations for salary (Avg) : {salary_expect_avg:.2f}")
""" 
ANSWER : High CGPA & more experience in language trend to have high expectations for salary (Avg) : 13.94
"""


# 18. How many students know about the event from their colleges? Which of these are the Top 5 colleges?
college_promo = df[df['Specify in "Others" (how did you come to know about this event)']=="College"]
top_5_college = college_promo['College Name'].value_counts().head(5)
print(f"Students know about the event from their colleges? Which of these are the Top 5 colleges : {top_5_college}")
""" 
ANSWER : 
Students know about the event from their colleges? Which of these are the Top 5 colleges : College Name
priyadarshini college of engineering, nagpur                                                275
vidyalankar institute of technology, mumbai                                                 257
ld college of engineering, ahmedabad, gujarat                                               247
government polytechnic gandhinagar                                                          205
b. k. birla college of arts, science & commerce (autonomous), kalyan                        205
Name: count, dtype: int64
"""



# Live Project : Data Analysis 
# Cloud Counselage
# ***** COMPLETED *****