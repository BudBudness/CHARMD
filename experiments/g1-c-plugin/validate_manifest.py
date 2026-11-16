"""Strict validation for the proposed CHARMD browser-plugin manifest v1."""
import json
from pathlib import Path

ALLOWED_KINDS={"audio-effect","instrument","analyzer"}
ALLOWED_CAPABILITIES=set()

def validate(data):
    if not isinstance(data,dict): raise ValueError("manifest must be an object")
    required={"manifestVersion","pluginId","version","name","kind","entry","audio","parameters","stateVersion","capabilities"}
    if set(data)!=required: raise ValueError("manifest fields must match the v1 contract exactly")
    if data["manifestVersion"]!=1 or data["stateVersion"]!=1: raise ValueError("unsupported manifest/state version")
    for field in ("pluginId","version","name"):
        if not isinstance(data[field],str) or not data[field].strip(): raise ValueError(f"invalid {field}")
    if data["kind"] not in ALLOWED_KINDS: raise ValueError("unsupported plugin kind")
    entry=data["entry"]
    if not isinstance(entry,str) or not entry.endswith(".wasm") or entry.startswith("/") or ".." in entry.split("/"):
        raise ValueError("entry must be a safe relative WASM path")
    audio=data["audio"]
    if not isinstance(audio,dict) or set(audio)!={"inputs","outputs","supportedSampleRates","maximumBlockFrames","reportedLatencyFrames"}:
        raise ValueError("invalid audio contract")
    if audio["inputs"] not in (0,1,2) or audio["outputs"] not in (1,2): raise ValueError("unsupported channel layout")
    if not audio["supportedSampleRates"] or any(x not in (44100,48000,96000) for x in audio["supportedSampleRates"]): raise ValueError("invalid sample rates")
    if not 1<=audio["maximumBlockFrames"]<=8192: raise ValueError("invalid block limit")
    if not 0<=audio["reportedLatencyFrames"]<=48000: raise ValueError("invalid latency")
    if not isinstance(data["parameters"],list) or len(data["parameters"])>256: raise ValueError("invalid parameter list")
    ids=set()
    for p in data["parameters"]:
        if set(p)!={"id","type","default","min","max","unit","automatable"}: raise ValueError("invalid parameter schema")
        if not isinstance(p["id"],str) or not p["id"] or p["id"] in ids: raise ValueError("duplicate/empty parameter id")
        ids.add(p["id"])
        if p["type"]!="float" or not all(isinstance(p[k],(int,float)) for k in ("default","min","max")): raise ValueError("unsupported parameter type")
        if not p["min"]<=p["default"]<=p["max"] or p["min"]>=p["max"]: raise ValueError("parameter bounds invalid")
        if not isinstance(p["unit"],str) or not isinstance(p["automatable"],bool): raise ValueError("invalid parameter metadata")
    if not isinstance(data["capabilities"],list) or any(c not in ALLOWED_CAPABILITIES for c in data["capabilities"]):
        raise ValueError("unknown capability denied")
    return True

if __name__=="__main__":
    candidate=json.loads(Path(__file__).with_name("gain.plugin.json").read_text())
    validate(candidate)
    print("PASS: manifest accepted; no capabilities granted")
