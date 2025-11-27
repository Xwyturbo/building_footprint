**Import the fishnet data into Bigemap and download the imagery.**
Open the Bigemap software, click on Import Boundary, and in the dialog box that appears, select the fishnet data you just exported under Open File. Click Open, check all the target areas, and then click OK. 
 ![01](https://github.com/Xwyturbo/building_footprint/blob/main/pics/01.png) 
The result is as shown in the figure. The remote sensing imagery of the target area is now covered by the fishnet. Double-click to download the remote sensing imagery of the target area in tiles. In the dialog box that appears, choose an appropriate save path, keep the other settings as default, and check Level 18 under the level options. Click OK to start the download (the data volume is large, so the download process may be slow).
 ![02](https://github.com/Xwyturbo/building_footprint/blob/main/pics/02.png)
**Rural building footprint extraction by AI Earth**
You can use code (`deeplearning-main\step01_building_footprint_extraction.py`), or use the following no-code operation. Open the AI Earth official website and register on the platform. The following is the process of extracting buildings from a piece of remote sensing imagery:
Click to enter the platform → Processing and Analysis → AI Interpretation Tools → Building Extraction → Import Data → Upload Data Independently → Upload Data. Keep the upload method and data format as default.
  ![03](https://github.com/Xwyturbo/building_footprint/blob/main/pics/03.png)
Click on the Imagery File section, upload the remotely sensed imagery of the target area that was just downloaded in tiles, and click Open. Wait for the upload to complete.
 ![04](https://github.com/Xwyturbo/building_footprint/blob/main/pics/04.png)
After the upload is complete, click Publish. Once the publishing is finished, check the corresponding remote sensing image and select Import to Current Project.
On the right side of the page, under Data to Be Analyzed, select the remote sensing imagery, set the confidence level to High, assign a suitable name for the results, and keep other settings as default. Click Process and Analyze.
 ![05](https://github.com/Xwyturbo/building_footprint/blob/main/pics/05.png)
After the processing is complete, click the download icon on the right to download the extracted building footprint imagery from the remote sensing data.
 ![06](https://github.com/Xwyturbo/building_footprint/blob/main/pics/06.png)
 ![07](https://github.com/Xwyturbo/building_footprint/blob/main/pics/07.png)
**Merging Building Data**
First, extract all the downloaded building data and place it in the same folder. Then, copy the file path of this data. Use the following code to merge the building data (`deeplearning-main\step02_building_footprint_merge.py`). The highlighted parts need to be modified: the first highlighted part requires pasting the copied path of the downloaded building data, while also changing the backslashes "" to forward slashes "/"; the second highlighted part requires changing the name of the saved file.
 ![08](https://github.com/Xwyturbo/building_footprint/blob/main/pics/08.png)
 ![09](https://github.com/Xwyturbo/building_footprint/blob/main/pics/09.png)

