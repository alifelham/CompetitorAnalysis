import os
import requests

class DataRetrievalAgent:
    def __init__(self, sources):
        """
        :param sources: List of sources, where each source is a dictionary with a "name" key.
        """
        self.sources = sources

    def fetch_data(self, query):
        """
        Fetch data from each source by calling the appropriate API.
        Returns a dictionary mapping source names to their data.
        """
        data = {}
        for source in self.sources:
            source_name = source['name']
            if source_name == "Crunchbase":
                data[source_name] = self.fetch_crunchbase(query)
            elif source_name == "LinkedIn":
                data[source_name] = self.fetch_linkedin(query)
            elif source_name == "Reddit":
                data[source_name] = self.fetch_reddit(query)
            elif source_name == "Google":
                data[source_name] = self.fetch_google(query)
            elif source_name == "G2":
                data[source_name] = self.fetch_g2(query)
            else:
                print(f"No handler defined for source: {source_name}")
                data[source_name] = None
        return data

    def fetch_crunchbase(self, query):
        """
        Fetch competitor data from Crunchbase using the official API.
        """
        api_key = os.getenv("CRUNCHBASE_API_KEY")
        if not api_key:
            print("Error: CRUNCHBASE_API_KEY environment variable is not set.")
            return None

        url = "https://api.crunchbase.com/api/v4/entities/organizations"
        params = {"query": query}
        headers = {
            "X-Cb-User-Key": api_key,
            "Content-Type": "application/json"
        }

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            json_data = response.json()
            # Check that we have at least one result
            if (
                "data" in json_data and 
                "items" in json_data["data"] and 
                len(json_data["data"]["items"]) > 0
            ):
                # Return the properties of the first organization result.
                return json_data["data"]["items"][0]["properties"]
            else:
                print("No Crunchbase results found.")
                return None
        except Exception as e:
            print(f"Error fetching Crunchbase data: {e}")
            return None

    def fetch_linkedin(self, query):
        """
        Fetch competitor data from LinkedIn using the official API.
        """
        access_token = os.getenv("LINKEDIN_ACCESS_TOKEN")
        if not access_token:
            print("Error: LINKEDIN_ACCESS_TOKEN environment variable is not set.")
            return None

        url = "https://api.linkedin.com/v2/organizations"
        params = {"q": "vanityName", "vanityName": query}
        headers = {"Authorization": f"Bearer {access_token}"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            json_data = response.json()
            if "elements" in json_data and len(json_data["elements"]) > 0:
                return json_data["elements"][0]
            else:
                print("No LinkedIn results found.")
                return None
        except Exception as e:
            print(f"Error fetching LinkedIn data: {e}")
            return None

    def fetch_reddit(self, query):
        """
        Fetch competitor-related data from Reddit using the public API endpoint.
        """
        url = "https://www.reddit.com/search.json"
        params = {"q": query, "limit": 1}
        headers = {"User-Agent": "CompetitorAnalysisBot/1.0"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            json_data = response.json()
            if (
                "data" in json_data and 
                "children" in json_data["data"] and 
                len(json_data["data"]["children"]) > 0
            ):
                return json_data["data"]["children"][0]["data"]
            else:
                print("No Reddit results found.")
                return None
        except Exception as e:
            print(f"Error fetching Reddit data: {e}")
            return None

    def fetch_google(self, query):
        """
        Fetch competitor data from Google Custom Search.
        """
        api_key = os.getenv("GOOGLE_API_KEY")
        cx = os.getenv("GOOGLE_CX")
        if not api_key or not cx:
            print("Error: GOOGLE_API_KEY or GOOGLE_CX environment variable is not set.")
            return None

        url = "https://www.googleapis.com/customsearch/v1"
        params = {"key": api_key, "cx": cx, "q": query}

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            json_data = response.json()
            if "items" in json_data and len(json_data["items"]) > 0:
                # Return the first search result
                return json_data["items"][0]
            else:
                print("No Google Custom Search results found.")
                return None
        except Exception as e:
            print(f"Error fetching Google data: {e}")
            return None

    def fetch_g2(self, query):
        """
        Fetch competitor data from G2 using the official API.
        """
        api_key = os.getenv("G2_API_KEY")
        if not api_key:
            print("Error: G2_API_KEY environment variable is not set.")
            return None

        url = "https://api.g2.com/v1/products/search"
        params = {"query": query}
        headers = {"Authorization": f"Bearer {api_key}"}

        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()
            json_data = response.json()
            if "products" in json_data and len(json_data["products"]) > 0:
                return json_data["products"][0]
            else:
                print("No G2 results found.")
                return None
        except Exception as e:
            print(f"Error fetching G2 data: {e}")
            return None
