# Name: Justin Coon
# Date: 09-30-2025
# A program that mimicks the analysis of phishing attempts

# Variable declaration for for the email subject 
email_subject = input("Enter the email subject line: ")

# Variable declaration for allowing the if, elif, else clauses to check for 
# lowercase flags in the middle or end of the subject line
email_flag = email_subject.lower()

# if clause checking for all caps or all lowercase for the word urgent and also
# 'immediate action recuired and if those flags are present, prints HIGH Risk statement
if 'urgent' in email_flag or email_subject == 'URGENT' or email_subject == 'immediate action required':
    
    print("\nSECURITY ASSESSMENT:\nHIGH RISK: Possible phishing attempt.")
    print("------------------------")
    print(f"Analyzed subject: \"{email_subject}\"")
    
elif 'win' in email_flag or 'free' in email_flag:
    
    print("\nSECURITY ASSESSMENT:\nMEDIUM RISK: Suspicious offer detected.")
    print("------------------------")
    print(f"Analyzed subject: \"{email_subject}\"")
    
elif 'password reset' in email_flag:
    
    print("\nSECURITY ASSESSMENT:\nLOW RISK: Verify legitimacy with sender.")
    print("------------------------")
    print(f"Analyzed subject: \"{email_subject}\"")
    
else:
    
    print("\nNo phishing indicators detected.")
    print("------------------------")
    print(f"Analyzed subject: \"{email_subject}\"")
    
    
    