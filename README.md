# fix-vtt-times
## A short Python script to adjust timings in VTT files.

Ever cut a video for upload that came with a VTT caption file? Need a quick way to shift timings so your captions will sync up on YouTube?

My spin on Nat Dunn's WebVTT timestamp adjustment script. See the original [here](https://www.webucator.com/article/fixing-webvtt-times-with-python/).

This version changes Nat's in two ways:

1. I use the pyperclip module to skip a step and copy the contents of the output to the clipboard. To install pyperclip see: [here](https://github.com/asweigart/pyperclip).
2. The output of the fix_vtt_times function on its own produces three trailing zeros. YouTube doesn't like this. So output in my version is formatted to remove the last three leading zeros in the timestamps.
