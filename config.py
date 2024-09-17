import os


BASE_URL = "https://jobs.dou.ua/vacancies/"
CATEGORIES_URLS = {
    "Python": BASE_URL + "?category=Python"
}

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
RESULT_DIR = os.path.join(BASE_DIR, "results")
PLOT_DIR = os.path.join(BASE_DIR, "result_plots")

LEVELS = [
    "UNKNOWN",
    "TRAINEE",
    "JUNIOR",
    "MIDDLE",
    "SENIOR",
    "TEAM LEAD",
    "HEAD"
]

EXPERIENCE = [
    "0-1",
    "1-3",
    "3-5",
    "5plus",
]

TECHNOLOGIES = [
    "CircleCI", "Infrastructure Monitoring", "Static Site Generators",
    "Continuous Integration (CI)", "Flask", "Beautiful Soup", "Penetration Testing",
    "Change Management", "Scrapy", "Security Automation", "Data Security",
    "Virtualenv", "Databases", "OAuth", "SQLAlchemy", "UX/UI Design", "Blockchain",
    "Data Modeling", "Version Control", "Application Security", "Regulatory Affairs",
    "Web2py", "Big Data", "Server-side rendering", "Alerting", "GraphQL", "Heroku",
    "Database Administration", "Compliance", "Azure", "ORM (Object-Relational Mapping)",
    "Site Reliability Engineering (SRE)", "MongoDB", "Data Warehousing", "Spark",
    "Celery", "Capacity Management", "REST API", "Security Auditing", "Selenium",
    "End-to-End Testing", "Django", "Machine Learning", "Backend frameworks",
    "Continuous Deployment (CD)", "Incident Management",
    "Performance Testing", "ITIL (Information Technology Infrastructure Library)",
    "Jamstack", "Collaboration Tools", "DevSecOps", "Code Quality", "PyTorch",
    "Pair Programming", "Cloud Security", "SQL", "IaaS (Infrastructure as a Service)",
    "Cybersecurity", "OpenID Connect", "Pipenv", "Code Review", "SQLite", "Pygame",
    "API Gateway", "Server Security", "Microservices", "Kanban",
    "Load Testing", "Application Performance Management (APM)", "Problem Management",
    "Web3", "Docker", "Logging", "Static Code Analysis", "Python", "Scikit-Learn",
    "Flask-RESTful", "PyInstaller", "Firewalls", "Intrusion Prevention System (IPS)",
    "Jupyter Notebook", "Security Information and Event Management (SIEM)", "Conda",
    "Full-stack development", "Encryption", "Multicloud", "Automation", "Travis CI",
    "Decentralized applications (DApps)", "Release Management", "Kivy",
    "REST API Security", "Data Privacy", "ITSM (IT Service Management)",
    "CISSP (Certified Information Systems Security Professional)", "Game development",
    "GitHub", "Endpoint Security", "Security Policies", "Risk Management",
    "HIPAA (Health Insurance Portability and Accountability Act)", "ETL (Extract, Transform, Load)",
    "Hybrid Cloud", "Keras", "Matplotlib", "Git", "Automated Testing", "Hadoop",
    "SSL/TLS", "Seaborn", "RESTful API", "NIST Cybersecurity Framework", "PostgreSQL",
    "Splunk", "Fault Tolerance", "SecDevOps", "Unit Testing", "MySQL", "Lambda Functions",
    "Scrum", "Containerization", "Ethereum", "Cryptography", "ELK Stack", "NumPy",
    "Data Science", "Flake8", "Vulnerability Management", "Serverless Architecture",
    "Integration testing", "Solidity", "Network Security", "FaaS (Function as a Service)",
    "Dynamic Code Analysis", "Kubernetes", "Plotly", "Tkinter", "Smart Contracts",
    "GitLab", "Configuration Management", "Incident Response", "Unit testing",
    "JWT (JSON Web Tokens)", "Data Lakes", "Pytest", "Business Intelligence (BI)",
    "Public Cloud", "Monitoring", "Swagger", "Penetration testing",
    "GDPR (General Data Protection Regulation)", "FastAPI", "High Availability",
    "Responsive design", "Grafana", "Client-side rendering", "Scalability",
    "Server-side rendering (SSR)", "NoSQL", "Micro Frontends", "PyQt", "XML",
    "Private Cloud", "Prometheus", "DevOps", "XP (Extreme Programming)",
    "React", "Angular", "Vue.js", "Cross-platform development",
    "Serverless", "IT Governance", "AWS", "Data Engineering",
    "Application Performance Monitoring (APM)", "Security Testing", "Bitbucket",
    "TensorFlow", "Progressive Web Apps (PWA)", "WebSocket", "Jenkins", "WebSockets",
    "Dashboards", "Identity and Access Management (IAM)", "SaaS (Software as a Service)",
    "Data Mining", "ISO/IEC 27001", "Mobile app development", "PaaS (Platform as a Service)",
    "JSON", "OWASP ZAP", "SAFe (Scaled Agile Framework)", "Lean", "Infrastructure as Code (IaC)",
    "Continuous Delivery (CD)", "Code Coverage", "Automation Testing", "Caching",
    "Orchestration", "Integration Testing", "PyLint", "CDN (Content Delivery Network)",
    "Data Analytics", "Pyramid", "Service Desk", "Single Page Applications (SPA)",
    "Smart Contract Auditing", "Intrusion Detection System (IDS)", "Data Governance",
    "Natural Language Processing (NLP)", "Cloud Computing", "CI/CD (Continuous Integration/Continuous Deployment)",
    "OWASP Top Ten", "Google Cloud Platform (GCP)", "Pandas", "Agile", "Headless CMS",
    "Deep Learning", "Node.js", "TypeScript", "React", "CSS", "HTML", "JavaScript", "Next.js",
    "Amazon Web Services", "DigitalOcean", "aiogram", "Telethon",
]
