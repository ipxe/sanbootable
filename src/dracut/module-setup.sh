#!/bin/bash

check() {
    return 0
}

depends() {
    return 0
}

install() {
    inst_hook cmdline 89 "$moddir/sanbootable-cmdline.sh"
}
