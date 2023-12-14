from langchain import llms, prompts, chains
from dotenv import load_dotenv
# Internal usage
import os
HuggingFaceHub = llms.HuggingFaceHub

class StartChat:
    def __init__(self, model_identifier, max_length):
        load_dotenv()
        self.access_token = os.environ["HUGGINGFACEHUB_API_TOKEN"]
        if not self.access_token:
            raise ValueError("HuggingFace API token not found in environment variables.")
        os.environ["HUGGINGFACEHUB_API_TOKEN"] = self.access_token

        self.max_length = max_length

        self.llm = HuggingFaceHub(repo_id=model_identifier , 
                         model_kwargs={"min_length":30,
                                       "max_new_tokens":max_length, "do_sample":True, 
                                       "temperature":0.2, "top_k":50, 
                                       "top_p":0.95, "eos_token_id":49155})
        
    def generate_reply(self, prompt_text, template):
        # Set up the prompt template
        prompt_template = prompts.PromptTemplate(template=template, 
                                                 input_variables=["prompt_text"])

        # Create a chain for processing the language model output
        llm_chain = chains.LLMChain(prompt=prompt_template, llm=self.llm)

        # Generate the reply
        llm_reply = llm_chain.run(prompt_text)
        reply = llm_reply.partition('-')[0]
        return reply