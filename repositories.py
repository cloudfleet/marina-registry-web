import yaml
import os
import settings

def load_repository_info(image_name):
    with open(settings.IMAGES_DATA_PATH  , "r") as fh:
        repository_info = ([image_data for image_data in yaml.safe_load(fh) if image_data["name"] == image_name ] + [None])[0]
    if repository_info:
        repository_info["builds"] = _load_builds(image_name)
        return repository_info
    else:
        return None

def _load_builds(image_name):
    return [_load_build_info(image_name, build_id) for build_id in os.listdir(settings.BUILD_LOGS_PATH)]

def _load_build_info(image_name, build_id):
    try:
        with open(settings.BUILD_LOGS_PATH + "/" + image_name + "/" + build_id + "/build-data.yml", "r") as fh:
            build_info = yaml.safe_load(fh)
            build_info["id"] = build_id
    except:
        build_info = {
            "id": build_id,
            "success": False
        }

    return build_info

def load_build_logs(image_name, build_id):
    build_logs = {
        "out": None,
        "err": None
    }

    try:
        with open(settings.BUILD_LOGS_PATH + "/" + image_name + "/" + build_id + "/out.log", "r") as fh:
            build_logs["out"] = fh.read()
    except:
        pass

    try:
        with open(settings.BUILD_LOGS_PATH + "/" + image_name + "/" + build_id + "/err.log", "r") as fh:
            build_logs["err"] = fh.read()
    except:
        pass

    return build_logs
