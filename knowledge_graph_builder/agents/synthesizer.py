from tools.research_api_tool import EURI_CLIENT

def run_synthesizer(raw_data: dict):
    def stringify(value):
        if isinstance(value, list):
            return "\n".join([str(v) for v in value])
        return str(value)

    combined_text = "\n".join([stringify(v) for v in raw_data.values()])
    prompt = f"""
You are an expert career roadmap planner and  education advisor.

When users ask about  courses or preparation strategies for a specific career path, you will provide a detailed roadmap.
The roadmap should be tailored to the user's current knowledge level and the specific career they are interested in.
The roadmap should be comprehensive, covering all necessary skills, tools, and concepts.
The roadmap should be structured in a way that is easy to follow, with clear milestones and timelines.
The roadmap should be designed for someone who is serious about their career and is willing to commit time and effort to learning.
Break down the roadmap into clear phases:

- Phase (e.g. Fundamentals, Specialization)
- Subtopics (e.g. Python, SQL, ML algorithms)
- Recommended Tools/Concepts
- Estimated Time to Complete (in weeks or days)

Output Format (Strict):
Phase -> Subtopic -> Tool or Detail (Time Estimate)
Use arrows only. No colons or lists.

Example:
"Fundamentals -> Python -> Python Basics (2 weeks)
Fundamentals -> SQL -> SQL Basics (2 weeks)
Fundamentals -> ML Algorithms -> Linear Regression (1 week)

Encourage commitment and clarity with timelines.
Ensure 12-20 roadmap paths.

Context:
{combined_text}
"""

    response = EURI_CLIENT.generate_completion(prompt=prompt)
    try:
        return response["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError):
        return str(response)