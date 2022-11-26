if [ -d generated-images ]; then
    rm -r generated-images
fi
mkdir generated-images

touch ./figma_htmlgenerator/temp.html

python3 html-to-png.py