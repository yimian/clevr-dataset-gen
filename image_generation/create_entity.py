# -*- coding: utf-8 -*-

# @File    : create_entity.py
# @Date    : 2020-09-05
# @Author  : skym
import argparse
import sys
import os

import bpy

parser = argparse.ArgumentParser()
parser.add_argument('--name', default='A', type=str, help="name")
parser.add_argument('--output_dir', default='data/shapes', type=str, help="output dir")


def extract_args(input_argv=None):
    """
    Pull out command-line arguments after "--". Blender ignores command-line flags
    after --, so this lets us forward command line arguments from the blender
    invocation to our own script.
    """
    if input_argv is None:
        input_argv = sys.argv
    output_argv = []
    if '--' in input_argv:
        idx = input_argv.index('--')
        output_argv = input_argv[(idx + 1):]
    return output_argv


def parse_args(parser, argv=None):
    return parser.parse_args(extract_args(argv))


def main():
    argv = extract_args()
    args = parser.parse_args(argv)

    # 插入文字
    bpy.ops.object.delete(use_global=False)
    bpy.ops.object.text_add(enter_editmode=False, align='WORLD', location=(0, 0, 0), scale=(1, 1, 1))
    # 旋转90
    bpy.ops.transform.rotate(value=1.5708, orient_axis='X', orient_type='GLOBAL',
                             orient_matrix=((1, 0, 0), (0, 1, 0), (0, 0, 1)), orient_matrix_type='GLOBAL',
                             constraint_axis=(True, False, False), mirror=True, use_proportional_edit=False,
                             proportional_edit_falloff='SMOOTH', proportional_size=1, use_proportional_connected=False,
                             use_proportional_projected=False)
    # 设置data大小
    bpy.context.object.data.extrude = 0.1
    bpy.context.object.data.size = 2.5
    bpy.context.object.name = args.name
    # fnt = bpy.data.fonts.load('/System/Library/Fonts/Helvetica.ttc')
    # txt = bpy.data.objects[args.name]
    # txt.data.font = fnt
    bpy.context.object.data.body = args.name[0]
    bpy.ops.object.origin_set(type='GEOMETRY_ORIGIN', center='MEDIAN')

    bpy.ops.wm.save_as_mainfile(filepath=os.path.join(args.output_dir, '{}.blend'.format(args.name)))


if __name__ == '__main__':
    main()
