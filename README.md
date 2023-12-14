# Usage and Installation

## Virtual Environment
Create a virtual environment to isolate project from anothers

```bash
python -m venv venv
# Windows
source venv/Scripts/Activate
# Mac and Unix
source venv/bin/activate
```
## Install Dependencies
```bash
pip install -r requirements.txt
```

## Define huggingface api key
create a `.env` file and assign your api key to `HUGGINGFACEHUB_API_TOKEN`

```bash
HUGGINGFACEHUB_API_TOKEN=yourapitokenhere
```

## Run the App
To run the chatbot application, execute the `app.py` script. 
```
python app.py 'Your Prompt'
```
