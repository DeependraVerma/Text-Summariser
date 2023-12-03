# End-to-end Text Summarization NLP Project

Welcome to the End-to-end Text Summarization NLP project! This project provides a complete solution for text summarization using natural language processing (NLP). The workflow includes updating configurations, managing entities, and deploying the application on AWS with GitHub Actions.

## Workflows

1. **Update Configuration Files:**
   - `config.yaml`: Update the configuration file.
   - `params.yaml`: Update parameters.
   - `entity`: Update entity information.
   - `src/config`: Update the configuration manager.

2. **Update Components:**
   - Update the components in the pipeline.
   - Update `main.py` and `app.py` as needed.

## How to Run

Follow these steps to set up and run the project:

### Step 1: Clone the Repository

```bash
git clone https://github.com/DeependraVerma/Text-Summariser-Project.git
```

### Step 2: Create and Activate Conda Environment

```bash
conda create -n summary python=3.8 -y
conda activate summary
```

### Step 3: Install Requirements

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
python app.py
```

Access the application by opening your local host and port.

## Author

- **Deependra Verma**
  - Data Scientist
  - Email: deependra.verma00@gmail.com

## AWS CI/CD Deployment with GitHub Actions

1. **Login to AWS console.**
2. **Create IAM user for deployment:**
   - EC2 Access: Virtual machine.
   - ECR: Elastic Container Registry to store your Docker image in AWS.

### Description: About the Deployment

1. Build Docker image of the source code.
2. Push your Docker image to ECR.
3. Launch your EC2 instance.
4. Pull your image from ECR on EC2.
5. Launch your Docker image on EC2.

### Policy

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

### Steps:

1. Create ECR repo to store Docker image.
   - Save the URI: `774517090665.dkr.ecr.eu-north-1.amazonaws.com/text_summarizer_deependra`
2. Create EC2 machine (Ubuntu).
3. Install Docker on EC2 (Optional steps included).
4. Configure EC2 as a self-hosted runner.

### GitHub Secrets

- `AWS_ACCESS_KEY_ID=`
- `AWS_SECRET_ACCESS_KEY=`
- `AWS_REGION=us-east-1`
- `AWS_ECR_LOGIN_URI=demo>>566373416292.dkr.ecr.ap-south-1.amazonaws.com`
- `ECR_REPOSITORY_NAME=simple-app`
