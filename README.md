This repo classifies the input butterfly image among the 10 classes of butterfly. The model is created using [teachable machine](https://teachablemachine.withgoogle.com/train/image)

Dataset Used for training model: [Leeds Butterfly Dataset](http://www.josiahwang.com/dataset/leedsbutterfly/)

Input: `Image or image path`

Output: `predicted label and prediction probability`
```
Labels:
     Danaus plexippus	
     Heliconius charitonius	
     Heliconius erato	
     Junonia coenia	
     Lycaena phlaeas
     Nymphalis antiopa	
     Papilio cresphontes	
     Pieris rapae	
     Vanessa atalanta	
     Vanessa cardui
``` 
To Run:
1. Install tensorflow servering
```
$ sudo apt-get update
$ sudo apt-get install tensorflow-model-server
$ tensorflow_model_server --version
TensorFlow ModelServer: 2.2.0-rc2+dev.sha.d22fc19
TensorFlow Library: 2.2.0
```
2. Starting tensorflow servering server
```
$ tensorflow_model_server --model_base_path=path_to_model/model/ (or absolute path for the model) --rest_api_port=9000 --model_name=butterfly_classify(or name of your serving server)
```
3. Start flask server
```
python app/app.py
```
4. Use postman/insomnia's post request, input image as filetype and get the prediction
```
http://127.0.0.1:5000/predict/butterfly/
```
OR

Upload the image file and click `predict` button at `http://127.0.0.1:5000/`
![img](https://github.com/pinksi/butterfly_classification/blob/master/readme_img.jpg)