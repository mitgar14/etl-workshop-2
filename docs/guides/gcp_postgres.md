# 🚀 Guide to Creating a PostgreSQL Instance in GCP

## ✅ Prerequisites

1. 🛡️ A Google Cloud account (if you don't have one, [sign up here](https://cloud.google.com/free)).
2. 📂 A Google Cloud project created (you can create it in the [GCP console](https://console.cloud.google.com/)).
3. 🔧 Google Cloud **SQL** and **Compute Engine** APIs enabled in the project.

## 💰 Claim Free Credits on GCP

If you want to claim $300 free to use on Google Cloud Platform services, you can go to this [Notion page](https://www.notion.so/Instructivo-para-Reclamar-Cr-ditos-Gratis-en-Google-Cloud-103a9368866a80f98490e68b4a944c4d?pvs=21).

## 🛠️ Steps to Create a PostgreSQL Instance on GCP

### 1. Log in to GCP

- Log in to your Google Cloud account and select the project in which you want to create the PostgreSQL instance. You can also create a new project as follows:

![drive-crear.gif](drive-crear.gif)

- You can select which project to choose by clicking on the box at the top. Choose from the menu among all the projects you have.
    
    ![image.png](image.png)
    

### 2. Access the Cloud SQL Console and Create a New Instance

- In the GCP console, navigate to the side menu and select **SQL**.
    - 🔍 Or use the search bar and type "SQL" to go directly to the section.
- Click on the **Create Instance** ➕ button.
- Select **PostgreSQL** 🐘 as the database type.
- Important to enable the Compute Engine API: until you have it active, you cannot create an instance.

![drive-sql.gif](drive-sql.gif)

### 3. Configure Instance Options

- **💻 Cloud SQL Editions:**
    - Choose the *Enterprise* edition plan to reduce costs. Additionally, you can choose between the *Sandbox* and *Development* settings.
- **🔑 Authentication and Connection**:
    - Provide a unique name for your instance.
    - Provide a username and password for the database (the default user is `postgres`).
- **⚙️ Machine Configuration**:
    - Select the PostgreSQL version you wish to use.
    - Configure the 🌍 **region** and **zone** where you want the instance to be hosted (choose the closest to you or your users).
    - Define the machine type and specifications (CPU, memory, etc.) according to your needs.
- **💾 Storage**:
    - Define the disk size and whether you want it to expand automatically when necessary.
- **🌐 Connectivity**:
    - Add the IP `0.0.0.0/0` to the list of authorized networks in *Connections*.
- **📦 Backup**:
    - Enable automatic backups if desired (recommended).

---

![drive-instancia.gif](drive-instancia.gif)

### 4. Review and Create

- Review the instance configurations and click on **Create Instance** ✅.
- The instance may take a few minutes ⏳ to initialize.

### 5. Connect to the PostgreSQL Instance

Once the instance is active, you can connect to it using:

- **💻 Cloud Shell**:
    1. Click on **Connect using Cloud Shell** on your instance's details page.
    2. This will open a terminal with an authenticated session that you can use to connect directly.
- **🐘 PostgreSQL Client:**
    
    You can connect to the PostgreSQL database using your favorite client (for example, pgAdmin or psql).
    
    In your PostgreSQL client, provide the following connection details:
    
    - **Host**: The server's public IP.
    - **Port**: 5432.
    - **Username**: The administrator username (e.g., `postgres`).
    - **Password**: The password you set when creating the database.
    - **Database Name**: `postgres` (*default database or any other you create afterwards*).
    
    ---
    
    ![pgadmin.gif](pgadmin.gif)
    

---

## 🎉 Conclusion

You have successfully created a PostgreSQL database on GCP and connected to it using a PostgreSQL client. Remember to regularly monitor performance and manage costs efficiently.