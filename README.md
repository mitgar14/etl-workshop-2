# Workshop #2: Data Engineer <img src="https://cdn-icons-png.flaticon.com/512/8618/8618924.png" alt="Data Icon" width="30px"/>

Realized by **Martín García** ([@mitgar14](https://github.com/mitgar14)).

## Overview ✨
> [!NOTE]
> It's important to note that the raw Grammys dataset must be stored in a database in order to be read correctly.

In this workshop we will use two datasets (*spotify_dataset* and *the_grammys_awards*) that will be processed through Apache Airflow applying data cleaning, transformation and loading and storage including a merge of both datasets. The result will culminate in visualizations on a dashboard that will give us important conclusions about this dataset.

The tools used are:

* Python 3.10 ➜ [Download site](https://www.python.org/downloads/)
* Jupyter Notebook ➜ [VS Code tool for using notebooks](https://youtu.be/ZYat1is07VI?si=BMHUgk7XrJQksTkt)
* PostgreSQL ➜ [Download site](https://www.postgresql.org/download/)
* Power BI (Desktop version) ➜ [Download site](https://www.microsoft.com/es-es/power-platform/products/power-bi/desktop)

> [!WARNING]
> Apache Airflow only runs correctly in Linux environments. If you have Windows, we recommend using a virtual machine or WSL.

The dependencies needed for Python are

* Apache Airflow
* Dotenv
* Pandas
* Matplotlib
* Seaborn
* SQLAlchemy
* PyDrive2

These dependencies are included in the `requirements.txt` file of the Python project. The step-by-step installation will be described later.

## Dataset Information <img src="https://github.com/user-attachments/assets/5fa5298c-e359-4ef1-976d-b6132e8bda9a" alt="Dataset" width="30px"/>


The datasets used (*spotify_dataset* and *the_grammy_awards*) are crucial for analyzing music trends, comparing track features, and understanding the relation between track characteristics and award recognition.

Here’s an overview of the two datasets that were provided:

### 1. **Spotify Dataset** (`spotify_dataset.csv`) <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/7/71/Spotify.png/1200px-Spotify.png" alt="Spotify" width="22px"/>

This dataset contains a wide variety of information about songs available on Spotify. Each row represents a single track with multiple attributes describing both the track's metadata and musical characteristics. The most important columns are:

- **Unnamed: 0**: Acts as an index for the dataset.
- **track_id**: A unique identifier for each track on Spotify.
- **artists**: Name(s) of the artist(s) associated with the track.
- **album_name**: The name of the album the track is from.
- **track_name**: The title of the track.
- **popularity**: A score between 0 and 100 indicating the popularity of the track on Spotify, where higher values mean more popularity.
- **duration_ms**: The duration of the track in milliseconds.
- **danceability**: A measure of how suitable a track is for dancing, where higher values indicate better danceability.
- **energy**: A measure of intensity and activity in the track.
- **key**: The musical key of the track (0 = C, 1 = C#, etc.).
- **loudness**: The overall loudness of the track in decibels.
- **mode**: Whether the track is in a major (1) or minor (0) mode.
- **explicit**: Indicates if the track contains explicit content (True/False).
- **tempo**: The speed of the track measured in beats per minute (BPM).
- **valence**: A measure of the musical positiveness of the track.
- **time_signature**: An estimated overall time signature of a track.
- **track_genre**: The genre associated with the track.

### 2. **Grammy Awards Dataset** (`the_grammy_awards.csv`) <img src="https://www.pngall.com/wp-content/uploads/9/Grammy-Awards-PNG-Download-Image.png" alt="Grammys" width="22px"/>

This dataset contains information about Grammy Awards, with each row representing a nomination for a particular award. Key columns include:

- **year**: The year the Grammy Awards took place.
- **title**: The name of the Grammy event.
- **published_at**: The date when the Grammy event details were published.
- **category**: The category of the Grammy award (e.g., Record Of The Year, Best Pop Solo Performance).
- **nominee**: The name of the nominated song or album.
- **artist**: The artist(s) associated with the nominated song or album.
- **workers**: Contributors (such as producers, engineers) involved in the nominated work.
- **img**: URL linking to the image of the Grammy event or nominee.
- **winner**: A boolean indicating whether the nominee won the award (True/False).


## Generate your Google Drive Auth file (`client_secrets.json`) 🔑

To learn how to generate a `client_secrets.json` file, you can follow [the following guide](https://github.com/mitgar14/etl-workshop-2/blob/main/docs/guides/drive_api.md). This guide explains step by step how to generate the authentication key to use the Google Drive API via PyDrive 2 in your *Store* script.

In case you receive an **error 400 - redirect_uri_mismatch**, you can follow the [next page](https://elcuaderno.notion.site/Solucionado-Acceso-bloqueado-La-solicitud-de-esta-app-no-es-v-lida-Google-Drive-API-106a9368866a8037b597ecdec3346405?pvs=4).

## Configure PyDrive2 (`settings.yaml`) 📄

To properly configure this project and ensure it works as expected, please follow the detailed instructions provided in the **PyDrive2 configuration guide**. This guide walks you through setting up the necessary variables, OAuth credentials, and project settings for Google Drive API integration using PyDrive2. 

You will configure your `settings.yaml` file for authentication and authorization. You can find the step-by-step guide [here](https://github.com/mitgar14/etl-workshop-2/blob/develop/docs/guides/drive_settings.md).

## Run the project <img src="https://github.com/user-attachments/assets/99bffef1-2692-4cb8-ba13-d6c8c987c6dd" alt="Running code" width="30px"/>


### Clone the repository

Execute the following command to clone the repository:

```bash
  git clone https://github.com/mitgar14/etl-workshop-2.git
```

#### Demonstration of the process

![Git Clone](https://github.com/user-attachments/assets/0885fcdd-d4d8-4774-98bc-ac34914d9a94)


### Enviromental variables

> [!IMPORTANT]
> Remember that you must use the absolute routes to the path.

For this project we use some environment variables that will be stored in one file named ***.env***, this is how we will create this file:

1. We create a directory named ***env*** inside our cloned repository.

2. There we create a file called ***.env***.

3. In that file we declare 6 enviromental variables. Remember that some variables in this case go without double quotes, i.e. the string notation (`"`). Only the absolute routes go with these notation:
  ```python
  # PostgreSQL Variables
  
  # PG_HOST: Specifies the hostname or IP address of the PostgreSQL server.
  PG_HOST = # db-server.example.com
  
  # PG_PORT: Defines the port used to connect to the PostgreSQL database.
  PG_PORT = # 5432 (default PostgreSQL port)
  
  # PG_USER: The username for authenticating with the PostgreSQL database.
  PG_USER = # your-postgresql-username
  
  # PG_PASSWORD: The password for authenticating with the PostgreSQL database.
  PG_PASSWORD = # your-postgresql-password
  
  # PG_DATABASE: The name of the PostgreSQL database to connect to.
  PG_DATABASE = # your-database-name
  
  # Google Drive Variables
  
  # CLIENT_SECRETS_PATH: Path to the client secrets file used for Google Drive authentication.
  CLIENT_SECRETS_PATH = "/path/to/your/credentials/client_secrets.json"
  
  # SETTINGS_PATH: Path to the settings file for the application configuration.
  SETTINGS_PATH = "/path/to/your/env/settings.yaml"
  
  # SAVED_CREDENTIALS_PATH: Path to the file where Google Drive saved credentials are stored.
  SAVED_CREDENTIALS_PATH = "/path/to/your/credentials/saved_credentials.json"

  # FOLDER_ID: The ID of your Google Drive folder. You can get it from the link in your folder.
  FOLDER_ID = # your-drive-folder-id
  ```

#### Demonstration of the process

![Env Variables](https://github.com/user-attachments/assets/9e756e5e-db1a-4953-8d7c-1fa0a92d0500)


### Installing the dependencies with *Poetry*

> To install Poetry follow [this link](https://elcuaderno.notion.site/Poetry-8f7b23a0f9f340318bbba4ef36023d60?pvs=4).


1. Enter the Poetry shell with `poetry shell`.

2. Once the virtual environment is created, execute `poetry install` to install the dependencies. In some case of error with the *.lock* file, just execute `poetry lock` to fix it.

3. Now you can execute the notebooks!

#### Demonstration of the process

![Poetry](https://github.com/user-attachments/assets/3e683921-df9d-4e85-bb3f-c3761a8e3c73)


### Running the notebooks

We execute the 3 notebooks following the next order. You can run it just pressing the "Execute All" button:

   1. *001_rawDataLoad.ipynb*
   2. *002_candidatesEDA.ipynb*
   3. *003_cleanDataLoad.ipynb*

![image](https://github.com/user-attachments/assets/7599de5a-3330-4d1d-ac08-ced17639c320)
  
Remember to choose **the right Python kernel** at the time of running the notebook and **install the *ipykernel*** to support Jupyter notebooks in VS Code.


## Thank you! 💕🐍

Thanks for visiting my project. Any suggestion or contribution is always welcome 👄.
