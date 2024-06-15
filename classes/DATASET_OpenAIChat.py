from openai import OpenAI
import os

class DATASET_OpenAIChat:

    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "model": (["gpt-4", "gpt-4-32k", "gpt-3.5-turbo", "gpt-4-0125-preview", "gpt-4-turbo-preview", "gpt-4-1106-preview", "gpt-4-0613"], {"default": "gpt-3.5-turbo"}),
                "api_url": ("STRING", {"multiline": False, "default": "https://api.openai.com/v1"}),
                "api_key": ("STRING", {"multiline": False}),
                "prompt": ("STRING", {"multiline": True, "default": ""}),
                "token_length": ("INT", {"default": 1024})
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "generate"
    CATEGORY = "🔶DATASET🔶"

    def generate(self, model, api_url, api_key, prompt, token_length):
        try:
            ai = OpenAI(api_key=api_key, base_url=api_url)
            if not api_key:
                return "OpenAI API key is required."
            request = [{"role": "system","content": "You are GPT-4"},{"role": "user","content": prompt}]
            response = ai.chat.completions.create(model=model,messages=request,max_tokens=token_length)
            answer = response.choices[0].message.content
            return (answer,)
        except Exception as e:
            return (f"Error: {str(e)}",)
    
    @classmethod
    def IS_CHANGED(s, model, api_url, api_key, prompt, token_length):       
       return os.urandom(16).hex()

N_CLASS_MAPPINGS = {
    "DATASET_OpenAIChat": DATASET_OpenAIChat,
}

N_DISPLAY_NAME_MAPPINGS = {
    "DATASET_OpenAIChat": "DATASET_OpenAIChat",
}