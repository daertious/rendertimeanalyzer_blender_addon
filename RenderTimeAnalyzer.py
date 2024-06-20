import bpy
import time

bl_info = {
    "name": "Render Time Analyzer",
    "author": "Ruslan Haru",
    "version": (1, 0),
    "blender": (4, 0, 0),
    "location": "Render > Analyze Render Time",
    "description": "Analyzes the render time of all frames in Blender.",
    "warning": "",
    "wiki_url": "",
    "category": "Render",
}

class RenderTimeAnalyzer(bpy.types.Operator):
    bl_idname = "render.analyze_time"
    bl_label = "Analyze Render Time"

    def execute(self, context):
        start_time = time.time()
        bpy.ops.render.render(animation=False)
        end_time = time.time()
        render_time_per_frame = end_time - start_time

        frame_start = bpy.context.scene.frame_start
        frame_end = bpy.context.scene.frame_end
        frame_step = bpy.context.scene.frame_step
        total_frames = len(range(frame_start, frame_end + 1, frame_step))

        total_render_time = render_time_per_frame * total_frames

        total_render_time_minutes = total_render_time / 60
        total_render_time_hours = total_render_time / 3600

        info = "Total render time for all frames:\n"
        info += "In Seconds: {:.1f}\n".format(total_render_time)
        info += "In Minutes: {:.1f}\n".format(total_render_time_minutes)
        info += "In Hours: {:.1f}".format(total_render_time_hours)
        self.report({'INFO'}, info)

        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(RenderTimeAnalyzer.bl_idname)

def register():
    bpy.utils.register_class(RenderTimeAnalyzer)
    bpy.types.TOPBAR_MT_render.append(menu_func)

def unregister():
    bpy.utils.unregister_class(RenderTimeAnalyzer)
    bpy.types.TOPBAR_MT_render.remove(menu_func)

if __name__ == "__main__":
    register()
