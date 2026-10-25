#!/usr/bin/env python3
"""Build an ordinary-key witness by consulting the executable's public state.
Run only when intentionally refreshing the fixture, not during the gate.
Breadth-first routes pursue meat; a safe next cell is used while it respawns.
"""
from collections import deque
from pathlib import Path
import re
import subprocess

ROOT=Path(__file__).resolve().parents[1]
bin=ROOT/'target/release/trail'
path=ROOT/'target/natural-route.pk'
header='pk 1\nseed 52\ntier rich\nsize 200x60\n'
keys=['t 0 start']
w,h=28,8
vectors={1:(0,-1),2:(0,1),3:(-1,0),4:(1,0)}
words={1:'up',2:'down',3:'left',4:'right'}
opposite={1:2,2:1,3:4,4:3}
out=ROOT/'target/natural-route'
last_head=None
for tick in range(1100):
    path.write_text(header+'\n'.join(keys)+'\n')
    p=subprocess.run([str(bin),'--headless','--script',str(path),'--frames',str(tick+1),'--every','1000000','--dump',str(out)],capture_output=True,text=True)
    assert p.returncode==0,p.stderr
    text=(out/'final.state').read_text()
    parts=text.splitlines()[0].split()
    st={parts[i]:int(parts[i+1]) for i in range(0,len(parts),2)}
    wolves=[tuple(map(int,m.split())) for m in re.findall(r'^wolf (.*)$',text,re.M)]
    meat={tuple(map(int,m.split())) for m in re.findall(r'^meat (.*)$',text,re.M)}
    if st['phase']==2:break
    head=wolves[0]
    if head[:2]!=last_head:
        blocked={x[:2] for x in wolves[1:-1]}
        todo=deque([(head[0],head[1],head[2],None)])
        seen={(head[0],head[1],head[2])}
        chosen=None
        while todo:
            x,y,d,first=todo.popleft()
            if (x,y) in meat and first is not None:chosen=first;break
            for k,(dx,dy) in vectors.items():
                nx,ny=(x+dx)%w,(y+dy)%h
                key=(nx,ny,k)
                if k==opposite[d] or (nx,ny) in blocked or key in seen:continue
                seen.add(key);todo.append((nx,ny,k,first or k))
        if chosen is None:
            chosen=next((k for k,(dx,dy) in vectors.items() if k!=opposite[head[2]] and ((head[0]+dx)%w,(head[1]+dy)%h) not in blocked),head[2])
        keys.append(f't {tick+1} {words[chosen]}')
        last_head=head[:2]
    if st['strikes']>=1 and st['eaten']>=3:break
keys.append(f't {tick+1} quit')
# The final appended quit runs one tick after the observed score state.
frames=tick+2
case=ROOT/'tests/cases/natural-200.pk'
case.write_text(header+f'# frames {frames} every 60 from 600\n# score {st["score"]}\n'+'\n'.join(keys)+'\n')
print('natural witness',frames,'ticks',st,flush=True)
assert st['eaten']>=3 and st['strikes']>=1,st
