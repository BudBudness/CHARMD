# G1-B — Project Model and Persistence Spike

- Gate: G1 Discover
- Status: Design artifact; no browser persistence experiment executed
- Date: 2026-11-08
- Decision informed: versioned project model and browser storage split

## Scope

Define a minimal, versioned project document and a reproducible local persistence experiment. This is not the production project format and does not authorize broad DAW implementation.

## Candidate logical model

```json
{
  "schemaVersion": 1,
  "project": {
    "id": "project_uuid",
    "name": "Untitled",
    "createdAt": "ISO-8601",
    "updatedAt": "ISO-8601",
    "sampleRate": 48000,
    "tempo": 120,
    "timeSignature": [4, 4]
  },
  "tracks": [{
    "id": "track_uuid",
    "kind": "audio",
    "name": "Track 1",
    "order": 0,
    "muted": false,
    "solo": false,
    "gainDb": 0,
    "pan": 0,
    "clips": [{
      "id": "clip_uuid",
      "assetId": "asset_uuid",
      "startTicks": 0,
      "sourceOffsetFrames": 0,
      "durationFrames": 0,
      "gainDb": 0
    }],
    "processors": [],
    "automation": []
  }],
  "buses": [],
  "assets": [{
    "id": "asset_uuid",
    "mediaType": "audio/wav",
    "byteLength": 0,
    "sha256": "hex",
    "storageKey": "asset_uuid",
    "sampleRate": 48000,
    "channels": 2,
    "frames": 0
  }],
  "revision": 1
}
```

IDs are stable opaque identifiers. Timeline positions use integer ticks/frames rather than floating-point seconds. The project format is independent of IndexedDB/OPFS so it can be exported and migrated.

## Storage hypothesis

- IndexedDB: project metadata, revisions, asset manifests, transaction coordination.
- OPFS: large binary audio assets where supported and beneficial.
- Import/export: portable manifest plus asset payloads; checksums verified on import.
- Request persistent storage where supported, but never treat it as guaranteed.
- Autosave by immutable revision or atomic revision pointer update; never overwrite the only recoverable revision.
- Surface quota, write failure, persistence grant and recovery status to the user.

## Required prototype cases

1. Create project, track, clip, asset manifest; reload and verify exact round trip.
2. Write asset bytes, compute SHA-256, reload and verify byte count/hash.
3. Interrupt between asset write and manifest commit; orphan assets must be detectable.
4. Interrupt between revision creation and active-revision pointer update; previous revision remains readable.
5. Inject QuotaExceededError and storage exceptions; preserve last committed revision.
6. Migrate v1 fixture to v2 with deterministic, idempotent migration.
7. Reject unsupported future schema versions without destructive rewrite.
8. Export/import and verify project and asset hashes.
9. Test private browsing, storage denial and browser restart behavior where available.

## Acceptance measurements

Record browser/version, OS/device, storage estimate, persistence grant, bytes written/read, transaction duration, reload recovery, injected failure point, resulting revision, hash match and error. Repeat each destructive-failure case at least three times.

## Invariants

- A committed revision is immutable.
- Active revision always points to a fully committed revision.
- Asset references resolve or are explicitly marked missing.
- Failed writes never silently replace the last good project.
- Schema migrations are pure, versioned and fixture-tested.
- Exported projects do not depend on browser-origin storage keys.

## Not yet proven

No quota, eviction, crash, migration, OPFS, IndexedDB, import/export or mobile-browser behavior has been measured. The schema above is a candidate only.

## Exit decision

G1-B remains Partial until a runnable prototype produces the measurements above on representative mobile browsers and at least one desktop browser.
