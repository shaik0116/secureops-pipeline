import json
import os
import sys
from google import genai
def load_scan_results(filepath: str) -> dict:
    if not os.path.exists(filepath):
        return {"error": f"File not found: {filepath}"}
    with open(filepath, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {"error": f"Invalid JSON in {filepath}"}
def extract_findings(bandit: dict, secrets: dict, checkov: dict, trivy: dict) -> str:
    summary = []

    bandit_issues = bandit.get("results", [])
    high = [i for i in bandit_issues if i.get("issue_severity") == "HIGH"]
    medium = [i for i in bandit_issues if i.get("issue_severity") == "MEDIUM"]
    summary.append(f"SAST (Bandit): {len(bandit_issues)} issues found — {len(high)} HIGH, {len(medium)} MEDIUM")
    for issue in high[:3]:
        summary.append(f"  - {issue.get('issue_text')} in {issue.get('filename')} line {issue.get('line_number')}")

    secret_results = secrets.get("results", {})
    secret_count = sum(len(v) for v in secret_results.values()) if isinstance(secret_results, dict) else 0
    summary.append(f"Secrets Detection: {secret_count} potential secrets found")

    checkov_failed = checkov.get("summary", {}).get("failed", 0)
    checkov_passed = checkov.get("summary", {}).get("passed", 0)
    summary.append(f"IaC Scan (Checkov): {checkov_failed} checks failed, {checkov_passed} passed")

    trivy_vulns = trivy.get("Results", [])
    critical = sum(1 for r in trivy_vulns for v in r.get("Vulnerabilities", []) if v.get("Severity") == "CRITICAL")
    high_trivy = sum(1 for r in trivy_vulns for v in r.get("Vulnerabilities", []) if v.get("Severity") == "HIGH")
    summary.append(f"Container Scan (Trivy): {critical} CRITICAL, {high_trivy} HIGH vulnerabilities")

    return "\n".join(summary)
def generate_ai_summary(findings_text: str) -> str:
    api_key = os.environ.get("GEMINI_API_KEY")
    if not api_key:
        return "GEMINI_API_KEY not set — skipping AI summary"

    client = genai.Client(api_key=api_key)

    prompt = f"""You are a senior cloud security engineer writing a risk report for a non-technical manager.
Below are automated security scan results from a DevSecOps pipeline.
Write a clear, concise 3-paragraph summary:
- Paragraph 1: Overall risk level (Critical/High/Medium/Low) and why
- Paragraph 2: The 2-3 most important findings that need immediate attention
- Paragraph 3: Recommended next steps in priority order

Scan Results:
{findings_text}"""

    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=prompt
        )
        return response.text
    except Exception as e:
        return f"AI summary unavailable: {str(e)[:200]}"


if __name__ == "__main__":
    print("Loading scan results...")
    bandit = load_scan_results("bandit-results.json")
    secrets = load_scan_results("secrets-results.json")
    checkov = load_scan_results("results_json.json")
    trivy = load_scan_results("trivy-results.json")

    print("Extracting findings...")
    findings = extract_findings(bandit, secrets, checkov, trivy)
    print("\n--- RAW FINDINGS ---")
    print(findings)

    print("\n--- AI RISK SUMMARY ---")
    summary = generate_ai_summary(findings)
    print(summary)

    with open("ai-risk-summary.txt", "w") as f:
        f.write(summary)
    print("\nSummary saved to ai-risk-summary.txt")
