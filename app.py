import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from crewai import Agent, Task, Crew, Process, LLM
from pydantic import BaseModel
from typing import List
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")


# 1. Define the Output Format for the UI
class PhishingReport(BaseModel):
    riskLevel: str
    riskClass: str # 'high', 'medium', or 'low'
    riskScore: int
    isPhishing: bool
    factors: List[str]
    recommendations: List[str]

app = Flask(__name__)
CORS(app) # Allows your HTML file to talk to this API



@app.route('/api/analyze-email', methods=['POST'])
def analyze_email():
    data = request.json
    email_text = data.get('emailContent', '')

    if not email_text:
        return jsonify({"error": "No content provided"}), 400
    
    llm = LLM(
        model="gemini/gemini-2.5-flash",
        api_key=os.getenv("GEMINI_API_KEY")
    )

    # 2. Define Agents
    analyst = Agent(
        role='Senior Cybersecurity Analyst',
        goal='Analyze email text for phishing indicators like urgency, suspicious links, and sender spoofing.',
        backstory='Expert in digital forensics and social engineering patterns.',
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    reporter = Agent(
        role='Security Risk Reporter',
        goal='Synthesize analysis into a structured risk report.',
        backstory='Specializes in clear security communication and risk assessment.',
        allow_delegation=False,
        verbose=True,
        llm=llm
    )

    # 3. Define Tasks
    analysis_task = Task(
        description=f"Analyze this email for phishing threats: {email_text}",
        expected_output="A detailed list of suspicious elements and a risk assessment.",
        agent=analyst
    )

    reporting_task = Task(
        description="Generate a structured JSON report based on the analysis.",
        expected_output="A JSON object following the PhishingReport schema.",
        output_json=PhishingReport, # This forces the AI to match your UI's structure
        agent=reporter,
        context=[analysis_task]
    )

    # 4. Run the Crew
    crew = Crew(
        agents=[analyst, reporter],
        tasks=[analysis_task, reporting_task],
        process=Process.sequential
    )

    result = crew.kickoff()
    
    # Return the structured JSON to the frontend
    return jsonify(result.to_dict())

if __name__ == '__main__':
    app.run(port=5000, debug=True)