import sys
from chat import StartChat 


def main():
    if len(sys.argv) < 2:
        raise ValueError("Usage: python -m app '[Your prompt Here]'")
    
    prompt = sys.argv[1]

    repo="HuggingFaceH4/starchat-beta"
    template = "\n\n\n{query}\n"
    starchat = StartChat(repo, 150)    

    res = starchat.generate_reply(prompt, template)
    print(prompt)
    print("---")
    print(res)

if __name__ == "__main__":
    main()