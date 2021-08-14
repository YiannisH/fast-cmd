from typing import Optional
from fastapi import APIRouter, Depends
from dependencies import get_token_header
import nmap3

prefix="nmap"
router = APIRouter(
    prefix=fr"/{prefix}",
    tags=[fr"{prefix}"],
    # dependencies=[Depends(get_token_header)],
    responses={404: {"description": fr"/{prefix}: Not found"}},
)

# https://pypi.org/project/python3-nmap/

def getAddrString(ip_addr: str, subnet_mask: str):
	if subnet_mask != None:
		return ip_addr+"/"+subnet_mask
	else:
		return ip_addr

@router.get("/ping/{ip_addr}")
def nmapScan(ip_addr: str, subnet_mask: Optional[str] = None):
	addrString = getAddrString(ip_addr, subnet_mask)
	return  nmap3.NmapScanTechniques().nmap_ping_scan(addrString)

@router.get("/tcp/{ip_addr}")
def nmapScan(ip_addr: str, subnet_mask: Optional[str] = None):
	addrString = getAddrString(ip_addr, subnet_mask)
	return  nmap3.NmapScanTechniques().nmap_tcp_scan(addrString)

@router.get("/port/{ip_addr}")
def nmapScan(ip_addr: str, subnet_mask: Optional[str] = None):
	addrString = getAddrString(ip_addr, subnet_mask)
	return  nmap3.NmapHostDiscovery().nmap_portscan_only(addrString)

@router.get("/os/{ip_addr}")
def nmapHostDiscovery(ip_addr: str):
	return nmap3.NmapHostDiscovery().nmap_os_detection(ip_addr)

@router.get("/arp/{ip_addr}")
def nmapHostDiscovery(ip_addr: str, subnet_mask: Optional[str] = None):
	addrString = getAddrString(ip_addr, subnet_mask)
	return nmap3.NmapHostDiscovery().nmap_arp_discovery(addrString)

@router.get("/version")
def nmapVersion():
	return nmap3.NmapHostDiscovery().nmap_version()