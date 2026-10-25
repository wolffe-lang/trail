#!/usr/bin/env python3
"""Black-box assertions independent of the golden bytes, on each shipped backend."""
import argparse
import pathlib
import re
import subprocess

ROOT = pathlib.Path(__file__).resolve().parents[1]

def run(bin, script, frames=1, extra=()):
    out = ROOT / 'target' / 'gameplay' / script.stem
    result = subprocess.run([str(bin), '--headless', '--script', str(script), '--frames', str(frames),
                             '--every', str(frames), '--dump', str(out), *extra], capture_output=True, text=True)
    assert result.returncode == 0, (script, result.returncode, result.stderr)
    text = (out / 'final.state').read_text()
    words = text.splitlines()[0].split()
    state = {words[i]: int(words[i+1]) for i in range(0, len(words), 2)}
    return state, text, (out/'final.txt').read_text()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--bin', required=True)
    a = ap.parse_args()
    bin = pathlib.Path(a.bin).resolve()
    for size in (80, 200):
        def case(name): return ROOT/'tests'/'cases'/f'{name}-{size}.pk'
        title, _, screen = run(bin,case('title'))
        assert title['phase'] == 0 and 'T R A I L' in screen
        one, _, _ = run(bin,case('one'))
        assert one['length'] == 1 and one['score'] == 0 and one['phase'] == 1
        summoned, _, _ = run(bin,case('summons'))
        assert summoned['pending'] == 1 and summoned['length'] == 1
        telegraph, _, _ = run(bin,case('telegraph'))
        assert telegraph['eagle_age'] == 19 and telegraph['strikes'] == 0
        hit, _, hit_screen = run(bin,case('hit'))
        assert hit['length'] == 2 and 1 <= hit['roll'] <= 7 and hit['strikes'] == 1
        assert 'HIT' in hit_screen and '35%' in hit_screen
        miss, _, miss_screen = run(bin,case('miss'))
        assert miss['length'] == 3 and 8 <= miss['roll'] <= 20 and miss['survived'] == 1 and miss['score'] == 25
        assert 'miss' in miss_screen
        for heading,word in enumerate(('up','down','left','right'),1):
            st,text,_=run(bin,case('stride-'+word),8)
            assert st['phase']==1 and st['length']==1
            assert re.search(r'^gait 0 1$',text,re.M),text
            assert int(re.search(r'^wolf \d+ \d+ (\d+)$',text,re.M)[1])==heading
        dead, _, screen = run(bin,case('death'))
        assert dead['phase'] == 2 and 'THE TRAIL ENDS' in screen
        for i,name in enumerate(('up','down','left','right')):
            st, text, _ = run(bin,case('wrap-'+name))
            wraps = list(map(int,text.splitlines()[1].split()[1:]))
            assert wraps[i] == 1, (name,wraps)
            wolf = list(map(int,re.search(r'^wolf (.*)$',text,re.M)[1].split()))
            c, r = size//5, ((24 if size==80 else 60)-2)//3
            assert wolf[:2] == ([c//2,r-1],[c//2,0],[c-1,r//2],[0,r//2])[i], (name,wolf)
    for path in sorted((ROOT/'tests'/'replays').glob('*.pk')):
        frames = int(re.search(r'^t (\d+) quit$',path.read_text(),re.M)[1])+1
        state, _, _ = run(bin,path,frames)
        claim = int(re.search(r'^# score (\d+)$',path.read_text(),re.M)[1])
        assert state['score'] == claim
        assert state['eaten'] >= 1, 'recordings must demonstrate a real meal'
        print(f'gameplay: recorded {path.name}: score {claim}, length {state["length"]}, meals {state["eaten"]} verified')
    natural = ROOT/'tests/cases/natural-80.pk'
    st, _, _ = run(bin,natural,561)
    assert st['score'] == 2500 and st['eaten'] == 25 and st['strikes'] == 1 and st['roll'] == 3 and st['length'] == 22
    print('gameplay: natural ordinary-key run: 25 meals, 23 wolves, first eagle hit, score 2500')
    bad = [('--size','39x12'),('--size','40x11'),('--every','0'),('--seed','x')]
    for flags in bad:
        p = subprocess.run([str(bin),'--headless',*flags],capture_output=True,text=True)
        assert p.returncode == 2 and ('small' in p.stderr or 'parse' in p.stderr)
    print(f'gameplay: {bin.name}: scene semantics, four seams, score verification, refusals green')

if __name__ == '__main__': main()
