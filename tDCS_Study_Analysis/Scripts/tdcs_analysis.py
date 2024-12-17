# Load essential libraries for data analysis 
import pandas as pd
import pyreadstat 
import matplotlib.pyplot as plt
print("Libraries imported successfully!")
# Libraries are now loaded~

# Load in the tDCS data for analysis & viewing
    # Load the .sav File: Use pyreadstat to load the SPSS .sav file into a pandas DataFrame.
data, meta = pyreadstat.read_sav("C:\\Users\\leahl\\OneDrive\\Desktop\\Data Analysis Projects\\Effect of tDCS, TENS and neural mobilization on pain in patients with lumbar radicular pain\\Mendeley dataset.sav")
    # The meta variable holds metadata information (like variable labels) to explore what each column represents.

# Display the first few rows to understand the structure of the dataset
print(data.head())

# Check the basic structure and data types
print(data.info())

# Look at summary statistics
print(data.describe())

# Display the metadata about the Group variable to facilitate accurate interpretation
# print(meta.column_names_to_labels) 
    # Shows labels for each column
# print(meta.value_labels) 
    # Shows mappings for categorical variables 

# Group 1: Likely represents the experimental group (active tDCS + TENS)
# Group 2: Likely represents the control group (sham tDCS + TENS).

# Visualise data distributions of variables:
    # Pre_NPRS, Mid_NPRS, Post_NPRS, Pre_SF, Mid_SF, and Post_SF
       
        # Pre_NPRS = Numeric Pain Rating Scale (NPRS) before treatment 
        # Mid_NPRS = NPRS score during treatment / at interim point
        # Post_NPRS = NPRS score after treatment (are they still in a lot of pain?)
        
        # Pre_SF = SF health survey score before treatment 
        # Mid_SF = SF score during treatment 
        # Post_SF = SF score after treatment 

# Let's look at how people rated their pain before treatment
data['Pre_NPRS'].hist()
plt.title("Pre-Treatment NPRS Distribution")
plt.xlabel("NPRS Score")
plt.ylabel("Frequency")
plt.show()

plt.clf()  # Clear the plot

# Let's look at how people rated their pain after treatment 
data['Post_NPRS'].hist()
plt.title("Post-Treatment NPRS Distribution")
plt.xlabel("NPRS Score")
plt.ylabel("Frequency")
plt.show()

plt.clf()  # Clear the plot

# Now let's visualise and compase post-NPRS scores across these 2 Groups using boxplot
# Step 1: Map Group to Treatment Type
data['Treatment_Type'] = data['Group'].map({1: "Sham tDCS + TENS", 2: "Active tDCS + TENS"})

# Step 2: Create the boxplot using Treatment_Type
data.boxplot(column='Post_NPRS', by='Treatment_Type')
plt.title("Post-Treatment NPRS Scores by Treatment Type")
plt.xlabel("Treatment Type")
plt.ylabel("Post-NPRS Scores")
plt.show()

plt.clf()  # Clear the plot

# Let's calculate the change over time in NPRS Scores
    # Pre-to-Post ChangeL The difference between pre-treatment and post-treatment NPRS Scores

data['Change_NPRS'] = data['Post_NPRS'] - data['Pre_NPRS']
   
    # Display the change in NPRS scores 
print(data[['Reference_no', 'Change_NPRS']])

# Now let's calculate the midpoint of change -- shows how pain scores evolved over time
data['Change_Pre_to_Mid'] = data['Mid_NPRS'] - data['Pre_NPRS']
data['Change_Mid_to_Post'] = data['Post_NPRS'] - data['Mid_NPRS']

# Now let's visualise the change between Active tDCS + TENS & Sham tDCS + TENS groups 
    # See which one resulted in greater pain reduction visually 
    # Boxplot of Change in NPRS by Treatment Type 
data.boxplot(column='Change_NPRS', by='Treatment_Type')
plt.title("Change in NPRS Scores by Treatment Type")
plt.xlabel("Treatment Type")
plt.ylabel("Change in NPRS Scores")
plt.show()

plt.clf() # Clear the plot

# Now let's determine any statistically significant differences in pain reduction between the 2 treatment groups
    # First we need to check for a Normal Distribution (in order to use t-test)

# Let's use a Histogram for a quick visual cue:
data['Change_NPRS'].hist(bins=10) # binds parameter controls the no. of bars 'bins' in the histogram
plt.title("Histogram of Change in NPRS Scores")
plt.xlabel("Change in NPRS")
plt.ylabel("Frequency")
plt.show()

# Now that we have a visual cue, let's perform a Shapiro-WIlk test to confirm normality
    # If the p-value is less than .05, can reject null hypothesis that data is normally distributed 
from scipy.stats import shapiro 

# Shapiro-Wilk Test for Change_NPRS
stat, p_value = shapiro(data['Change_NPRS'])
print(f"Shaprio-Wilk Test: W = {stat}, p = {p_value}")

if p_value < 0.05:
    print("The data is not normally distributed.")
else: 
    print("The data is normally distributed.")

# Because data is borderline normal, perform an Anderson-Darling test
from scipy.stats import anderson

# Anderson-Darling Test for normality on Change_NPRS
result = anderson(data['Change_NPRS'])
print("Anderson-Darling Test Statistic:", result.statistic)
print("Critical Values:")

for i in range(len(result.critical_values)):
    sig_level, crit_value = result.significance_level[i], result.critical_values[i]
    print(f"At the {sig_level}% significance level, the critical value is {crit_value}")
    if result.statistic > crit_value:
        print(f"The data is not normally distributed at the {sig_level}% signficance level.")
    else:
        print(f"The data is normally distributed at the {sig_level}% signficance level.")

# Given the data does not meet normality assumptions, can't perform t-test so let's perform Mann-Whitney U test:
    # Mann-Whitney U test is a non-parametric test that can be used to compare differences between two independent groups when the data does not follow a normal distribution

# Seperate the Change_NPRS scores into 2 groups based on treatment type via Boolean condition that checks each row in Treatment_Type column of the data Dataframe:
active_change = data[data['Treatment_Type'] == "Active tDCS + TENS"]['Change_NPRS']
sham_change = data[data['Treatment_Type'] == "Sham tDCS + TENS"]['Change_NPRS']

from scipy.stats import mannwhitneyu

# Perform Mann-Whitney U test
u_stat, p_value = mannwhitneyu(active_change, sham_change, alternative='two-sided') # alternative ='two-sided' specifies a two-sided test, which is standard unless you have a specific reason to believe one group should have higher or lower scores than the other.
print(f"Mann-Whitney U test result: U = {u_stat}, p = {p_value}")

#  Mann-Whitney U revealed non-normal distribution 

# Code test
print("This code worked!")