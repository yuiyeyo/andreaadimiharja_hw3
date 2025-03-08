# CSCV 337 Assignment 3  

This web application is designed as part of the **CSCV 337 Web Programming Assignment**.  
 

---

## **File Overview**  

### **Backend (Django)**
- **Django Framework** is used to handle server-side logic, including database management and dynamic content rendering.
- **Database:** Stores articles and visual content for the news platform.
- **Views:** Handles requests for the homepage, individual articles, and search functionality.
- **URL Routing:** Maps user requests to corresponding views.

### **Frontend (HTML, CSS, JavaScript)**
- **Homepage (`home.html`)**
  - Displays featured articles dynamically.
  - Uses Django template engine for content rendering.
- **Article Page (`article.html`)**
  - Shows individual articles with images and videos.
  - Fetches related articles dynamically.
- **Search Feature**
  - Users can search for articles using a search bar.
  - Queries the database and returns matching results.

### **Functionality**
- **Dynamic Content Loading:** Articles and visual content are fetched from the database.
- **Search & Filtering:** Users can search for specific articles by keywords.
- **Responsive Design:** Optimized for both desktop and mobile screens.

