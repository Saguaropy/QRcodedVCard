import streamlit as st
from segno import helpers

import base64
from io import StringIO
import matplotlib.pyplot as plt
import numpy as np

# st_JY_qrCodeGenVCard0.py - Ver0 (7/27/2023)
# C:\Users\email\OneDrive\DesktopSP7\JY_pyTools\QRcodeGeneratorVCard\st_JY_qrCodeGenVCard0.py
# (1) Generate a QR code in a vCard format per input of contact information
# Therefore, when the QR code is read by a mobile phone camera, the contact info from the QR code
# can be saved into the contact list on the phone.
# https://segno.readthedocs.io/en/latest/contact-information.html

# - Display a svg file in streamlit app
# https://discuss.streamlit.io/t/display-svg/172/4

CODE_TITLE='st_JY_qrCodedVCard0.py'

# # INPUT CONSTANTS
name_input='John Yoon'
# name_input='Jennie Yoon'
displayname_input='John Yoon, Ph.D.'
# displayname_input='Jennie Yoon'
email_input='drjyoon@gmail.com'
city_input='Tucson'
region_input='Arizona'
org_input='Rayem'
title_input='Founder/President'
cellphone_input='520-481-3439'
# cellphone_input='520-730-4695'
url_input='www.rayem.com'

vcard_img='my-vcard.svg'
vcard_img_color='my-vcard_color.svg'


def render_svg(svg):
    """Renders the given svg string."""
    b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
    html = r'<img src="data:image/svg+xml;base64,%s"/>' % b64
    st.write(html, unsafe_allow_html=True)
# ########################## END OF render_svg() #############################

def display_svg(vcard_img_svg):
    f=open(vcard_img_svg,'r')
    lines=f.readlines()
    line_string="".join(lines)
    return line_string
# ########################## END OF display_svg() #############################


if __name__ == "__main__":
    st.title(CODE_TITLE)
    st.caption('Ver0')
    qrcode=helpers.make_vcard(name=name_input,
                            displayname=displayname_input,
                            email=email_input,
                            city=city_input,
                            region=region_input,
                            org=org_input,
                            title=title_input,
                            cellphone=cellphone_input
                            )
    # qrcode.designator

    # # Some params accept multiple values, like email, phone, url
    # qrcode = helpers.make_vcard(name='Doe;John', displayname='John Doe',
    #                             email=('me@example.org', 'another@example.org'),
    #                             url=['http://www.example.org', 'https://example.org/~joe'])

    qrcode.save(vcard_img, scale=4)
    qrcode.save(vcard_img_color, scale=4, 
                # dark='navy',
                dark=(8,90,117),
                # data_dark='darkorange',
                # data_light='yellow',
                )
    # qrcode.save(vcard_img_color, dark=(8,90,117))
    # st.image(vcard_img)  # Not working;

    st.markdown("""___""")
    # st.markdown("""<hr style="height:10px;border:none;color:#333;background-color:#333;" /> """, unsafe_allow_html=True)  # Alternative method;
    # # https://discuss.streamlit.io/t/horizontal-separator-line/11788/5
    st.markdown('')
    st.subheader(displayname_input)

    # # Display the generated URL code
    # Code by Rkubinski (12/10/2019)
    # https://gist.github.com/treuille/8b9cbfec270f7cda44c5fc398361b3b1
    line_string=display_svg(vcard_img)
    render_svg(line_string)

    # # Display the colorful QR Code
    # st.markdown("""___""")
    st.markdown('')
    st.markdown('')
    st.markdown('')
    st.markdown('')
    # https://segno.readthedocs.io/en/latest/serializers.html
    st.subheader(displayname_input)
    line_string_color=display_svg(vcard_img_color)
    render_svg(line_string_color)

    for i in range(10):
        st.markdown('')
  
# ############################ END OF MAIN ###############################