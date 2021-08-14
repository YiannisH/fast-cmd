from typing import Optional
from fastapi import APIRouter, Depends
from dependencies import get_token_header
import json, os

prefix="docker"
router = APIRouter(
    prefix=fr"/{prefix}",
    tags=[fr"{prefix}"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": fr"/{prefix}: Not found"}},
)

def constructCmd(op: str, flag: Optional[str]=""):
	print(rf"op: {op} flag: {flag}")
	return rf"docker {op} {flag} --format " + "'{{json .}}' | jq --slurp"

@router.get("/docker")
def runCmd(op: str, flag: Optional[str]=""):
	if flag != "":
		return json.loads(os.popen(constructCmd(op, flag)).read()) 
	return json.loads(os.popen(constructCmd(op)).read()) 

@router.get("/docker/container/ls")
def runCmd():
	return json.loads(os.popen(constructCmd("container")).read()) 

@router.get("/docker/image/ls")
def runCmd():
	return json.loads(os.popen(constructCmd("image")).read()) 

@router.get("/docker/volume/ls")
def runCmd():
	return json.loads(os.popen(constructCmd("volume")).read()) 

@router.get("/docker/info")
def runCmd():
	return json.loads(os.popen(constructCmd("info")).read()) 

