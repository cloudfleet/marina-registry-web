from flask import Flask, jsonify, request
import settings, traceback, getopt, sys, os
import repositories

app = Flask(__name__)

api_base = "/api/v1/"

@app.route(api_base + '/repos/<namespace>/<repository>', methods=['GET'])
def get_repository(namespace, repository):

    repository_info = repositories.load_repository_info('%s/%s' % (namespace, repository))

    return jsonify(repository_info)

@app.route(api_base + '/repos/<namespace>/<repository>/builds/<build_id>/logs', methods=['GET'])
def get_repository(namespace, repository, build_id):
    return jsonify(repositories.load_build_logs('%s/%s' % (namespace, repository), build_id))


if __name__ == '__main__':
    print os.environ
    app.run(host='0.0.0.0')
