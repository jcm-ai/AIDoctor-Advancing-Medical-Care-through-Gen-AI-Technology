# AIDoctor: Advancing Medical Care through Gen AI Technology

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

### Techstack Used:
- Python
- Pinecone
- LangChain
- Meta Llama2
- Flask

