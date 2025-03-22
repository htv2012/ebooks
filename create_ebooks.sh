#!/usr/bin/env bash

create_ebook() {
    cd "$1"
    name=$(date "+/tmp/$1_%Y-%m-%d.epub")
    rm -f "$name"
    zip -q -r "$name" *
    cd ..
}

create_ebook dai_duong_song_long
