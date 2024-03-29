# UVA Basketball Dashboard
This dashabord was created by Max Ryoo, Cepehr Alizadeh, and Seth Galluzzi under the supervision of Jonathan Kropko and Natalie Kupperman.

These repo has two main aspects.
1. Jupyter Lab Workspace
    - After following the steps (listed below), you will have access to see a jupyter lab workspace.

2. Plotly Dash Dashbord
    - After following the steps (lsited below), you will be given a dashboard to explore the data.

**Note:** Any changes done while working in the jupyter lab workspace will directly affect the dashboard. We advise that you create new files/notebooks to do additional analysis.

Please follow the instructions below to view the dashabord.

## Requirments

- Docker
    - If you do not have docker please install it [here](https://www.docker.com/).

- Data 
    - The data that is required for this dashboard to run is the folder of `Athleticism` and `ClinicianReport`.

## Steps
1. Clone the repo using the following command
    - `git clone https://github.com/UVA-Basketball-Analysts/basketballdashboard.git`
2. In your terminal (CLI) please navigate inside the repository
    - `cd basketballdashboard`
3. Make a folder within the repo called `data`
4. Move the required data (`Athleticism` and `ClinicianReport`) folders into the data folder that you have created in step 3
5. Run the following command to make a docker image for the jupyter lab.
    - `docker build -t bballimage .`
6. Run the following command to make a docker image for the dashboard.
    - `docker build -f DockerfileDashboard -t bballdashboard .`
7. Run the docker compose up command to bring up the two images.
    - `docker compose up`
8. To reach the dashboard please navigate to `http://localhost:8050`
    - **Note** Because we are proceessing the data during the first load, this may take some time. Pleae look out for a message in your CLI that looks like the following. 
    
```
dashboard_1  | Dash is running on http://0.0.0.0:8050/
dashboard_1  | 
dashboard_1  |  * Serving Flask app 'app'
dashboard_1  |  * Debug mode: on
```
8. To reach the jupyter lab workspace please wait for a message in the CLI and navigate towards the workspace.
    - The token generated by jupyterlab was replace by {{someSecretToken}}. Please copy and paste your server address directly instead of the {{someSecretToken}}.
    - **note** Please change the web url to http://127.0.0.1:888**9** instead of http://127.0.0.1:8888
```
jupyter_1    |     
jupyter_1    |     To access the server, open this file in a browser:
jupyter_1    |         file:///root/.local/share/jupyter/runtime/jpserver-1-open.html
jupyter_1    |     Or copy and paste one of these URLs:
jupyter_1    |         http://f22015ee9982:8888/lab?token={{someSecretToken}}
jupyter_1    |         http://127.0.0.1:8888/lab?token={{someSecretToken}}
```

## Troubleshoot steps
- If the dashboard is not loading or says there is an error, make sure that the directory that you are running this in has the folder called `data` with the two folders included in the data folder/

- If the command `docker compose up` is not working and you think you might have a previous version of docker installed try running `docker-compose-v1 up`
    - If this still continues to fail, please check the docker forum with your error.