
# Mask/No-Mask

This code detects if the person is 
wearing a mask or not.










## How to Use

The dataset used along with the 
trained model is available in the 
repository. Press 'q' key to close 
the running python file. 


To detect mask run

```bash
  python mask.py
```
To use the pre-trained model run
```bash
from tensorflow.keras.models import load_model
model = load_model('mask_detection_model.h5')
```
## Run Locally

Clone the repository.

```bash
  git clone https://github.com/shubhharkawat1406/Mask-NoMask.git
```

Go to the project directory

```bash
  cd Mask-NoMask
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the code

```bash
  python mask.py
```



