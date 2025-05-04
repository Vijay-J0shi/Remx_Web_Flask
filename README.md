### Remx_Web_Flask
https://remx-web-flask.onrender.com
</br>
Thid is the  RemxWebsite developed using Flask and my model Api ,Please check out</br>
</br>
<img src="https://github.com/user-attachments/assets/36ec0b12-2477-4799-9d8a-b67d39a26648" alt="image" width="700"/>

### Introduction
The Remx Web Flask application is a user-friendly web interface designed to visualize and interact with the Remx API, a tool developed for Wildlife India to automate animal detection and measurement in images captured by motion-sensing cameras. Hosted at [https://remx-web-flask.onrender.com](https://remx-web-flask.onrender.com), this Flask-based application enables authenticated users to upload images or ZIP files, view predicted animal bounding box coordinates, download results as CSV files, and access historical data. Integrated with the Remx API (deployed on an AWS EC2 instance), the application serves as a front-end component of the Animeter software, facilitating wildlife conservation efforts by providing an intuitive platform for researchers and conservationists.

This document provides a comprehensive overview of the application's purpose, functionality, architecture, and file structure, detailing how each component contributes to the system's operation and its connection to the Remx API.

### Purpose
The Remx Web Flask application aims to make the Remx API accessible and practical for end-users, particularly wildlife researchers and conservationists. Its key objectives are:
- **User Interaction**: Provide a web interface for uploading images or ZIP files containing wildlife images and visualizing the predicted bounding box coordinates.
- **Data Management**: Store and display historical prediction data for each user, enabling tracking and analysis of processed images.
- **Result Accessibility**: Allow users to download prediction results in CSV format for further analysis.
- **Integration**: Seamlessly connect with the Remx API to process uploaded images and retrieve bounding box predictions.
- **Security**: Implement user authentication to ensure secure access to data and functionalities.
