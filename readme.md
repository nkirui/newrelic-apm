# FastAPI & New Relic APM Simulation

This project simulates New Relic Application Performance Monitoring (APM) for a FastAPI application hosted on Render. It includes a FastAPI codebase that generates and logs data to New Relic, as well as an endpoint (`/upload_video`) to simulate a long-awaiting process.

## Objectives

- **Generate Logs**: Logs are generated based on endpoints and monitored on New Relic.
- **Monitoring Long Processes**: Ability to check and filter endpoints/tasks that take a long time to process.

## Application Stack

- **FastAPI**: A modern, fast (high-performance) web framework for building APIs with Python 3.11
- **Hosting**: The application is hosted on Render.

## Requirements

- **Generate and Log to New Relic**: The FastAPI codebase is designed to generate logs and send them to New Relic for monitoring.
- **Upload Video Endpoint**: An endpoint named `/upload_video` is implemented to simulate a long-awaiting process (e.g., 1.5 seconds).
- **GitHub Repository**: The codebase is uploaded to GitHub for version control and deployment purposes.
- **Render Configuration**: Render is configured to deploy the application based on the GitHub repository.

## Assumptions

This project focuses on functionality and does not implement security measures.

## Setup and Usage

1. **Repository**: You can Clone this repository to your local machine.git clone git@github.com:nkirui/newrelic-apm.git
2. **Configuration** : Update the New Relic API credentials in the codebase **newrelic.ini file**. Note: Exercise caution with sensitive information.
3. **Production Endpoint** : **https://fastapi-newrelic-apm.onrender.com/upload_video**
4. **Deployment** : Configure Render to deploy the application based on the GitHub repository. Ensure Render settings are appropriately configured for environment variables and secrets.
5. **Monitoring** : Monitor the application's performance on New Relic, analyzing logs and identifying long-running processes.
