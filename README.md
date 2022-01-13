# img_to_webp
With these two python scripts you can automatically update all your images to the next gen formats, with fallbacks to your old images. To serve images as the most optimized formats as possible.

# how to use 
```python

# clone the two scripts.
git clone https://github.com/beaupd/img_to_webp.git

# install pip packages from requirements.txt
pip install -r requirements.txt

# make sure to have libwebp installed, this is an example in anaconda:
conda install -c conda-forge libwebp

# edit path variable on line 28 to the destination of your images folder and run generate.py
python generate.py

# get the html code you want to replace the img tags in with the fallback stuff 
# in a file in the same directory as html_replace.py run and input file name
python html_replace.py

```
Enjoy :)
