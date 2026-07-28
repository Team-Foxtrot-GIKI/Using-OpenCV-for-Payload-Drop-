# Foxtrot — Payload Drop / Landing Marker Detection

Vision system that detects a colored landing marker in a video feed, computes its centroid
`(Cx, Cy)` in real time, and passes that data to a simulated DroneKit/SITL script that logs a
`DROP` event when the marker is centered in frame.

## Objective

Build an end-to-end pipeline: camera feed → HSV masking → contour detection → centroid calculation → alignment check → simulated drop trigger.