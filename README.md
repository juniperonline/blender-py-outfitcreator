
# Full-body Outfit Creator Add-on

<img width="400" alt="Capture" src="https://user-images.githubusercontent.com/46087451/197553643-e7637a82-9e50-48d5-8603-38d09e335c26.PNG" >

### TO DO: 

- [ ] JSON File import
- [ ] Refactor nested loops 

### Overview 

Using this tool, you can preview and pick your favourite combinations of three-part outfits inside Blender. Afterwards, a model will be exported in the format of your choice.

### Naming the outfit 

![Name_Gif](https://user-images.githubusercontent.com/46087451/197572177-dc47b2e8-df50-492b-a5cc-f7b102d70fbb.gif)

To name your outfit, write your desired text in the first input cell.

### Picking the combination

![Picking_Pieces](https://user-images.githubusercontent.com/46087451/197572202-95468d4b-010c-46ee-a97d-25bb4084d65c.gif)

In the drop-down menus named **Top Style**, **Bottom Style** and **Footwear Style**, you can find all the possible outfit pieces, named by style. 
The **Compose Outfit** button will preview your choice in the viewport.

### Randomizing

![Random](https://user-images.githubusercontent.com/46087451/197575461-8918a3b7-6678-4ebc-9b5d-9e7b52df0a6d.gif)

You can generate a random outift using the **Generate Random** button. 

### Export format 

![Export](https://user-images.githubusercontent.com/46087451/197573963-06585ad8-8bce-4d7f-878a-0a285d7e80fc.gif)

Once you're happy with the combination, pick an export format and press the **Export Outfit button**. This action will create a 3D file in the directory where your currently open .blend file is located. This file contains the three clothing pieces, as well as a full body mesh and rig. What is specified in the textbox will be used as it's name.

### Batch Generation and Export

The most exciting way to use this tool is by clicking the **Batch Generate and Export** button. It creates 10 different randomly generated combinations and exports them in the .blend file location. They use the same name, while adding the version number at the end. You can find some of the exported outfits in the ```examples``` folder.

