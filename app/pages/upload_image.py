from utils import load_model, upload_img, get_prediction


def upload_image(st, **state):    
    model = load_model()
    img = upload_img()
    if img is not None:
        st.image(img)
        get_prediction(model, img, from_uri=False)
