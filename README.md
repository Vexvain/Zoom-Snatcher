![Zoom Snatcher](https://i.ibb.co/KGNfQc2/image.png)

-----------------------------------------------------------
Finds all the zoom codes you could ever want :)

# Info
This tool searches for Zoom codes/URLs posted by users on Twitter. It filters possible results

## Preview
![](https://i.ibb.co/DW9DTDX/image.png)<br/>
![](https://i.ibb.co/H7mgTD0/image-2020-11-05-170534.png)

## Usage
- Python 3.8 or above
- If you do not already have the **requests** library installed, run setup.py — make sure PIP is added to PATH.

1. Launch any HTTP debugger — built-in browser debuggers work
2. Head over to the [Network tab](https://i.imgur.com/UAzJL0R.png).
3. Visit [this URL](https://twitter.com/search?q=zoom%20code&src=typed_query&f=live) — in the same tab.
4. Click on [this request](https://i.imgur.com/Pxc4gGh.png) for further details.
5. Under the "Request Headers" tab, copy the [authorization header's value](https://i.imgur.com/38aPHHV.png). Replace **BEARER TOKEN** with **the authorization header** in Config.json.
6. Below the authorization header, copy the [cookie's value](https://i.imgur.com/OphifTK.png). Replace **COOKIE** with **the cookie header** in Config.json. Take notice how the cookie includes 2 double quotation marks. Put a backslash before personalization_id's double quotation marks like this: ```personalization_id=\"...\";```
7. Save Config.json
8. Run main.py
