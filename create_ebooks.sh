#!/usr/bin/env bash

create_ebook() {
    cd "$1"
    name=$(date "+/tmp/ebooks/$1_%Y-%m-%d.epub")
    rm -f "$name"
    zip -q -r "$name" *
    cd ..
}

mkdir /tmp/ebooks
create_ebook dai_duong_song_long
create_ebook tam_tan_ky
