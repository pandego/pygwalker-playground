# Simple EDA WebUi
Just a simple EDA WebUI using PyG-Walker and Streamlit, deployed with Docker.

## Install it
- With Conda, create an environment:
  ```
  conda env create -f environment.yml
  conda activate pygwalker_ui
  ```
- Install dependencies with Poetry:
  ```
  poetry install --no-root
  ```
- Launch Streamlit App:
  ```
  streamlit run app.py
  ```
- Or simply with Docker Compose:
  ```
  docker compose up --build -d
  ```
