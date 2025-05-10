import elasticsearch
import json
import sys
from faker import Faker


class ElasticsearchDemo:
    def __init__(self):
        self.es_host = "localhost"
        self.es_port = 9200
        self.es_password = "e46yYv8rTVy3EgbTTs"

        # Connect to Elasticsearch 8.x with custom headers
        self.es = elasticsearch.Elasticsearch(
            f"http://{self.es_host}:{self.es_port}",
            basic_auth=("elastic", self.es_password),
            request_timeout=30,
            headers={"Content-Type": "application/json", "Accept": "application/json"},
        )

    def populate_people(self):
        fake = Faker()

        # create 1000 people
        for i in range(1000):
            person = {
                "first_name": fake.first_name(),
                "last_name": fake.last_name(),
                "email": fake.email(),
                "address": fake.address(),
                "city": fake.city(),
                "state": fake.state(),
                "zip_code": fake.zipcode(),
                "country": fake.country(),
            }
            # In Elasticsearch 8.x, doc_type is removed and body is now document
            self.es.index(index="people", document=person)

    def get_person(self, search_term):
        try:
            # Search for a person by their first or last name
            # Use bool query with should clauses for OR logic
            query = {
                "query": {
                    "bool": {
                        "should": [
                            {"match": {"first_name": search_term}},
                            {"match": {"last_name": search_term}},
                        ],
                        "minimum_should_match": 1,
                    }
                }
            }
            # In Elasticsearch 8.x, body is now just passed directly
            # Execute the search query
            result = self.es.search(index="people", **query)

            # Convert the ObjectApiResponse to a dictionary
            result_dict = result.body if hasattr(result, "body") else dict(result)

            # Pretty print the results
            print(json.dumps(result_dict, indent=2, sort_keys=True))

            # Return the hits for further processing if needed
            return result_dict.get("hits", {}).get("hits", [])

        except Exception as e:
            print(f"Error searching for person: {e}")
            return None


def populate_people():
    ElasticsearchDemo().populate_people()


# poetry run get_person Eric
def get_person():
    search_term = sys.argv[1]
    ElasticsearchDemo().get_person(search_term)
