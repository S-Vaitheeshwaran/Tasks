def run_with_retry(llm, prompt, retries=2):
    last_error = None
    for _ in range(retries):
        try:
            return llm.generate(prompt)
        except Exception as e:
            last_error = e
    raise last_error
