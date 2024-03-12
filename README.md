# Flask App Deployment on Google Kubernetes Engine (GKE)

This repository contains code and configurations for deploying a simple Flask application on Google Kubernetes Engine (GKE) using Google Cloud Build. The Flask application serves a "Hello, World!" message.

## Contents

- `app.py`: Python file containing the Flask application.
- `cloudbuild.yaml`: Cloud Build configuration file for building and deploying the Docker container to GKE.
- `Dockerfile`: Dockerfile for building the Docker image of the Flask application.
- `gke.yaml`: Kubernetes deployment and service configuration file for deploying the Flask application on GKE.
- `requirements.txt`: Python dependencies required by the Flask application.

## Instructions

1. **Clone Repository:**
   Clone this repository to your local machine.

   ```bash
   git clone https://github.com/ahmetaslan13/gcp-devops.git
   cd gcp-devops
   ```
2. **Set Up Google Cloud Project:**
   Ensure you have a Google Cloud Platform (GCP) project set up with billing enabled and the necessary APIs enabled (such as Kubernetes Engine API).

3. **Configure Cloud Build Trigger:**
   Set up a Cloud Build trigger to automatically build and deploy the application whenever changes are pushed to the repository. You can use the `cloudbuild.yaml` file as the build configuration.

4. **Update GKE Configuration:**
   Modify the `gke.yaml` file according to your GKE cluster configuration. Ensure the `image` field under `containers` points to your Docker image repository.

5. **Build and Deploy Application:**
   Once the Cloud Build trigger is set up, any changes pushed to the repository will trigger a build and deployment process to GKE.

6. **Access the Application:**
   Once deployed, you can access the Flask application by navigating to the external IP address of the GKE service.

## Additional Notes

- Make sure to replace `<repository_url>` and `<repository_name>` with the appropriate values.
- Ensure that you have the necessary permissions to create and manage resources in your GCP project.
- This setup assumes basic familiarity with Google Cloud Platform services and Kubernetes concepts.

For more detailed instructions, please refer to the official [Google Cloud Platform documentation](https://cloud.google.com/docs).

Feel free to reach out with any questions or issues you encounter during the setup process. Happy coding!
