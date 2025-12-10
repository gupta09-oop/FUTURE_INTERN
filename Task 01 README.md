Task 01 — Web Application Security Testing (OWASP Juice Shop)

Author: Kshitij Gupta
Internship: Future Interns — Cyber Security
Project: FUTURE_CS_01

🔍 Overview

This task focuses on identifying, exploiting, and documenting common web security vulnerabilities using OWASP Juice Shop, an intentionally vulnerable web application used for cybersecurity training.

This project includes hands-on exploitation of:

SQL Injection (SQLi)

Cross-Site Scripting (XSS)

Weak JWT Verification

Insecure Direct Object Reference (IDOR)

Broken Access Control (Admin Panel Access)

All findings are documented with screenshots and detailed explanations.

🧨 1. SQL Injection (Authentication Bypass)

✔ Bypassed login authentication using payload:

' OR 1=1--


✔ Gained access without a valid password
✔ Juice Shop displayed challenge as solved

📸 Screenshot:
/screenshots/sqli.png

🧨 2. Cross-Site Scripting (Reflected XSS)

Tested XSS from the search bar using payload:

"><script>alert('XSS')</script>


✔ JavaScript executed successfully
✔ Challenge solved

📸 /screenshots/xss.png

🔐 3. Weak JWT Verification → Admin Access

Steps performed:

Logged in normally

Extracted JWT from Local Storage

Modified payload:

"role": "admin"


Removed signature

Replaced token in Local Storage

Reloaded → Full admin access

📸 /screenshots/jwt.png

🔓 4. IDOR (Accessing Other Users’ Information)

Found vulnerable endpoint:

/rest/user/id


Manipulated ID:

?id=1 → admin user  
?id=7 → morty user


✔ Application returned private data without authorization checks

📸 /screenshots/idor.png

🔥 5. Admin Panel Access

After JWT privilege escalation:

✔ Accessed /administration
✔ Viewed all registered users
✔ Challenge solved

📸 /screenshots/admin.png

📝 Conclusion

In this task, I successfully identified and exploited several core OWASP Top 10 vulnerabilities in a safe, controlled environment.

This challenge improved my understanding of:

Input validation flaws

Access control weaknesses

Token-based authentication risks

Real-world attack methodologies

Secure coding practices

This task builds the foundation needed for further penetration testing and cybersecurity research.
