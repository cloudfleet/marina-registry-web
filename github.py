from subprocess import Popen

def handle_push(payload):
  build_args = [
    "python",
    "/opt/marina/registry/scripts/build.py",
    "-i",
    payload["repository"]["clone_url"]
  ]

  process = Popen(build_args)

  process.pid
