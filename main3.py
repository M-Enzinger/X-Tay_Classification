import streamlit as st
import requests
import json

with st.expander("Chapter 1: Business Understanding"):
    st.write(" ")
    #Ilayda hier gerne informationen über lunkenkrankheiten einfügen was du so findest, paar infos, paar grafiken, paar hinweise wie man es an x-rays erkennt
with st.expander("Chapter 2: Data Preparation"):
    st.title("Chapter 2: Data Preparation")
    st.write("At first we reviewed our Data set and checked the relative balances between test, training and validation data. The given data set contained:")
    st.warning("training set: 5,216 files [89%] belonging to two classes, 1,341 to 'NORMAL' [26%] and 3,875 to 'PNEUMONIA' [74%]")
    st.warning("test set: 624 files [11%] belonging to two classes, 234 to 'NORMAL' [36%] and 390 to 'PNEUMONIA' [64%]")
    st.warning("validation set: 16 [<1%] files belonging to two classes, 8 to 'NORMAL' [50%] and 8 to 'PNEUMONIA' [50%]")
    st.write("As you can see we have some unbalances we have to deal with: First of all we moved around 5% of the training data to the test data. Because of the fact that we have a relatively small dataset in sum, we considered a 84%/16% ratio as appropriate.")
    st.write("Additionally we created some augmented picture of the class 'NORMAL' in the training set to get a 40%/60% ratio of both classes. We used vertical flip and up to 20% zoom range for the augmentation (we defined the output size as 1200x1200 even if we use a smaller one later, but downsizing is always easier than upsizing. Of course we will use augmentation in the model as well, but we would not solve the problem of a dominant class this way.")
    st.write("We didn´t touched the validation data set yet.")
    st.write("At the end, our data set looked like this:")
    st.success("training set: 6154 files [84%] belonging to two classes, 2400 to 'NORMAL' [39%] and 3,754 to 'PNEUMONIA' [61%]")
    st.success("test set: 1158 files [16%] belonging to two classes, 486 to 'NORMAL' [42%] and 672 to 'PNEUMONIA' [58%]")
    st.success("validation set: 16 [<1%] files belonging to two classes, 8 to 'NORMAL' [50%] and 8 to 'PNEUMONIA' [50%]")
    st.write("We used the following code:")
    st.image("chapter2_code1.PNG",
             caption="Data Generator Code",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("We also recognized some potential bias sources, like the sensors on many PNEUMONIA pictures. But we decided to check on potential biases later by visualizing a trained model and finding potential solutions, if needed, later. To deal with the different picture sizes, we standardize them in Chapter 3 under 'Data Generator And Augmentation' ")
with st.expander("Chapter 3: First CN-Network Including Augmentation"):
    st.title("Chapter 3: First CN-Network Including Augmentation")
    st.subheader("CNN Architecture")
    st.write("As out third step we build our first CNN using Tensorflow and Keras. On the following pictures you can study the code and settings we used at the end, after testing and validating dozens of variations (regarding amount of layers, augmentation settings, filter sizes, padding, pooling size, batch sizes and much more).")
    st.image("chapter3_arch1.PNG",
             caption="CNN Architecture",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter3_arch3.PNG",
             caption="CNN Architecture/ Summary",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter3_arch2.PNG",
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
    st.write("At first we used the tensorflow Data Generator, we have had to realize that the Generator causes big performance losses.")
    st.image("chapter3_firstdatagen.PNG",
             caption="1. Data Generator",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter3_firstdatagengraf.PNG",
             caption="1. Data Generator Graphic Card Monitor (Cuda Kernels)",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.write("As a better alternative we found the following way to implement data augmentation (which was very importent to us because of our relatively small amount of data).")
    st.image("chapter3_seconddatagen.PNG",
             caption="2. Data Augmentation",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter3_seconddatagengraf.PNG",
             caption="2. Data Augmentation Graphic Card Monitor (Cuda Kernels)",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")

with st.expander("Chapter 4: Validation, Visualisation And Bias Verification Of Our First CNN"):
    st.title("Chapter 4: Validation, Visualisation And Bias Verification Of Our First CNN")
    st.subheader("Validation - Understanding The Metrics")
    st.write("Before measuring values like the accuracy or sensitivity we have to understand them - a brief summary:")
    st.image("chapter4_accsensspec.PNG",
             caption="Accuracy, Sensitivity, Specificity; Source: https://lexjansen.com/nesug/nesug10/hl/hl07.pdf, Page 1",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.info("Sensitivity: The sensitivity shows the performance of detecting PNEUMONIA if someone does really have PNEUMONIA. In Other words: The sensitivity contribute to the rate of True Positive/ False negativ detections. In reference to the Picture above: TP/(TP + FN)")
    st.info("Specificity: The specificity shows the performance of detecting a NORMAL lung if someone is really healthy. In Other words: The specificity contribute to the rate of false Positive/ true negativ detections. In reference to the Picture above: TN/(TN + FP)")
    st.info("Accuracy: The accuracy shows the overall and combined performance of the model trough all classes. In reference to the Picture above:  (TN + TP)/(TN+TP+FN+FP)")
    st.subheader("Validation - Measuring")
    st.write("At first we only measured the Accuracy. But we recognized that the validation accuracy can be very misleading. An example: If your model has a specificity of nearly 100% and a sensitivity of 40%, the accuracy could still be around 80%, even if the model only detects 40% of all PNEUMONIA lungs as not healthy.")
    st.write("We implemented the sensitivity and specificity the following way, including an automated stop with the best weights (training until 30th epoch and recover best weights:")
    st.image("chapter4_accsensspecimpl.PNG",
             caption="Accuracy, Sensitivity, Specificity implementation",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.subheader("Validation - Plotting the Metrics")
    st.write("To get a better overview we plotted the accuracy and validation accuracy as well as loss and validation loss. Especially for overfitting detection.")
    st.image("chapter4_grafacc.PNG",
             caption="Graph Accuracy",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter4_grafloss.PNG",
             caption="Graph Loss",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.subheader("Validation - Visualisation!")
    st.write("To visualize our classification we first tried to use a function provided by the xception pre trained model, after that we created and trained a completely new pytorch model to visualize our classification but in the end we managed it to visuakize it in our original Keras model,")
    st.write("Here should be pictures of our visualisation, but as you can see, you can see nothing")
    st.write("That´s because we had some struggle implementing visualisation into a Keras model, so we followed the advice to build a pre-Trained, transfer learned and fine tuned pytorch model and to visualize this one")
    st.write("That´s why you will find the last two chapters (3 and 4) repeating in chapter 5 and 6, just with our new pytorch model...")
    st.subheader("Our Overall Performance Of The First CNN")
    st.success("Validation Accuracy: 87%")
    st.success("Validation Sensitivity: 83%")
    st.success("Validation Specificity: 90%")

with st.expander("Chapter 5: Second CN-Network Including Augmentation, Transfer Learning And Fine-Tuning"):
    st.title("Chapter 3: First CN-Network Including Augmentation")
    st.error("In progress, added BEFORE second deadline. First model working and testable")
    st.subheader("CNN Architecture")
    st.write("Because of reasons we already described in chapter 4, we build this second CNN with pytorch. On the following pictures you can study the code and settings we used at the end, after testing and validating dozens of variations (regarding amount of layers, augmentation settings, filter sizes, padding, pooling size, batch sizes and much more).")
    st.write("PICTURE OF OUR FINAL pytorch CNN, the architecture, summary, compile and fit part")

with st.expander("Chapter 6: Validation, Visualisation And Bias Verification Of Second CNN"):
    st.title("Chapter 4: Validation, Visualisation And Bias Verification Of Our Second CNN")
    st.error("In progress, added BEFORE second deadline. First model working and testable")

with st.expander("Chapter 7: Performance, System and CO2 Emission"):
    st.title("Chapter 5: Performance, System and CO2 Emission")
    st.subheader("Operating System")
    st.info("CPU: AMD RYZON 7 1700x; Threads: 16; Cores: 8; CPU Clock: 3.8 mhz")
    st.info("GPU: GeForce GTX 1080; Cores: 2560; Memory Size: 8GB; Memory Type: GDDR5X")
    st.info("RAM: 15GB; DDR4")
    st.subheader("Performance and Resources Monitoring")
    st.write("All Screenshots were captured while training our latest model")
    st.image("chapter5_ram.PNG",
             caption="RAM Usage",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter5_gpu.PNG",
             caption="GPU And GPU Memory Usage; Most Important: Cuda Load",
             width=None, use_column_width=None, clamp=False, channels="RGB", output_format="auto")
    st.image("chapter5_temp.PNG",
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
with st.expander("Chapter 8: Interactive Online Test of both CNNs"):
    st.title("Chapter 8: Interactive Online Test Of Our First (Keras) And Second (Pytorch) Model")
    st.subheader("Online Test Of Our First Model:")
    st.subheader("Online Test Of Our Second Model:")
    st.success("Will be added BEFORE second deadline.")
with st.expander("Chapter 9: Conclusion"):
    st.title("Chapter 9: Conclusion")