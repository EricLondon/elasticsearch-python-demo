import elasticsearch
import json
import sys
from faker import Faker

ES_PASSWORD = "e46yYv8rTVy3EgbTTs"

#
# Example usage:
#
# poetry run get_person Eric
#


class ElasticsearchDemo:
    def __init__(self):
        self.es_host = "localhost"
        self.es_port = 9200
        self.es_password = ES_PASSWORD

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
            self.es.index(index="people", document=person)

    def get_person(self, search_term):
        try:
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
            result = self.es.search(index="people", **query)

            # Convert the ObjectApiResponse to a dictionary
            result_dict = result.body if hasattr(result, "body") else dict(result)

            # Pretty print the results
            print(json.dumps(result_dict, indent=2, sort_keys=True))

        except Exception as e:
            print(f"Error searching for person: {e}")
            return None


def populate_people():
    ElasticsearchDemo().populate_people()


def get_person():
    search_term = sys.argv[1]
    ElasticsearchDemo().get_person(search_term)
