<img src='https://huggingface.co/HuggingFaceH4/starchat-beta/resolve/main/model_logo.png' alt='StarChat Logo' width='400' />

## StarChat - Your Local Coding Assistant 🌟

This project harnesses the power of the StarChat Beta text generation model to serve as a helpful coding assistant. StarChat Beta is an advanced AI model designed to assist with coding tasks. To learn more about StarChat Beta, visit [HuggingFace's StarChat Beta](https://huggingface.co/HuggingFaceH4/starchat-beta).

### Why Longchain Instead of Pipeline?

Unlike traditional approaches that involve downloading and using specific models, this project leverages a Longchain architecture. It seamlessly accesses Hugging Face's free models for text generation without the need for downloading any models to your computer. This allows for efficient and hassle-free text generation with the assistance of StarChat Beta.

Get started with your coding assistant and enjoy productive coding sessions! ✨


# Usage and Installation

## Virtual Environment
To isolate the project from other Python installations, create a virtual environment using the following commands:

```bash
python -m venv venv
# Windows
source venv/Scripts/Activate
# Mac and Unix
source venv/bin/activate
```
## Install Dependencies
Install the required dependencies from requirements.txt by running the following command:

```bash
pip install -r requirements.txt
```

## Define huggingface api key
Create a `.env` file in the project directory and assign your Hugging Face API token to the variable HUGGINGFACEHUB_API_TOKEN like this:


```bash
HUGGINGFACEHUB_API_TOKEN=yourapitokenhere
```

## Run the App
To start the chatbot application, execute the app.py script with your desired prompt:

```bash
python app.py 'Your Prompt'
```
