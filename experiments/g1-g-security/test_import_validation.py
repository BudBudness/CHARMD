"""Executable security boundary checks for future CHARMD import handling.

These are policy-level primitives, not a test of an application upload endpoint.
"""
import unittest
from pathlib import PurePosixPath

MAX_ARCHIVE_BYTES=100*1024*1024
MAX_ENTRIES=10_000

def safe_archive_path(raw: str) -> str:
    if not raw or "\x00" in raw or "\\" in raw: raise ValueError("invalid path")
    p=PurePosixPath(raw)
    if p.is_absolute() or any(part in ("..","") for part in p.parts): raise ValueError("path traversal")
    if p.parts and ":" in p.parts[0]: raise ValueError("drive or URI path")
    return str(p)

def validate_archive(entries):
    if len(entries)>MAX_ENTRIES: raise ValueError("too many entries")
    total=0; names=set()
    for name,size in entries:
        clean=safe_archive_path(name)
        if clean in names: raise ValueError("duplicate normalized path")
        names.add(clean)
        if not isinstance(size,int) or size<0: raise ValueError("invalid size")
        total+=size
        if total>MAX_ARCHIVE_BYTES: raise ValueError("archive too large")
    return total

class ImportSecurityTests(unittest.TestCase):
    def test_accepts_relative_path(self): self.assertEqual(safe_archive_path("audio/clip.wav"),"audio/clip.wav")
    def test_rejects_parent_traversal(self):
        for p in ("../secret","audio/../../secret","/etc/passwd"):
            with self.assertRaises(ValueError): safe_archive_path(p)
    def test_rejects_windows_and_null_paths(self):
        for p in ("..\\secret","C:/secret","audio\x00.wav"):
            with self.assertRaises(ValueError): safe_archive_path(p)
    def test_rejects_duplicate_and_oversized_archives(self):
        with self.assertRaises(ValueError): validate_archive([("a.wav",1),("a.wav",2)])
        with self.assertRaises(ValueError): validate_archive([("large.bin",MAX_ARCHIVE_BYTES+1)])
    def test_rejects_negative_size(self):
        with self.assertRaises(ValueError): validate_archive([("a.wav",-1)])

if __name__ == "__main__": unittest.main()
