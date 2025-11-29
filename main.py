import flask
import functions_framework

@functions_framework.http
def main(request: flask.wrappers.Request) -> flask.Response:
    log_headline: str = f"main()"
    print(f"{log_headline} · Init")


if __name__ == '__main__':
    print("versions-tracker local run")
    print(f"Remember to login with: gcloud auth application-default login")


    app = flask.Flask(__name__)  # Create a Flask app instance
    request = flask.request
    main(request)