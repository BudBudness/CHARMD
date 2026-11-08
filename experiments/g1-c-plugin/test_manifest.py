import copy, json, unittest
from pathlib import Path
from validate_manifest import validate

FIXTURE=json.loads(Path(__file__).with_name("gain.plugin.json").read_text())

class ManifestTests(unittest.TestCase):
    def test_accepts_minimal_gain_manifest(self): self.assertTrue(validate(FIXTURE))
    def test_rejects_unknown_fields(self):
        x=copy.deepcopy(FIXTURE); x["network"]=True
        with self.assertRaises(ValueError): validate(x)
    def test_rejects_path_traversal(self):
        x=copy.deepcopy(FIXTURE); x["entry"]="../evil.wasm"
        with self.assertRaises(ValueError): validate(x)
    def test_rejects_unknown_capability(self):
        x=copy.deepcopy(FIXTURE); x["capabilities"]=["network"]
        with self.assertRaises(ValueError): validate(x)
    def test_rejects_invalid_parameter_range(self):
        x=copy.deepcopy(FIXTURE); x["parameters"][0]["default"]=3
        with self.assertRaises(ValueError): validate(x)
    def test_rejects_duplicate_parameter_ids(self):
        x=copy.deepcopy(FIXTURE); x["parameters"].append(copy.deepcopy(x["parameters"][0]))
        with self.assertRaises(ValueError): validate(x)

if __name__=="__main__": unittest.main()
