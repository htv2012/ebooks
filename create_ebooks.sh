#!/usr/bin/env bash

create_ebook() {
    cd "$1"
    name=$(date "+/tmp/ebooks/$1_%Y-%m-%d.epub")
    rm -f "$name"
    zip -q -r "$name" *
    cd ..
}

rm -fr /tmp/ebooks/*
mkdir -p /tmp/ebooks
cd src
for d in *
do
    create_ebook "$d"
done

