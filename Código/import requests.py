import requests
def download_img (img_url, img_name) :
    req = requests.get (img_url)
    req.headers ['User-Agent']= 'Mozilla/5.0'
    response = req.content
    
    with open (img_name, "wb") as f:
        f.write (response)

download_img("https://www.google.com/imgres?imgurl=https%3A%2F%2Fm.media-amazon.com%2Fimages%2FI%2F51fqAeNbHhL.jpg&imgrefurl=https%3A%2F%2Fwww.amazon.com%2FPublicar-libro-Amazon-pr%25C3%25A1ctico-promocionarlo-ebook%2Fdp%2FB017J4HXQS&tbnid=HkE2ay2D3mDayM&vet=12ahUKEwiW2_bngenzAhUBDd8KHb_IDsIQMygBegUIARC7AQ..i&docid=imlqN0DRB_GmfM&w=333&h=500&q=amazon%20libros&ved=2ahUKEwiW2_bngenzAhUBDd8KHb_IDsIQMygBegUIARC7AQ", "amazon.jpg")