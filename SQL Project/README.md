# Decoding Cyber Threats In India
This Python project analyzes cybersecurity threat data using MySQL, Mysql-connector-python, Pandas, Matplotlib, and Seaborn. The dataset provides critical insights into factors such as protocols, packet types, malware indicators, anomaly scores, attack signatures, severity levels, and their impact on network security. High risks of cyber attacks are observed under specific conditions, emphasizing the need for targeted interventions and advanced threat detection measures.

# Data
The analysis uses a CSV file named cybersecurity_attacks.csv. This file should be placed in the root directory of the repository. The expected data includes information about the Year, Month, Day, Source Port, Destination Port, Protocol, Packet Length, Packet Type, Traffic Type, Malware Indicators, Anomaly Scores, Alerts, Attack Type, Attack Signature, Action Taken, Severity Level, User Information, Device Information, Network Segment, States, Proxy Information, Firewall Logs, IPS Alerts, Log Source, Source IP Address, and Destination IP Address.

# Analysis and Visualizations
 -> Handles missing values .
 
 -> Converts data types where necessary (e.g., date columns to datetime objects) .
 
 -> Drops irrelevant or mostly empty columns .

 # Exploratory Data Analysis:
 Generates various visualizations using Matplotlib, Seaborn, providing insights into different aspects of the dataset:
 1. Malware Indicators Distribution By Months
 2. Traffic Type Distribution
 3. No. Of Devices by Traffic Type & Protocol
 4. Packet Length Distribution
 5. Anomaly Scores By Days
 6. Action Taken Distribution
 7. Alerts By Months
 8. Severity Level By Years
 9. User Count By Years & Months
 10. Attack Signature Distribution By Months
 11. Attack Type Distribution
 12. Unique IP Source By States

# Conclusion:
 This analysis highlights time-based cyber threat patterns, protocol vulnerabilities, and regional disparities. Key findings, such as the dominance of DNS attacks and 33% intrusion rates, emphasize the need for targeted cybersecurity measures. These insights provide a foundation for stronger defense strategies across India.

# Usage
  Prerequisites:
   Python 3.x

   MySQL 

   mysql-connector-python
   
   pandas
   
   matplotlib
   
   seaborn
 
