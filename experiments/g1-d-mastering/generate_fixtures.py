"""Generate deterministic PCM16 WAV golden-signal fixtures using only Python stdlib."""
import hashlib, json, math, struct, wave
from pathlib import Path

RATE=48000
OUT=Path(__file__).with_name("fixtures")
DURATION=1.0

def write(name, samples, channels=1):
    OUT.mkdir(parents=True,exist_ok=True)
    path=OUT/(name+".wav")
    with wave.open(str(path),"wb") as w:
        w.setnchannels(channels); w.setsampwidth(2); w.setframerate(RATE)
        frames=bytearray()
        for frame in samples:
            values=frame if isinstance(frame,tuple) else (frame,)*channels
            for value in values:
                value=max(-1.0,min(0.999969482421875,float(value)))
                frames.extend(struct.pack("<h",round(value*32768)))
        w.writeframes(frames)
    digest=hashlib.sha256(path.read_bytes()).hexdigest()
    return {"file":path.name,"sha256":digest,"sampleRate":RATE,"channels":channels,
            "frames":len(samples),"format":"PCM_S16LE"}

n=int(RATE*DURATION)
fixtures=[]
fixtures.append(write("silence",[0.0]*n))
fixtures.append(write("sine_1khz",[(0.5*math.sin(2*math.pi*1000*i/RATE),) for i in range(n)]))
fixtures.append(write("impulse",[1.0 if i==0 else 0.0 for i in range(n)]))
fixtures.append(write("stereo_left_only",[(0.5*math.sin(2*math.pi*440*i/RATE),0.0) for i in range(n)],2))
fixtures.append(write("stereo_anti_phase",[(0.5*math.sin(2*math.pi*440*i/RATE),-0.5*math.sin(2*math.pi*440*i/RATE)) for i in range(n)],2))
fixtures.append(write("log_sweep",[0.5*math.sin(2*math.pi*(20*(1000**(i/n)))*i/RATE) for i in range(n)]))
(OUT/"manifest.json").write_text(json.dumps({"generator":"Python stdlib","sampleRate":RATE,"fixtures":fixtures},indent=2)+"\n")
print(json.dumps(fixtures,indent=2))
