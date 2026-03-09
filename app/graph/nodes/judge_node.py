import json
from app.core.provider_factory import get_provider


def build_judge_prompt(task, outputs):

    prompt = f"""
You are an expert software engineer evaluating multiple AI-generated solutions.

USER TASK:
{task}

MODEL RESPONSES:
"""

    for model, output in outputs.items():
        prompt += f"""

MODEL: {model}

{output}

"""

    prompt += """
Evaluate the solutions.

Possible actions:

1. recommend
   - One solution is clearly best

2. refine
   - Best solution exists but needs improvement

3. regenerate
   - All solutions are weak or incorrect

Return JSON ONLY in this format:

{
 "action": "recommend | refine | regenerate",
 "winner": "model_name",
 "reasoning": "why this answer is better",
 "refined_answer": "improved answer if refine",
 "improved_prompt": "better prompt if regenerate"
}
"""

    return prompt


async def judge_node(state: dict):

    judge_model = state["judge_model"]
    task = state["refined_prompt"]
    outputs = state["outputs"]

    provider = get_provider(judge_model)

    judge_prompt = build_judge_prompt(task, outputs)

    buffer = ""

    async for token in provider.stream_generate(judge_prompt):

        buffer += token

        yield {
            "type": "judge_stream",
            "token": token
        }

    try:
        parsed = json.loads(buffer)

        action = parsed.get("action")
        winner = parsed.get("winner")
        reasoning = parsed.get("reasoning")
        refined = parsed.get("refined_answer")
        improved_prompt = parsed.get("improved_prompt")

    except Exception:

        action = "recommend"
        winner = list(outputs.keys())[0]
        reasoning = "Fallback due to parsing failure"
        refined = outputs[winner]
        improved_prompt = None

    yield {
        "type": "judge_complete",
        "action": action,
        "winner": winner
    }

    yield{
        "judge_action": action,
        "winner": winner,
        "judge_reason": reasoning,
        "final_answer": refined,
        "regen_prompt": improved_prompt
    }