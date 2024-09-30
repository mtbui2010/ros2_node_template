#!/bin/bash
PKG_PATH_LIST=("/media/keti/workdir/projects/ketisdk"
"/media/keti/workdir/projects/node_recognition"
"/media/keti/workdir/projects/Grounded-Segment-Anything"
)

for p in "${PKG_PATH_LIST[@]}"; do
    ln -sf $p .
    echo $p "symbol link created."
done
