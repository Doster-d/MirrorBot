import logging
from json import load

api_key = ""

upstream_owner = ""
upstream_repo = ""

downstream_owner = ""
downstream_repo = ""

local_repo_directory = "local_downstream_clone"
mirror_pr_title_prefix = "[MIRROR] "
mirror_branch_prefix = "upstream-merge-"

log_level = logging.INFO
event_stream_wait = 60

with open("config.json") as f:
    data = load(f)
    for key, value in data.items():
        exec(f"{key}=\"{value}\"")
