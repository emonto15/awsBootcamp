import boto3
import io
from PIL import Image
import base64



#def lambda_handler(event, context):
s3 = boto3.resource('s3')

filename='images6.jpg'

file = base64.b64encode(image_file.read())

rek = boto3.client('rekognition')
object = rek.detect_faces(
    Image={
        'S3Object': {
            'Bucket': 'eafit-team1-input',
            'Name': filename
        }
    },
    Attributes=[
        'ALL'
    ])
im = s3.Object('eafit-team1-input', filename).get()
source_img = Image.open(im.get('Body'))
for face in object.get('FaceDetails'):
    left = float(face.get('BoundingBox').get('Left'))
    top = float(face.get('BoundingBox').get('Top'))
    width = float(face.get('BoundingBox').get('Width'))
    height = float(face.get('BoundingBox').get('Height'))
    x1 = int(source_img.size[0] * left)
    y1 = int(source_img.size[1] * top)
    x2 = int(x1 + (source_img.size[0] * width))
    y2 = int(y1 + (source_img.size[1] * height))
    #emotion = max(face.get('Emotions'), key=lambda item: item['Confidence'])
    emotion = face.get('Emotions')[0]
    a = int(x2 - x1)
    b = int(y2 - y1)
    if emotion.get('Type') == 'HAPPY':
        emoji = Image.open('Assets/happy.png')
    elif emotion.get('Type') == 'SAD':
        emoji = Image.open('Assets/sad.png')
    elif emotion.get('Type') == 'ANGRY':
        emoji = Image.open('Assets/angry.png')
    elif emotion.get('Type') == 'CONFUSED':
        emoji = Image.open('Assets/confused.png')
    elif emotion.get('Type') == 'DISGUSTED':
        emoji = Image.open('Assets/disgusted.png')
    elif emotion.get('Type') == 'SURPRISED':
        emoji = Image.open('Assets/surprised.png')
    elif emotion.get('Type') == 'CALM':
        emoji = Image.open('Assets/calm.png')
    else:
        emoji = Image.open('Assets/unknown.png')

    emoji = emoji.resize((a, b))
    source_img.paste(emoji, (x1, y1), emoji)

    file = io.BytesIO()
    source_img.save(file, "JPEG")
    file.name = 'output1.png'
    file.seek(0)
s3.Object('eafit-team1-output', filename).upload_fileobj(file)
#return True
