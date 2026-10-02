import requests


class KoviClient:
    def __init__(self, api_key: str, base_url: str = "https://kovi-backend-398838744187.asia-south1.run.app"):
        """
        Initialize the Kovi API Client.
        :param api_key: Your enterprise branch API key.
        :param base_url: The production base URL of your Kovi backend.
        """
        self.api_key = api_key
        self.base_url = base_url.rstrip("/")
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

    def schedule_interview(
            self,
            job_id: str,
            candidate_name: str,
            candidate_email: str,
            role: str,
            interview_type: str,
            evaluation_level: str,
            tech_stack: list,
            duration: int,
            pass_score: float,
            mobile_number: str = "",
            deadline_hours: int = 72
    ) -> dict:
        """
        Programmatically schedule an AI interview and trigger the invitation email.
        """
        endpoint = f"{self.base_url}/api/v1/schedule"

        payload = {
            "jobId": job_id,
            "candidateName": candidate_name,
            "candidateEmail": candidate_email,
            "mobileNumber": mobile_number,
            "role": role,
            "interviewType": interview_type,
            "evaluationLevel": evaluation_level,
            "techStack": tech_stack,
            "duration": duration,
            "passScore": pass_score,
            "deadlineHours": deadline_hours
        }

        try:
            response = requests.post(endpoint, json=payload, headers=self.headers)

            if response.status_code == 200:
                return response.json()
            else:
                error_detail = response.json().get("detail", "Unknown Server Error")
                raise Exception(f"Kovi API Error ({response.status_code}): {error_detail}")

        except requests.exceptions.RequestException as e:
            raise Exception(f"Network Connection Error: {e}")
