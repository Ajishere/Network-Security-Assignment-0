import streamlit as st
# to check for UPPERCASE
def isupper(ch):
    if ch >= 'A' and ch <= 'Z':
        return True
    return False

# to check for LOWERCASE
def islower(ch):
    if ch >= 'a' and ch <= 'z':
        return True
    return False

# To print reciprocal string
def reciprocalString(word):
    ch = ''
    ct = ""
    for i in range(len(word)):

        # converting uppercase character
        # To reciprocal character
        # display the character
        if isupper(word[i]):
            ch = chr(ord('Z') -
                     ord(word[i]) + ord('A'))
            ct=ct+ch



        # converting lowercase character
        # To reciprocal character
        # display the character
        elif islower(word[i]):
            ch = chr(ord('z') -
                     ord(word[i]) + ord('a'))
            ct=ct+ch;
        else:
            ct=ct+word[i]

    return ct;


st.title('Network Security Assignment0 by Ajitesh Pandey')
in_txt = st.text_input('Text', placeholder="Enter text to encipher/decipher")
crypt_opt = st.radio(
    "Choose any one function to perform",
    ('Encipher', 'Decipher'))
if in_txt != "":
    if crypt_opt == "Encipher":
        st.write("Here is the encipher:")
        st.markdown('*' + reciprocalString(in_txt) + '*')
    else:
        st.write("Here is the decipher:")
        st.markdown('*' + reciprocalString(in_txt) + '*')