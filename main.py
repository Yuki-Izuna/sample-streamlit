import streamlit as st
import requests
import io
from PIL import Image
from PIL import ImageDraw

st.title('顔認識アプリ')

SUBSCRIPTION_KEY = "e6e64117fbf24c47a89ecc2a6eec1835"
assert SUBSCRIPTION_KEY
face_api_url = 'https://20210207-izuna.cognitiveservices.azure.com/face/v1.0/detect'

upload_file = st.file_uploader("Choose an image...", type='jpg')
if upload_file is not None:
    img = Image.open(upload_file)

    with io.BytesIO() as output:
        img.save(output, format="JPEG")
        binary_img = output.getvalue() # バイナリ取得

    # with open('unnamed.jpg', 'rb') as f:
    #     binary_img = f.read()
    
    
    headers = {
        'Content-Type': 'application/octet-stream',
        'Ocp-Apim-Subscription-Key': SUBSCRIPTION_KEY
    }

    params = {
        'returnFaceId': 'true',
        'returnFaceAttributes': 'age'
    }

    res = requests.post(face_api_url, params=params,
                            headers=headers, data=binary_img)

    results = res.json()

    for result in results:
        rect = result['faceRectangle']

        draw = ImageDraw.Draw(img)
        draw.rectangle([(rect['left'], rect['top']), (rect['left'] + rect['width'], rect['top'] + rect['height'])], fill=None, outline='green', width=5)
    
    st.image(img, caption='Uploaded Image.', use_column_width=True)



# st.write('データフレーム')
# st.write(
#     pd.DataFrame({
#         '1st column': [1, 2, 3, 4],
#         '2nd column': [10, 20, 30, 40]
#     })
# )

# """

# # My 1st App
# ## マジックコマンド
# こんな感じでマジックコマンドを使用できる、MagicCommand対応

# """

# if st.checkbox('Show DataFarme'):
#     chart_df = pd.DataFrame(
#         np.random.randn(20, 3),
#         columns = ['a', 'b', 'c']
#     )
#     st.line_chart(chart_df)


