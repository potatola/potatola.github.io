#!/bin/bash
#program to create a template for an article

read -p "category of the article:" category
read -p "file name of the new article(end with .md):" name

if [ -f  "content/$category/$name" ]; then
	echo "file exists!"
	exit 1;
fi

if [ ! -d "content/$category" ]; then
	echo "dir doesn't exist!"
	mkdir content/$category
fi

read -p "title:" title
read -p "tags:(tag1[,tags]):" tags
echo "Title: $title 
Date: "`date +'%F %T'`"
Category: $category
Tags: $tags
Slug: ${name%.md}" > "content/$category/$name"

