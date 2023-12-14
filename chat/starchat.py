from langchain import llms
# Internal usage
import os
HuggingFaceHub = llms.HuggingFaceHub
# Set HF API token  and HF repo
yourHFtoken = "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" #here your HF token

### INITIALIZING STARCHAT FUNCTION MODEL
def starchat(model,myprompt, your_template):
    from langchain import prompts, chains
    os.environ["HUGGINGFACEHUB_API_TOKEN"] = yourHFtoken
    llm = HuggingFaceHub(repo_id=model , 
                         model_kwargs={"min_length":30,
                                       "max_new_tokens":256, "do_sample":True, 
                                       "temperature":0.2, "top_k":50, 
                                       "top_p":0.95, "eos_token_id":49155})
    template = your_template
    prompt = prompts.PromptTemplate(template=template, input_variables=["myprompt"])
    llm_chain = chains.LLMChain(prompt=prompt, llm=llm)
    llm_reply = llm_chain.run(myprompt)
    reply = llm_reply.partition('<|end|>')[0]
    return reply