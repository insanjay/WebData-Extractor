# WebData Extractor


# **Project: Web Data Extractor**  

## **1. Overview**  
This project is designed to extract data from websites such as book names, prices, and stock availability. It saves the extracted data in JSON and CSV formats, making it easier to analyze and share.  

### **Purpose**  
Initially created for practice, this project now showcases my web scraping and data manipulation skills in my portfolio, targeting clients and professionals in my network.  

### **Target Audience**  
- **Clients**: To demonstrate my web scraping capabilities.  
- **Professionals**: To connect with quality contacts in the tech domain.  

---

## **2. Features**  
1. **Data Extraction**: Scrapes data like book names, prices, and stock availability from static websites.  
2. **File Format Support**:  
   - **JSON**: Ideal for structured, hierarchical data that can be used in APIs or web applications.  
   - **CSV**: Perfect for tabular data, compatible with Excel and analytical tools.  
3. **Customizable**:  
   - Designed for users with basic Python knowledge.  
   - Comments in the script provide guidance for customization.  

---

## **3. Technical Details**  
1. **Technologies Used**:  
   - Python for scripting.  
   - BeautifulSoup for parsing HTML content.  
   - Requests for sending and handling HTTP requests.  
2. **Supported File Formats**: JSON and CSV.  
3. **Dependencies**:  
   - **Required Libraries**: BeautifulSoup (`bs4`) and requests.  
   - **Installation**:  
     ```bash  
     pip install bs4 requests  
     ```  
   - **Imports**:  
     ```python  
     from bs4 import BeautifulSoup  
     import requests  
     ```  

---

## **4. Process and Demo**  
1. **Steps to Use**:  
   - Paste the target website URL in the `url` variable.  
   - Inspect the website to identify the elements containing the desired data.  
   - For multiple elements, use `soup.find_all('tag_name')` and loop through them.  
   - For single elements, use `soup.find('tag_name')`.  
   - Note: Basic HTML and Python knowledge is essential for customization.  
2. **Sample Data**: Screenshots of extracted data (add them in this section).  

---

## **5. Future Scope**  
1. **Planned Enhancements**:  
   - Adding Selenium to scrape data from dynamic websites.  
2. **Challenges**:  
   - Identifying the right HTML elements for data extraction.  
   - Handling encoding issues while saving CSV files (e.g., using `utf-8-sig` to resolve the "Â" issue).  

---

## **6. Personal Branding**  
1. **GitHub Link**: [insanjay](https://github.com/insanjay).  
2. **LinkedIn**: [Sanjay Kumar](www.linkedin.com/in/insanjay).  
3. **E-mail**: [insanjay.work@gmail.com](mailto:insanjay.work@gmail.com).  

---

## **7. License**  
This project is **open-source** and free to use.  

<div class="badge-base LI-profile-badge" data-locale="en_US" data-size="medium" data-theme="dark" data-type="VERTICAL" data-vanity="insanjay" data-version="v1"><a class="badge-base__link LI-simple-link" href="https://in.linkedin.com/in/insanjay?trk=profile-badge">Sanjay Kumar</a></div>
              
              