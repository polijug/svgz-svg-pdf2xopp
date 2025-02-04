# SVGZ / SVG / PDF to XOPP
## svgz2xopp:
This script converts all .svgz files in given folder (and subfolders) to .xopp. 
### Dependences
- gunzip (on linux should be default)
- inkscape
- pdf2xopp.py file from this repository
- pdf2image module (can by obtained from pip - `pip install pdf2image`)

### Usage
`pythom3 svgz2xopp.py /path/to/dir`

## svg2xopp:
This script converts all .svg files in given folder (and subfolders) to .xopp. 
### Dependences
- inkscape
- pdf2xopp.py file from this repository
- pdf2image module (can by obtained from pip - `pip install pdf2image`)

### Usage
`pythom3 svg2xopp.py /path/to/dir`

## pdf2xopp:
This script converts **one** .pdf file to .xopp. Here is mainly as library for other scripts.
### Dependence
- pdf2image module (can by obtained from pip - `pip install pdf2image`)

### Usage
`pythom3 pdf2xopp.py output-file.xopp input-file.pdf`
