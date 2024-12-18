# Bank Transaction Fraud Detection
## Project Overview
This project analyzes bank transaction data to detect fraudulent activities using machine learning techniques. Fraud detection is crucial for maintaining financial security and preventing monetary losses.

### Project Folder Structure
*   Data
    *   Contains raw and preprocessed datasets.

*   Models
    *   Contains machine learning models and checkpoints.

*   Notebooks
    *   Contains Jupyter notebooks for data exploration and modeling.

*   Scripts
    *   Python scripts for data preprocessing training, and evaluation.

*   README.md
    *   Further detailed project documentation.

The Dataset & The Details
-----------

### The Source
The data utilised was sourced from Kaggle:

 _**Bank Transaction Dataset for Fraud Detection**_.  
* _Link:_ https://www.kaggle.com/datasets/valakhorasani/bank-transaction-dataset-for-fraud-detection 
    

### The Features

*   **Transaction ID** - Unique identifier for each transaction.
*   **Transaction Amount** - The monetary value of the transaction (in USD).
*   **Transaction Type** - Type of transaction (e.g., withdrawal, transfer, payment).
*   **Account Balance** - The account balance at the time of the transaction (in USD).
*   **Transaction Timestamp** - Date and time of the transaction.
*   **Location** - The geographical location of the transaction.
*   **Device or Channel Used** - Device type (mobile, web, ATM) used for the transaction.
*   **Fraud Label** - Indicates if the transaction is fraudulent (1) or not (0).

### The Target Variable

*   **Target**: Binary classification (Fraud vs. Not Fraud).

### The Approach

* **Exploratory Data Analysis (EDA)**
    * Visualize patterns and trends.
* **Identify imbalanced data.**
    * Data Preprocessing
* **Handle missing values.**
    * Encode categorical features.
    * Feature scaling.
* **Modeling**
    * Algorithms used: Logistic Regression, Random Forest, XGBoost, etc.
    * Metrics: Precision, Recall, F1-score, ROC-AUC.
* **Evaluation**
    * Model performance compared using metrics.
    * Challenges including false positives and false negatives addressed.
    * Handle missing values.
    * Encode categorical features.
    * Feature scaling.

### Dependencies Used
* **Python 3.8+**
    * **Libraries**: pandas, numpy, scikit-learn, matplotlib, seaborn, xgboost

Why _is_ Fraud Detection Important, Anyway?
-------------------------------------------

### The Big-Picture Data:

60% of US credit card holders have been victims of fraud, with 45% experiencing multiple fraudulent attacks. \[1\]  
This equates to 52 million Americans falling victim to fraudulent charges on their bank cards in the last year alone, with unauthorised purchases exceeding $5 billion. \[1\]

Fraudulent transactions have increased by 14% since 2022. \[2\] 

Methodologies are becoming more sophisticated and prevalent, including targeted phishing attacks, skimming and card-not-present (CNP) fraud, key reasons as to why fraud detection is vital include:

1.  **Financial Protection**
    *   Detecting fraud prevents monetary losses for individuals, businesses and financial institutions.
2.  **Customer Trust**
    *   Ensuring secure transactions builds trust and confidence amongst customers in financial systems.
3.  **Legal Compliance**
    *   Financial institutions are required to comply with regulations, such as the the _Anti-Money Laundering Act of 2020_ (AMLA).
4.  **Real-Time Monitoring**
    *   Advanced fraud detection techniques, including machine learning algorithms and anomaly detection, enable the prevention of fraud in real-time, mitigating potential damages.
5.  **Scalability in Digital Finance**
    *   As transaction volumes grow with increasing access to digital finance platforms, robust fraud detection systems are vital to ensure sustainability and reliability.

What Challenges Exist in Detecting Fraudulent Transactions Currently?
---------------------------------------------------------------------

### Let's Take a Closer Look...

Detecting fraudulent transactions poses multiple challenges due to the dynamic and evolving nature of fraudulent techniques used. Such challenges include:

1.  **Imbalanced Data**

    *   Fraudulent transactions (the minority class) are rare compared to legitimate ones (the majority class), resulting in imblanced datasets where machine learning models may become biased towards predicting the majority class, subsequently resulting in poor fraud detection. \[3\]

2.  **Evolving Fraud Techniques**

    *   Traditional fraud detection methods are often reliant on rule-based systems and manual intervention and these are proving increasingly inadequate in the face of evolving threats. \[4\]

5.  **False Positives and False Negatives**

    *   **False Postives**: Incorrectly flagging legitimate transactions as fraud can frustrate customers and damage business relationships.
    *   **False Negatives**: Missing actual fraudulent transactions can result in significant financial losses and reduced customer trust.

6.  **Real-Time Detection**

    *   Fraud detection often requires real-time analysis of large volumes of transaction data, which demands high computational power and optimised models.

7.  **Complex Patterns**
    *   Fraudulent transactions often exhibit subtle, complex patterns that are difficult to detect without advanced machine learning or deep learning techniques.

8.  **Anonymity in Digital Transactions**
    *   Fraudsters can hide their identities or operate through anonymized digital payment systems, making detection and prevention harder.

9.  **Scalability**
    *   With increasing transaction volumes, fraud detection systems must be scalable and efficient to process large datasets without delays.

## References
1.  https://www.security.org/digital-safety/credit-card-fraud-report/
2. https://www.featurespace.com/newsroom/unmasking-the-persistent-challenge-of-check-fraud-in-the-us
3. https://medium.com/@juanc.olamendy/tackling-the-challenge-of-imbalanced-datasets-a-comprehensive-guide-2feb11ca2fa0 
4. https://ajmrr.org/journal/article/view/217?articlesBySimilarityPage=3 
