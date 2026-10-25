"""Game rows: title/start/pause, minimum, resize, Escape and recorder round-trip."""
import fcntl
import os
from pathlib import Path
import struct
import subprocess
import termios

def title(bin,ctx):
    s=ctx.Session([bin,'--seed','7'],24,80,ctx.env_for())
    s.pump(.2)
    problems=[]
    before=ctx.screen_text(bin,s.out)
    if 'T R A I L' not in before: problems.append('title missing')
    s.type(b'\r',.2)
    s.type(b' ',.2)
    if 'PAUSED' not in ctx.screen_text(bin,s.out): problems.append('Space did not pause')
    s.type(b' ',.1)
    s.type(b'q');s.finish();ctx.common_checks(s,0,problems)
    return s,problems

def title_start(bin,ctx,key):
    s=ctx.Session([bin,'--seed','7','--trace'],24,80,ctx.env_for())
    s.pump(.1)
    problems=[]
    if 'T R A I L' not in ctx.screen_text(bin,s.out):problems.append('title missing before start key')
    s.type(key,.08)
    first=ctx.screen_text(bin,s.out)
    if 'T R A I L' in first:problems.append('starting key left title card visible')
    if 'PAUSED' in first:problems.append('starting Space paused instead of starting gameplay')
    if 'Arrows turn | Space pauses | q quits' not in first:problems.append('first gameplay controls missing')
    if 'pack 1  score 0' not in first:problems.append('first gameplay HUD missing')
    if b'carries_key' not in s.err:problems.append('no carrying frame for actual start key')
    s.type(b'q');s.finish();ctx.common_checks(s,0,problems)
    return s,problems

def title_cr(bin,ctx):return title_start(bin,ctx,b'\r')
def title_space(bin,ctx):return title_start(bin,ctx,b' ')

def minimum(bin,ctx):
    s=ctx.Session([bin,'--size','40x16','--plain'],16,40,ctx.env_for())
    s.type(b'\r',.2)
    # At 40x16 the compact HUD must still expose the odds and threshold.
    if b'35%' not in s.out: problems=['minimum HUD hid fixed odds']
    else: problems=[]
    s.type(b'q');s.finish();ctx.common_checks(s,0,problems)
    return s,problems

def escape(bin,ctx):
    s=ctx.Session([bin,'--no-title'],24,80,ctx.env_for())
    s.type(b'\x1b',.2);s.finish();problems=[];ctx.common_checks(s,0,problems)
    if b'the quit key' not in s.err:problems.append('Escape did not quit')
    return s,problems

def resize(bin,ctx):
    path=Path(ctx.ROOT)/'target/pty/resize.pk'
    path.parent.mkdir(parents=True,exist_ok=True)
    s=ctx.Session([bin,'--no-title','--record',str(path)],24,80,ctx.env_for())
    fcntl.ioctl(s.master,termios.TIOCSWINSZ,struct.pack('HHHH',30,100,0,0))
    s.pump(.3)
    s.type(b'q');s.finish();problems=[];ctx.common_checks(s,0,problems)
    text=path.read_text()
    if 'size 100x30' not in text:problems.append('SIGWINCH was not recorded')
    # The kernel delivers SIGWINCH for our own pty's size change; no signal API.
    return s,problems

def record(bin,ctx):
    path=Path(ctx.ROOT)/'target/pty/record.pk'
    path.parent.mkdir(parents=True,exist_ok=True)
    s=ctx.Session([bin,'--no-title','--seed','7','--record',str(path)],24,80,ctx.env_for())
    s.type(b'\x1b[A',.2);s.type(b'q');s.finish();problems=[];ctx.common_checks(s,0,problems)
    text=path.read_text()
    if 'up' not in text or 'quit' not in text or '# score ' not in text:problems.append('record missing actual inputs/score')
    ticks=int([x for x in text.splitlines() if x.endswith(' quit')][-1].split()[1])+1
    p=subprocess.run([bin,'--headless','--script',str(path),'--frames',str(ticks),'--dump',str(path.parent/'record')],capture_output=True,text=True)
    if p.returncode or 'verified score' not in p.stderr:problems.append('recorded score did not verify: '+p.stderr)
    return s,problems

ROWS={'title-pause':title,'title-cr':title_cr,'title-space':title_space,'minimum-40x16':minimum,'escape':escape,'resize':resize,'record-roundtrip':record}
