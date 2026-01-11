from app.llm.prompts import DOCUMENT_QA_PROMPT
from app.llm.agent import run_with_retry
from app.logging.logger import log_experiment

def run_document_qa(experiment, question, llm):
    prompt = DOCUMENT_QA_PROMPT.format(
        document=experiment["document_text"],
        question=question
    )

    output = run_with_retry(llm, prompt)

    log_experiment({
        "experiment_id": experiment["id"],
        "prompt": prompt,
        "input": question,
        "output": output,
        "status": "completed"
    })

    return output
