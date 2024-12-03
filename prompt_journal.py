class PromptJournal:
    def __init__(self):
        self.prompts = [""]
        self.prompt_number = 1

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "prompts": ("STRING", {"multiline": True, "default": ""}),
                "prompt_number": ("INT", {"default": 1, "min": 1, "max": 4096, "step": 1}),
            },
        }

    RETURN_TYPES = ("STRING", "STRING")
    FUNCTION = "process"
    CATEGORY = "Text"

    def process(self, prompts, prompt_number):
        self.prompts = prompts.split('\n')
        self.prompt_number = prompt_number

        # Filter out empty rows for prompt selection
        non_empty_prompts = [prompt for prompt in self.prompts if prompt.strip()]

        # Wrap around the prompt_number if it's too high
        effective_prompt_number = (self.prompt_number - 1) % len(non_empty_prompts)

        # Get the selected prompt
        prompt = non_empty_prompts[effective_prompt_number]

        # Join all prompts back into a single string, keeping empty rows
        all_prompts = '\n'.join(self.prompts)

        return (prompt, all_prompts)

# A dictionary that contains all nodes you want to export with their names
NODE_CLASS_MAPPINGS = {
    "PromptJournal": PromptJournal
}

# A dictionary that contains the friendly/humanly readable titles for the nodes
NODE_DISPLAY_NAME_MAPPINGS = {
    "PromptJournal": "Prompt Journal"
}
