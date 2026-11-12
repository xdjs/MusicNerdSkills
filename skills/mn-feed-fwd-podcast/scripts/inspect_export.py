#!/usr/bin/env python3
"""Read-only technical export inspection. This is not perceptual or editorial QC."""
import argparse, hashlib, json, shutil, subprocess
from pathlib import Path
p = argparse.ArgumentParser(description=__doc__)
p.add_argument('movie', type=Path)
p.add_argument('--decode', action='store_true', help='Decode entire video/audio to null; may take time')
a = p.parse_args()
f = a.movie.expanduser().resolve(strict=True)
probe = shutil.which('ffprobe')
if not probe:
    p.error('ffprobe is required; use the existing approved installation')
r = subprocess.run([probe, '-v', 'error', '-show_format', '-show_streams', '-of', 'json', str(f)], capture_output=True, text=True, check=True)
h = hashlib.sha256()
with f.open('rb') as src:
    for block in iter(lambda: src.read(4*1024*1024), b''): h.update(block)
out = {'file': str(f), 'bytes': f.stat().st_size, 'sha256': h.hexdigest(), 'probe': json.loads(r.stdout), 'perceptual_review': 'NOT PERFORMED', 'full_decode': 'NOT REQUESTED'}
if a.decode:
    ffmpeg = shutil.which('ffmpeg')
    if not ffmpeg: p.error('ffmpeg is required for --decode')
    d = subprocess.run([ffmpeg, '-nostdin', '-xerror', '-v', 'error', '-i', str(f), '-map', '0:v?', '-map', '0:a?', '-f', 'null', '-'], capture_output=True, text=True)
    out['full_decode'] = {'exit_code': d.returncode, 'errors': d.stderr, 'passed': d.returncode == 0 and not d.stderr.strip()}
print(json.dumps(out, indent=2))
raise SystemExit(1 if a.decode and not out['full_decode']['passed'] else 0)
