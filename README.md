# AIDoctor: Advancing Medical Care through Gen AI Technology

**Final outcome of this project:**

![AIDoctor](https://github.com/user-attachments/assets/876f6fd3-d526-4874-a344-6ce3f3e919d4)



### How to run?

**STEPS:**
*Clone Project Repository:*
```Bash
https://github.com/jcm-ai/AIDoctor-Advancing-Medical-Care-through-Gen-AI-Technology.git
```

**STEP 01- Create a `conda environment` after opening the repository**
```Bash
conda create --name AIDoctor python=3.8 -y
```
*Incase if you get error (for example: CondaError: Run 'conda init' before 'conda activate') when activate environment, use below command:*
```Bash
source activate base
```
*Then, Activate an environment:*
```Bash
conda activate AIDoctor
```
*Deactivate the current environment:*
```Bash
conda deactivate
```
**Optional:**
*List all environments:*
```Bash
conda env list
```
*Remove an environment:*
```Bash
conda env remove -n "environment name"
```

**STEP 02- Install the required packages**
*Install the required packages using pip or conda. For example, to install the required packages using pip , run the following command:*
```Bash
pip install -r requirements.txt
```
**Git commands:**
```Bash
git add .
```
```Bash
git commit -m "Your commit message"
```
```Bash
git push origin main
```
**Create a `.env` file in the root directory and add our Pinecone credentials as follows:**
```Bash
PINECONE_API_KEY = "***********************************"
```

**Download the quantized Llama2 model from the `Hugging Face` link provided in the model folder and place it in the model directory:**
*Download the Llama 2 Model:*
```Bash
llama-2-7b-chat.ggmlv3.q4_0.bin
```
*From the following link:*
```Bash
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

![huggingface1](https://github.com/user-attachments/assets/7a7924d0-d792-4aea-89cf-e38d32f6e447)


*Or direct download from this link:*
```Bash
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/blob/main/llama-2-7b-chat.ggmlv3.q4_0.bin
```

![huggingface2](https://github.com/user-attachments/assets/bbe60d2e-c2ed-4c07-b437-27c82b7f2da9)


*Run the following command to execute `Pinecone vector database`:*
```Bash
python store_index.py
```

*Finally run the following command:*
```Bash
python app.py
```
*Now, open up:*
```Bash
localhost:8080
```

### Techstack Used:
- Python
- Pinecone
- LangChain
- Meta Llama2
- Flask

## Automating Amazon Web Services(AWS) CI/CD Deployments through GitHub Actions

#### 1. Login to AWS Console.
#### 2. Create a new Identity and Access Management (IAM) user with programmatic access.

**Policy:**

1. AmazonEC2ContainerRegistryFullAccess
2. AmazonEC2FullAccess

*with specific access:*
1. EC2 access : It is virtual machine
2. ECR: Elastic Container Registry to save our Docker Image in AWS

**Description: About the deployment**

1. Build docker image of the source code
2. Push the docker image to ECR (Elastic Container Registry)
3. Create a new EC2 instance
4. Run the docker image on the EC2 instance
5. Deploy the docker image on the EC2 instance

#### 3. Create ECR repo to store/save docker image.
```Bash
URI: 954976285001.dkr.ecr.ap-south-1.amazonaws.com/ai-doctor
```
#### 4. Create EC2 machine (Ubuntu)
#### 5. Open EC2 and Install Docker in EC2 Machine:
*optinal:*
```Bash
sudo apt-get update -y
```
```Bash
sudo apt-get upgrade
```
**Required:**

```Bash
curl -fsSL https://get.docker.com -o get-docker.sh
```
```Bash
sudo sh get-docker.sh
```
```Bash
sudo usermod -aG docker ubuntu
```
```Bash
newgrp docker
```
#### 6. Configure EC2 as self-hosted runner:
```Bash
Settings>Actions>Runners>New self-hosted runner> choose os> then run command one by one
```
#### 7. Setup GitHub secrets:
```Bash
Settings>Secrets and variables>Actions>New repository secret
```

```Bash
AWS_ACCESS_KEY_ID = ***********************************

AWS_SECRET_ACCESS_KEY = ***********************************

AWS_REGION = ap-south-1

AWS_ECR_LOGIN_URI = ai-doctor
```