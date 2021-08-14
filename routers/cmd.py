import os
from fastapi import APIRouter, Depends
from dependencies import get_token_header
import json

from urllib.parse import urlparse

prefix="cmd"
router = APIRouter(
    prefix=fr"/{prefix}",
    tags=[fr"{prefix}"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": fr"/{prefix}: Not found"}},
)

def constructCmd(cmd_name: str, cmd_flags=None):
	if cmd_flags:	
		cmd = fr'{cmd_name} -{cmd_flags} | jc --{cmd_name} -p'
	else:
		cmd = fr'{cmd_name} | jc --{cmd_name} -p'
	return cmd

@router.get("/ls")
def runCmd(path: str):
	decodedPath = urlparse(path)
	return json.loads(os.popen(rf"ls -latr {decodedPath.path} | jc --ls").read())

@router.get("/{cmd_name}")
def runCmd(cmd_name: str): 
	return json.loads(os.popen(constructCmd(cmd_name)).read()) 

@router.get("/{cmd_name}/{cmd_flags}")
def runCmd(cmd_name: str, cmd_flags: str):
	return json.loads(os.popen(constructCmd(cmd_name, cmd_flags)).read())
