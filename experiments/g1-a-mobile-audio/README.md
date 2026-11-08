# G1-A Mobile Audio Benchmark Harness

A single-file, isolated browser benchmark for the CHARMD G1 mobile-audio discovery workstream.

## Run

1. Serve this directory from a secure context (HTTPS or localhost). Do not open the HTML as a `file://` URL if the browser refuses audio permissions or APIs.
2. Open `index.html` in the target mobile or desktop browser.
3. Record device model, OS/build, browser/version, power mode, battery level, output route, and screen state.
4. Run each track-count/signal configuration at least three times. Start with 4, 8, 16, 32 and 64 voices, stopping when playback becomes unstable or the device overheats.
5. Listen for clicks, dropouts, distortion, silence and unexpected pauses. Record observations alongside the downloaded JSON.
6. Repeat with the screen locked/backgrounded only as a separately labelled lifecycle experiment; expect platform policy to suspend audio.

## What it measures

- Whether an AudioContext can be created/resumed at the selected sample rate.
- Synthetic looping AudioBufferSourceNode voice workload with gain and stereo panning.
- Browser-reported base/output latency when exposed.
- AudioContext state changes and document visibility events while the page remains alive.
- Main-thread heartbeat maximum delay (a coarse scheduling/jank indicator).
- Browser/device metadata and elapsed test time in a downloadable JSON record.

## Important limitations

This is **not** a DAW engine, not a calibrated audio analyzer, and not a proof of glitch-free playback. It does not measure hardware CPU load, thermal state, actual output underruns, round-trip microphone latency, Bluetooth codec delay, recording quality, or background survival reliably. Browser timing and latency properties are estimates and vary by implementation. The generated signals are synthetic; they do not represent decoding, editing, automation, plugin chains, or realistic project graphs.

A low heartbeat delay does not prove clean audio. A running AudioContext does not prove that the operating system delivered every audio buffer on time. Audible observations and a future loopback/recording test are required.

## Evidence protocol

Store raw JSON results outside source control unless the user explicitly approves committing device-identifying evidence. For each run, preserve:
- test configuration and JSON output;
- exact device/OS/browser versions;
- foreground/background and screen-lock conditions;
- output route and power mode;
- audible observations and repeat count.

Do not claim G1-A passed based on this harness alone. G1-A requires repeatable evidence across the agreed representative low-, mid- and high-tier device matrix, interruption/recovery tests, and acceptance thresholds approved in the discovery report.

## Safety

Keep volume low; stop if the device becomes unusually hot or unstable. Do not run while driving. No microphone capture, network requests, analytics, account access, uploads, provider calls, or infrastructure changes are performed by this harness.
