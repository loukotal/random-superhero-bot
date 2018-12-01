from mastodon import Mastodon
import os

#
mastodon = Mastodon(
    access_token=os.getenv("MASTODON_ACCESS_KEY"),
    api_base_url="https://botsin.space"
)


def lambda_handler(event, context):
    mastodon.status_post("Hello world from lambda function")
    return {
        "statusCode": 200,
        "body": "hello world?"
    }