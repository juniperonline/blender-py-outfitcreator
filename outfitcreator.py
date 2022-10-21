import bpy      

        
class Enums(bpy.types.PropertyGroup):
    
    my_string : bpy.props.StringProperty(name= "Name Your Outfit")
    
    my_enum_top : bpy.props.EnumProperty(
        name= "Top Style",
        description= "sample text",
        items= [('OP1', "Casual", ""),
                ('OP2', "Cyberpunk", ""),
                ('OP3', "Office", "")
        ]
    )
    my_enum_bottom : bpy.props.EnumProperty(
        name= "Bottom Style",
        description= "sample text",
        items= [('OP1', "Casual", ""),
                ('OP2', "Cyberpunk", ""),
                ('OP3', "Office", "")
        ]
    )
    my_enum_footwear : bpy.props.EnumProperty(
        name= "Footwear Style",
        description= "sample text",
        items= [('OP1', "Casual", ""),
                ('OP2', "Cyberpunk", ""),
                ('OP3', "Office", "")
        ]
    )
    
    
class OutfitCreatorPanel(bpy.types.Panel):
    bl_idname = "outfitcreator"
    bl_label = "Full-body Outfit Creator"
    bl_space_type = "VIEW_3D"
    bl_region_type = "UI"
    bl_category = "Tool"

    def draw(self, context):
        layout = self.layout 
        layout.label(text="Create a custom outfit!")
        row = layout.row()
        scene = context.scene
        mytool = scene.my_tool
        
        layout.prop(mytool, "my_string")
        layout.prop(mytool, "my_enum_top")   
        layout.prop(mytool, "my_enum_bottom")
        layout.prop(mytool, "my_enum_footwear")
 
        layout.operator("outfitcreator.operator")
        
        

class OutfitCreatorOperator(bpy.types.Operator):
    bl_label = "Export Outfit"
    bl_idname = "outfitcreator.operator"
    
    
    
    def execute(self, context):
        scene = context.scene
        mytool = scene.my_tool
        
        
        # def enforce_naming(string):
        #def load_mesh(path):
              
        
        if mytool.my_enum_top == 'OP1':
            bpy.context.object.name = mytool.my_string       
            
        if mytool.my_enum_top == 'OP2':
            bpy.context.object.name = mytool.my_string
            
        if mytool.my_enum_top == 'OP3':
            bpy.context.object.name = mytool.my_string
        
        if mytool.my_enum_bottom == 'OP1':
            bpy.context.object.name = mytool.my_string        
            
        if mytool.my_enum_bottom == 'OP2':
            bpy.context.object.name = mytool.my_string
            
        if mytool.my_enum_bottom == 'OP3':
            bpy.context.object.name = mytool.my_string
        
        if mytool.my_enum_footwear == 'OP1':         
            bpy.context.object.name = mytool.my_string       
            
        if mytool.my_enum_footwear == 'OP2':
            bpy.context.object.name = mytool.my_string
            
        if mytool.my_enum_footwear == 'OP3':
            bpy.context.object.name = mytool.my_string
        
        return {'FINISHED'}
    
 
def register():
    bpy.utils.register_class(Enums)
    bpy.utils.register_class(OutfitCreatorPanel)
    bpy.utils.register_class(OutfitCreatorOperator)
    bpy.types.Scene.my_tool = bpy.props.PointerProperty(type=Enums)
 
def unregister():
    bpy.utils.unregister_class(Enums)
    bpy.utils.unregister_class(OutfitCreatorPanel)
    bpy.utils.unregister_class(OutfitCreatorOperator)
    del bpy.types.Scene.my_tool

def load_paths():
    with open ("meshes_abspath.txt", 'r') as input_file:
        paths = [line.rstrip() for line in input_file.readlines()]
        print(paths)
 
if __name__ == "__main__":
    register()