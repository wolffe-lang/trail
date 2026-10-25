#!/usr/bin/env python3
"""Create two real pty recordings. Only ordinary start/arrow/quit inputs;
no scene fixtures, score injection, teleports or force-eagle events."""
import importlib.machinery
import importlib.util
import os
from pathlib import Path
import subprocess

ROOT=Path(__file__).resolve().parents[1]
loader=importlib.machinery.SourceFileLoader('trail_pty',str(ROOT/'.lair/tools/pty'))
ctx=importlib.util.module_from_spec(importlib.util.spec_from_loader('trail_pty',loader));loader.exec_module(ctx)
bin=str(ROOT/'target/release/trail')
out=ROOT/'tests/replays';out.mkdir(parents=True,exist_ok=True)
(ROOT/'target/pty').mkdir(parents=True,exist_ok=True)
for cols,rows,tier in [(80,24,'rich'),(200,60,'plain')]:
    w,h=cols//7,(rows-2)//7
    desired=(h//2)*w+(w//2+3)
    def suitable(seed):
        rng=seed+1
        for n in range(5):
            rng=rng*48271%2147483647
            if n==0 and rng%(w*h)!=desired:return False
        return (rng%(w*h))//w!=h//2
    seed=next(s for s in range(100000) if suitable(s))
    path=out/f'recorded-{cols}-{tier}.pk'
    s=ctx.Session([bin,'--no-title','--seed',str(seed),'--size',f'{cols}x{rows}',
                   '--tier',tier,'--record',str(path)],rows,cols,ctx.env_for())
    s.pump(1.8)
    if cols==200:s.type(b'\x1b[B',.5)
    s.pump(.5)
    s.type(b'q');s.finish()
    problems=[];ctx.common_checks(s,0,problems)
    assert not problems,problems
    print(path.name,'seed',seed,'exit',s.status,flush=True)
    print(path.read_text(),flush=True)
    ticks=int([x for x in path.read_text().splitlines() if x.endswith(' quit')][-1].split()[1])+1
    check=ROOT/'target/record-witnesses'/path.stem
    subprocess.run([bin,'--headless','--script',str(path),'--frames',str(ticks),'--dump',str(check)],check=True)
    print((check/'final.state').read_text(),flush=True)
    (ROOT/'target/pty'/f'{path.stem}.bin').write_bytes(s.out)
