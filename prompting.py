ALPACA_FORMAT = """
### Instruction:
{}

### Input:
{}

### Response:
""".strip()

def get_alpaca_prompt(system_prompt: str, message: str) -> str:
    return ALPACA_FORMAT.format(system_prompt, message)

LLAMA_INSTRUCT_FORMAT = """
[INST] <<SYS>>
{}
<</SYS>>

{} [/INST]
""".strip()

def get_llama_prompt(system_prompt: str, message: str) -> str:
    return LLAMA_INSTRUCT_FORMAT.format(system_prompt, message)