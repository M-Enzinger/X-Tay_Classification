import streamlit as st
import requests
import json
import matplotlib.pyplot as plt
import numpy as np
import torch
from torchvision import datasets, models, transforms
import os
import torch.nn as nn
from PIL import Image
import pytorch_grad_cam

with st.expander("Chapter 1: Business Understanding"):
    st.title("Chapter 1: Business Understanding")
    st.write("Lung disease is one of the most common forms of illness and can come in a variety of forms. Common chronic diseases are, for example, chronic obstructive pulmonary disease (COPD), or asthma. An acute lung disease, from which 15,287 people died in Germany in 2020, is pneumonia [1]. Common symptoms besides fever are chest pain when coughing and rapid breathing [2]. ")
    st.write("How can pneumonia be diagnosed?")
    st.write("In addition to checking the levels of inflammation in the blood, X-rays are an important tool for diagnosis. When the disease is present, white spots stand out in the affected areas of the lungs [2].")
    st.write("[1]: https://de.statista.com/statistik/daten/studie/1042795/umfrage/todesfaelle-aufgrund-der-haeufigsten-diagnosen-von-krankheiten-des-atmungssystems/, [2]: https://www.navigator-medizin.de/krankheiten/lungenentzuendung/behandlung-und-prognose.html?9-sieht-man-eine-lungenentz%c3%bcndung-immer-im-r%c3%b6ntgenbild.html#:~:text=Im%20Blut%20zeigen%20sich%20erh%C3%B6hte%20Entz%C3%BCndungswerte%20von%20CRP,schwarz%20erscheint.%20Neben%20typischen%20gibt%20es%20atypische%20Lungenentz%C3%BCndungen.")

    
with st.expander("Chapter 2: Data Preparation"):
    st.title("Chapter 2: Data Preparation")
    st.write("At first we reviewed our data set and checked the relative balances between test, training and validation data. The given data set contained:")
    st.warning("training set: 5,216 files [89%] belonging to two classes, 1,341 to 'NORMAL' [26%] and 3,875 to 'PNEUMONIA' [74%]")
    st.warning("test set: 624 files [11%] belonging to two classes, 234 to 'NORMAL' [36%] and 390 to 'PNEUMONIA' [64%]")
    st.warning("validation set: 16 [<1%] files belonging to two classes, 8 to 'NORMAL' [50%] and 8 to 'PNEUMONIA' [50%]")
    st.write("As you can see we had some uneven distribution we had to deal with: First of all we moved around 5% of the training data to the test data. Because of the fact that we have a relatively small dataset in sum, we considered a 84%/16% ratio as appropriate.")
    st.write("Additionally we created some augmented pictures of the class 'NORMAL' in the training set to get a 40%/60% ratio of both classes. We used vertical flip and up to 20% zoom range for the augmentation (we defined the output size as 1200x1200 even if we use a smaller one later, but downsizing is always easier than upsizing) Of course we will use augmentation in the model as well, but we would not solve the problem of a dominant class this way.")
    st.write("We hadn´t touched the validation data set yet.")
    st.write("At the end, our data set looked like this:")
    st.success("training set: 6154 files [84%] belonging to two classes, 2400 to 'NORMAL' [39%] and 3,754 to 'PNEUMONIA' [61%]")
    st.success("test set: 1158 files [16%] belonging to two classes, 486 to 'NORMAL' [42%] and 672 to 'PNEUMONIA' [58%]")
    st.success("validation set: 16 [<1%] files belonging to two classes, 8 to 'NORMAL' [50%] and 8 to 'PNEUMONIA' [50%]")
    st.write("We used the following code:")
    st.image("img/chapter2_code1.png",
             caption="Data Generator Code",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("We also recognized some potential bias sources, like the sensors on many PNEUMONIA pictures. But we decided to check on potential biases later by visualizing a trained model and finding potential solutions, if needed, later. To deal with the different picture sizes, we standardized them in Chapter 3 under 'Data Generator And Augmentation' ")

    
with st.expander("Chapter 3: First CN-Network Including Augmentation"):
    st.title("Chapter 3: First CN-Network Including Augmentation")
    st.subheader("CNN Architecture")
    st.write("As our third step we built our first CNN using Tensorflow and Keras. On the following pictures you can study the code and settings we used at the end, after testing and validating dozens of variations (regarding amount of layers, augmentation settings, filter sizes, padding, pooling size, batch sizes and much more).")
    st.image("img/chapter3_arch1.png",
             caption="CNN Architecture",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter3_arch3.png",
             caption="CNN Architecture/ Summary",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter3_arch2.png",
             caption="CNN Architecture/ Fit-Part",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("Summary of the key values:")
    st.info("Total Params: 92.165.473")
    st.info("Amount of convolutional layers: 2")
    st.info("Amount of layers and neurons of the fully connected network: 1. -> 128, 2. -> 1")
    st.info("Filter size: 3x3")
    st.info("Padding: Same")
    st.info("Batch size: 32")
    st.info("Img-size: 600x600")
    st.info("Amount of Kernels: 16, 32")
    st.info("Amount of epochs: 6, until earlystopping")
    st.info("Steps per epoch: whole dataset")
    st.info("Optimizer: adam")
    st.subheader("Data Generator And Augmentation")
    st.write("At first, we used the tensorflow Data Generator, but unfortunately had to learn that the Generator causes big performance losses.")
    st.image("img/chapter3_firstdatagen.png",
             caption="1. Data Generator",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter3_firstdatagengraf.png",
             caption="1. Data Generator Graphics Card Monitor (Cuda Kernels)",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("As a better alternative we found the following way to implement data augmentation (which was very important to us because of our relatively small amount of data).")
    st.image("img/chapter3_seconddatagen.png",
             caption="2. Data Augmentation",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter3_seconddatagengraf.png",
             caption="2. Data Augmentation Graphic Card Monitor (Cuda Kernels)",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

    
with st.expander("Chapter 4: Validation, Visualization And Bias Verification Of Our First CNN"):
    st.title("Chapter 4: Validation, Visualization And Bias Verification Of Our First CNN")
    st.subheader("Validation - Understanding The Metrics")
    st.write("Before measuring values like the accuracy or sensitivity we have to understand them - a brief summary:")
    st.image("img/chapter4_accsensspec.png",
             caption="Accuracy, Sensitivity, Specificity; Source: https://lexjansen.com/nesug/nesug10/hl/hl07.pdf, Page 1",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.info("Sensitivity: The sensitivity shows the performance of detecting PNEUMONIA if someone does really have PNEUMONIA. In Other words: The sensitivity contribute to the rate of True Positive/ False negativ detections. In reference to the Picture above: TP/(TP + FN)")
    st.info("Specificity: The specificity shows the performance of detecting a NORMAL lung if someone is really healthy. In Other words: The specificity contribute to the rate of false Positive/ true negativ detections. In reference to the Picture above: TN/(TN + FP)")
    st.info("Accuracy: The accuracy shows the overall and combined performance of the model trough all classes. In reference to the Picture above:  (TN + TP)/(TN+TP+FN+FP)")
    st.subheader("Validation - Measuring")
    st.write("At first we only measured the accuracy. But we eventually found out that the validation accuracy can be very misleading. An example: If your model has a specificity of nearly 100% and a sensitivity of 40%, the accuracy could still be around 80%, even if the model only detects 40% of all PNEUMONIA lungs as not healthy.")
    st.write("We implemented the sensitivity and specificity the following way, including an automated stop with the best weights (training until 30th epoch and recover best weights:")
    st.image("img/chapter4_accsensspecimpl.png",
             caption="Accuracy, Sensitivity, Specificity implementation",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.subheader("Validation - Plotting the Metrics")
    st.write("To get a better overview we plotted the accuracy and validation accuracy as well as loss and validation loss. Especially for overfitting detection.")
    st.image("img/chapter4_grafacc.png",
             caption="Graph Accuracy",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter4_grafloss.png",
             caption="Graph Loss",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter4_graf2.png",
             caption="Early Stopping",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.subheader("Validation - Visualization!")
    st.write("To visualize our classifications we first tried to use a function provided by the xception pretrained model, after that we created and trained a completely new pre-trained pytorch model to visualize our classification.")
    st.write("Here should be the pictures of our visualization, but as you can see, you see nothing")
    st.write("That´s because we had some struggle implementing visualization into a Keras model, so we followed the advice to build a pytorch model and to visualize this one.")
    st.write("For that reason, you will find the last two chapters (3 and 4) repeating in chapter 5 and 6, just with our new pytorch model...")
    st.subheader("Our Overall Performance Of The First CNN")
    st.success("Validation Accuracy: 87%")
    st.success("Validation Sensitivity: 83%")
    st.success("Validation Specificity: 90%")

    
with st.expander("Chapter 5: Second CN-Network Including Augmentation"):
    st.title("Chapter 5: Second CN-Network Including Augmentation, Transfer Learning And Fine-Tuning")
    st.write("Because of reasons we already described in chapter 4, we build this second CNN with pytorch as a pre-trained Resnet-18 model. On the following pictures you can study the code and settings we used at the end, after testing and validating dozens of variations (regarding amount of layers, augmentation settings, filter sizes, padding, pooling size, batch sizes and much more).")
    st.subheader("CNN Architecture")
    st.write("Using PyTorch, we implemented a pretrained model. This had two main advantages for us: The model had already been trained (okay,  that one should have been obvious...).")
    st.write("The second advantage was that we did not have to think of a model architecture, as the models layers are already defined. Thus, we just had to define a few final parameters like the output sample size and the optimizer function (see image below) and the model was ready to be retrained using our X-Ray Images.")
    st.image("img/chapter5-ModelParameters.png",
        caption="Here we imported the pretrained ResNet18 model and set the according parameters. We chose 25 epochs because we observed the best results around that range. We even tried 1000 for fun, but the results were hardly better.",
        width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("For detailed documentation about the ResNet18 model architecture check: https://arxiv.org/pdf/1512.03385.pdf")
    st.subheader("Augmentation")
    st.image("img/chapter5-DataPreparation.png",
         caption="Basic augmentation vor train dataset like cropping with a random center point or a partial horizontal turn.",
         width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("Data augmentation is usually only applied to the training set, as the test set is only used for validation and the augmentation would have no effect.")
   

with st.expander("Chapter 6: Validation, Visualization And Bias Verification Of Second CNN"):
    st.title("Chapter 6: Validation, Visualization And Bias Verification Of Second CNN")
    st.subheader("Visualization")
    st.write("After a long trial and error process, we got our heatmap visualization to work properly using GradCAM. Here you will find the code we used and some example images we were able to produce and analyse.")
    st.image("img/chapter6-gradcamCode.png",
         caption="Our GradCAM implementation",
         width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.subheader("Resuts And Interpretation Of The Visualization")
    st.write("GradCam results of pneumonia lung WITHOUT sensors:")
    st.image("GradCam-Images/AUGSMOOTHperson1951_bacteria_4882.jpeg",
             caption="Pneumonia Without Sensors",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("GradCam-Images/AUGSMOOTHperson16_virus_47.jpeg",
             caption="Pneumonia Without Sensors",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("GradCam results of pneumonia lungs WITH sensors:")
    st.image("GradCam-Images/AUGSMOOTHperson30_virus_69.jpeg",
             caption="Pneumonia With Sensors",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("As you can see on the pictures above, the sensors are not highly marked and, in consequence, not effectively considered in the decision progress. At this point we excluded the sensors as a possible bias source.")
    st.subheader("Our Overall Performance Of The Second CNN")
    st.success("Validation Accuracy: 95.299%")
    st.success("Validation Sensitivity: 98.718%")
    st.success("Validation Specificity: 91.880%")
                    

with st.expander("Chapter 7: Performance, System and CO2 Emission"):
    st.title("Chapter 7: Performance, System and CO2 Emission")
    st.subheader("Operating System")
    st.info("CPU: AMD RYZON 7 1700x; Threads: 16; Cores: 8; CPU Clock: 3.8 mhz")
    st.info("GPU: GeForce GTX 1080; Cores: 2560; Memory Size: 8GB; Memory Type: GDDR5X")
    st.info("RAM: 15GB; DDR4")
    st.subheader("Performance and Resources Monitoring")
    st.write("All Screenshots were captured while training our latest model")
    st.image("img/chapter5_ram.png",
             caption="RAM Usage",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter5_gpu.png",
             caption="GPU And GPU Memory Usage; Most Important: Cuda Load",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("img/chapter5_temp.png",
             caption="CPU And Mainboard Temperature; Cooling System: Water-cooling",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.success("Training Time (per 10 epochs): 32 min.")
    st.success("Time per Step: 400-650 ms/step.")
    st.subheader("CO2 Emission")
    st.write("To measure the amount of CO2 emission due to training a model, we first measured the consumption of the PC")
    st.warning("Energy Consumption: < 450W")
    st.write("Taking into account the time for training and the german energy mix...")
    st.error("CO2 Emission Per kWh (german energy mix): 420g CO2")
    st.error("CO2 Emission Per training (10epochs): 420g*(32/60)*0.45 = 100,8g CO2")
    st.error("CO2 Emission Per Model Development (50-100x training 10epochs each): 5.040kg-10.080kg CO2")
    st.warning("This Amount equals a 80 to 100 km car ride")
    
    
with st.expander("Chapter 8: Interaktive Prediction With Our PyTorch Model"):
    st.title("Chapter 8: Interaktive Prediction With Our PyTorch Model")
    st.subheader("Upload An Image To Classify And Click The 'Predict' Button (Below The Appearing Uploaded Picture)")
    @st.cache
    def load_image(image_file):
        img = Image.open(image_file)
        return img

    image_file = st.file_uploader("Upload An Image To Classify, to classify an additional picture, just upload a new one and the one before will be replaced.")
    if image_file is not None:
        file_details = {"FileName":image_file.name,"FileType":image_file.type}
        st.write(file_details)
        img = load_image(image_file)
        st.image(img)
        with open(os.path.join("tempDir/test/NORMAL/",image_file.name),"wb") as f: 
          f.write(image_file.getbuffer())
        with open(os.path.join("tempDir/test/PNEUMONIA/",image_file.name),"wb") as f: 
          f.write(image_file.getbuffer()) 
        st.success("Saved File")

    col1, col2, col3, col4, col5 = st.columns(5)
    with col3:
        startButton = st.button("Predict")


    if (startButton):
        os.environ["KMP_DUPLICATE_LIB_OK"] = "True"
        device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")


        # In[2]:


        # Data augmentation and normalization for training
        # Just normalization for validation
        data_transforms = {
            'train': transforms.Compose([
                transforms.RandomResizedCrop(224),
                transforms.RandomHorizontalFlip(),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
            'test': transforms.Compose([
                transforms.Resize(256),
                transforms.CenterCrop(224),
                transforms.ToTensor(),
                transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
            ]),
        }

        # Directory of 'train' and 'test' folders
        data_dir = 'tempDir/'

        # Retrieving the images by folder
        image_datasets = {x: datasets.ImageFolder(os.path.join(data_dir, x),
                                                  data_transforms[x])
                          for x in ['test']}

        dataloaders = {x: torch.utils.data.DataLoader(image_datasets[x], batch_size=4,
                                                     shuffle=True, num_workers=4)
                      for x in ['test']}
        class_names = image_datasets['test'].classes


        # In[3]:


        #model = models.resnet18()
        model = torch.load("models/FULLRetrainedResNetModel.pt", map_location=torch.device('cpu'))
        num_ftrs = model.fc.in_features

        # Here the size of each output sample is set to 2.
        model.fc = nn.Linear(num_ftrs, 2)

        #model.load_state_dict(torch.load("models/FULLRetrainedResNetModel.pt", map_location=torch.device('cpu')))

        model = model.to(device)


        # In[4]:


        number_of_predictions = 1

        with torch.no_grad():
            model.eval()
            for data in dataloaders['test']:
                images, labels = data

                plt.imshow(np.squeeze(images[0][0:1]), cmap='gray')

                images = images.to(device)
                labels = labels.to(device)

                pred_outputs = model(images)
                predicted = torch.argmax(pred_outputs.data, 1)

        #print('True Value: ', ' '.join('%s' % class_names[predicted[j]] for j in range(number_of_predictions)))
        print('Predicted: ', ' '.join('%s' % class_names[predicted[0]] for j in range(number_of_predictions)))
        st.warning(class_names[predicted[0]])

        st.write("Visualization of the classified picture will be added before second deadline.")

        # In[ ]:
    
with st.expander("Chapter 9: Conclusion"):
    st.title("Chapter 9: Conclusion")
    st.write("Part of the fine tuning process, will be added before second deadline. All the others chapters will also be fullfilled before second deadline. The process description and anything in chapter 1 to 9 is not final yet, but gives a good overfiew. The working and interaktive model is under Chapter 8. Visual effects (like different colors if pneumonia/healthy) etc. will be added as well. We are also going to clean the code before the second deadline")
    st.write("All original code files are available in our GitHub repository: https://github.com/M-Enzinger/X-Ray_Classification.git")
